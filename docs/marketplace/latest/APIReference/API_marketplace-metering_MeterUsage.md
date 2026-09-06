---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-metering_MeterUsage.html
---

# MeterUsage
<a name="API_marketplace-metering_MeterUsage"></a>

As a seller, your software hosted in the buyer's AWS account uses this API action to emit metering records directly to AWS Marketplace. You must use the following buyer AWS account credentials to sign the API request.
+ For **Amazon EC2** deployments, your software must use the [IAM role for Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html) to sign the API call for `MeterUsage` API operation.
+ For **Amazon EKS** deployments, your software must use [IAM roles for service accounts (IRSA)](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html) to sign the API call for the `MeterUsage` API operation. Using [EKS Pod Identity](https://docs.aws.amazon.com/eks/latest/userguide/pod-identities.html), the node role, or long-term access keys is not supported.
+ For **Amazon ECS** deployments, your software must use [Amazon ECS task IAM](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html) role to sign the API call for the `MeterUsage` API operation. Using the node role or long-term access keys are not supported.
+ For **Amazon Bedrock AgentCore Runtime** deployments, your software must use the [AgentCore Runtime execution role](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-permissions.html#runtime-permissions-execution) to sign the API call for the `MeterUsage` API operation. Long-term access keys are not supported.

The handling of `MeterUsage` requests varies between Amazon Bedrock AgentCore Runtime and non-Amazon Bedrock AgentCore deployments.
+ For **non-Amazon Bedrock AgentCore Runtime** deployments, you can only report usage once per hour for each dimension. For AMI-based products, this is per dimension and per EC2 instance. For container products, this is per dimension and per ECS task or EKS pod. You can't modify values after they're recorded. If you report usage before a current hour ends, you will be unable to report additional usage until the next hour begins. The `Timestamp` request parameter is rounded down to the hour and used to enforce this once-per-hour rule for idempotency. For requests that are identical after the `Timestamp` is rounded down, the API is idempotent and returns the metering record ID.
+ For **Amazon Bedrock AgentCore Runtime** deployments, you can report usage multiple times per hour for the same dimension. You do not need to aggregate metering records by the hour. You must include an idempotency token in the `ClientToken` request parameter. If using an Amazon SDK or the AWS CLI, you must use the latest version which automatically includes an idempotency token in the `ClientToken` request parameter so that the request is processed successfully. The `Timestamp` request parameter is not rounded down to the hour and is not used for duplicate validation. Requests with duplicate `Timestamps` are aggregated as long as the `ClientToken` is unique.

If you submit records more than six hours after events occur, the records won't be accepted. The timestamp in your request determines when an event is recorded.

You can optionally include multiple usage allocations, to provide customers with usage data split into buckets by tags that you define or allow the customer to define.

For AWS Regions that support `MeterUsage`, see [MeterUsage Region support for Amazon EC2](https://docs.aws.amazon.com/marketplace/latest/APIReference/metering-regions.html#meterusage-region-support-ec2) and [MeterUsage Region support for Amazon ECS and Amazon EKS](https://docs.aws.amazon.com/marketplace/latest/APIReference/metering-regions.html#meterusage-region-support-ecs-eks).

## Request Syntax
<a name="API_marketplace-metering_MeterUsage_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "DryRun": {{boolean}},
   "ProductCode": "{{string}}",
   "Timestamp": {{number}},
   "UsageAllocations": [
      {
         "AllocatedUsageQuantity": {{number}},
         "Tags": [
            {
               "Key": "{{string}}",
               "Value": "{{string}}"
            }
         ]
      }
   ],
   "UsageDimension": "{{string}}",
   "UsageQuantity": {{number}}
}
```

## Request Parameters
<a name="API_marketplace-metering_MeterUsage_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [ProductCode](#API_marketplace-metering_MeterUsage_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-metering_MeterUsage-request-ProductCode"></a>
Product code is used to uniquely identify a product in AWS Marketplace. The product code should be the same as the one used during the publishing of a new product.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `^[-a-zA-Z0-9/=:_.@]*$`
Required: Yes

 ** [Timestamp](#API_marketplace-metering_MeterUsage_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-metering_MeterUsage-request-Timestamp"></a>
Timestamp, in UTC, for which the usage is being reported. Your application can meter usage for up to six hours in the past. Make sure the `timestamp` value is not before the start of the software usage.
Type: Timestamp
Required: Yes

 ** [UsageDimension](#API_marketplace-metering_MeterUsage_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-metering_MeterUsage-request-UsageDimension"></a>
It will be one of the fcp dimension name provided during the publishing of the product.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\s\S]+`
Required: Yes

 ** [ClientToken](#API_marketplace-metering_MeterUsage_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-metering_MeterUsage-request-ClientToken"></a>
Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a [UUID type of value](https://wikipedia.org/wiki/Universally_unique_identifier).
If you don't provide this value, then AWS generates a random one for you.
If you retry the operation with the same `ClientToken`, but with different parameters, the retry fails with an `IdempotencyConflictException` error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** [DryRun](#API_marketplace-metering_MeterUsage_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-metering_MeterUsage-request-DryRun"></a>
Checks whether you have the permissions required for the action, but does not make the request. If you have the permissions, the request returns `DryRunOperation`; otherwise, it returns `UnauthorizedException`. Defaults to `false` if not specified.
Type: Boolean
Required: No

 ** [UsageAllocations](#API_marketplace-metering_MeterUsage_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-metering_MeterUsage-request-UsageAllocations"></a>
The set of `UsageAllocations` to submit.
The sum of all `UsageAllocation` quantities must equal the `UsageQuantity` of the `MeterUsage` request, and each `UsageAllocation` must have a unique set of tags (include no tags).
Type: Array of [UsageAllocation](API_marketplace-metering_UsageAllocation.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2500 items.
Required: No

 ** [UsageQuantity](#API_marketplace-metering_MeterUsage_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-metering_MeterUsage-request-UsageQuantity"></a>
Consumption value for the hour. Defaults to `0` if not specified.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: No

## Response Syntax
<a name="API_marketplace-metering_MeterUsage_ResponseSyntax"></a>

```
{
   "MeteringRecordId": "string"
}
```

## Response Elements
<a name="API_marketplace-metering_MeterUsage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MeteringRecordId](#API_marketplace-metering_MeterUsage_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-metering_MeterUsage-response-MeteringRecordId"></a>
Metering record id.
Type: String

## Errors
<a name="API_marketplace-metering_MeterUsage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CustomerNotEntitledException **
Exception thrown when the customer does not have a valid subscription for the product.
HTTP Status Code: 400

 ** DuplicateRequestException **
A metering record has already been emitted by the same EC2 instance, ECS task, or EKS pod for the given {`usageDimension`, `timestamp`} with a different `usageQuantity`.
HTTP Status Code: 400

 ** IdempotencyConflictException **
The `ClientToken` is being used for multiple requests.
HTTP Status Code: 400

 ** InternalServiceErrorException **
An internal error has occurred. Retry your request. If the problem persists, post a message with details on the AWS forums.
HTTP Status Code: 500

 ** InvalidEndpointRegionException **
The endpoint being called is in a AWS Region different from your EC2 instance, ECS task, or EKS pod. The Region of the Metering Service endpoint and the AWS Region of the resource must match.
HTTP Status Code: 400

 ** InvalidProductCodeException **
The product code passed does not match the product code used for publishing the product.
HTTP Status Code: 400

 ** InvalidTagException **
The tag is invalid, or the number of tags is greater than 5.
HTTP Status Code: 400

 ** InvalidUsageAllocationsException **
Sum of allocated usage quantities is not equal to the usage quantity.
HTTP Status Code: 400

 ** InvalidUsageDimensionException **
The usage dimension does not match one of the `UsageDimensions` associated with products.
HTTP Status Code: 400

 ** ThrottlingException **
The calls to the API are throttled.
HTTP Status Code: 400

 ** TimestampOutOfBoundsException **
The `timestamp` value passed in the `UsageRecord` is out of allowed range.
For `BatchMeterUsage`, if any of the records are outside of the allowed range, the entire batch is not processed. You must remove invalid records and try again.
HTTP Status Code: 400

## See Also
<a name="API_marketplace-metering_MeterUsage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/meteringmarketplace-2016-01-14/MeterUsage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/meteringmarketplace-2016-01-14/MeterUsage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/meteringmarketplace-2016-01-14/MeterUsage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/meteringmarketplace-2016-01-14/MeterUsage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/meteringmarketplace-2016-01-14/MeterUsage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/meteringmarketplace-2016-01-14/MeterUsage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/meteringmarketplace-2016-01-14/MeterUsage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/meteringmarketplace-2016-01-14/MeterUsage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/meteringmarketplace-2016-01-14/MeterUsage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/meteringmarketplace-2016-01-14/MeterUsage)
