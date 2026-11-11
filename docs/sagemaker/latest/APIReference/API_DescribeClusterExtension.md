---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeClusterExtension.html
---

# DescribeClusterExtension
<a name="API_DescribeClusterExtension"></a>

Retrieves information about an extension installed on a SageMaker HyperPod cluster. The information includes the extension's version, configuration, and status, and a summary of how many cluster nodes are running the current version and configuration of the extension.

## Request Syntax
<a name="API_DescribeClusterExtension_RequestSyntax"></a>

```
{
   "ClusterArn": "{{string}}",
   "ExtensionArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeClusterExtension_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterArn](#API_DescribeClusterExtension_RequestSyntax) **   <a name="sagemaker-DescribeClusterExtension-request-ClusterArn"></a>
The Amazon Resource Name (ARN) of the SageMaker HyperPod cluster on which the extension is installed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:cluster/[a-z0-9]{12}`
Required: Yes

 ** [ExtensionArn](#API_DescribeClusterExtension_RequestSyntax) **   <a name="sagemaker-DescribeClusterExtension-request-ExtensionArn"></a>
The Amazon Resource Name (ARN) of the extension to describe. `CreateClusterExtension` returns this ARN, and `ListClusterExtensions` lists it. If you delete an extension and create it again, the new extension has a new ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:extension/(sagemaker|eks|pcs)-[a-z0-9-]+/[a-z0-9-]+/[a-z0-9]+`
Required: Yes

## Response Syntax
<a name="API_DescribeClusterExtension_ResponseSyntax"></a>

```
{
   "ExtensionDetails": {
      "ClusterArn": "string",
      "ConfigurationValues": "string",
      "CreationTime": number,
      "ExtensionArn": "string",
      "ExtensionName": "string",
      "ExtensionVersion": "string",
      "LastModifiedTime": number,
      "Status": "string"
   },
   "NodeSummary": {
      "ActiveCount": number,
      "TotalCount": number
   }
}
```

## Response Elements
<a name="API_DescribeClusterExtension_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ExtensionDetails](#API_DescribeClusterExtension_ResponseSyntax) **   <a name="sagemaker-DescribeClusterExtension-response-ExtensionDetails"></a>
The details of the extension.
Type: [ExtensionDetails](API_ExtensionDetails.md) object

 ** [NodeSummary](#API_DescribeClusterExtension_ResponseSyntax) **   <a name="sagemaker-DescribeClusterExtension-response-NodeSummary"></a>
A summary of how many nodes in your cluster the extension targets, and how many of them run the extension's current version and configuration.
Type: [ExtensionNodeSummary](API_ExtensionNodeSummary.md) object

## Errors
<a name="API_DescribeClusterExtension_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeClusterExtension_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeClusterExtension)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeClusterExtension)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeClusterExtension)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeClusterExtension)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeClusterExtension)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeClusterExtension)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeClusterExtension)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeClusterExtension)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeClusterExtension)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeClusterExtension)
