---
source_url: https://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/architecture-overview.html
---

# Architecture overview
<a name="architecture-overview"></a>

This section provides a reference implementation architecture diagram for the components deployed with this solution.

## Architecture diagram
<a name="architecture-diagram"></a>

Deploying this solution with the default parameters deploys the following components in your AWS account.

![Image depicts an architecture diagram for Quota Monitor for AWS.](https://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/images/quota-monitor-architecture-diagram.png)

Quota Monitor for AWS includes a **hub template** that you deploy in your monitoring account. Additionally, the solution provides a **Service Quotas spoke template** and a **Trusted Advisor spoke template**. You must deploy each of these templates in the member accounts that need quota monitoring. The solution won’t deploy the **Trusted Advisor spoke template** if the account doesn’t have a support plan that includes the Trusted Advisor service.

Refer to [Choose your deployment scenario](step-1.-choose-your-deployment-scenario.md) for more information on how to use these templates, as well as two supplemental templates.

The **hub template** launches the following workflow:

1.  **Reporting** - This workflow provisions an [Amazon SNS](https://aws.amazon.com/sns/) topic, [Amazon Simple Queue Service](https://aws.amazon.com/sqs/) (Amazon SQS) queue, [AWS Lambda](https://aws.amazon.com/lambda) function summarizer, and [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) table. The queue receives usage events from all monitored accounts. The Lambda function puts all usage data on the DynamoDB table.

1.  **Centralized event collection** - The workflow provisions a custom [Amazon EventBridge](https://aws.amazon.com/eventbridge) bus, a corresponding rule, and Amazon SNS topic to raise alerts. The workflow raises alerts for quota usage and defines alert levels as:
   +  **OK** (less than 80% utilization)
   +  **WARN** (80% to 99% utilization)
   +  **ERROR** (100% utilization)

     You can filter the alerts by excluding certain services or quotas through a notification configuration in [AWS Systems Manager](https://aws.amazon.com/systems-manager/) [Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html). The workflow also sends *all* events to the reporting queue for saving usage data in DynamoDB.

1.  **Deployment management** - The workflow provisions Parameter Store, an [Amazon EventBridge](https://aws.amazon.com/eventbridge) rule, a Lambda function, and CloudFormation StackSets. The workflow manages:
   + Permissions on the centralized EventBridge bus so that monitored accounts can send their usage events to it.
   + Deployment of spoke templates in the monitored accounts using StackSets when the solution is deployed in an organization (or OU).
**Note**
When you update the Systems Manager parameter value with OU IDs or account IDs, the workflow makes needed configuration changes to start monitoring the updated list of OUs or accounts.

The **Service Quotas spoke template** launches the following workflow:

1.  **Quota list generation** - The workflow provisions a Lambda function and two DynamoDB tables. The workflow manages an active and validated list of Service Quotas that support usage monitoring using CloudWatch metrics.

1.  **Quota utilization alerting** - The workflow provisions a schedule-based Lambda function, custom EventBridge bus, and an [Amazon EventBridge](https://aws.amazon.com/eventbridge) rule. The `CW Poller` function queries the quota list table and retrieves usage data for those quotas from CloudWatch metrics. The workflow sends the usage data as events to the EventBridge bus. The spoke bus routes these usage events to both the centralized bus and the spoke SNS bus (if provided).

The **Spoke SNS template** launches the following workflow:

1.  **Spoke account notifications** - The workflow provisions notification resources in the spoke account to decentralize notifications. Specifically, it provisions an EventBridge bus with a rule that routes messages to the SNS publisher Lambda function. This function applies any notification muting rules configured through the notification muting parameter in the SSM Parameter Store. The Lambda function then publishes the relevant events to the SNS topic in the spoke account.

The **Trusted Advisor spoke template** launches the following workflow:

1.  **Trust Advisor alerting** - The workflow provisions a Lambda function and an [Amazon EventBridge](https://aws.amazon.com/eventbridge) rule to support quota usage monitoring using Trusted Advisor. The Lambda function executes at an interval of 24 hours to refresh Trusted Advisor checks. The Events rule routes Trusted Advisor usage events to the centralized bus.
**Note**
AWS CloudFormation resources are created from [AWS Cloud Development Kit](https://aws.amazon.com/cdk) (AWS CDK) components.
