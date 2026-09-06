---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_ModifyTrustStore.html
---

# ModifyTrustStore
<a name="API_ModifyTrustStore"></a>

Update the ca certificate bundle for the specified trust store.

## Request Parameters
<a name="API_ModifyTrustStore_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** CaCertificatesBundleS3Bucket **
The Amazon S3 bucket for the ca certificates bundle.
Type: String
Required: Yes

 ** CaCertificatesBundleS3Key **
The Amazon S3 path for the ca certificates bundle.
Type: String
Required: Yes

 ** CaCertificatesBundleS3ObjectVersion **
The Amazon S3 object version for the ca certificates bundle. If undefined the current version is used.
Type: String
Required: No

 ** TrustStoreArn **
The Amazon Resource Name (ARN) of the trust store.
Type: String
Required: Yes

## Response Elements
<a name="API_ModifyTrustStore_ResponseElements"></a>

The following element is returned by the service.

 **TrustStores.member.N**
Information about the modified trust store.
Type: Array of [TrustStore](API_TrustStore.md) objects

## Errors
<a name="API_ModifyTrustStore_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CaCertificatesBundleNotFound **
The specified ca certificate bundle does not exist.
HTTP Status Code: 400

 ** InvalidCaCertificatesBundle **
The specified ca certificate bundle is in an invalid format, or corrupt.
HTTP Status Code: 400

 ** TrustStoreNotFound **
The specified trust store does not exist.
HTTP Status Code: 400

## Examples
<a name="API_ModifyTrustStore_Examples"></a>

### Modify a trust store.
<a name="API_ModifyTrustStore_Example_1"></a>

This example replaces the ca certificate bundle in the specified trust store.

#### Sample Request
<a name="API_ModifyTrustStore_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=ModifyTrustStore
&TrustStoreArn=arn:aws:elasticloadbalancing:us-east-1:111122223333:truststore/my-trust-store/d5f637c79df8c943
&CaCertificatesBundleS3Bucket=amzn-s3-demo-bucket
&CaCertificatesBundleS3Key=CACertBundle.pem
&Version=2015-12-01
&AUTHPARAMS
```

## See Also
<a name="API_ModifyTrustStore_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancingv2-2015-12-01/ModifyTrustStore)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancingv2-2015-12-01/ModifyTrustStore)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/ModifyTrustStore)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancingv2-2015-12-01/ModifyTrustStore)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/ModifyTrustStore)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancingv2-2015-12-01/ModifyTrustStore)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancingv2-2015-12-01/ModifyTrustStore)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancingv2-2015-12-01/ModifyTrustStore)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancingv2-2015-12-01/ModifyTrustStore)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/ModifyTrustStore)
