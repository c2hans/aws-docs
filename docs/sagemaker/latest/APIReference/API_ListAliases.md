---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListAliases.html
---

# ListAliases
<a name="API_ListAliases"></a>

Lists the aliases of a specified image or image version.

## Request Syntax
<a name="API_ListAliases_RequestSyntax"></a>

```
{
   "Alias": "{{string}}",
   "ImageName": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "Version": {{number}}
}
```

## Request Parameters
<a name="API_ListAliases_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Alias](#API_ListAliases_RequestSyntax) **   <a name="sagemaker-ListAliases-request-Alias"></a>
The alias of the image version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(?!^[.-])^([a-zA-Z0-9-_.]+)`
Required: No

 ** [ImageName](#API_ListAliases_RequestSyntax) **   <a name="sagemaker-ListAliases-request-ImageName"></a>
The name of the image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9]([-.]?[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [MaxResults](#API_ListAliases_RequestSyntax) **   <a name="sagemaker-ListAliases-request-MaxResults"></a>
The maximum number of aliases to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListAliases_RequestSyntax) **   <a name="sagemaker-ListAliases-request-NextToken"></a>
If the previous call to `ListAliases` didn't return the full set of aliases, the call returns a token for retrieving the next set of aliases.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [Version](#API_ListAliases_RequestSyntax) **   <a name="sagemaker-ListAliases-request-Version"></a>
The version of the image. If image version is not specified, the aliases of all versions of the image are listed.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## Response Syntax
<a name="API_ListAliases_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "SageMakerImageVersionAliases": [ "string" ]
}
```

## Response Elements
<a name="API_ListAliases_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListAliases_ResponseSyntax) **   <a name="sagemaker-ListAliases-response-NextToken"></a>
A token for getting the next set of aliases, if more aliases exist.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

 ** [SageMakerImageVersionAliases](#API_ListAliases_ResponseSyntax) **   <a name="sagemaker-ListAliases-response-SageMakerImageVersionAliases"></a>
A list of SageMaker AI image version aliases.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(?!^[.-])^([a-zA-Z0-9-_.]+)`

## Errors
<a name="API_ListAliases_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_ListAliases_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListAliases)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListAliases)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListAliases)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListAliases)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListAliases)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListAliases)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListAliases)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListAliases)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListAliases)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListAliases)
