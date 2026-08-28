---
source_url: https://docs.aws.amazon.com/cur/latest/userguide/table-dictionary-focus-1-0-aws.html
---

# FOCUS 1.0 with AWS columns
<a name="table-dictionary-focus-1-0-aws"></a>

The FOCUS 1.0 with AWS columns table contains your cost and usage data formatted with FinOps Open Cost and Usage Specification (FOCUS) 1.0, along with five additional columns from AWS that contain proprietary billing data. These columns are **x\_CostCategories**, **x\_Discounts**, **x\_Operation**, **x\_ServiceCode**, and **x\_UsageType**. For more information about the FOCUS open-source specification, refer to the [FOCUS](https://focus.finops.org/) website.

The SQL table name for FOCUS 1.0 with AWS columns is `FOCUS_1_0_AWS`

## Table configurations
<a name="focus-1-0-table-configurations"></a>

There are no table configurations for the FOCUS 1.0 with AWS columns table.

## AWS Organizations support
<a name="focus-1-0-table-organizations"></a>

The FOCUS 1.0 with AWS columns table inherits the settings you made in the consolidated billing feature in AWS Organizations. When consolidated billing is enabled, there are different behaviors for management and member accounts. If you’re using a management account, your FOCUS 1.0 with AWS columns table includes cost and usage data for the management account and all member accounts in your organization. If you’re using a member account, your FOCUS 1.0 with AWS columns table only includes cost and usage data for that member account.

After joining an organization, a member account can only export data for the time that the account has been a member of the organization. For example, let's say that a member account leaves organization A and joins organization B on the 15th of the month. Then, the member account creates an export. Because the member account created an export after joining organization B, the member account’s export of FOCUS 1.0 with AWS columns for the month only includes cost and usage data for the time that the account has been a member of organization B.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cur` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
