---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_ContactChannelAddress.html
---

# ContactChannelAddress
<a name="API_SSMContacts_ContactChannelAddress"></a>

The details that Incident Manager uses when trying to engage the contact channel.

## Contents
<a name="API_SSMContacts_ContactChannelAddress_Contents"></a>

 ** SimpleAddress **   <a name="IncidentManager-Type-SSMContacts_ContactChannelAddress-SimpleAddress"></a>
The format is dependent on the type of the contact channel. The following are the expected formats:
+ SMS - '\+' followed by the country code and phone number
+ VOICE - '\+' followed by the country code and phone number
+ EMAIL - any standard email format
Type: String
Length Constraints: Minimum length of 1. Maximum length of 320.
Required: No

## See Also
<a name="API_SSMContacts_ContactChannelAddress_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-contacts-2021-05-03/ContactChannelAddress)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-contacts-2021-05-03/ContactChannelAddress)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-contacts-2021-05-03/ContactChannelAddress)
