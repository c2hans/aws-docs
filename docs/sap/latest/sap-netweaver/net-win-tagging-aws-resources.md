---
source_url: https://docs.aws.amazon.com/sap/latest/sap-netweaver/net-win-tagging-aws-resources.html
---

# Tagging AWS Resources
<a name="net-win-tagging-aws-resources"></a>

A tag is a label that you assign to an AWS resource. Each tag consists of a *key* and an optional *value*, both of which you define. Adding tags to the various AWS resources will not only make managing your SAP environment much easier but can also be used to quickly search for resources. Many Amazon EC2 API calls can be used with a special tag filter. Refer to [AWS Tagging Strategies](https://aws.amazon.com/answers/account-management/aws-tagging-strategies/) and use it as a starting point to define the tags you need for your resources. Some examples on how you can use tags for operational needs are:
+ You can tag your EBS Volumes to identify their environment (for example Environment= DEV/QAS/PRD etc.) and use these tags to create backup policies for EBS Volumes
+ You can use similar tags as in above example with EC2 instances and use them for patching your operating systems or running scripts to stop/start application or EC2 instances.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for SAP on AWS Technical Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
