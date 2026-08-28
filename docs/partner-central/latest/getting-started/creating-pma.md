---
source_url: https://docs.aws.amazon.com/partner-central/latest/getting-started/creating-pma.html
---

# Creating a program management account
<a name="creating-pma"></a>

To create a program management account, you will need an AWS management account ID and an active channel program registration.

Member accounts and standalone accounts cannot be used as PMAs. Additionally, you can not use an AWS Management Account that is already onboarded as a payer account in legacy Partner Central Channel Management. You must first offboard the legacy payer account prior to creating a PMA with the same account ID.

Common scenarios for creating a new PMA include:
+ Expanding into a new geographic region with different billing requirements
+ Setting up a dedicated account for a specific business division
+ Separating management of different AWS Channel Programs

**To create a PMA**

1. Navigate to Channel Management in AWS Partner Central.

1. On the program management accounts tab, choose **Create**.

1. Enter AWS management account ID.

1. Select Channel Program type.

1. (Optional) Add descriptive name for the PMA.

1. Submit for activation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
