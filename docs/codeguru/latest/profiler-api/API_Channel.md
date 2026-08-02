---
source_url: https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_Channel.html
---

# Channel
<a name="API_Channel"></a>

Notification medium for users to get alerted for events that occur in application profile. We support SNS topic as a notification channel.

## Contents
<a name="API_Channel_Contents"></a>

 ** eventPublishers **   <a name="profiler-Type-Channel-eventPublishers"></a>
List of publishers for different type of events that may be detected in an application from the profile. Anomaly detection is the only event publisher in Profiler.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `AnomalyDetection`
Required: Yes

 ** uri **   <a name="profiler-Type-Channel-uri"></a>
Unique arn of the resource to be used for notifications. We support a valid SNS topic arn as a channel uri.
Type: String
Required: Yes

 ** id **   <a name="profiler-Type-Channel-id"></a>
Unique identifier for each `Channel` in the notification configuration of a Profiling Group. A random UUID for channelId is used when adding a channel to the notification configuration if not specified in the request.
Type: String
Pattern: `.*[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}.*`
Required: No

## See Also
<a name="API_Channel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguruprofiler-2019-07-18/Channel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguruprofiler-2019-07-18/Channel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguruprofiler-2019-07-18/Channel)
