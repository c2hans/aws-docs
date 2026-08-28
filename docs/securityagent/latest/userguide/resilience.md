---
source_url: https://docs.aws.amazon.com/securityagent/latest/userguide/resilience.html
---

# Resilience in AWS Security Agent
<a name="resilience"></a>

**Note**
AWS Security Agent is available in the following Regions: US East (N. Virginia) – `us-east-1`, US West (Oregon) – `us-west-2`, Asia Pacific (Mumbai) – `ap-south-1`, Asia Pacific (Singapore) – `ap-southeast-1`, Asia Pacific (Sydney) – `ap-southeast-2`, Asia Pacific (Tokyo) – `ap-northeast-1`, Europe (Frankfurt) – `eu-central-1`, Europe (Ireland) – `eu-west-1`, and South America (São Paulo) – `sa-east-1`. It uses [cross-region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html). In Asia Pacific (Mumbai), Asia Pacific (Singapore), and South America (São Paulo), AWS Security Agent uses [global cross-region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/global-cross-region-inference.html), which routes inference requests to any [commercial AWS Region](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html#region). In all other Regions, it uses [geographic cross-region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/geographic-cross-region-inference.html), which keeps data processing within specific geographic boundaries. AWS Security Agent is a tool used during the development of your application, and should not be deployed as critical or customer-facing infrastructure.

The AWS global infrastructure is built around AWS Regions and Availability Zones. AWS Regions provide multiple physically separated and isolated Availability Zones, which are connected with low-latency, high-throughput, and highly redundant networking. With Availability Zones, you can design and operate applications and databases that automatically fail over between zones without interruption. Availability Zones are more highly available, fault tolerant, and scalable than traditional single or multiple data center infrastructures.

For more information about AWS Regions and Availability Zones, see [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
