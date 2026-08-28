---
source_url: https://docs.aws.amazon.com/partner-central/latest/sales-guide/stage-visibility.html
---

# AWS stage visibility
<a name="stage-visibility"></a>

When an opportunity has reached its terminal stage (status `Launched` or `Closed/Lost`), the AWS Partner must complete the following:

1. Update the opportunity close date.

1. Enter an AWS account ID if applicable.

1. Update the opportunity stage.

Opportunities in a terminal stage (`Launched` or `Closed/Lost`) do not show an Opportunity Quality score or a co-sell motion. This is why some open opportunities are scored and others are not.

If the AWS seller updates an opportunity to a terminal stage in their CRM (customer relationship management) system, three new fields will populate for the opportunity:
+ **AWS Stage**
+ **AWS Close Date**
+ **AWS Closed/Lost Reason**

**To view AWS Stage, AWS Close Date, AWS Closed/Lost Reason fields**

1. On the **Opportunities** page, click the opportunity ID of the validated opportunity you want to update. Validated opportunities have a status of `Approved`.

1. Choose the **Additional Details** tab.

Edits to **AWS Close Date** on the **Additional details** tab do not affect the **Target Close Date** on the **Project details** tab. Edits to **AWS Stage** on the **Additional details** tab do not affect **Stage** in the **Overview** section on the opportunity detail page.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
