---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_PreferredContactWindow.html
---

# PreferredContactWindow

The time window during which the sender prefers to be contacted about an account plan. This information is advisory. Both fields are optional.

## Contents
<a name="API_PreferredContactWindow_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Timezone **   <a name="AWSPartnerCentral-Type-PreferredContactWindow-Timezone"></a>
The IANA time zone name that the window is expressed in, for example `America/Chicago`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_+-]+(?:/[A-Za-z0-9_+-]+)*`
Required: No

 ** Window **   <a name="AWSPartnerCentral-Type-PreferredContactWindow-Window"></a>
The preferred time-of-day band for contact.
Type: String
Valid Values: `MORNING | AFTERNOON | EVENING`
Required: No

## See Also
<a name="API_PreferredContactWindow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/PreferredContactWindow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/PreferredContactWindow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/PreferredContactWindow)
