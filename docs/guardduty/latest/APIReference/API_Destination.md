---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_Destination.html
---

# Destination
<a name="API_Destination"></a>

Contains information about the publishing destination, including the ID, type, and status.

## Contents
<a name="API_Destination_Contents"></a>

 ** destinationId **   <a name="guardduty-Type-Destination-destinationId"></a>
The unique ID of the publishing destination.
Type: String
Required: Yes

 ** destinationType **   <a name="guardduty-Type-Destination-destinationType"></a>
The type of resource used for the publishing destination. Currently, only Amazon S3 buckets are supported.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Valid Values: `S3`
Required: Yes

 ** status **   <a name="guardduty-Type-Destination-status"></a>
The status of the publishing destination.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Valid Values: `PENDING_VERIFICATION | PUBLISHING | UNABLE_TO_PUBLISH_FIX_DESTINATION_PROPERTY | STOPPED`
Required: Yes

## See Also
<a name="API_Destination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/Destination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/Destination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/Destination)
