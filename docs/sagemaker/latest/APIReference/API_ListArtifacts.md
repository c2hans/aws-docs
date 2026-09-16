---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListArtifacts.html
---

# ListArtifacts
<a name="API_ListArtifacts"></a>

Lists the artifacts in your account and their properties.

## Request Syntax
<a name="API_ListArtifacts_RequestSyntax"></a>

```
{
   "ArtifactType": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}",
   "SourceUri": "{{string}}"
}
```

## Request Parameters
<a name="API_ListArtifacts_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ArtifactType](#API_ListArtifacts_RequestSyntax) **   <a name="sagemaker-ListArtifacts-request-ArtifactType"></a>
A filter that returns only artifacts of the specified type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [MaxResults](#API_ListArtifacts_RequestSyntax) **   <a name="sagemaker-ListArtifacts-request-MaxResults"></a>
The maximum number of artifacts to return in the response. The default value is 10.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListArtifacts_RequestSyntax) **   <a name="sagemaker-ListArtifacts-request-NextToken"></a>
If the previous call to `ListArtifacts` didn't return the full set of artifacts, the call returns a token for getting the next set of artifacts.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListArtifacts_RequestSyntax) **   <a name="sagemaker-ListArtifacts-request-SortBy"></a>
The property used to sort results. The default value is `CreationTime`.
Type: String
Valid Values: `CreationTime`
Required: No

 ** [SortOrder](#API_ListArtifacts_RequestSyntax) **   <a name="sagemaker-ListArtifacts-request-SortOrder"></a>
The sort order. The default value is `Descending`.
Type: String
Valid Values: `Ascending | Descending`
Required: No

 ** [SourceUri](#API_ListArtifacts_RequestSyntax) **   <a name="sagemaker-ListArtifacts-request-SourceUri"></a>
A filter that returns only artifacts with the specified source URI.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `.*`
Required: No

## Response Syntax
<a name="API_ListArtifacts_ResponseSyntax"></a>

```
{
   "ArtifactSummaries": [
      {
         "ArtifactArn": "string",
         "ArtifactName": "string",
         "ArtifactType": "string",
         "Source": {
            "SourceTypes": [
               {
                  "SourceIdType": "string",
                  "Value": "string"
               }
            ],
            "SourceUri": "string"
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListArtifacts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ArtifactSummaries](#API_ListArtifacts_ResponseSyntax) **   <a name="sagemaker-ListArtifacts-response-ArtifactSummaries"></a>
A list of artifacts and their properties.
Type: Array of [ArtifactSummary](API_ArtifactSummary.md) objects

 ** [NextToken](#API_ListArtifacts_ResponseSyntax) **   <a name="sagemaker-ListArtifacts-response-NextToken"></a>
A token for getting the next set of artifacts, if there are any.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListArtifacts_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_ListArtifacts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListArtifacts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListArtifacts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListArtifacts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListArtifacts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListArtifacts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListArtifacts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListArtifacts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListArtifacts)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListArtifacts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListArtifacts)
