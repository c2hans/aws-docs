---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteClusterExtension.html
---

# DeleteClusterExtension
<a name="API_DeleteClusterExtension"></a>

Deletes an extension from a SageMaker HyperPod cluster. SageMaker HyperPod removes the extension's software from every node in the cluster. While SageMaker HyperPod removes the extension, its status is `Deleting`. After SageMaker HyperPod removes the extension from all nodes, it no longer appears in `ListClusterExtensions`, and `DescribeClusterExtension` returns a `ResourceNotFound` error.

Deleting an extension doesn't delete data that the extension sent to other AWS services, such as metrics in Amazon CloudWatch or Amazon Managed Service for Prometheus.

## Request Syntax
<a name="API_DeleteClusterExtension_RequestSyntax"></a>

```
{
   "ClusterArn": "{{string}}",
   "ExtensionArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteClusterExtension_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterArn](#API_DeleteClusterExtension_RequestSyntax) **   <a name="sagemaker-DeleteClusterExtension-request-ClusterArn"></a>
The Amazon Resource Name (ARN) of the SageMaker HyperPod cluster on which the extension is installed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:cluster/[a-z0-9]{12}`
Required: Yes

 ** [ExtensionArn](#API_DeleteClusterExtension_RequestSyntax) **   <a name="sagemaker-DeleteClusterExtension-request-ExtensionArn"></a>
The Amazon Resource Name (ARN) of the extension to delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:extension/(sagemaker|eks|pcs)-[a-z0-9-]+/[a-z0-9-]+/[a-z0-9]+`
Required: Yes

## Response Syntax
<a name="API_DeleteClusterExtension_ResponseSyntax"></a>

```
{
   "ExtensionArn": "string"
}
```

## Response Elements
<a name="API_DeleteClusterExtension_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ExtensionArn](#API_DeleteClusterExtension_ResponseSyntax) **   <a name="sagemaker-DeleteClusterExtension-response-ExtensionArn"></a>
The Amazon Resource Name (ARN) of the extension that is being deleted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:extension/(sagemaker|eks|pcs)-[a-z0-9-]+/[a-z0-9-]+/[a-z0-9]+`

## Errors
<a name="API_DeleteClusterExtension_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
There was a conflict when you attempted to modify a SageMaker entity such as an `Experiment` or `Artifact`.
HTTP Status Code: 400

 ** ResourceInUse **
Resource being accessed is in use.
HTTP Status Code: 400

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DeleteClusterExtension_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DeleteClusterExtension)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DeleteClusterExtension)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DeleteClusterExtension)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DeleteClusterExtension)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DeleteClusterExtension)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DeleteClusterExtension)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DeleteClusterExtension)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DeleteClusterExtension)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DeleteClusterExtension)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DeleteClusterExtension)
