---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListClusterExtensionVersions.html
---

# ListClusterExtensionVersions
<a name="API_ListClusterExtensionVersions"></a>

Lists the versions of an extension that you can install on a SageMaker HyperPod cluster, from the highest version to the lowest. Use a version from this list as the `ExtensionVersion` in `CreateClusterExtension` or `UpdateClusterExtension`.

The list contains only versions that you can install. Versions that SageMaker HyperPod no longer offers for new installations don't appear. If SageMaker HyperPod doesn't offer an extension with the name that you specify, the response contains an empty list.

## Request Syntax
<a name="API_ListClusterExtensionVersions_RequestSyntax"></a>

```
{
   "ExtensionName": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListClusterExtensionVersions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ExtensionName](#API_ListClusterExtensionVersions_RequestSyntax) **   <a name="sagemaker-ListClusterExtensionVersions-request-ExtensionName"></a>
The name of the extension whose versions you want to list, for example `sagemaker-observability`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-z]([a-z0-9]|-[a-z0-9])*`
Required: Yes

 ** [MaxResults](#API_ListClusterExtensionVersions_RequestSyntax) **   <a name="sagemaker-ListClusterExtensionVersions-request-MaxResults"></a>
The maximum number of versions to return in the response. If you don't specify a value, SageMaker HyperPod returns up to 100 versions.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListClusterExtensionVersions_RequestSyntax) **   <a name="sagemaker-ListClusterExtensionVersions-request-NextToken"></a>
If the result of the previous `ListClusterExtensionVersions` request was truncated, the response includes a `NextToken`. To retrieve the next set of versions, use the token in the next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

## Response Syntax
<a name="API_ListClusterExtensionVersions_ResponseSyntax"></a>

```
{
   "ExtensionVersions": [
      {
         "ExtensionVersion": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListClusterExtensionVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ExtensionVersions](#API_ListClusterExtensionVersions_ResponseSyntax) **   <a name="sagemaker-ListClusterExtensionVersions-response-ExtensionVersions"></a>
The versions of the extension that you can install, from the highest version to the lowest.
Type: Array of [ExtensionVersionSummary](API_ExtensionVersionSummary.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [NextToken](#API_ListClusterExtensionVersions_ResponseSyntax) **   <a name="sagemaker-ListClusterExtensionVersions-response-NextToken"></a>
If the response is truncated, a token that you can use in the next request to retrieve the next set of versions.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListClusterExtensionVersions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListClusterExtensionVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListClusterExtensionVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListClusterExtensionVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListClusterExtensionVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListClusterExtensionVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListClusterExtensionVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListClusterExtensionVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListClusterExtensionVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListClusterExtensionVersions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListClusterExtensionVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListClusterExtensionVersions)
