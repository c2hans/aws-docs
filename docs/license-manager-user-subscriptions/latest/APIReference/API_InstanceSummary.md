---
source_url: https://docs.aws.amazon.com/license-manager-user-subscriptions/latest/APIReference/API_InstanceSummary.html
---

# InstanceSummary
<a name="API_InstanceSummary"></a>

Describes an EC2 instance providing user-based subscriptions.

## Contents
<a name="API_InstanceSummary_Contents"></a>

 ** InstanceId **   <a name="licensemanagerusersubscriptions-Type-InstanceSummary-InstanceId"></a>
The ID of the EC2 instance, which provides user-based subscriptions.
Type: String
Required: Yes

 ** Products **   <a name="licensemanagerusersubscriptions-Type-InstanceSummary-Products"></a>
A list of provided user-based subscription products.
Type: Array of strings
Required: Yes

 ** Status **   <a name="licensemanagerusersubscriptions-Type-InstanceSummary-Status"></a>
The status of an EC2 instance resource.
Type: String
Required: Yes

 ** IdentityProvider **   <a name="licensemanagerusersubscriptions-Type-InstanceSummary-IdentityProvider"></a>
The `IdentityProvider` resource specifies details about the identity provider.
Type: [IdentityProvider](API_IdentityProvider.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** LastStatusCheckDate **   <a name="licensemanagerusersubscriptions-Type-InstanceSummary-LastStatusCheckDate"></a>
The date of the last status check.
Type: String
Required: No

 ** OwnerAccountId **   <a name="licensemanagerusersubscriptions-Type-InstanceSummary-OwnerAccountId"></a>
The AWS Account ID of the owner of this resource.
Type: String
Required: No

 ** StatusMessage **   <a name="licensemanagerusersubscriptions-Type-InstanceSummary-StatusMessage"></a>
The status message for an EC2 instance.
Type: String
Required: No

## See Also
<a name="API_InstanceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-user-subscriptions-2018-05-10/InstanceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-user-subscriptions-2018-05-10/InstanceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-user-subscriptions-2018-05-10/InstanceSummary)
