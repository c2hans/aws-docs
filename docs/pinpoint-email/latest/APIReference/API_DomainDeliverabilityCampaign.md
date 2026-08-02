---
source_url: https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_DomainDeliverabilityCampaign.html
---

# DomainDeliverabilityCampaign
<a name="API_DomainDeliverabilityCampaign"></a>

An object that contains the deliverability data for a specific campaign. This data is available for a campaign only if the campaign sent email by using a domain that the Deliverability dashboard is enabled for (`PutDeliverabilityDashboardOption` operation).

## Contents
<a name="API_DomainDeliverabilityCampaign_Contents"></a>

 ** CampaignId **   <a name="pinpoint-Type-DomainDeliverabilityCampaign-CampaignId"></a>
The unique identifier for the campaign. Amazon Pinpoint automatically generates and assigns this identifier to a campaign. This value is not the same as the campaign identifier that Amazon Pinpoint assigns to campaigns that you create and manage by using the Amazon Pinpoint API or the Amazon Pinpoint console.
Type: String
Required: No

 ** DeleteRate **   <a name="pinpoint-Type-DomainDeliverabilityCampaign-DeleteRate"></a>
The percentage of email messages that were deleted by recipients, without being opened first. Due to technical limitations, this value only includes recipients who opened the message by using an email client that supports images.
Type: Double
Required: No

 ** Esps **   <a name="pinpoint-Type-DomainDeliverabilityCampaign-Esps"></a>
The major email providers who handled the email message.
Type: Array of strings
Required: No

 ** FirstSeenDateTime **   <a name="pinpoint-Type-DomainDeliverabilityCampaign-FirstSeenDateTime"></a>
The first time, in Unix time format, when the email message was delivered to any recipient's inbox. This value can help you determine how long it took for a campaign to deliver an email message.
Type: Timestamp
Required: No

 ** FromAddress **   <a name="pinpoint-Type-DomainDeliverabilityCampaign-FromAddress"></a>
The verified email address that the email message was sent from.
Type: String
Required: No

 ** ImageUrl **   <a name="pinpoint-Type-DomainDeliverabilityCampaign-ImageUrl"></a>
The URL of an image that contains a snapshot of the email message that was sent.
Type: String
Required: No

 ** InboxCount **   <a name="pinpoint-Type-DomainDeliverabilityCampaign-InboxCount"></a>
The number of email messages that were delivered to recipients’ inboxes.
Type: Long
Required: No

 ** LastSeenDateTime **   <a name="pinpoint-Type-DomainDeliverabilityCampaign-LastSeenDateTime"></a>
The last time, in Unix time format, when the email message was delivered to any recipient's inbox. This value can help you determine how long it took for a campaign to deliver an email message.
Type: Timestamp
Required: No

 ** ProjectedVolume **   <a name="pinpoint-Type-DomainDeliverabilityCampaign-ProjectedVolume"></a>
The projected number of recipients that the email message was sent to.
Type: Long
Required: No

 ** ReadDeleteRate **   <a name="pinpoint-Type-DomainDeliverabilityCampaign-ReadDeleteRate"></a>
The percentage of email messages that were opened and then deleted by recipients. Due to technical limitations, this value only includes recipients who opened the message by using an email client that supports images.
Type: Double
Required: No

 ** ReadRate **   <a name="pinpoint-Type-DomainDeliverabilityCampaign-ReadRate"></a>
The percentage of email messages that were opened by recipients. Due to technical limitations, this value only includes recipients who opened the message by using an email client that supports images.
Type: Double
Required: No

 ** SendingIps **   <a name="pinpoint-Type-DomainDeliverabilityCampaign-SendingIps"></a>
The IP addresses that were used to send the email message.
Type: Array of strings
Required: No

 ** SpamCount **   <a name="pinpoint-Type-DomainDeliverabilityCampaign-SpamCount"></a>
The number of email messages that were delivered to recipients' spam or junk mail folders.
Type: Long
Required: No

 ** Subject **   <a name="pinpoint-Type-DomainDeliverabilityCampaign-Subject"></a>
The subject line, or title, of the email message.
Type: String
Required: No

## See Also
<a name="API_DomainDeliverabilityCampaign_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-email-2018-07-26/DomainDeliverabilityCampaign)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-email-2018-07-26/DomainDeliverabilityCampaign)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-email-2018-07-26/DomainDeliverabilityCampaign)
