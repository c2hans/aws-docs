---
source_url: https://docs.aws.amazon.com/mediatailor/latest/ug/cdn-optimize-routing.html
---

# Request routing optimization for CDN and MediaTailor integrations
<a name="cdn-optimize-routing"></a>

Implement these routing optimizations for all AWS Elemental MediaTailor CDN integrations:
+ Create separate cache behaviors for manifest and segment requests
+ Configure origin request policies to control header forwarding
+ Set up proper error handling and failover mechanisms
+ Implement origin shields if available in your CDN to reduce origin load
+ Implement request collapsing at the CDN level to efficiently handle concurrent requests

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
