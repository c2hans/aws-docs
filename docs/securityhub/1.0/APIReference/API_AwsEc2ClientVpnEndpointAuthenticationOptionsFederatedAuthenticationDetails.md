---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEc2ClientVpnEndpointAuthenticationOptionsFederatedAuthenticationDetails.html
---

# AwsEc2ClientVpnEndpointAuthenticationOptionsFederatedAuthenticationDetails
<a name="API_AwsEc2ClientVpnEndpointAuthenticationOptionsFederatedAuthenticationDetails"></a>

 Describes the IAM SAML identity providers used for federated authentication.

## Contents
<a name="API_AwsEc2ClientVpnEndpointAuthenticationOptionsFederatedAuthenticationDetails_Contents"></a>

 ** SamlProviderArn **   <a name="securityhub-Type-AwsEc2ClientVpnEndpointAuthenticationOptionsFederatedAuthenticationDetails-SamlProviderArn"></a>
 The Amazon Resource Name (ARN) of the IAM SAML identity provider.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SelfServiceSamlProviderArn **   <a name="securityhub-Type-AwsEc2ClientVpnEndpointAuthenticationOptionsFederatedAuthenticationDetails-SelfServiceSamlProviderArn"></a>
 The Amazon Resource Name (ARN) of the IAM SAML identity provider for the self-service portal.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEc2ClientVpnEndpointAuthenticationOptionsFederatedAuthenticationDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEc2ClientVpnEndpointAuthenticationOptionsFederatedAuthenticationDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEc2ClientVpnEndpointAuthenticationOptionsFederatedAuthenticationDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEc2ClientVpnEndpointAuthenticationOptionsFederatedAuthenticationDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
