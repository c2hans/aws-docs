---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/aggregated-delete.html
---

# Deleting Aggregators for AWS Config
<a name="aggregated-delete"></a>

You can use the AWS Config console or the AWS CLI to delete your aggregators.

------
#### [ Deleting Aggregators (Console) ]

1. Sign in to the AWS Management Console and open the AWS Config console at [https://console.aws.amazon.com/config/home](https://console.aws.amazon.com/config/home).

1. Navigate to the **Aggregator** page, and choose the aggregator name.

1. Choose **Actions** and then choose **Delete**.

   A warning message is displayed. Deleting an aggregator results in the loss of all aggregated data. You cannot recover this data but data in the source account(s) is not impacted.

1. Choose **Delete** to confirm your selection.

------
#### [ Deleting Aggregators (AWS CLI) ]

Enter the following command:

```
aws configservice delete-configuration-aggregator --configuration-aggregator-name MyAggregator
```

If successful, the command executes with no additional output.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
