---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListDlpSettings.html
---

# ListDlpSettings
<a name="API_ListDlpSettings"></a>

Lists all DLP settings in an AWS account.

## Request Syntax
<a name="API_ListDlpSettings_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/data-loss-prevention/settings?max-results={{MaxResults}}&next-token={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDlpSettings_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_ListDlpSettings_RequestSyntax) **   <a name="QS-ListDlpSettings-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the DLP settings that you want to list.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

 ** [MaxResults](#API_ListDlpSettings_RequestSyntax) **   <a name="QS-ListDlpSettings-request-uri-MaxResults"></a>
The maximum number of results to return per request.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListDlpSettings_RequestSyntax) **   <a name="QS-ListDlpSettings-request-uri-NextToken"></a>
The token for the next set of results, or null if there are no more results.
Length Constraints: Minimum length of 1. Maximum length of 4096.

## Request Body
<a name="API_ListDlpSettings_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDlpSettings_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DlpSettingSummaries": [
      {
         "Arn": "string",
         "CreatedAt": number,
         "DlpSettingId": "string",
         "Name": "string",
         "ProviderType": "string",
         "Status": "string",
         "UpdatedAt": number
      }
   ],
   "NextToken": "string",
   "RequestId": "string"
}
```

## Response Elements
<a name="API_ListDlpSettings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DlpSettingSummaries](#API_ListDlpSettings_ResponseSyntax) **   <a name="QS-ListDlpSettings-response-DlpSettingSummaries"></a>
A list of `DlpSettingSummary` objects for the DLP settings in the account. The list is empty if no DLP settings have been configured.
Type: Array of [DlpSettingSummary](API_DlpSettingSummary.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [NextToken](#API_ListDlpSettings_ResponseSyntax) **   <a name="QS-ListDlpSettings-response-NextToken"></a>
The token for the next set of results, or null if there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [RequestId](#API_ListDlpSettings_ResponseSyntax) **   <a name="QS-ListDlpSettings-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

## Errors
<a name="API_ListDlpSettings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 401

 ** InternalFailureException **
An internal failure occurred.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 500

 ** InvalidRequestException **
You don't have this feature activated for your account. To fix this issue, contact AWS support.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

 ** ThrottlingException **
Access is throttled.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 429

## See Also
<a name="API_ListDlpSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/ListDlpSettings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/ListDlpSettings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ListDlpSettings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/ListDlpSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ListDlpSettings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/ListDlpSettings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/ListDlpSettings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/ListDlpSettings)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/ListDlpSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ListDlpSettings)
