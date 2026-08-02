---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetails.html
---

# AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetails
<a name="API_AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetails"></a>

 A list of additional authentication providers for the GraphqlApi API.

## Contents
<a name="API_AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetails_Contents"></a>

 ** AuthenticationType **   <a name="securityhub-Type-AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetails-AuthenticationType"></a>
 The type of security configuration for your GraphQL API: API key, AWS Identity and Access Management (IAM), OpenID Connect (OIDC), Amazon Cognito user pools, or AWS Lambda.
Type: String
Pattern: `.*\S.*`
Required: No

 ** LambdaAuthorizerConfig **   <a name="securityhub-Type-AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetails-LambdaAuthorizerConfig"></a>
 The configuration for Lambda function authorization.
Type: [AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetails](API_AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetails.md) object
Required: No

 ** OpenIdConnectConfig **   <a name="securityhub-Type-AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetails-OpenIdConnectConfig"></a>
 The OpenID Connect configuration.
Type: [AwsAppSyncGraphQlApiOpenIdConnectConfigDetails](API_AwsAppSyncGraphQlApiOpenIdConnectConfigDetails.md) object
Required: No

 ** UserPoolConfig **   <a name="securityhub-Type-AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetails-UserPoolConfig"></a>
 The Amazon Cognito user pools configuration.
Type: [AwsAppSyncGraphQlApiUserPoolConfigDetails](API_AwsAppSyncGraphQlApiUserPoolConfigDetails.md) object
Required: No

## See Also
<a name="API_AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetails)
