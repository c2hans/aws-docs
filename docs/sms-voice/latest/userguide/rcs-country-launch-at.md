---
source_url: https://docs.aws.amazon.com/sms-voice/latest/userguide/rcs-country-launch-at.html
---

# Launching RCS in Austria
<a name="rcs-country-launch-at"></a>

To launch your AWS RCS Agent in Austria, submit a country launch registration using the `AT_RCS_LAUNCH_REGISTRATION` registration type. Austria uses the standard baseline registration form. For the baseline fields, see [Standard country launch registration](rcs-country-launch-standard.md).

## A1 Telekom carrier requirements
<a name="rcs-country-launch-at-a1"></a>

**Important**
A1 Telekom (one of three Austrian carriers) requires additional legal documentation for brand approval beyond the standard registration form. Other Austrian carriers (Hi3G and T-Mobile) follow the standard approval process with no additional documentation.

During the A1 Telekom review process, you may be asked to provide the following documents:
+ Certificate of good standing
+ Excerpt of register of companies
+ Registered company address
+ VAT number

**Note**
Your agent may reach PARTIAL status (approved on Hi3G and T-Mobile) while A1 Telekom completes their additional review. You can begin sending RCS messages to recipients on approved carriers while waiting for A1 Telekom approval.

For general compliance guidance that applies to all countries, see [RCS country launch compliance guide](rcs-country-launch-compliance.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sms-voice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
