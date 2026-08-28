---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_GetTrustStoreRevocationContent.html
---

# GetTrustStoreRevocationContent
<a name="API_GetTrustStoreRevocationContent"></a>

Retrieves the specified revocation file.

This action returns a pre-signed S3 URI which is active for ten minutes.

## Request Parameters
<a name="API_GetTrustStoreRevocationContent_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** RevocationId **
The revocation ID of the revocation file.
Type: Long
Required: Yes

 ** TrustStoreArn **
The Amazon Resource Name (ARN) of the trust store.
Type: String
Required: Yes

## Response Elements
<a name="API_GetTrustStoreRevocationContent_ResponseElements"></a>

The following element is returned by the service.

 ** Location **
The revocation files Amazon S3 URI.
Type: String

## Errors
<a name="API_GetTrustStoreRevocationContent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** RevocationIdNotFound **
The specified revocation ID does not exist.
HTTP Status Code: 400

 ** TrustStoreNotFound **
The specified trust store does not exist.
HTTP Status Code: 400

## Examples
<a name="API_GetTrustStoreRevocationContent_Examples"></a>

### Retrieve a certificate revocation list.
<a name="API_GetTrustStoreRevocationContent_Example_1"></a>

This example retrieves the specified certificate revocation IDs list contents from the specified trust store and provides a pre-signed S3 URI.

#### Sample Request
<a name="API_GetTrustStoreRevocationContent_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=GetTrustStoreRevocationContent
&TrustStoreArn=arn:aws:elasticloadbalancing:us-east-1:111122223333:truststore/my-trust-store/3ym756xh7yj
&RevocationId=1
&Version=2015-12-01
&AUTHPARAMS
```

## See Also
<a name="API_GetTrustStoreRevocationContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancingv2-2015-12-01/GetTrustStoreRevocationContent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancingv2-2015-12-01/GetTrustStoreRevocationContent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/GetTrustStoreRevocationContent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancingv2-2015-12-01/GetTrustStoreRevocationContent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/GetTrustStoreRevocationContent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancingv2-2015-12-01/GetTrustStoreRevocationContent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancingv2-2015-12-01/GetTrustStoreRevocationContent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancingv2-2015-12-01/GetTrustStoreRevocationContent)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancingv2-2015-12-01/GetTrustStoreRevocationContent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/GetTrustStoreRevocationContent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Elastic Load Balancing. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticloadbalancing` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
