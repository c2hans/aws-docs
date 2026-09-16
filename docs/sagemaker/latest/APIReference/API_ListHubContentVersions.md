---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListHubContentVersions.html
---

# ListHubContentVersions
<a name="API_ListHubContentVersions"></a>

List hub content versions.

## Request Syntax
<a name="API_ListHubContentVersions_RequestSyntax"></a>

```
{
   "HubContentName": "{{string}}",
   "HubContentType": "{{string}}",
   "HubName": "{{string}}",
   "MaxResults": {{number}},
   "MaxSchemaVersion": "{{string}}",
   "MinVersion": "{{string}}",
   "NextToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}"
}
```

## Request Parameters
<a name="API_ListHubContentVersions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [HubContentName](#API_ListHubContentVersions_RequestSyntax) **   <a name="sagemaker-ListHubContentVersions-request-HubContentName"></a>
The name of the hub content.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [HubContentType](#API_ListHubContentVersions_RequestSyntax) **   <a name="sagemaker-ListHubContentVersions-request-HubContentType"></a>
The type of hub content to list versions of.
Type: String
Valid Values: `Model | Notebook | ModelReference | DataSet | JsonDoc`
Required: Yes

 ** [HubName](#API_ListHubContentVersions_RequestSyntax) **   <a name="sagemaker-ListHubContentVersions-request-HubName"></a>
The name of the hub to list the content versions of.
Type: String
Pattern: `(arn:[a-z0-9-\.]{1,63}:sagemaker:\w+(?:-\w+)+:(\d{12}|aws):hub\/)?[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [MaxResults](#API_ListHubContentVersions_RequestSyntax) **   <a name="sagemaker-ListHubContentVersions-request-MaxResults"></a>
The maximum number of hub content versions to list.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [MaxSchemaVersion](#API_ListHubContentVersions_RequestSyntax) **   <a name="sagemaker-ListHubContentVersions-request-MaxSchemaVersion"></a>
The upper bound of the hub content schema version.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 14.
Pattern: `\d{1,4}.\d{1,4}.\d{1,4}`
Required: No

 ** [MinVersion](#API_ListHubContentVersions_RequestSyntax) **   <a name="sagemaker-ListHubContentVersions-request-MinVersion"></a>
The lower bound of the hub content versions to list.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 14.
Pattern: `\d{1,4}.\d{1,4}.\d{1,4}`
Required: No

 ** [NextToken](#API_ListHubContentVersions_RequestSyntax) **   <a name="sagemaker-ListHubContentVersions-request-NextToken"></a>
If the response to a previous `ListHubContentVersions` request was truncated, the response includes a `NextToken`. To retrieve the next set of hub content versions, use the token in the next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListHubContentVersions_RequestSyntax) **   <a name="sagemaker-ListHubContentVersions-request-SortBy"></a>
Sort hub content versions by either name or creation time.
Type: String
Valid Values: `HubContentName | CreationTime | HubContentStatus`
Required: No

 ** [SortOrder](#API_ListHubContentVersions_RequestSyntax) **   <a name="sagemaker-ListHubContentVersions-request-SortOrder"></a>
Sort hub content versions by ascending or descending order.
Type: String
Valid Values: `Ascending | Descending`
Required: No

## Response Syntax
<a name="API_ListHubContentVersions_ResponseSyntax"></a>

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
<a name="API_ListHubContentVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [HubContentSummaries](#API_ListHubContentVersions_ResponseSyntax) **   <a name="sagemaker-ListHubContentVersions-response-HubContentSummaries"></a>
The summaries of the listed hub content versions.
Type: Array of [HubContentInfo](API_HubContentInfo.md) objects

 ** [NextToken](#API_ListHubContentVersions_ResponseSyntax) **   <a name="sagemaker-ListHubContentVersions-response-NextToken"></a>
If the response is truncated, SageMaker returns this token. To retrieve the next set of hub content versions, use it in the subsequent request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListHubContentVersions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_ListHubContentVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListHubContentVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListHubContentVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListHubContentVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListHubContentVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListHubContentVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListHubContentVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListHubContentVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListHubContentVersions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListHubContentVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListHubContentVersions)
