---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeContributorInsights.html
---

# DescribeContributorInsights
<a name="API_DescribeContributorInsights"></a>

Returns information about contributor insights for a given table or global secondary index.

## Request Syntax
<a name="API_DescribeContributorInsights_RequestSyntax"></a>

```
{
   "IndexName": "{{string}}",
   "TableName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeContributorInsights_RequestParameters"></a>

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [TableName](#API_DescribeContributorInsights_RequestSyntax) **   <a name="DDB-DescribeContributorInsights-request-TableName"></a>
The name of the table to describe. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** [IndexName](#API_DescribeContributorInsights_RequestSyntax) **   <a name="DDB-DescribeContributorInsights-request-IndexName"></a>
The name of the global secondary index to describe, if applicable.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

## Response Syntax
<a name="API_DescribeContributorInsights_ResponseSyntax"></a>

```
{
   "ContributorInsightsMode": "string",
   "ContributorInsightsRuleList": [ "string" ],
   "ContributorInsightsStatus": "string",
   "FailureException": {
      "ExceptionDescription": "string",
      "ExceptionName": "string"
   },
   "IndexName": "string",
   "LastUpdateDateTime": number,
   "TableName": "string"
}
```

## Response Elements
<a name="API_DescribeContributorInsights_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContributorInsightsMode](#API_DescribeContributorInsights_ResponseSyntax) **   <a name="DDB-DescribeContributorInsights-response-ContributorInsightsMode"></a>
The mode of CloudWatch Contributor Insights for DynamoDB that determines which events are emitted. Can be set to track all access and throttled events or throttled events only.
Type: String
Valid Values: `ACCESSED_AND_THROTTLED_KEYS | THROTTLED_KEYS`

 ** [ContributorInsightsRuleList](#API_DescribeContributorInsights_ResponseSyntax) **   <a name="DDB-DescribeContributorInsights-response-ContributorInsightsRuleList"></a>
List of names of the associated contributor insights rules.
Type: Array of strings
Pattern: `[A-Za-z0-9][A-Za-z0-9\-\_\.]{0,126}[A-Za-z0-9]`

 ** [ContributorInsightsStatus](#API_DescribeContributorInsights_ResponseSyntax) **   <a name="DDB-DescribeContributorInsights-response-ContributorInsightsStatus"></a>
Current status of contributor insights.
Type: String
Valid Values: `ENABLING | ENABLED | DISABLING | DISABLED | FAILED`

 ** [FailureException](#API_DescribeContributorInsights_ResponseSyntax) **   <a name="DDB-DescribeContributorInsights-response-FailureException"></a>
Returns information about the last failure that was encountered.
The most common exceptions for a FAILED status are:
+ LimitExceededException - Per-account Amazon CloudWatch Contributor Insights rule limit reached. Please disable Contributor Insights for other tables/indexes OR disable Contributor Insights rules before retrying.
+ AccessDeniedException - Amazon CloudWatch Contributor Insights rules cannot be modified due to insufficient permissions.
+ AccessDeniedException - Failed to create service-linked role for Contributor Insights due to insufficient permissions.
+ InternalServerError - Failed to create Amazon CloudWatch Contributor Insights rules. Please retry request.
Type: [FailureException](API_FailureException.md) object

 ** [IndexName](#API_DescribeContributorInsights_ResponseSyntax) **   <a name="DDB-DescribeContributorInsights-response-IndexName"></a>
The name of the global secondary index being described.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`

 ** [LastUpdateDateTime](#API_DescribeContributorInsights_ResponseSyntax) **   <a name="DDB-DescribeContributorInsights-response-LastUpdateDateTime"></a>
Timestamp of the last time the status was changed.
Type: Timestamp

 ** [TableName](#API_DescribeContributorInsights_ResponseSyntax) **   <a name="DDB-DescribeContributorInsights-response-TableName"></a>
The name of the table being described.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`

## Errors
<a name="API_DescribeContributorInsights_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
 ** message **
The server encountered an internal error trying to fulfill the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The operation tried to access a nonexistent table or index. The resource might not be specified correctly, or its status might not be `ACTIVE`.
 ** message **
The resource which is being requested does not exist.
HTTP Status Code: 400

## See Also
<a name="API_DescribeContributorInsights_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dynamodb-2012-08-10/DescribeContributorInsights)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dynamodb-2012-08-10/DescribeContributorInsights)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/DescribeContributorInsights)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dynamodb-2012-08-10/DescribeContributorInsights)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/DescribeContributorInsights)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dynamodb-2012-08-10/DescribeContributorInsights)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dynamodb-2012-08-10/DescribeContributorInsights)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dynamodb-2012-08-10/DescribeContributorInsights)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dynamodb-2012-08-10/DescribeContributorInsights)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/DescribeContributorInsights)
