---
source_url: https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_InstanceUserSummary.html
---

# InstanceUserSummary
<a name="API_InstanceUserSummary"></a>

Describes users of an EC2 instance providing user-based subscriptions.

## Contents
<a name="API_InstanceUserSummary_Contents"></a>

 ** IdentityProvider **   <a name="licensemanagerusersubscriptions-Type-InstanceUserSummary-IdentityProvider"></a>
The `IdentityProvider` resource specifies details about the identity provider.
Type: [IdentityProvider](API_IdentityProvider.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** InstanceId **   <a name="licensemanagerusersubscriptions-Type-InstanceUserSummary-InstanceId"></a>
The ID of the EC2 instance that provides user-based subscriptions.
Type: String
Required: Yes

 ** Status **   <a name="licensemanagerusersubscriptions-Type-InstanceUserSummary-Status"></a>
The status of a user associated with an EC2 instance.
Type: String
Required: Yes

 ** Username **   <a name="licensemanagerusersubscriptions-Type-InstanceUserSummary-Username"></a>
The user name from the identity provider for the user.
Type: String
Required: Yes

 ** AssociationDate **   <a name="licensemanagerusersubscriptions-Type-InstanceUserSummary-AssociationDate"></a>
The date a user was associated with an EC2 instance.
Type: String
Required: No

 ** DisassociationDate **   <a name="licensemanagerusersubscriptions-Type-InstanceUserSummary-DisassociationDate"></a>
The date a user was disassociated from an EC2 instance.
Type: String
Required: No

 ** Domain **   <a name="licensemanagerusersubscriptions-Type-InstanceUserSummary-Domain"></a>
The domain name of the Active Directory that contains the user information for the product subscription.
Type: String
Required: No

 ** InstanceUserArn **   <a name="licensemanagerusersubscriptions-Type-InstanceUserSummary-InstanceUserArn"></a>
The Amazon Resource Name (ARN) that identifies the instance user.
Type: String
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{1,63}:[a-zA-Z0-9-\.]{1,510}/[a-zA-Z0-9-\.]{1,510}`
Required: No

 ** StatusMessage **   <a name="licensemanagerusersubscriptions-Type-InstanceUserSummary-StatusMessage"></a>
The status message for users of an EC2 instance.
Type: String
Required: No

## See Also
<a name="API_InstanceUserSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-user-subscriptions-2018-05-10/InstanceUserSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-user-subscriptions-2018-05-10/InstanceUserSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-user-subscriptions-2018-05-10/InstanceUserSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for License Manager User Subscriptions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query license-manager-user-subscriptions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
