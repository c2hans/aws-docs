---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DomainDescriptionType.html
---

# DomainDescriptionType
<a name="API_DomainDescriptionType"></a>

A container for information about the user pool domain associated with the hosted UI and OAuth endpoints.

This data type is a response parameter of [DescribeUserPoolDomain](API_DescribeUserPoolDomain.md).

## Contents
<a name="API_DomainDescriptionType_Contents"></a>

 ** AWSAccountId **   <a name="CognitoUserPools-Type-DomainDescriptionType-AWSAccountId"></a>
The AWS account that you created the user pool in.
Type: String
Length Constraints: Maximum length of 12.
Pattern: `[0-9]+`
Required: No

 ** CloudFrontDistribution **   <a name="CognitoUserPools-Type-DomainDescriptionType-CloudFrontDistribution"></a>
The Amazon CloudFront endpoint that hosts your custom domain.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: No

 ** CustomDomainConfig **   <a name="CognitoUserPools-Type-DomainDescriptionType-CustomDomainConfig"></a>
The configuration for a custom domain that hosts the sign-up and sign-in webpages for your application.
Type: [CustomDomainConfigType](API_CustomDomainConfigType.md) object
Required: No

 ** Domain **   <a name="CognitoUserPools-Type-DomainDescriptionType-Domain"></a>
The domain string. For custom domains, this is the fully-qualified domain name, such as `auth.example.com`. For Amazon Cognito prefix domains, this is the prefix alone, such as `auth`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `^[a-z0-9](?:[a-z0-9\-]{0,61}[a-z0-9])?$`
Required: No

 ** ManagedLoginVersion **   <a name="CognitoUserPools-Type-DomainDescriptionType-ManagedLoginVersion"></a>
The version of managed login branding that you want to apply to your domain. A value of `1` indicates hosted UI (classic) branding and a version of `2` indicates managed login branding.
Managed login requires that your user pool be configured for any [feature plan](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-sign-in-feature-plans.html) other than `Lite`.
Type: Integer
Required: No

 ** Routing **   <a name="CognitoUserPools-Type-DomainDescriptionType-Routing"></a>
The routing configuration for the domain, including failover settings for multi-region deployments. Currently only `Failover` configurations are allowed.
Type: [RoutingType](API_RoutingType.md) object
Required: No

 ** S3Bucket **   <a name="CognitoUserPools-Type-DomainDescriptionType-S3Bucket"></a>
The Amazon S3 bucket where the static files for this domain are stored.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 1024.
Pattern: `^[0-9A-Za-z\.\-_]*(?<!\.)$`
Required: No

 ** Status **   <a name="CognitoUserPools-Type-DomainDescriptionType-Status"></a>
The domain status.
Type: String
Valid Values: `CREATING | DELETING | UPDATING | ACTIVE | FAILED`
Required: No

 ** UserPoolId **   <a name="CognitoUserPools-Type-DomainDescriptionType-UserPoolId"></a>
The ID of the user pool that the domain is attached to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`
Required: No

 ** Version **   <a name="CognitoUserPools-Type-DomainDescriptionType-Version"></a>
The app version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Required: No

## See Also
<a name="API_DomainDescriptionType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/DomainDescriptionType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/DomainDescriptionType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/DomainDescriptionType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito User Pools. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognito-user-identity-pools` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
