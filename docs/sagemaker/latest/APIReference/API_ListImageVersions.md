---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListImageVersions.html
---

# ListImageVersions
<a name="API_ListImageVersions"></a>

Lists the versions of a specified image and their properties. The list can be filtered by creation time or modified time.

## Request Syntax
<a name="API_ListImageVersions_RequestSyntax"></a>

```
{
   "ImageName": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}"
}
```

## Request Parameters
<a name="API_ListImageVersions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ImageName](#API_ListImageVersions_RequestSyntax) **   <a name="sagemaker-ListImageVersions-request-ImageName"></a>
The name of the image to list the versions of.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9]([-.]?[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [MaxResults](#API_ListImageVersions_RequestSyntax) **   <a name="sagemaker-ListImageVersions-request-MaxResults"></a>
The maximum number of versions to return in the response. The default value is 10.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListImageVersions_RequestSyntax) **   <a name="sagemaker-ListImageVersions-request-NextToken"></a>
If the previous call to `ListImageVersions` didn't return the full set of versions, the call returns a token for getting the next set of versions.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListImageVersions_RequestSyntax) **   <a name="sagemaker-ListImageVersions-request-SortBy"></a>
The property used to sort results. The default value is `CREATION_TIME`.
Type: String
Valid Values: `CREATION_TIME | LAST_MODIFIED_TIME | VERSION`
Required: No

 ** [SortOrder](#API_ListImageVersions_RequestSyntax) **   <a name="sagemaker-ListImageVersions-request-SortOrder"></a>
The sort order. The default value is `DESCENDING`.
Type: String
Valid Values: `ASCENDING | DESCENDING`
Required: No

## Response Syntax
<a name="API_ListImageVersions_ResponseSyntax"></a>

```
{
   "ImageVersions": [
      {
         "FailureReason": "string",
         "ImageArn": "string",
         "ImageVersionArn": "string",
         "ImageVersionStatus": "string",
         "Version": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListImageVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ImageVersions](#API_ListImageVersions_ResponseSyntax) **   <a name="sagemaker-ListImageVersions-response-ImageVersions"></a>
A list of versions and their properties.
Type: Array of [ImageVersion](API_ImageVersion.md) objects

 ** [NextToken](#API_ListImageVersions_ResponseSyntax) **   <a name="sagemaker-ListImageVersions-response-NextToken"></a>
A token for getting the next set of versions, if there are any.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListImageVersions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_ListImageVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListImageVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListImageVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListImageVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListImageVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListImageVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListImageVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListImageVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListImageVersions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListImageVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListImageVersions)
