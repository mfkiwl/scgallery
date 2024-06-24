from siliconcompiler import Chip, Checklist
import json


def setup(chip, rules_file='rules.json'):
    '''
    '''

    standard = 'asicflow_rules'

    job = chip.get('option', 'jobname')
    flow = chip.get('option', 'flow')

    checklist = Checklist(chip, standard)

    with open(rules_file, 'r') as f:
        rules = json.load(f)

    mainlib = chip.get('asic', 'logiclib')[0]

    if mainlib not in rules:
        raise ValueError(f'{mainlib} is missing from rules')

    flow = chip.get('option', 'flow')
    if flow not in rules[mainlib]:
        raise ValueError(f'{flow} is missing from rules')

    rules = rules[mainlib][flow]["rules"]

    for name, info in rules.items():
        criteria = set()
        nodes = set()

        for node in info['nodes']:
            if node['step'] == '*':
                steps = chip.getkeys('flowgraph', flow)
            else:
                steps = [node['step']]

            for step in steps:
                if node['index'] == '*':
                    indexes = chip.getkeys('flowgraph', flow, step)
                else:
                    indexes = [node['index']]

                for index in indexes:
                    nodes.add((job, step, index))

        for rule in info['criteria']:
            if rule['value'] is None:
                continue

            criteria.add(f"{rule['metric']}{rule['operator']}{rule['value']}")

        checklist.set('checklist', standard, name, 'criteria', criteria)
        checklist.add('checklist', standard, name, 'task', nodes)

    return checklist


##################################################
if __name__ == "__main__":
    checklist = setup(Chip('<checklist>'))
    checklist.write_manifest(f"{checklist.top()}.json")
