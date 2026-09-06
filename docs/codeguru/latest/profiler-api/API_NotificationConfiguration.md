---
source_url: https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_NotificationConfiguration.html
---

# NotificationConfiguration
<a name="API_NotificationConfiguration"></a>

The configuration for notifications stored for each profiling group. This includes up to to two channels and a list of event publishers associated with each channel.

## Contents
<a name="API_NotificationConfiguration_Contents"></a>

 ** channels **   <a name="profiler-Type-NotificationConfiguration-channels"></a>
List of up to two channels to be used for sending notifications for events detected from the application profile.
Type: Array of [Channel](API_Channel.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: No

## See Also
<a name="API_NotificationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguruprofiler-2019-07-18/NotificationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguruprofiler-2019-07-18/NotificationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguruprofiler-2019-07-18/NotificationConfiguration)
