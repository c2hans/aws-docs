---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListActions.html
---

# ListActions
<a name="API_ListActions"></a>

Lists the actions in your account and their properties.

## Request Syntax
<a name="API_ListActions_RequestSyntax"></a>

```
{
   "ActionType": "{{string}}",
   "CreatedAfter": {{number}},
   "CreatedBefore": {{number}},
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}",
   "SourceUri": "{{string}}"
}
```

## Request Parameters
<a name="API_ListActions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ActionType](#API_ListActions_RequestSyntax) **   <a name="sagemaker-ListActions-request-ActionType"></a>
A filter that returns only actions of the specified type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [CreatedAfter](#API_ListActions_RequestSyntax) **   <a name="sagemaker-ListActions-request-CreatedAfter"></a>
A filter that returns only actions created on or after the specified time.
Type: Timestamp
Required: No

 ** [CreatedBefore](#API_ListActions_RequestSyntax) **   <a name="sagemaker-ListActions-request-CreatedBefore"></a>
A filter that returns only actions created on or before the specified time.
Type: Timestamp
Required: No

 ** [MaxResults](#API_ListActions_RequestSyntax) **   <a name="sagemaker-ListActions-request-MaxResults"></a>
The maximum number of actions to return in the response. The default value is 10.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListActions_RequestSyntax) **   <a name="sagemaker-ListActions-request-NextToken"></a>
If the previous call to `ListActions` didn't return the full set of actions, the call returns a token for getting the next set of actions.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListActions_RequestSyntax) **   <a name="sagemaker-ListActions-request-SortBy"></a>
The property used to sort results. The default value is `CreationTime`.
Type: String
Valid Values: `Name | CreationTime`
Required: No

 ** [SortOrder](#API_ListActions_RequestSyntax) **   <a name="sagemaker-ListActions-request-SortOrder"></a>
The sort order. The default value is `Descending`.
Type: String
Valid Values: `Ascending | Descending`
Required: No

 ** [SourceUri](#API_ListActions_RequestSyntax) **   <a name="sagemaker-ListActions-request-SourceUri"></a>
A filter that returns only actions with the specified source URI.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `.*`
Required: No

## Response Syntax
<a name="API_ListActions_ResponseSyntax"></a>

```
{
   "ActionSummaries": [
      {
         "ActionArn": "string",
         "ActionName": "string",
         "ActionType": "string",
         "CreationTime": number,
         "LastModifiedTime": number,
         "Source": {
            "SourceId": "string",
            "SourceType": "string",
            "SourceUri": "string"
         },
         "Status": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListActions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ActionSummaries](#API_ListActions_ResponseSyntax) **   <a name="sagemaker-ListActions-response-ActionSummaries"></a>
A list of actions and their properties.
Type: Array of [ActionSummary](API_ActionSummary.md) objects

 ** [NextToken](#API_ListActions_ResponseSyntax) **   <a name="sagemaker-ListActions-response-NextToken"></a>
A token for getting the next set of actions, if there are any.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListActions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_ListActions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListActions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListActions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListActions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListActions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListActions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListActions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListActions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListActions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListActions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListActions)
