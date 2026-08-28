---
source_url: https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_ProductUserSummary.html
---

# ProductUserSummary
<a name="API_ProductUserSummary"></a>

A summary of the user-based subscription products for a specific user.

## Contents
<a name="API_ProductUserSummary_Contents"></a>

 ** IdentityProvider **   <a name="licensemanagerusersubscriptions-Type-ProductUserSummary-IdentityProvider"></a>
An object that specifies details for the identity provider.
Type: [IdentityProvider](API_IdentityProvider.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** Product **   <a name="licensemanagerusersubscriptions-Type-ProductUserSummary-Product"></a>
The name of the user-based subscription product.
Type: String
Required: Yes

 ** Status **   <a name="licensemanagerusersubscriptions-Type-ProductUserSummary-Status"></a>
The status of a product for this user.
Type: String
Required: Yes

 ** Username **   <a name="licensemanagerusersubscriptions-Type-ProductUserSummary-Username"></a>
The user name from the identity provider for this product user.
Type: String
Required: Yes

 ** Domain **   <a name="licensemanagerusersubscriptions-Type-ProductUserSummary-Domain"></a>
The domain name of the Active Directory that contains the user information for the product subscription.
Type: String
Required: No

 ** ProductUserArn **   <a name="licensemanagerusersubscriptions-Type-ProductUserSummary-ProductUserArn"></a>
The Amazon Resource Name (ARN) for this product user.
Type: String
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{1,63}:[a-zA-Z0-9-\.]{1,510}/[a-zA-Z0-9-\.]{1,510}`
Required: No

 ** StatusMessage **   <a name="licensemanagerusersubscriptions-Type-ProductUserSummary-StatusMessage"></a>
The status message for a product for this user.
Type: String
Required: No

 ** SubscriptionEndDate **   <a name="licensemanagerusersubscriptions-Type-ProductUserSummary-SubscriptionEndDate"></a>
The end date of a subscription.
Type: String
Required: No

 ** SubscriptionStartDate **   <a name="licensemanagerusersubscriptions-Type-ProductUserSummary-SubscriptionStartDate"></a>
The start date of a subscription.
Type: String
Required: No

## See Also
<a name="API_ProductUserSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-user-subscriptions-2018-05-10/ProductUserSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-user-subscriptions-2018-05-10/ProductUserSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-user-subscriptions-2018-05-10/ProductUserSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for License Manager User Subscriptions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query license-manager-user-subscriptions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
