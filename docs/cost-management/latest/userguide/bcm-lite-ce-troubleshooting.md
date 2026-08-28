---
source_url: https://docs.aws.amazon.com/cost-management/latest/userguide/bcm-lite-ce-troubleshooting.html
---

# Troubleshoot Cost Explorer in the AWS Billing and Cost Management console
<a name="bcm-lite-ce-troubleshooting"></a>

**Warning**
We're currently releasing our new experience to a limited number of customers. You might not be able to access this experience yet.

The following troubleshooting content can help you resolve issues with Cost Explorer.

## If you receive a data threshold error
<a name="bcm-lite-ce-ts-data-threshold"></a>

Cost Explorer supports up to 500 million usage records for resource-level data at daily granularity. If you receive this error, your filtering has used too many usage records. Reduce the number of services you want to use for resource-level filtering.

## If AWS does not forecast your future cost or usage
<a name="bcm-lite-ce-ts-no-forecast"></a>

AWS requires enough data to construct an 80% prediction interval. If you do not see a forecast, your project does not have enough data. This often happens for projects that have not been open for a full billing cycle.

## There is an inconsistency between my billing data and what is shown on Cost Explorer
<a name="bcm-lite-ce-ts-billing-inconsistency"></a>

In the current billing period, the data depends on your upstream data from your billing applications. Some data might be updated later than 24 hours. Slight inconsistencies between billing data and Cost Explorer can be expected.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
