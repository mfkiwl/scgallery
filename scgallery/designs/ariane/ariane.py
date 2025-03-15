#!/usr/bin/env python3

'''
Ariane core

Source: https://github.com/pulp-platform/ariane
'''

import os

from siliconcompiler import Chip
from siliconcompiler.targets import freepdk45_demo
from scgallery import Gallery


def setup():
    chip = Chip('cva6')

    extra_root = os.path.join('ariane', 'extra')

    chip.register_source('cva6',
                         path='https://github.com/openhwgroup/cva6/archive/refs/tags/',
                         ref='v5.0.1')

    chip.register_source('cv-hpdcache',
                         path='git+https://github.com/openhwgroup/cv-hpdcache.git',
                         ref='645e4222c3d23fbedb5b0fec1922f72fd692a40a')

    target_config = 'cv32a6_imac_sv0'
    chip.input('core/include/cva6_hpdcache_default_config_pkg.sv', package='cva6')
    chip.input('rtl/src/hpdcache_pkg.sv', package='cv-hpdcache')
    chip.input('rtl/src/hwpf_stride/hwpf_stride_pkg.sv', package='cv-hpdcache')
    for src in ('vendor/pulp-platform/fpga-support/rtl/SyncDpRam.sv',
                'vendor/pulp-platform/fpga-support/rtl/AsyncDpRam.sv',
                'vendor/pulp-platform/fpga-support/rtl/AsyncThreePortRam.sv',
                'vendor/openhwgroup/cvfpu/src/fpnew_pkg.sv',
                'vendor/openhwgroup/cvfpu/src/fpnew_cast_multi.sv',
                'vendor/openhwgroup/cvfpu/src/fpnew_classifier.sv',
                'vendor/openhwgroup/cvfpu/src/fpnew_divsqrt_multi.sv',
                'vendor/openhwgroup/cvfpu/src/fpnew_fma_multi.sv',
                'vendor/openhwgroup/cvfpu/src/fpnew_fma.sv',
                'vendor/openhwgroup/cvfpu/src/fpnew_noncomp.sv',
                'vendor/openhwgroup/cvfpu/src/fpnew_opgroup_block.sv',
                'vendor/openhwgroup/cvfpu/src/fpnew_opgroup_fmt_slice.sv',
                'vendor/openhwgroup/cvfpu/src/fpnew_opgroup_multifmt_slice.sv',
                'vendor/openhwgroup/cvfpu/src/fpnew_rounding.sv',
                'vendor/openhwgroup/cvfpu/src/fpnew_top.sv',
                'vendor/openhwgroup/cvfpu/src/fpu_div_sqrt_mvp/hdl/defs_div_sqrt_mvp.sv',
                'vendor/openhwgroup/cvfpu/src/fpu_div_sqrt_mvp/hdl/control_mvp.sv',
                'vendor/openhwgroup/cvfpu/src/fpu_div_sqrt_mvp/hdl/div_sqrt_top_mvp.sv',
                'vendor/openhwgroup/cvfpu/src/fpu_div_sqrt_mvp/hdl/iteration_div_sqrt_mvp.sv',
                'vendor/openhwgroup/cvfpu/src/fpu_div_sqrt_mvp/hdl/norm_div_sqrt_mvp.sv',
                'vendor/openhwgroup/cvfpu/src/fpu_div_sqrt_mvp/hdl/nrbd_nrsc_mvp.sv',
                'vendor/openhwgroup/cvfpu/src/fpu_div_sqrt_mvp/hdl/preprocess_mvp.sv',
                'core/include/config_pkg.sv',
                f'core/include/{target_config}_config_pkg.sv',
                'core/include/riscv_pkg.sv',
                'core/include/ariane_pkg.sv',
                'vendor/pulp-platform/axi/src/axi_pkg.sv',
                'core/include/wt_cache_pkg.sv',
                'core/include/std_cache_pkg.sv',
                'core/include/build_config_pkg.sv',
                'core/include/cvxif_pkg.sv',
                'core/cvxif_example/include/cvxif_instr_pkg.sv',
                'core/cvxif_fu.sv',
                'core/cvxif_example/cvxif_example_coprocessor.sv',
                'core/cvxif_example/instr_decoder.sv',
                'vendor/pulp-platform/common_cells/src/cf_math_pkg.sv',
                'vendor/pulp-platform/common_cells/src/fifo_v3.sv',
                'vendor/pulp-platform/common_cells/src/lfsr.sv',
                'vendor/pulp-platform/common_cells/src/lfsr_8bit.sv',
                'vendor/pulp-platform/common_cells/src/stream_arbiter.sv',
                'vendor/pulp-platform/common_cells/src/stream_arbiter_flushable.sv',
                'vendor/pulp-platform/common_cells/src/stream_mux.sv',
                'vendor/pulp-platform/common_cells/src/stream_demux.sv',
                'vendor/pulp-platform/common_cells/src/lzc.sv',
                'vendor/pulp-platform/common_cells/src/rr_arb_tree.sv',
                'vendor/pulp-platform/common_cells/src/shift_reg.sv',
                'vendor/pulp-platform/common_cells/src/unread.sv',
                'vendor/pulp-platform/common_cells/src/popcount.sv',
                'vendor/pulp-platform/common_cells/src/exp_backoff.sv',
                'vendor/pulp-platform/common_cells/src/counter.sv',
                'vendor/pulp-platform/common_cells/src/delta_counter.sv',
                'core/cva6.sv',
                'core/cva6_rvfi_probes.sv',
                'core/alu.sv',
                'core/fpu_wrap.sv',
                'core/branch_unit.sv',
                'core/compressed_decoder.sv',
                'core/macro_decoder.sv',
                'core/controller.sv',
                'core/csr_buffer.sv',
                'core/csr_regfile.sv',
                'core/decoder.sv',
                'core/ex_stage.sv',
                'core/instr_realign.sv',
                'core/id_stage.sv',
                'core/issue_read_operands.sv',
                'core/issue_stage.sv',
                'core/load_unit.sv',
                'core/load_store_unit.sv',
                'core/lsu_bypass.sv',
                'core/mult.sv',
                'core/multiplier.sv',
                'core/serdiv.sv',
                'core/perf_counters.sv',
                'core/ariane_regfile_ff.sv',
                'core/ariane_regfile_fpga.sv',
                'core/scoreboard.sv',
                'core/store_buffer.sv',
                'core/amo_buffer.sv',
                'core/store_unit.sv',
                'core/commit_stage.sv',
                'core/axi_shim.sv',
                'core/acc_dispatcher.sv',
                'core/frontend/btb.sv',
                'core/frontend/bht.sv',
                'core/frontend/ras.sv',
                'core/frontend/instr_scan.sv',
                'core/frontend/instr_queue.sv',
                'core/frontend/frontend.sv',
                'core/cache_subsystem/wt_dcache_ctrl.sv',
                'core/cache_subsystem/wt_dcache_mem.sv',
                'core/cache_subsystem/wt_dcache_missunit.sv',
                'core/cache_subsystem/wt_dcache_wbuffer.sv',
                'core/cache_subsystem/wt_dcache.sv',
                'core/cache_subsystem/cva6_icache.sv',
                'core/cache_subsystem/wt_cache_subsystem.sv',
                'core/cache_subsystem/wt_axi_adapter.sv',
                'core/cache_subsystem/tag_cmp.sv',
                'core/cache_subsystem/axi_adapter.sv',
                'core/cache_subsystem/miss_handler.sv',
                'core/cache_subsystem/cache_ctrl.sv',
                'core/cache_subsystem/cva6_icache_axi_wrapper.sv',
                'core/cache_subsystem/std_cache_subsystem.sv',
                'core/cache_subsystem/std_nbdcache.sv',
                'core/cache_subsystem/cva6_hpdcache_subsystem.sv',
                'core/cache_subsystem/cva6_hpdcache_subsystem_axi_arbiter.sv',
                'core/cache_subsystem/cva6_hpdcache_if_adapter.sv',
                'core/pmp/src/pmp.sv',
                'core/pmp/src/pmp_entry.sv',
                'common/local/util/tc_sram_wrapper.sv',
                'vendor/pulp-platform/tech_cells_generic/src/rtl/tc_sram.sv',
                'common/local/util/sram.sv',
                'core/mmu_sv39/mmu.sv',
                'core/mmu_sv39/ptw.sv',
                'core/mmu_sv39/tlb.sv',
                'core/mmu_sv32/cva6_mmu_sv32.sv',
                'core/mmu_sv32/cva6_ptw_sv32.sv',
                'core/mmu_sv32/cva6_tlb_sv32.sv',
                'core/mmu_sv32/cva6_shared_tlb_sv32.sv'):
        chip.input(src, package='cva6')

    chip.add('option', 'idir', 'core/include', package='cva6')
    chip.add('option', 'idir', 'vendor/pulp-platform/common_cells/include', package='cva6')
    chip.add('option', 'idir', 'rtl/include', package='cv-hpdcache')

    for src in ('macros.v',):
        chip.input(os.path.join(extra_root, src), package='scgallery-designs')

    chip.set('tool', 'yosys', 'task', 'syn_asic', 'var', 'flatten', 'false')
    chip.set('tool', 'yosys', 'task', 'syn_asic', 'var', 'preserve_modules', [
             'SyncSpRamBeNx64_00000008_00000100_0_2',
             'ariane_regfile_64_2_00000002_1',
             'btb_NR_ENTRIES64',
             'csr_regfile_0000000000000000_1',
             'ex_stage',
             'fifo_v2_DEPTH8',
             'fifo_v3_0_00000020_00000008',
             'frontend_0000000000000000',
             'issue_read_operands',
             'issue_stage_NR_ENTRIES8_NR_WB_PORTS4',
             'load_store_unit',
             'miss_handler_NR_PORTS3',
             'mmu_16_16_00000001',
             'mult',
             'multiplier',
             'perf_counters',
             'scoreboard_00000008_00000004',
             'sram_00000080_00000100',
             'std_cache_subsystem_0000000080000000',
             'std_icache',
             'std_nbdcache_0000000080000000',
             'store_buffer',
             'store_unit',
             'tlb_00000010_00000001'])

    return chip


def setup_physical(chip):
    chip.set('tool', 'yosys', 'task', 'syn_asic', 'var', 'flatten', 'false')
    chip.set('tool', 'yosys', 'task', 'syn_asic', 'var', 'preserve_modules', [
             'SyncSpRamBeNx64_00000008_00000100_0_2',
             'ariane_regfile_64_2_00000002_1',
             'btb_NR_ENTRIES64',
             'csr_regfile_0000000000000000_1',
             'ex_stage',
             'fifo_v2_DEPTH8',
             'fifo_v3_0_00000020_00000008',
             'frontend_0000000000000000',
             'issue_read_operands',
             'issue_stage_NR_ENTRIES8_NR_WB_PORTS4',
             'load_store_unit',
             'miss_handler_NR_PORTS3',
             'mmu_16_16_00000001',
             'mult',
             'multiplier',
             'perf_counters',
             'scoreboard_00000008_00000004',
             'sram_00000080_00000100',
             'std_cache_subsystem_0000000080000000',
             'std_icache',
             'std_nbdcache_0000000080000000',
             'store_buffer',
             'store_unit',
             'tlb_00000010_00000001'])

    chip.set('tool', 'yosys', 'task', 'syn_asic', 'var', 'abc_clock_derating', '0.95')

    if chip.get('option', 'pdk') == 'asap7':
        for task in ('macro_placement', 'global_placement', 'pin_placement'):
            chip.set('tool', 'openroad', 'task', task, 'var', 'gpl_uniform_placement_adjustment',
                     '0.05')

        for task in ('global_place', 'global_route', 'repair_antenna'):
            chip.set('tool', 'openroad', 'task', task, 'var', 'M2_adjustment', '0.7')
            chip.set('tool', 'openroad', 'task', task, 'var', 'M3_adjustment', '0.6')


if __name__ == '__main__':
    chip = setup()
    Gallery.design_commandline(chip, target=freepdk45_demo, module_path=__file__)
    setup_physical(chip)

    chip.run()
    chip.summary()
