---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_DisableOutboundWebIdentityFederation.html
---

# DisableOutboundWebIdentityFederation
<a name="API_DisableOutboundWebIdentityFederation"></a>

Disables the outbound identity federation feature for your AWS account. When disabled, IAM principals in the account cannot use the `GetWebIdentityToken` API to obtain JSON Web Tokens (JWTs) for authentication with external services. This operation does not affect tokens that were issued before the feature was disabled.

## Errors
<a name="API_DisableOutboundWebIdentityFederation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** FeatureDisabled **
The request failed because outbound identity federation is already disabled for your AWS account. You cannot disable the feature multiple times
HTTP Status Code: 404

## Examples
<a name="API_DisableOutboundWebIdentityFederation_Examples"></a>

### Example
<a name="API_DisableOutboundWebIdentityFederation_Example_1"></a>

This example illustrates one usage of DisableOutboundWebIdentityFederation.

#### Sample Request
<a name="API_DisableOutboundWebIdentityFederation_Example_1_Request"></a>

```
                https://iam.amazonaws.com/?Action=DisableOutboundWebIdentityFederation
                &Version=2010-05-08
                &AUTHPARAMS
```

#### Sample Response
<a name="API_DisableOutboundWebIdentityFederation_Example_1_Response"></a>

```
                <DisableOutboundWebIdentityFederationResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
                  <ResponseMetadata>
                    <RequestId>ddf52f44-6fe3-406a-92f7-3eEXAMPLE21f</RequestId>
                  </ResponseMetadata>
                </DisableOutboundWebIdentityFederationResponse>
```

## See Also
<a name="API_DisableOutboundWebIdentityFederation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/DisableOutboundWebIdentityFederation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/DisableOutboundWebIdentityFederation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/DisableOutboundWebIdentityFederation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/DisableOutboundWebIdentityFederation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/DisableOutboundWebIdentityFederation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/DisableOutboundWebIdentityFederation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/DisableOutboundWebIdentityFederation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/DisableOutboundWebIdentityFederation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/DisableOutboundWebIdentityFederation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/DisableOutboundWebIdentityFederation)
