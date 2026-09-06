---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_SuppressedDestination.html
---

# SuppressedDestination
<a name="API_SuppressedDestination"></a>

An object that contains information about an email address that is on the suppression list for your account or for a specific tenant.

## Contents
<a name="API_SuppressedDestination_Contents"></a>

 ** EmailAddress **   <a name="SES-Type-SuppressedDestination-EmailAddress"></a>
The email address that is on the suppression list for your account or for a specific tenant.
Type: String
Required: Yes

 ** LastUpdateTime **   <a name="SES-Type-SuppressedDestination-LastUpdateTime"></a>
The date and time when the suppressed destination was last updated, shown in Unix time format.
Type: Timestamp
Required: Yes

 ** Reason **   <a name="SES-Type-SuppressedDestination-Reason"></a>
The reason that the address was added to the suppression list for your account or for a specific tenant.
Type: String
Valid Values: `BOUNCE | COMPLAINT`
Required: Yes

 ** Attributes **   <a name="SES-Type-SuppressedDestination-Attributes"></a>
An optional value that can contain additional information about the reasons that the address was added to the suppression list for your account or for a specific tenant.
Type: [SuppressedDestinationAttributes](API_SuppressedDestinationAttributes.md) object
Required: No

 ** TenantName **   <a name="SES-Type-SuppressedDestination-TenantName"></a>
The name of the tenant that the suppressed destination belongs to. This field is present only when the suppressed destination is on a tenant's suppression list.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_SuppressedDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/SuppressedDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/SuppressedDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/SuppressedDestination)
