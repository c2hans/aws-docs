---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsAppSyncGraphQlApiDetails.html
---

# AwsAppSyncGraphQlApiDetails
<a name="API_AwsAppSyncGraphQlApiDetails"></a>

 Provides details about an AWS AppSync Graph QL API, which lets you query multiple databases, microservices, and APIs from a single GraphQL endpoint.

## Contents
<a name="API_AwsAppSyncGraphQlApiDetails_Contents"></a>

 ** AdditionalAuthenticationProviders **   <a name="securityhub-Type-AwsAppSyncGraphQlApiDetails-AdditionalAuthenticationProviders"></a>
 A list of additional authentication providers for the GraphQL API.
Type: Array of [AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetails](API_AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetails.md) objects
Required: No

 ** ApiId **   <a name="securityhub-Type-AwsAppSyncGraphQlApiDetails-ApiId"></a>
 The unique identifier for the API.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Arn **   <a name="securityhub-Type-AwsAppSyncGraphQlApiDetails-Arn"></a>
 The Amazon Resource Name (ARN) of the API.
Type: String
Pattern: `.*\S.*`
Required: No

 ** AuthenticationType **   <a name="securityhub-Type-AwsAppSyncGraphQlApiDetails-AuthenticationType"></a>
 The type of security configuration for your GraphQL API: API key, AWS Identity and Access Management (IAM), OpenID Connect (OIDC), Amazon Cognito user pools, or AWS Lambda.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Id **   <a name="securityhub-Type-AwsAppSyncGraphQlApiDetails-Id"></a>
The unique identifier for the API.
Type: String
Pattern: `.*\S.*`
Required: No

 ** LambdaAuthorizerConfig **   <a name="securityhub-Type-AwsAppSyncGraphQlApiDetails-LambdaAuthorizerConfig"></a>
 Specifies the configuration for AWS Lambda function authorization.
Type: [AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetails](API_AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetails.md) object
Required: No

 ** LogConfig **   <a name="securityhub-Type-AwsAppSyncGraphQlApiDetails-LogConfig"></a>
 The Amazon CloudWatch Logs configuration.
Type: [AwsAppSyncGraphQlApiLogConfigDetails](API_AwsAppSyncGraphQlApiLogConfigDetails.md) object
Required: No

 ** Name **   <a name="securityhub-Type-AwsAppSyncGraphQlApiDetails-Name"></a>
 The API name.
Type: String
Pattern: `.*\S.*`
Required: No

 ** OpenIdConnectConfig **   <a name="securityhub-Type-AwsAppSyncGraphQlApiDetails-OpenIdConnectConfig"></a>
 Specifies the authorization configuration for using an OpenID Connect compliant service with an AWS AppSync GraphQL API endpoint.
Type: [AwsAppSyncGraphQlApiOpenIdConnectConfigDetails](API_AwsAppSyncGraphQlApiOpenIdConnectConfigDetails.md) object
Required: No

 ** UserPoolConfig **   <a name="securityhub-Type-AwsAppSyncGraphQlApiDetails-UserPoolConfig"></a>
 The Amazon Cognito user pools configuration.
Type: [AwsAppSyncGraphQlApiUserPoolConfigDetails](API_AwsAppSyncGraphQlApiUserPoolConfigDetails.md) object
Required: No

 ** WafWebAclArn **   <a name="securityhub-Type-AwsAppSyncGraphQlApiDetails-WafWebAclArn"></a>
 The Amazon Resource Name (ARN) of the AWS WAF web access control list (web ACL) associated with this GraphQL API, if one exists.
Type: String
Pattern: `.*\S.*`
Required: No

 ** XrayEnabled **   <a name="securityhub-Type-AwsAppSyncGraphQlApiDetails-XrayEnabled"></a>
 Indicates whether to use AWS X-Ray tracing for the GraphQL API.
Type: Boolean
Required: No

## See Also
<a name="API_AwsAppSyncGraphQlApiDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsAppSyncGraphQlApiDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsAppSyncGraphQlApiDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsAppSyncGraphQlApiDetails)
