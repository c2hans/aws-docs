---
source_url: https://docs.aws.amazon.com/controltower/latest/userguide/controls-dedicated-env-implement.html
---

# Implementation Process
<a name="controls-dedicated-env-implement"></a>

 If you proceed without AWS Config, your environment will be immediately ready for preventive and proactive controls within the Control Catalog.

 However, when you're ready to enable your first detective control, you'll need to enable AWS Config recording through the new `ConfigBaseline` being enabled on the target OUs. This is a one-time setup process per OU and incurs AWS Config pricing based on the number of accounts per OU and resources per account, per AWS Region.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
