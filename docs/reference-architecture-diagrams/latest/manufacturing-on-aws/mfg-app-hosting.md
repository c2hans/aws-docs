---
source_url: https://docs.aws.amazon.com/reference-architecture-diagrams/latest/manufacturing-on-aws/mfg-app-hosting.html
---

# Application hosting
<a name="mfg-app-hosting"></a>

The application hosting diagram shows how to run enterprise and engineering applications on AWS.

![Application hosting diagram for enterprise and engineering workloads on AWS.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/manufacturing-on-aws/images/manufacturing-on-aws-ra-4.png)

1. Use [AWS Outposts](https://docs.aws.amazon.com/outposts/latest/userguide/) for latency-sensitive workloads that must run close to on-premises systems.

1. Use AWS Snowball Edge for disconnected or intermittent connectivity use cases.

1. Host enterprise applications on [Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/) with Auto Scaling and Elastic Load Balancing.

1. Use [Amazon FSx](https://docs.aws.amazon.com/fsx/latest/LustreGuide/) and Amazon EC2 with WorkSpaces Applications for high performance computing (HPC), CAD, and CAE workloads.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Reference Architecture Diagrams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query reference-architecture-diagrams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
