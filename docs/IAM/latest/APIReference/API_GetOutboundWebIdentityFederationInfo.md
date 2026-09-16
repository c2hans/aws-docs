---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetOutboundWebIdentityFederationInfo.html
---

# GetOutboundWebIdentityFederationInfo
<a name="API_GetOutboundWebIdentityFederationInfo"></a>

Retrieves the configuration information for the outbound identity federation feature in your AWS account. The response includes the unique issuer URL for your AWS account and the current enabled/disabled status of the feature. Use this operation to obtain the issuer URL that you need to configure trust relationships with external services.

## Response Elements
<a name="API_GetOutboundWebIdentityFederationInfo_ResponseElements"></a>

The following elements are returned by the service.

 ** IssuerIdentifier **
A unique issuer URL for your AWS account that hosts the OpenID Connect (OIDC) discovery endpoints at `/.well-known/openid-configuration and /.well-known/jwks.json`. The OpenID Connect (OIDC) discovery endpoints contain verification keys and metadata necessary for token verification.
Type: String

 ** JwtVendingEnabled **
Indicates whether outbound identity federation is currently enabled for your AWS account. When true, IAM principals in the account can call the `GetWebIdentityToken` API to obtain JSON Web Tokens (JWTs) for authentication with external services.
Type: Boolean

## Errors
<a name="API_GetOutboundWebIdentityFederationInfo_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** FeatureDisabled **
The request failed because outbound identity federation is already disabled for your AWS account. You cannot disable the feature multiple times
HTTP Status Code: 404

## Examples
<a name="API_GetOutboundWebIdentityFederationInfo_Examples"></a>

### Example
<a name="API_GetOutboundWebIdentityFederationInfo_Example_1"></a>

This example illustrates one usage of GetOutboundWebIdentityFederationInfo.

#### Sample Request
<a name="API_GetOutboundWebIdentityFederationInfo_Example_1_Request"></a>

```
                https://iam.amazonaws.com/?Action=GetOutboundWebIdentityFederationInfo
                &Version=2010-05-08
                &AUTHPARAMS
```

#### Sample Response
<a name="API_GetOutboundWebIdentityFederationInfo_Example_1_Response"></a>

```
                <GetOutboundWebIdentityFederationInfoResponse>
                  <GetOutboundWebIdentityFederationInfoResult>
                    <IssuerIdentifier>https://a1d2b0fd-1177-4468-9351-2fEXAMPLE723.tokens.sts.global.api.aws</IssuerIdentifier>
                    <JwtVendingEnabled>true</JwtVendingEnabled>
                  </GetOutboundWebIdentityFederationInfoResult>
                  <ResponseMetadata>
                    <RequestId>a6dac9b4-fdc8-4489-acec-b1EXAMPLEf44</RequestId>
                  </ResponseMetadata>
                </GetOutboundWebIdentityFederationInfoResponse>
```

## See Also
<a name="API_GetOutboundWebIdentityFederationInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/GetOutboundWebIdentityFederationInfo)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/GetOutboundWebIdentityFederationInfo)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/GetOutboundWebIdentityFederationInfo)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/GetOutboundWebIdentityFederationInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/GetOutboundWebIdentityFederationInfo)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/GetOutboundWebIdentityFederationInfo)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/GetOutboundWebIdentityFederationInfo)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/GetOutboundWebIdentityFederationInfo)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/GetOutboundWebIdentityFederationInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/GetOutboundWebIdentityFederationInfo)
