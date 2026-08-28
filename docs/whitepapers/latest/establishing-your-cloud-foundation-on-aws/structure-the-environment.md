---
source_url: https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/structure-the-environment.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Structure your identities to access your environment
<a name="structure-the-environment"></a>

Once your roles have been defined and you have decided what services you will start using, you need to structure your environment in a way that allows you to assign and separate the responsibilities previously described. We recommend that you start small where you can, and separate the security functions, workload environments (separating production from the rest of the environments), and sandbox environments. You can achieve this by using a mechanism to create isolated group of resources from each other.

**You can group workloads with a common business purpose** in a distinct isolated group of resources. This enables you to align the ownership and decision making with the isolated group of resources and avoid dependencies and conflicts with how workloads in other isolated group of resources are secured and managed.

Workloads often have distinct security profiles that require separate control policies and mechanisms to support them, you can **apply distinct security controls by environment.**

When you limit sensitive data stores to an account that is built to manage it, you can more easily **constrain the number of people and processes that can access and manage the data store**. This approach simplifies the process of achieving least privilege access.

In the early stages of a workload’s lifecycle, you can help **promote innovation** by providing your builders with separate isolated group of resources in support of experimentation, development, and early testing.

Organizations often have **multiple IT operating models** or ways in which they divide responsibilities among parts of the organization to deliver their application workloads and platform capabilities.

Additionally, creating isolated group will help you organized your resources** based on their function**, and **share them across these the** different isolated groups when needed. Restrictions can also be applied across isolated group of resources that perform a similar action **applying common policies.**

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
