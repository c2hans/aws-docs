---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsAppSyncGraphQlApiOpenIdConnectConfigDetails.html
---

# AwsAppSyncGraphQlApiOpenIdConnectConfigDetails
<a name="API_AwsAppSyncGraphQlApiOpenIdConnectConfigDetails"></a>

 Specifies the authorization configuration for using an OpenID Connect compliant service with your AWS AppSync GraphQL API endpoint.

## Contents
<a name="API_AwsAppSyncGraphQlApiOpenIdConnectConfigDetails_Contents"></a>

 ** AuthTtL **   <a name="securityhub-Type-AwsAppSyncGraphQlApiOpenIdConnectConfigDetails-AuthTtL"></a>
 The number of milliseconds that a token is valid after being authenticated.
Type: Long
Required: No

 ** ClientId **   <a name="securityhub-Type-AwsAppSyncGraphQlApiOpenIdConnectConfigDetails-ClientId"></a>
 The client identifier of the relying party at the OpenID identity provider. This identifier is typically obtained when the relying party is registered with the OpenID identity provider. You can specify a regular expression so that AWS AppSync can validate against multiple client identifiers at a time.
Type: String
Pattern: `.*\S.*`
Required: No

 ** IatTtL **   <a name="securityhub-Type-AwsAppSyncGraphQlApiOpenIdConnectConfigDetails-IatTtL"></a>
 The number of milliseconds that a token is valid after it's issued to a user.
Type: Long
Required: No

 ** Issuer **   <a name="securityhub-Type-AwsAppSyncGraphQlApiOpenIdConnectConfigDetails-Issuer"></a>
 The issuer for the OIDC configuration. The issuer returned by discovery must exactly match the value of `iss` in the ID token.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsAppSyncGraphQlApiOpenIdConnectConfigDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsAppSyncGraphQlApiOpenIdConnectConfigDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsAppSyncGraphQlApiOpenIdConnectConfigDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsAppSyncGraphQlApiOpenIdConnectConfigDetails)
