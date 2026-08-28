---
source_url: https://docs.aws.amazon.com/controltower/latest/userguide/controls-dedicated-env-considerations.html
---

# AWS Config Considerations
<a name="controls-dedicated-env-considerations"></a>

 You have the option to enable AWS Config during initial setup or later as needed. AWS Config is required if you plan to use detective controls in your environment. If you choose to enable AWS Config, you'll need to designate an aggregator account to collect configuration and compliance data. You can either select an existing account or create a new one during setup. Additional options include configuring AWS KMS key encryption and specifying Amazon S3 log retention periods for the recording.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
