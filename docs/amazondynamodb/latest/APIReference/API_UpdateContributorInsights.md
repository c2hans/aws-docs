---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateContributorInsights.html
---

# UpdateContributorInsights
<a name="API_UpdateContributorInsights"></a>

Updates the status for contributor insights for a specific table or index. CloudWatch Contributor Insights for DynamoDB graphs display the partition key and (if applicable) sort key of frequently accessed items and frequently throttled items in plaintext. If you require the use of AWS Key Management Service (KMS) to encrypt this table’s partition key and sort key data with an AWS managed key or customer managed key, you should not enable CloudWatch Contributor Insights for DynamoDB for this table.

## Request Syntax
<a name="API_UpdateContributorInsights_RequestSyntax"></a>

```
{
   "ContributorInsightsAction": "{{string}}",
   "ContributorInsightsMode": "{{string}}",
   "IndexName": "{{string}}",
   "TableName": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateContributorInsights_RequestParameters"></a>

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [ContributorInsightsAction](#API_UpdateContributorInsights_RequestSyntax) **   <a name="DDB-UpdateContributorInsights-request-ContributorInsightsAction"></a>
Represents the contributor insights action.
Type: String
Valid Values: `ENABLE | DISABLE`
Required: Yes

 ** [TableName](#API_UpdateContributorInsights_RequestSyntax) **   <a name="DDB-UpdateContributorInsights-request-TableName"></a>
The name of the table. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** [ContributorInsightsMode](#API_UpdateContributorInsights_RequestSyntax) **   <a name="DDB-UpdateContributorInsights-request-ContributorInsightsMode"></a>
Specifies whether to track all access and throttled events or throttled events only for the DynamoDB table or index.
Type: String
Valid Values: `ACCESSED_AND_THROTTLED_KEYS | THROTTLED_KEYS`
Required: No

 ** [IndexName](#API_UpdateContributorInsights_RequestSyntax) **   <a name="DDB-UpdateContributorInsights-request-IndexName"></a>
The global secondary index name, if applicable.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

## Response Syntax
<a name="API_UpdateContributorInsights_ResponseSyntax"></a>

```
{
   "ContributorInsightsMode": "string",
   "ContributorInsightsStatus": "string",
   "IndexName": "string",
   "TableName": "string"
}
```

## Response Elements
<a name="API_UpdateContributorInsights_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContributorInsightsMode](#API_UpdateContributorInsights_ResponseSyntax) **   <a name="DDB-UpdateContributorInsights-response-ContributorInsightsMode"></a>
The updated mode of CloudWatch Contributor Insights that determines whether to monitor all access and throttled events or to track throttled events exclusively.
Type: String
Valid Values: `ACCESSED_AND_THROTTLED_KEYS | THROTTLED_KEYS`

 ** [ContributorInsightsStatus](#API_UpdateContributorInsights_ResponseSyntax) **   <a name="DDB-UpdateContributorInsights-response-ContributorInsightsStatus"></a>
The status of contributor insights
Type: String
Valid Values: `ENABLING | ENABLED | DISABLING | DISABLED | FAILED`

 ** [IndexName](#API_UpdateContributorInsights_ResponseSyntax) **   <a name="DDB-UpdateContributorInsights-response-IndexName"></a>
The name of the global secondary index, if applicable.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`

 ** [TableName](#API_UpdateContributorInsights_ResponseSyntax) **   <a name="DDB-UpdateContributorInsights-response-TableName"></a>
The name of the table.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`

## Errors
<a name="API_UpdateContributorInsights_Errors"></a>

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
<a name="API_UpdateContributorInsights_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dynamodb-2012-08-10/UpdateContributorInsights)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dynamodb-2012-08-10/UpdateContributorInsights)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/UpdateContributorInsights)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dynamodb-2012-08-10/UpdateContributorInsights)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/UpdateContributorInsights)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dynamodb-2012-08-10/UpdateContributorInsights)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dynamodb-2012-08-10/UpdateContributorInsights)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dynamodb-2012-08-10/UpdateContributorInsights)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dynamodb-2012-08-10/UpdateContributorInsights)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/UpdateContributorInsights)
