from datadog_checks.base.stubs.aggregator import AggregatorStub

TAGS = ['endpoint:http://localhost:25020/metrics_prometheus']

# "value" is only used in unit test
METRICS = [
    # tcmalloc
    {
        "name": "impala.statestore.tcmalloc.in_use",
        "value": 48179280,
    },
    {
        "name": "impala.statestore.tcmalloc.pageheap.free",
        "value": 10,
    },
    {
        "name": "impala.statestore.tcmalloc.pageheap.unmapped",
        "value": 14565376,
    },
    {
        "name": "impala.statestore.tcmalloc.physical_reserved",
        "value": 58187776,
    },
    {
        "name": "impala.statestore.tcmalloc.total_reserved",
        "value": 72753152,
    },
    # jvm
    {
        "name": "impala.catalog.jvm.code_cache.committed_usage",
        "value": 6553600,
    },
    {
        "name": "impala.catalog.jvm.code_cache.current_usage",
        "value": 6104000,
    },
    {
        "name": "impala.catalog.jvm.code_cache.init_usage",
        "value": 2555904,
    },
    {
        "name": "impala.catalog.jvm.code_cache.max_usage",
        "value": 251658240,
    },
    {
        "name": "impala.catalog.jvm.code_cache.peak_committed_usage",
        "value": 6553600,
    },
    {
        "name": "impala.catalog.jvm.code_cache.peak_current_usage",
        "value": 6493568,
    },
    {
        "name": "impala.catalog.jvm.code_cache.peak_init_usage",
        "value": 2555904,
    },
    {
        "name": "impala.catalog.jvm.code_cache.peak_max_usage",
        "value": 251658240,
    },
    {
        "name": "impala.catalog.jvm.compressed_class_space.committed_usage",
        "value": 3145728,
    },
    {
        "name": "impala.catalog.jvm.compressed_class_space.current_usage",
        "value": 3018288,
    },
    {
        "name": "impala.catalog.jvm.compressed_class_space.init_usage",
        "value": 0,
    },
    {
        "name": "impala.catalog.jvm.compressed_class_space.max_usage",
        "value": 1073741824,
    },
    {
        "name": "impala.catalog.jvm.compressed_class_space.peak_committed_usage",
        "value": 3145728,
    },
    {
        "name": "impala.catalog.jvm.compressed_class_space.peak_current_usage",
        "value": 3018288,
    },
    {
        "name": "impala.catalog.jvm.compressed_class_space.peak_init_usage",
        "value": 0,
    },
    {
        "name": "impala.catalog.jvm.gc.count",
        "value": 9,
        "type": AggregatorStub.MONOTONIC_COUNT,
    },
    {
        "name": "impala.catalog.jvm.gc.num_info_threshold_exceeded.count",
        "value": 12,
        "type": AggregatorStub.MONOTONIC_COUNT,
    },
    {
        "name": "impala.catalog.jvm.gc.num_warn_threshold_exceeded.count",
        "value": 55,
        "type": AggregatorStub.MONOTONIC_COUNT,
    },
    {
        "name": "impala.catalog.jvm.gc.time_millis.count",
        "value": 0.126,
        "type": AggregatorStub.MONOTONIC_COUNT,
    },
    {
        "name": "impala.catalog.jvm.gc.total_extra_sleep_time_millis.count",
        "value": 1.232,
        "type": AggregatorStub.MONOTONIC_COUNT,
    },
    {
        "name": "impala.catalog.jvm.heap.committed_usage",
        "value": 119013376,
    },
    {
        "name": "impala.catalog.jvm.heap.current_usage",
        "value": 29420832,
    },
    {
        "name": "impala.catalog.jvm.heap.init_usage",
        "value": 132120576,
    },
    {
        "name": "impala.catalog.jvm.heap.max_usage",
        "value": 1908932608,
    },
    {
        "name": "impala.catalog.jvm.heap.peak_committed_usage",
        "value": 0,
    },
    {
        "name": "impala.catalog.jvm.heap.peak_current_usage",
        "value": 0,
    },
    {
        "name": "impala.catalog.jvm.heap.peak_init_usage",
        "value": 0,
    },
    {
        "name": "impala.catalog.jvm.heap.peak_max_usage",
        "value": 0,
    },
    {
        "name": "impala.catalog.jvm.metaspace.committed_usage",
        "value": 29360128,
    },
    {
        "name": "impala.catalog.jvm.metaspace.current_usage",
        "value": 28849616,
    },
    {
        "name": "impala.catalog.jvm.metaspace.init_usage",
        "value": 0,
    },
    {
        "name": "impala.catalog.jvm.metaspace.max_usage",
        "value": -1.0,
    },
    {
        "name": "impala.catalog.jvm.metaspace.peak_committed_usage",
        "value": 29360128,
    },
    {
        "name": "impala.catalog.jvm.metaspace.peak_current_usage",
        "value": 28849616,
    },
    {
        "name": "impala.catalog.jvm.metaspace.peak_init_usage",
        "value": 0,
    },
    {
        "name": "impala.catalog.jvm.metaspace.peak_max_usage",
        "value": -1,
    },
    {
        "name": "impala.catalog.jvm.non_heap.committed_usage",
        "value": 39059456,
    },
    {
        "name": "impala.catalog.jvm.non_heap.current_usage",
        "value": 37971904,
    },
    {
        "name": "impala.catalog.jvm.non_heap.init_usage",
        "value": 2555904,
    },
    {
        "name": "impala.catalog.jvm.non_heap.max_usage",
        "value": -1,
    },
    {
        "name": "impala.catalog.jvm.non_heap.peak_committed_usage",
        "value": 0,
    },
    {
        "name": "impala.catalog.jvm.non_heap.peak_current_usage",
        "value": 0,
    },
    {
        "name": "impala.catalog.jvm.non_heap.peak_init_usage",
        "value": 0,
    },
    {
        "name": "impala.catalog.jvm.non_heap.peak_max_usage",
        "value": 0,
    },
    {
        "name": "impala.catalog.jvm.ps_eden_space.committed_usage",
        "value": 48758784,
    },
    {
        "name": "impala.catalog.jvm.ps_eden_space.current_usage",
        "value": 14748696,
    },
    {
        "name": "impala.catalog.jvm.ps_eden_space.init_usage",
        "value": 33554432,
    },
    {
        "name": "impala.catalog.jvm.ps_eden_space.max_usage",
        "value": 697827328,
    },
    {
        "name": "impala.catalog.jvm.ps_eden_space.peak_committed_usage",
        "value": 48758784,
    },
    {
        "name": "impala.catalog.jvm.ps_eden_space.peak_current_usage",
        "value": 33554432,
    },
    {
        "name": "impala.catalog.jvm.ps_eden_space.peak_init_usage",
        "value": 33554432,
    },
    {
        "name": "impala.catalog.jvm.ps_eden_space.peak_max_usage",
        "value": 705167360,
    },
    {
        "name": "impala.catalog.jvm.ps_old_gen.committed_usage",
        "value": 61865984,
    },
    {
        "name": "impala.catalog.jvm.ps_old_gen.current_usage",
        "value": 8830616,
    },
    {
        "name": "impala.catalog.jvm.ps_old_gen.init_usage",
        "value": 88080384,
    },
    {
        "name": "impala.catalog.jvm.ps_old_gen.max_usage",
        "value": 1431830528,
    },
    {
        "name": "impala.catalog.jvm.ps_old_gen.peak_committed_usage",
        "value": 88080384,
    },
    {
        "name": "impala.catalog.jvm.ps_old_gen.peak_current_usage",
        "value": 8830616,
    },
    {
        "name": "impala.catalog.jvm.ps_old_gen.peak_init_usage",
        "value": 88080384,
    },
    {
        "name": "impala.catalog.jvm.ps_old_gen.peak_max_usage",
        "value": 1431830528,
    },
    {
        "name": "impala.catalog.jvm.ps_survivor_space.committed_usage",
        "value": 8388608,
    },
    {
        "name": "impala.catalog.jvm.ps_survivor_space.current_usage",
        "value": 5841520,
    },
    {
        "name": "impala.catalog.jvm.ps_survivor_space.init_usage",
        "value": 5242880,
    },
    {
        "name": "impala.catalog.jvm.ps_survivor_space.max_usage",
        "value": 8388608,
    },
    {
        "name": "impala.catalog.jvm.ps_survivor_space.peak_committed_usage",
        "value": 10485760,
    },
    {
        "name": "impala.catalog.jvm.ps_survivor_space.peak_current_usage",
        "value": 5841520,
    },
    {
        "name": "impala.catalog.jvm.ps_survivor_space.peak_init_usage",
        "value": 5242880,
    },
    {
        "name": "impala.catalog.jvm.ps_survivor_space.peak_max_usage",
        "value": 10485760,
    },
    {
        "name": "impala.catalog.jvm.total_committed_usage",
        "value": 158072832,
    },
    {
        "name": "impala.catalog.jvm.total_current_usage",
        "value": 67392736,
    },
    {
        "name": "impala.catalog.jvm.total_init_usage",
        "value": 129433600,
    },
    {
        "name": "impala.catalog.jvm.total_max_usage",
        "value": 3463446527,
    },
    {
        "name": "impala.catalog.jvm.total_peak_committed_usage",
        "value": 186384384,
    },
    {
        "name": "impala.catalog.jvm.total_peak_current_usage",
        "value": 86588040,
    },
    {
        "name": "impala.catalog.jvm.total_peak_init_usage",
        "value": 129433600,
    },
    {
        "name": "impala.catalog.jvm.total_peak_max_usage",
        "value": 3472883711,
    },
]
