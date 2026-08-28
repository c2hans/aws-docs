---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/requirements-for-tagging.html
---

# Requirements for AWS Resource Groups—tagging
<a name="requirements-for-tagging"></a>

When users create channels, inputs, or input security groups, they can optionally attach tags to the resource during creation. Typically, your organization has a policy to tag or to omit tags. There are two services that control permissions for tagging, for two different scenarios:
+ The ability to tag during channel creation is controlled by actions within AWS Elemental MediaLive. See [Requirements for AWS Elemental MediaLive features](requirements-for-medialive.md).
+ The ability to modify tags in existing resources is controlled by actions within Resource Group Tagging. See [Working with Tag Editor](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/tag-editor.html) in [Getting Started with the AWS Management Console](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/getting-started.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
