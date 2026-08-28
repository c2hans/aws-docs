---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-mainframe-decoupling-patterns/applications-that-share-programs.html
---

# Applications that share programs
<a name="applications-that-share-programs"></a>

The following diagram illustrates mainframe applications A and B that run a shared program called program AB.1. This case is also applicable when applications A and B include programs that call shared subprograms.

![Mainframe applications A and B that run a shared program called program AB.1.](http://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-mainframe-decoupling-patterns/images/guide-img/a6175648-8ce0-4ab7-9a68-cebf41995535/images/7cad29af-ece8-4ae8-a068-e55aafd768e8.png)

 **Steps for analysis**

1. Perform an impact analysis of the shared program AB.1, so you can migrate applications A and B, and program AB.1 together. We recommend using the discovery tools listed in the [Additional resources](resources.md) section to automate the analysis.

1. Based on the impact analysis, identify the number of dependent applications that use shared programs such as program AB.1.

1. (Recommended) Complete a business domain analysis to determine whether the shared program can be aggregated into a domain with applications and exposed as an API as one of the domain services.

You can use one of the following approaches to decouple the applications in preparation for migration:
+ Use a standalone API
+ Use a shared library
+ Use a message queue

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
