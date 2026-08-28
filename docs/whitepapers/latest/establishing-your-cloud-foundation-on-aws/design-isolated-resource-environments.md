---
source_url: https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/design-isolated-resource-environments.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Design isolated resource environments
<a name="design-isolated-resource-environments"></a>

Creating an identity and access management isolation boundary for workloads reduces the risk of a workload infrastructure update impacting a different workload, simplifies cost management, and allows application teams to operate within a bounded environment. Being able to implement preventative or detective controls on isolated resource environments will allow different controls for different workload types or Software Development Life Cycle (SDLC) environments (such as dev, test, prod).

Workloads often have distinct security profiles that require separate control policies and mechanisms to support them. For example, it’s common to have different security and operational requirements for the non-production and production environments of a given workload. The resources and data that make up a workload are separated from other environments and workloads with defined isolation boundaries.

You can group workloads with a common business purpose in distinct environments. This enables you to align the ownership and decision making with those environments, avoiding dependencies and conflicts with how workloads in other environments are secured and managed.

 Different business units or product teams might have different processes. Depending on your overall business model, you might choose to isolate distinct business units or subsidiaries in different environments. Isolation of business units can help them operate with greater decentralized control, but still provides the ability for you to implement overarching guardrails. This approach might also ease divestment of those units over time. For information about best practices for organizing your environment on AWS, refer to [Organizing your AWS environment using multiple accounts](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
