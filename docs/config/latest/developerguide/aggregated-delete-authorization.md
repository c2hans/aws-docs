---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/aggregated-delete-authorization.html
---

# Deleting Authorization for Aggregator Accounts to Collect AWS Config Configuration and Compliance Data
<a name="aggregated-delete-authorization"></a>

*Authorization* refers to the permissions you grant to an aggregator account and region to collect your AWS Config configuration and compliance data. Authorization is not required if you are aggregating source accounts that are part of AWS Organizations. You can use the AWS Config console or the AWS CLI to delete authorizations.

**Topics**
+ [Considerations](#aggregated-delete-authorization-considerations)
+ [Deleting Authorization](#aaggregated-delete-authorization-procedure)

## Considerations
<a name="aggregated-delete-authorization-considerations"></a>

**There are two types of aggregators: Individual account aggregator and Organization aggregator**

For an individual account aggregator, authorization is required for all source accounts and Regions that you want to include, including both external accounts and Regions and Organization member accounts and Regions.

For an organization aggregator, authorization is not required for Organization member account regions since authorization is integrated with the AWS Organizations service.

**Aggregators do not automatically enable AWS Config on your behalf**

AWS Config needs to be enabled in the source account and Region for either type of aggregator, in order for AWS Config data to be generated in the source account and Region.

## Deleting Authorization
<a name="aaggregated-delete-authorization-procedure"></a>

------
#### [ Deleting Authorization (Console) ]

1. Sign in to the AWS Management Console and open the AWS Config console at [https://console.aws.amazon.com/config/home](https://console.aws.amazon.com/config/home).

1. Choose the aggregator account that you want to delete authorization, and then choose **Delete**.

   A warning message is displayed. When you delete this authorization, AWS Config data will no longer be shared with the aggregator account.

1. Choose **Delete** again to confirm your selection.

   The aggregator account is now deleted.

------
#### [ Deleting Authorization (AWS CLI) ]

Enter the following command:

```
aws configservice delete-aggregation-authorization --authorized-account-id  {{AccountID}} --authorized-aws-region {{Region}}
```

If successful, the command executes with no additional output.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
