---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_CreateTrustStore.html
---

# CreateTrustStore
<a name="API_CreateTrustStore"></a>

Creates a trust store.

For more information, see [Mutual TLS for Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/mutual-authentication.html).

## Request Parameters
<a name="API_CreateTrustStore_RequestParameters"></a>

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

 ** Name **
The name of the trust store.
This name must be unique per region and can't be changed after creation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `^([a-zA-Z0-9]+-)*[a-zA-Z0-9]+$`
Required: Yes

 **Tags.member.N**
The tags to assign to the trust store.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item.
Required: No

## Response Elements
<a name="API_CreateTrustStore_ResponseElements"></a>

The following element is returned by the service.

 **TrustStores.member.N**
Information about the trust store created.
Type: Array of [TrustStore](API_TrustStore.md) objects

## Errors
<a name="API_CreateTrustStore_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CaCertificatesBundleNotFound **
The specified ca certificate bundle does not exist.
HTTP Status Code: 400

 ** DuplicateTagKeys **
A tag key was specified more than once.
HTTP Status Code: 400

 ** DuplicateTrustStoreName **
A trust store with the specified name already exists.
HTTP Status Code: 400

 ** InvalidCaCertificatesBundle **
The specified ca certificate bundle is in an invalid format, or corrupt.
HTTP Status Code: 400

 ** TooManyTags **
You've reached the limit on the number of tags for this resource.
HTTP Status Code: 400

 ** TooManyTrustStores **
You've reached the limit on the number of trust stores for your AWS account.
HTTP Status Code: 400

## Examples
<a name="API_CreateTrustStore_Examples"></a>

### Create a trust store.
<a name="API_CreateTrustStore_Example_1"></a>

This example creates a trust store using the current version of the specified ca certificate bundle.

#### Sample Request
<a name="API_CreateTrustStore_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=CreateTrustStore
&Name=my-trust-store
&CaCertificatesBundleS3Bucket=amzn-s3-demo-bucket
&CaCertificatesBundleS3Key=CACertBundle.pem
&Version=2015-12-01
&AUTHPARAMS
```

## See Also
<a name="API_CreateTrustStore_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancingv2-2015-12-01/CreateTrustStore)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancingv2-2015-12-01/CreateTrustStore)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/CreateTrustStore)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancingv2-2015-12-01/CreateTrustStore)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/CreateTrustStore)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancingv2-2015-12-01/CreateTrustStore)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancingv2-2015-12-01/CreateTrustStore)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancingv2-2015-12-01/CreateTrustStore)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancingv2-2015-12-01/CreateTrustStore)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/CreateTrustStore)
