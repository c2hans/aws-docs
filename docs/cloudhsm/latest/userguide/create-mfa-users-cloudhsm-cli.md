---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/create-mfa-users-cloudhsm-cli.html
---

# Create users with MFA enabled for CloudHSM CLI
<a name="create-mfa-users-cloudhsm-cli"></a>

Follow these steps to create AWS CloudHSM users with multi-factor authentication (MFA) enabled.

1. Use CloudHSM CLI to log in to the HSM as an admin.

1. Use the [**user create**](cloudhsm_cli-user-create.md) command to create a user of your choice. Then follow the steps in [Set up MFA for CloudHSM CLI](set-up-mfa-for-cloudhsm-cli.md) to setup MFA for the user.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
