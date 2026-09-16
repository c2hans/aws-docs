---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_DescribeResourceCollectionHealth.html
---

# DescribeResourceCollectionHealth
<a name="API_DescribeResourceCollectionHealth"></a>

 Returns the number of open proactive insights, open reactive insights, and the Mean Time to Recover (MTTR) for all closed insights in resource collections in your account. You specify the type of AWS resources collection. The two types of AWS resource collections supported are AWS CloudFormation stacks and AWS resources that contain the same AWS tag. DevOps Guru can be configured to analyze the AWS resources that are defined in the stacks or that are tagged using the same tag *key*. You can specify up to 1000 AWS CloudFormation stacks.

## Request Syntax
<a name="API_DescribeResourceCollectionHealth_RequestSyntax"></a>

```
GET /accounts/health/resource-collection/{{ResourceCollectionType}}?NextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeResourceCollectionHealth_RequestParameters"></a>

The request uses the following URI parameters.

 ** [NextToken](#API_DescribeResourceCollectionHealth_RequestSyntax) **   <a name="DevOpsGuru-DescribeResourceCollectionHealth-request-uri-NextToken"></a>
The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`

 ** [ResourceCollectionType](#API_DescribeResourceCollectionHealth_RequestSyntax) **   <a name="DevOpsGuru-DescribeResourceCollectionHealth-request-uri-ResourceCollectionType"></a>
 An AWS resource collection type. This type specifies how analyzed AWS resources are defined. The two types of AWS resource collections supported are AWS CloudFormation stacks and AWS resources that contain the same AWS tag. DevOps Guru can be configured to analyze the AWS resources that are defined in the stacks or that are tagged using the same tag *key*. You can specify up to 1000 AWS CloudFormation stacks.
Valid Values: `AWS_CLOUD_FORMATION | AWS_SERVICE | AWS_TAGS`
Required: Yes

## Request Body
<a name="API_DescribeResourceCollectionHealth_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeResourceCollectionHealth_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CloudFormation": [
      {
         "AnalyzedResourceCount": number,
         "Insight": {
            "MeanTimeToRecoverInMilliseconds": number,
            "OpenProactiveInsights": number,
            "OpenReactiveInsights": number
         },
         "StackName": "string"
      }
   ],
   "NextToken": "string",
   "Service": [
      {
         "AnalyzedResourceCount": number,
         "Insight": {
            "OpenProactiveInsights": number,
            "OpenReactiveInsights": number
         },
         "ServiceName": "string"
      }
   ],
   "Tags": [
      {
         "AnalyzedResourceCount": number,
         "AppBoundaryKey": "string",
         "Insight": {
            "MeanTimeToRecoverInMilliseconds": number,
            "OpenProactiveInsights": number,
            "OpenReactiveInsights": number
         },
         "TagValue": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeResourceCollectionHealth_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CloudFormation](#API_DescribeResourceCollectionHealth_ResponseSyntax) **   <a name="DevOpsGuru-DescribeResourceCollectionHealth-response-CloudFormation"></a>
 The returned `CloudFormationHealthOverview` object that contains an `InsightHealthOverview` object with the requested system health information.
Type: Array of [CloudFormationHealth](API_CloudFormationHealth.md) objects

 ** [NextToken](#API_DescribeResourceCollectionHealth_ResponseSyntax) **   <a name="DevOpsGuru-DescribeResourceCollectionHealth-response-NextToken"></a>
The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`

 ** [Service](#API_DescribeResourceCollectionHealth_ResponseSyntax) **   <a name="DevOpsGuru-DescribeResourceCollectionHealth-response-Service"></a>
An array of `ServiceHealth` objects that describes the health of the AWS services associated with the resources in the collection.
Type: Array of [ServiceHealth](API_ServiceHealth.md) objects

 ** [Tags](#API_DescribeResourceCollectionHealth_ResponseSyntax) **   <a name="DevOpsGuru-DescribeResourceCollectionHealth-response-Tags"></a>
The AWS tags that are used by resources in the resource collection.
Tags help you identify and organize your AWS resources. Many AWS services support tagging, so you can assign the same tag to resources from different services to indicate that the resources are related. For example, you can assign the same tag to an Amazon DynamoDB table resource that you assign to an AWS Lambda function. For more information about using tags, see the [Tagging best practices](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html) whitepaper.
Each AWS tag has two parts.
+ A tag *key* (for example, `CostCenter`, `Environment`, `Project`, or `Secret`). Tag *keys* are case-sensitive.
+ An optional field known as a tag *value* (for example, `111122223333`, `Production`, or a team name). Omitting the tag *value* is the same as using an empty string. Like tag *keys*, tag *values* are case-sensitive.
Together these are known as *key*-*value* pairs.
When you create a *key*, the case of characters in the *key* can be whatever you choose. After you create a *key*, it is case-sensitive. For example, DevOps Guru works with a *key* named `devops-guru-rds` and a *key* named `DevOps-Guru-RDS`, and these act as two different *keys*. Possible *key*/*value* pairs in your application might be `Devops-Guru-production-application/RDS` or `Devops-Guru-production-application/containers`.
Type: Array of [TagHealth](API_TagHealth.md) objects

## Errors
<a name="API_DescribeResourceCollectionHealth_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see [Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html) in the *IAM User Guide*.
HTTP Status Code: 403

 ** InternalServerException **
An internal failure in an Amazon service occurred.
 ** RetryAfterSeconds **
 The number of seconds after which the action that caused the internal server exception can be retried.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to a request throttling.
 ** QuotaCode **
 The code of the quota that was exceeded, causing the throttling exception.
 ** RetryAfterSeconds **
 The number of seconds after which the action that caused the throttling exception can be retried.
 ** ServiceCode **
 The code of the service that caused the throttling exception.
HTTP Status Code: 429

 ** ValidationException **
 Contains information about data passed in to a field during a request that is not valid.
 ** Fields **
 An array of fields that are associated with the validation exception.
 ** Message **
 A message that describes the validation exception.
 ** Reason **
 The reason the validation exception was thrown.
HTTP Status Code: 400

## See Also
<a name="API_DescribeResourceCollectionHealth_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devops-guru-2020-12-01/DescribeResourceCollectionHealth)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devops-guru-2020-12-01/DescribeResourceCollectionHealth)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/DescribeResourceCollectionHealth)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devops-guru-2020-12-01/DescribeResourceCollectionHealth)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/DescribeResourceCollectionHealth)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devops-guru-2020-12-01/DescribeResourceCollectionHealth)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devops-guru-2020-12-01/DescribeResourceCollectionHealth)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devops-guru-2020-12-01/DescribeResourceCollectionHealth)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/devops-guru-2020-12-01/DescribeResourceCollectionHealth)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/DescribeResourceCollectionHealth)
