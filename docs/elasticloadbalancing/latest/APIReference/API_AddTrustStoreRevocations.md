---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_AddTrustStoreRevocations.html
---

# AddTrustStoreRevocations
<a name="API_AddTrustStoreRevocations"></a>

Adds the specified revocation file to the specified trust store.

## Request Parameters
<a name="API_AddTrustStoreRevocations_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **RevocationContents.member.N**
The revocation file to add.
Type: Array of [RevocationContent](API_RevocationContent.md) objects
Required: No

 ** TrustStoreArn **
The Amazon Resource Name (ARN) of the trust store.
Type: String
Required: Yes

## Response Elements
<a name="API_AddTrustStoreRevocations_ResponseElements"></a>

The following element is returned by the service.

 **TrustStoreRevocations.member.N**
Information about the revocation file added to the trust store.
Type: Array of [TrustStoreRevocation](API_TrustStoreRevocation.md) objects

## Errors
<a name="API_AddTrustStoreRevocations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidRevocationContent **
The provided revocation file is an invalid format, or uses an incorrect algorithm.
HTTP Status Code: 400

 ** RevocationContentNotFound **
The specified revocation file does not exist.
HTTP Status Code: 400

 ** TooManyTrustStoreRevocationEntries **
The specified trust store has too many revocation entries.
HTTP Status Code: 400

 ** TrustStoreNotFound **
The specified trust store does not exist.
HTTP Status Code: 400

## Examples
<a name="API_AddTrustStoreRevocations_Examples"></a>

### Add a revocation file to a trust store.
<a name="API_AddTrustStoreRevocations_Example_1"></a>

This example adds the specified certificate revocation list to the specified trust store.

#### Sample Request
<a name="API_AddTrustStoreRevocations_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=AddTrustStoreRevocations
&TrustStoreArn=arn:aws:elasticloadbalancing:us-east-1:111122223333:truststore/my-trust-store/3ym756xh7yj
&RevocationContents.member.1.RevocationType=CRL
&RevocationContents.member.1.S3Bucket=amzn-s3-demo-bucket
&RevocationContents.member.1.S3Key=my-crl.pem
&Version=2015-12-01
&AUTHPARAMS
```

## See Also
<a name="API_AddTrustStoreRevocations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancingv2-2015-12-01/AddTrustStoreRevocations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancingv2-2015-12-01/AddTrustStoreRevocations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/AddTrustStoreRevocations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancingv2-2015-12-01/AddTrustStoreRevocations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/AddTrustStoreRevocations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancingv2-2015-12-01/AddTrustStoreRevocations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancingv2-2015-12-01/AddTrustStoreRevocations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancingv2-2015-12-01/AddTrustStoreRevocations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancingv2-2015-12-01/AddTrustStoreRevocations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/AddTrustStoreRevocations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Elastic Load Balancing. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticloadbalancing` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
