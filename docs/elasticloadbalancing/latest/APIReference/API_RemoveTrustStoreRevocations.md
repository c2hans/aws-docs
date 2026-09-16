---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_RemoveTrustStoreRevocations.html
---

# RemoveTrustStoreRevocations
<a name="API_RemoveTrustStoreRevocations"></a>

Removes the specified revocation file from the specified trust store.

## Request Parameters
<a name="API_RemoveTrustStoreRevocations_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **RevocationIds.member.N**
The revocation IDs of the revocation files you want to remove.
Type: Array of longs
Required: Yes

 ** TrustStoreArn **
The Amazon Resource Name (ARN) of the trust store.
Type: String
Required: Yes

## Errors
<a name="API_RemoveTrustStoreRevocations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** RevocationIdNotFound **
The specified revocation ID does not exist.
HTTP Status Code: 400

 ** TrustStoreNotFound **
The specified trust store does not exist.
HTTP Status Code: 400

## Examples
<a name="API_RemoveTrustStoreRevocations_Examples"></a>

### Remove a revocation file from a trust store.
<a name="API_RemoveTrustStoreRevocations_Example_1"></a>

This example removes the specified certificate revocation ID from the specified trust store.

#### Sample Request
<a name="API_RemoveTrustStoreRevocations_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=RemoveTrustStoreRevocations
&TrustStoreArn=arn:aws:elasticloadbalancing:us-east-1:111122223333:truststore/my-trust-store/3ym756xh7yj
&RevocationIds.member.1.RevocationID=1
&Version=2015-12-01
&AUTHPARAMS
```

## See Also
<a name="API_RemoveTrustStoreRevocations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancingv2-2015-12-01/RemoveTrustStoreRevocations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancingv2-2015-12-01/RemoveTrustStoreRevocations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/RemoveTrustStoreRevocations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancingv2-2015-12-01/RemoveTrustStoreRevocations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/RemoveTrustStoreRevocations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancingv2-2015-12-01/RemoveTrustStoreRevocations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancingv2-2015-12-01/RemoveTrustStoreRevocations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancingv2-2015-12-01/RemoveTrustStoreRevocations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancingv2-2015-12-01/RemoveTrustStoreRevocations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/RemoveTrustStoreRevocations)
