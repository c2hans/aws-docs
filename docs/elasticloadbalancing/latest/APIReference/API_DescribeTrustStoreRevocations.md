---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeTrustStoreRevocations.html
---

# DescribeTrustStoreRevocations
<a name="API_DescribeTrustStoreRevocations"></a>

Describes the revocation files in use by the specified trust store or revocation files.

## Request Parameters
<a name="API_DescribeTrustStoreRevocations_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** Marker **
The marker for the next set of results. (You received this marker from a previous call.)
Type: String
Required: No

 ** PageSize **
The maximum number of results to return with this call.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 400.
Required: No

 **RevocationIds.member.N**
The revocation IDs of the revocation files you want to describe.
Type: Array of longs
Required: No

 ** TrustStoreArn **
The Amazon Resource Name (ARN) of the trust store.
Type: String
Required: Yes

## Response Elements
<a name="API_DescribeTrustStoreRevocations_ResponseElements"></a>

The following elements are returned by the service.

 ** NextMarker **
If there are additional results, this is the marker for the next set of results. Otherwise, this is null.
Type: String

 **TrustStoreRevocations.member.N**
Information about the revocation file in the trust store.
Type: Array of [DescribeTrustStoreRevocation](API_DescribeTrustStoreRevocation.md) objects

## Errors
<a name="API_DescribeTrustStoreRevocations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** RevocationIdNotFound **
The specified revocation ID does not exist.
HTTP Status Code: 400

 ** TrustStoreNotFound **
The specified trust store does not exist.
HTTP Status Code: 400

## Examples
<a name="API_DescribeTrustStoreRevocations_Examples"></a>

### Describe revocation file contents from a trust store.
<a name="API_DescribeTrustStoreRevocations_Example_1"></a>

This example describes the specified certificate revocation IDs list contents from the specified trust store.

#### Sample Request
<a name="API_DescribeTrustStoreRevocations_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=DescribeTrustStoreRevocations
&TrustStoreArn=arn:aws:elasticloadbalancing:us-east-1:111122223333:truststore/my-trust-store/3ym756xh7yj
&RevocationIds.member.1.RevocationId=1
&Version=2015-12-01
&AUTHPARAMS
```

## See Also
<a name="API_DescribeTrustStoreRevocations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancingv2-2015-12-01/DescribeTrustStoreRevocations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancingv2-2015-12-01/DescribeTrustStoreRevocations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/DescribeTrustStoreRevocations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancingv2-2015-12-01/DescribeTrustStoreRevocations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/DescribeTrustStoreRevocations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancingv2-2015-12-01/DescribeTrustStoreRevocations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancingv2-2015-12-01/DescribeTrustStoreRevocations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancingv2-2015-12-01/DescribeTrustStoreRevocations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancingv2-2015-12-01/DescribeTrustStoreRevocations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/DescribeTrustStoreRevocations)
