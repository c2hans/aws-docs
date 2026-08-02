---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_SuppressedDestinationSummary.html
---

# SuppressedDestinationSummary
<a name="API_SuppressedDestinationSummary"></a>

A summary that describes the suppressed email address.

## Contents
<a name="API_SuppressedDestinationSummary_Contents"></a>

 ** EmailAddress **   <a name="SES-Type-SuppressedDestinationSummary-EmailAddress"></a>
The email address that's on the suppression list for your account or for a specific tenant.
Type: String
Required: Yes

 ** LastUpdateTime **   <a name="SES-Type-SuppressedDestinationSummary-LastUpdateTime"></a>
The date and time when the suppressed destination was last updated, shown in Unix time format.
Type: Timestamp
Required: Yes

 ** Reason **   <a name="SES-Type-SuppressedDestinationSummary-Reason"></a>
The reason that the address was added to the suppression list for your account or for a specific tenant.
Type: String
Valid Values: `BOUNCE | COMPLAINT`
Required: Yes

## See Also
<a name="API_SuppressedDestinationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/SuppressedDestinationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/SuppressedDestinationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/SuppressedDestinationSummary)
