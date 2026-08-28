---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeTrustStores.html
---

# DescribeTrustStores
<a name="API_DescribeTrustStores"></a>

Describes all trust stores for the specified account.

## Request Parameters
<a name="API_DescribeTrustStores_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** Marker **
The marker for the next set of results. (You received this marker from a previous call.)
Type: String
Required: No

 **Names.member.N**
The names of the trust stores.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `^([a-zA-Z0-9]+-)*[a-zA-Z0-9]+$`
Required: No

 ** PageSize **
The maximum number of results to return with this call.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 400.
Required: No

 **TrustStoreArns.member.N**
The Amazon Resource Name (ARN) of the trust store.
Type: Array of strings
Required: No

## Response Elements
<a name="API_DescribeTrustStores_ResponseElements"></a>

The following elements are returned by the service.

 ** NextMarker **
If there are additional results, this is the marker for the next set of results. Otherwise, this is null.
Type: String

 **TrustStores.member.N**
Information about the trust stores.
Type: Array of [TrustStore](API_TrustStore.md) objects

## Errors
<a name="API_DescribeTrustStores_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** TrustStoreNotFound **
The specified trust store does not exist.
HTTP Status Code: 400

## Examples
<a name="API_DescribeTrustStores_Examples"></a>

### Describe a trust store.
<a name="API_DescribeTrustStores_Example_1"></a>

This example describes the specified trust store.

#### Sample Request
<a name="API_DescribeTrustStores_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=DescribeTrustStores
&TrustStoreArns.member.1.TrustStoreArn=arn:aws:elasticloadbalancing:us-east-1:111122223333:truststore/my-trust-store/3ym756xh7yj
&Version=2015-12-01
&AUTHPARAMS
```

## See Also
<a name="API_DescribeTrustStores_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancingv2-2015-12-01/DescribeTrustStores)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancingv2-2015-12-01/DescribeTrustStores)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/DescribeTrustStores)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancingv2-2015-12-01/DescribeTrustStores)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/DescribeTrustStores)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancingv2-2015-12-01/DescribeTrustStores)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancingv2-2015-12-01/DescribeTrustStores)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancingv2-2015-12-01/DescribeTrustStores)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancingv2-2015-12-01/DescribeTrustStores)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/DescribeTrustStores)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Elastic Load Balancing. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticloadbalancing` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
