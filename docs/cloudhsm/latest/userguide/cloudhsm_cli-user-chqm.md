---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-user-chqm.html
---

# The user change-quorum category in CloudHSM CLI
<a name="cloudhsm_cli-user-chqm"></a>

In the CloudHSM CLI, **user change-quorum** is a parent category for a group of commands that, when combined with the parent category, create a command specific to changing quorum for users.

**user change-quorum** is used to register user quorum authentication using a specified quorum strategy. As of SDK 5.8.0, there is only a single quorum strategy available for users as shown below.

Currently, this category consists of the following category and sub-command:
+ [token-sign](cloudhsm_cli-user-chqm-token.md)
  + [register](cloudhsm_cli-user-chqm-token-reg.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
