---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListHubContents.html
---

# ListHubContents
<a name="API_ListHubContents"></a>

List the contents of a hub.

## Request Syntax
<a name="API_ListHubContents_RequestSyntax"></a>

```
{
   "HubContentType": "{{string}}",
   "HubName": "{{string}}",
   "MaxResults": {{number}},
   "MaxSchemaVersion": "{{string}}",
   "NameContains": "{{string}}",
   "NextToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}"
}
```

## Request Parameters
<a name="API_ListHubContents_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [HubContentType](#API_ListHubContents_RequestSyntax) **   <a name="sagemaker-ListHubContents-request-HubContentType"></a>
The type of hub content to list.
Type: String
Valid Values: `Model | Notebook | ModelReference | DataSet | JsonDoc`
Required: Yes

 ** [HubName](#API_ListHubContents_RequestSyntax) **   <a name="sagemaker-ListHubContents-request-HubName"></a>
The name of the hub to list the contents of.
Type: String
Pattern: `(arn:[a-z0-9-\.]{1,63}:sagemaker:\w+(?:-\w+)+:(\d{12}|aws):hub\/)?[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [MaxResults](#API_ListHubContents_RequestSyntax) **   <a name="sagemaker-ListHubContents-request-MaxResults"></a>
The maximum amount of hub content to list.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [MaxSchemaVersion](#API_ListHubContents_RequestSyntax) **   <a name="sagemaker-ListHubContents-request-MaxSchemaVersion"></a>
The upper bound of the hub content schema verion.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 14.
Pattern: `\d{1,4}.\d{1,4}.\d{1,4}`
Required: No

 ** [NameContains](#API_ListHubContents_RequestSyntax) **   <a name="sagemaker-ListHubContents-request-NameContains"></a>
Only list hub content if the name contains the specified string.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9\-]+`
Required: No

 ** [NextToken](#API_ListHubContents_RequestSyntax) **   <a name="sagemaker-ListHubContents-request-NextToken"></a>
If the response to a previous `ListHubContents` request was truncated, the response includes a `NextToken`. To retrieve the next set of hub content, use the token in the next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListHubContents_RequestSyntax) **   <a name="sagemaker-ListHubContents-request-SortBy"></a>
Sort hub content versions by either name or creation time.
Type: String
Valid Values: `HubContentName | CreationTime | HubContentStatus`
Required: No

 ** [SortOrder](#API_ListHubContents_RequestSyntax) **   <a name="sagemaker-ListHubContents-request-SortOrder"></a>
Sort hubs by ascending or descending order.
Type: String
Valid Values: `Ascending | Descending`
Required: No

## Response Syntax
<a name="API_ListHubContents_ResponseSyntax"></a>

```
{
   "HubContentSummaries": [
      {
         "DocumentSchemaVersion": "string",
         "HubContentArn": "string",
         "HubContentDescription": "string",
         "HubContentDisplayName": "string",
         "HubContentName": "string",
         "HubContentSearchKeywords": [ "string" ],
         "HubContentStatus": "string",
         "HubContentType": "string",
         "HubContentVersion": "string",
         "SageMakerPublicHubContentArn": "string",
         "SupportStatus": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListHubContents_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [HubContentSummaries](#API_ListHubContents_ResponseSyntax) **   <a name="sagemaker-ListHubContents-response-HubContentSummaries"></a>
The summaries of the listed hub content.
Type: Array of [HubContentInfo](API_HubContentInfo.md) objects

 ** [NextToken](#API_ListHubContents_ResponseSyntax) **   <a name="sagemaker-ListHubContents-response-NextToken"></a>
If the response is truncated, SageMaker returns this token. To retrieve the next set of hub content, use it in the subsequent request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListHubContents_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_ListHubContents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListHubContents)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListHubContents)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListHubContents)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListHubContents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListHubContents)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListHubContents)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListHubContents)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListHubContents)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListHubContents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListHubContents)
