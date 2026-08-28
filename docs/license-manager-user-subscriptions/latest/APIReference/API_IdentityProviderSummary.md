---
source_url: https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_IdentityProviderSummary.html
---

# IdentityProviderSummary
<a name="API_IdentityProviderSummary"></a>

Describes an identity provider.

## Contents
<a name="API_IdentityProviderSummary_Contents"></a>

 ** IdentityProvider **   <a name="licensemanagerusersubscriptions-Type-IdentityProviderSummary-IdentityProvider"></a>
The `IdentityProvider` resource contains information about an identity provider.
Type: [IdentityProvider](API_IdentityProvider.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** Product **   <a name="licensemanagerusersubscriptions-Type-IdentityProviderSummary-Product"></a>
The name of the user-based subscription product.
Type: String
Required: Yes

 ** Settings **   <a name="licensemanagerusersubscriptions-Type-IdentityProviderSummary-Settings"></a>
The `Settings` resource contains details about the registered identity provider’s product related configuration settings, such as the subnets to provision VPC endpoints.
Type: [Settings](API_Settings.md) object
Required: Yes

 ** Status **   <a name="licensemanagerusersubscriptions-Type-IdentityProviderSummary-Status"></a>
The status of the identity provider.
Type: String
Required: Yes

 ** FailureMessage **   <a name="licensemanagerusersubscriptions-Type-IdentityProviderSummary-FailureMessage"></a>
The failure message associated with an identity provider.
Type: String
Required: No

 ** IdentityProviderArn **   <a name="licensemanagerusersubscriptions-Type-IdentityProviderSummary-IdentityProviderArn"></a>
The Amazon Resource Name (ARN) of the identity provider.
Type: String
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{1,63}:[a-zA-Z0-9-\.]{1,510}/[a-zA-Z0-9-\.]{1,510}`
Required: No

 ** OwnerAccountId **   <a name="licensemanagerusersubscriptions-Type-IdentityProviderSummary-OwnerAccountId"></a>
The AWS Account ID of the owner of this resource.
Type: String
Required: No

## See Also
<a name="API_IdentityProviderSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-user-subscriptions-2018-05-10/IdentityProviderSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-user-subscriptions-2018-05-10/IdentityProviderSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-user-subscriptions-2018-05-10/IdentityProviderSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for License Manager User Subscriptions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query license-manager-user-subscriptions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
