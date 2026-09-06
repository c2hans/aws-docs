---
source_url: https://docs.aws.amazon.com/health/latest/APIReference/API_EventDetails.html
---

# EventDetails
<a name="API_EventDetails"></a>

Detailed information about an event. A combination of an [Event](https://docs.aws.amazon.com/health/latest/APIReference/API_Event.html) object, an [EventDescription](https://docs.aws.amazon.com/health/latest/APIReference/API_EventDescription.html) object, and additional metadata about the event. Returned by the [DescribeEventDetails](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEventDetails.html) operation.

## Contents
<a name="API_EventDetails_Contents"></a>

 ** event **   <a name="AWSHealth-Type-EventDetails-event"></a>
Summary information about the event.
Type: [Event](API_Event.md) object
Required: No

 ** eventDescription **   <a name="AWSHealth-Type-EventDetails-eventDescription"></a>
The most recent description of the event.
Type: [EventDescription](API_EventDescription.md) object
Required: No

 ** eventMetadata **   <a name="AWSHealth-Type-EventDetails-eventMetadata"></a>
Additional metadata about the event.
Type: String to string map
Key Length Constraints: Maximum length of 32766.
Value Length Constraints: Maximum length of 32766.
Required: No

## See Also
<a name="API_EventDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/health-2016-08-04/EventDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/health-2016-08-04/EventDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/health-2016-08-04/EventDetails)
