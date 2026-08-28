---
source_url: https://docs.aws.amazon.com/mediatailor/latest/ug/cdn-optimization.html
---

# Performance optimization guide for CDN and MediaTailor integrations
<a name="cdn-optimization"></a>

AWS Elemental MediaTailor performance can be maximized through systematic content delivery network (CDN) optimization. Whether you're implementing server-side ad insertion (SSAI), channel assembly, or combined workflows, the optimization principles and performance targets remain consistent. This guide provides comprehensive optimization techniques and benchmarks that apply across all MediaTailor implementations.

For advanced routing optimization using dynamic variables and configuration aliases, see [MediaTailor dynamic ad variables for ADS requests](variables.md). For query parameter optimization strategies, see [MediaTailor manifest query parameters](manifest-query-parameters.md).

**Optimization workflow overview:**

1. **Configure caching** - Set appropriate TTL values and cache behaviors

1. **Optimize routing** - Configure request routing and origin policies

1. **Measure performance** - Track against established benchmarks

1. **Apply advanced techniques** - Implement additional optimization features

**Topics**
+ [Caching optimization](cdn-optimize-caching.md)
+ [Request routing optimization](cdn-optimize-routing.md)
+ [Performance benchmarks](cdn-performance-benchmarks.md)
+ [Advanced optimization](cdn-advanced-optimization.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
