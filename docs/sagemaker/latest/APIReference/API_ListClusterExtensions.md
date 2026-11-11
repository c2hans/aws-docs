---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListClusterExtensions.html
---

# ListClusterExtensions
<a name="API_ListClusterExtensions"></a>

Lists the extensions installed on a SageMaker HyperPod cluster.

## Request Syntax
<a name="API_ListClusterExtensions_RequestSyntax"></a>

```
{
   "ClusterArn": "{{string}}",
   "CreationTimeAfter": {{number}},
   "CreationTimeBefore": {{number}},
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListClusterExtensions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterArn](#API_ListClusterExtensions_RequestSyntax) **   <a name="sagemaker-ListClusterExtensions-request-ClusterArn"></a>
The Amazon Resource Name (ARN) of the SageMaker HyperPod cluster whose extensions you want to list.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:cluster/[a-z0-9]{12}`
Required: Yes

 ** [CreationTimeAfter](#API_ListClusterExtensions_RequestSyntax) **   <a name="sagemaker-ListClusterExtensions-request-CreationTimeAfter"></a>
A filter that returns extensions created at or after the specified time. Timestamps are formatted according to the ISO 8601 standard.
Type: Timestamp
Required: No

 ** [CreationTimeBefore](#API_ListClusterExtensions_RequestSyntax) **   <a name="sagemaker-ListClusterExtensions-request-CreationTimeBefore"></a>
A filter that returns extensions created at or before the specified time. The acceptable formats are the same as the timestamp formats for `CreationTimeAfter`.
Type: Timestamp
Required: No

 ** [MaxResults](#API_ListClusterExtensions_RequestSyntax) **   <a name="sagemaker-ListClusterExtensions-request-MaxResults"></a>
The maximum number of extensions to return in the response. If you don't specify a value, SageMaker HyperPod returns up to 100 extensions.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListClusterExtensions_RequestSyntax) **   <a name="sagemaker-ListClusterExtensions-request-NextToken"></a>
If the result of the previous `ListClusterExtensions` request was truncated, the response includes a `NextToken`. To retrieve the next set of extensions, use the token in the next request. When you use the `CreationTimeAfter` or `CreationTimeBefore` filters, a response can contain fewer extensions than `MaxResults`, or none, and still include a `NextToken`. Continue until the response doesn't include a `NextToken`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

## Response Syntax
<a name="API_ListClusterExtensions_ResponseSyntax"></a>

```
{
   "Extensions": [
      {
         "CreationTime": number,
         "ExtensionArn": "string",
         "ExtensionName": "string",
         "ExtensionVersion": "string",
         "Status": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListClusterExtensions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Extensions](#API_ListClusterExtensions_ResponseSyntax) **   <a name="sagemaker-ListClusterExtensions-response-Extensions"></a>
The list of extensions installed on the cluster.
Type: Array of [ExtensionSummary](API_ExtensionSummary.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [NextToken](#API_ListClusterExtensions_ResponseSyntax) **   <a name="sagemaker-ListClusterExtensions-response-NextToken"></a>
The next token specified for listing extensions on a SageMaker HyperPod cluster.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListClusterExtensions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_ListClusterExtensions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListClusterExtensions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListClusterExtensions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListClusterExtensions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListClusterExtensions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListClusterExtensions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListClusterExtensions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListClusterExtensions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListClusterExtensions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListClusterExtensions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListClusterExtensions)
