---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_DescribeOrganizationResourceCollectionHealth.html
---

# DescribeOrganizationResourceCollectionHealth
<a name="API_DescribeOrganizationResourceCollectionHealth"></a>

Provides an overview of your system's health. If additional member accounts are part of your organization, you can filter those accounts using the `AccountIds` field.

## Request Syntax
<a name="API_DescribeOrganizationResourceCollectionHealth_RequestSyntax"></a>

```
POST /organization/health/resource-collection HTTP/1.1
Content-type: application/json

{
   "AccountIds": [ "{{string}}" ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "OrganizationalUnitIds": [ "{{string}}" ],
   "OrganizationResourceCollectionType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DescribeOrganizationResourceCollectionHealth_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeOrganizationResourceCollectionHealth_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AccountIds](#API_DescribeOrganizationResourceCollectionHealth_RequestSyntax) **   <a name="DevOpsGuru-DescribeOrganizationResourceCollectionHealth-request-AccountIds"></a>
The ID of the AWS account.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Length Constraints: Fixed length of 12.
Pattern: `^\d{12}$`
Required: No

 ** [MaxResults](#API_DescribeOrganizationResourceCollectionHealth_RequestSyntax) **   <a name="DevOpsGuru-DescribeOrganizationResourceCollectionHealth-request-MaxResults"></a>
The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned `nextToken` value.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 500.
Required: No

 ** [NextToken](#API_DescribeOrganizationResourceCollectionHealth_RequestSyntax) **   <a name="DevOpsGuru-DescribeOrganizationResourceCollectionHealth-request-NextToken"></a>
The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: No

 ** [OrganizationalUnitIds](#API_DescribeOrganizationResourceCollectionHealth_RequestSyntax) **   <a name="DevOpsGuru-DescribeOrganizationResourceCollectionHealth-request-OrganizationalUnitIds"></a>
The ID of the organizational unit.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Length Constraints: Maximum length of 68.
Pattern: `^ou-[0-9a-z]{4,32}-[a-z0-9]{8,32}$`
Required: No

 ** [OrganizationResourceCollectionType](#API_DescribeOrganizationResourceCollectionHealth_RequestSyntax) **   <a name="DevOpsGuru-DescribeOrganizationResourceCollectionHealth-request-OrganizationResourceCollectionType"></a>
 An AWS resource collection type. This type specifies how analyzed AWS resources are defined. The two types of AWS resource collections supported are AWS CloudFormation stacks and AWS resources that contain the same AWS tag. DevOps Guru can be configured to analyze the AWS resources that are defined in the stacks or that are tagged using the same tag *key*. You can specify up to 1000 AWS CloudFormation stacks.
Type: String
Valid Values: `AWS_CLOUD_FORMATION | AWS_SERVICE | AWS_ACCOUNT | AWS_TAGS`
Required: Yes

## Response Syntax
<a name="API_DescribeOrganizationResourceCollectionHealth_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Account": [
      {
         "AccountId": "string",
         "Insight": {
            "OpenProactiveInsights": number,
            "OpenReactiveInsights": number
         }
      }
   ],
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
<a name="API_DescribeOrganizationResourceCollectionHealth_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Account](#API_DescribeOrganizationResourceCollectionHealth_ResponseSyntax) **   <a name="DevOpsGuru-DescribeOrganizationResourceCollectionHealth-response-Account"></a>
The name of the organization's account.
Type: Array of [AccountHealth](API_AccountHealth.md) objects

 ** [CloudFormation](#API_DescribeOrganizationResourceCollectionHealth_ResponseSyntax) **   <a name="DevOpsGuru-DescribeOrganizationResourceCollectionHealth-response-CloudFormation"></a>
The returned `CloudFormationHealthOverview` object that contains an `InsightHealthOverview` object with the requested system health information.
Type: Array of [CloudFormationHealth](API_CloudFormationHealth.md) objects

 ** [NextToken](#API_DescribeOrganizationResourceCollectionHealth_ResponseSyntax) **   <a name="DevOpsGuru-DescribeOrganizationResourceCollectionHealth-response-NextToken"></a>
The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`

 ** [Service](#API_DescribeOrganizationResourceCollectionHealth_ResponseSyntax) **   <a name="DevOpsGuru-DescribeOrganizationResourceCollectionHealth-response-Service"></a>
An array of `ServiceHealth` objects that describes the health of the AWS services associated with the resources in the collection.
Type: Array of [ServiceHealth](API_ServiceHealth.md) objects

 ** [Tags](#API_DescribeOrganizationResourceCollectionHealth_ResponseSyntax) **   <a name="DevOpsGuru-DescribeOrganizationResourceCollectionHealth-response-Tags"></a>
Tags help you identify and organize your AWS resources. Many AWS services support tagging, so you can assign the same tag to resources from different services to indicate that the resources are related. For example, you can assign the same tag to an Amazon DynamoDB table resource that you assign to an AWS Lambda function. For more information about using tags, see the [Tagging best practices](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html) whitepaper.
Each AWS tag has two parts.
+ A tag *key* (for example, `CostCenter`, `Environment`, `Project`, or `Secret`). Tag *keys* are case-sensitive.
+ An optional field known as a tag *value* (for example, `111122223333`, `Production`, or a team name). Omitting the tag *value* is the same as using an empty string. Like tag *keys*, tag *values* are case-sensitive.
Together these are known as *key*-*value* pairs.
When you create a *key*, the case of characters in the *key* can be whatever you choose. After you create a *key*, it is case-sensitive. For example, DevOps Guru works with a *key* named `devops-guru-rds` and a *key* named `DevOps-Guru-RDS`, and these act as two different *keys*. Possible *key*/*value* pairs in your application might be `Devops-Guru-production-application/RDS` or `Devops-Guru-production-application/containers`.
Type: Array of [TagHealth](API_TagHealth.md) objects

## Errors
<a name="API_DescribeOrganizationResourceCollectionHealth_Errors"></a>

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
<a name="API_DescribeOrganizationResourceCollectionHealth_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devops-guru-2020-12-01/DescribeOrganizationResourceCollectionHealth)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devops-guru-2020-12-01/DescribeOrganizationResourceCollectionHealth)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/DescribeOrganizationResourceCollectionHealth)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devops-guru-2020-12-01/DescribeOrganizationResourceCollectionHealth)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/DescribeOrganizationResourceCollectionHealth)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devops-guru-2020-12-01/DescribeOrganizationResourceCollectionHealth)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devops-guru-2020-12-01/DescribeOrganizationResourceCollectionHealth)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devops-guru-2020-12-01/DescribeOrganizationResourceCollectionHealth)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/devops-guru-2020-12-01/DescribeOrganizationResourceCollectionHealth)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/DescribeOrganizationResourceCollectionHealth)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DevOps Guru. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devops-guru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
