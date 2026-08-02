---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/quotas.html
---

# Quotas
<a name="quotas"></a>

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.

## Quotas for AWS services in this solution
<a name="quotas-for-aws-services-in-this-solution"></a>

Make sure you have sufficient quota for each of the [services implemented in this solution](architecture-details.md#aws-services-in-this-solution). For more information, refer to [AWS service quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html).

Use the following links to go to the page for that service. To view the Service Quotas for all AWS services in the documentation without switching pages, view the information in the [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-general.pdf#aws-service-information) page in the PDF instead.

## AWS CloudFormation quotas
<a name="aws-cloudformation-quotas"></a>

Your AWS account has AWS CloudFormation quotas that you should be aware of when [launching the stack](deployment.md#step-2) in this solution. By understanding these quotas, you can avoid limitation errors that would prevent you from deploying this solution successfully. For more information, see [AWS CloudFormation quotas](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html) in the *AWS CloudFormation User Guide*.

## AWS CloudWatch quotas
<a name="aws-cloudwatch-quotas"></a>

Your AWS account has AWS CloudWatch quotas tied to CloudWatch Resource Policies which only allows 10 resource policies per region per account and this cannot be requested for a quota increase, see [AWS CloudWatch Logs Quotas](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/cloudwatch_limits_cwl.html) in the *AWS CloudWatch User Guide*. Before your deployment please check your current usage to ensure you won’t cross this threshold when deploying the solution.

## AWS Organizations
<a name="aws-org-quotas"></a>

The solution’s Lambda functions make calls to the [AWS Organizations API](https://docs.aws.amazon.com/organizations/latest/APIReference/Welcome.html) in order to fetch the alias of the current account to include in messages published to the solution’s SNS topic. This enables human-readable account names to be visible in the solution’s notifications for debugging and tracking purposes.

AWS Organizations imposes limits on how often customers can invoke their API endpoints. If you find that the solution is exceeding the limits set for your account, you can disable the feature that fetches and displays the account alias.

To do this, **navigate to the Lambda function** named `SO0111-ASR-sendNotifications` located in the region and account where you deployed the Admin stack. Then, **locate the environment variable** named `DISABLE_ACCOUNT_ALIAS_LOOKUP` and change the value from "False" to **"True"**. The account alias field in the solution’s notifications will now be *"Unknown"* however this will not impact the functionality of the solution.
