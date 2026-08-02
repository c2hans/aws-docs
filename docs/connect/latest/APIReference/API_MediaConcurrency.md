---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_MediaConcurrency.html
---

# MediaConcurrency
<a name="API_MediaConcurrency"></a>

Contains information about which channels are supported, and how many contacts an agent can have on a channel simultaneously.

## Contents
<a name="API_MediaConcurrency_Contents"></a>

 ** Channel **   <a name="connect-Type-MediaConcurrency-Channel"></a>
The channels that agents can handle in the Contact Control Panel (CCP).
Type: String
Valid Values: `VOICE | CHAT | TASK | EMAIL`
Required: Yes

 ** Concurrency **   <a name="connect-Type-MediaConcurrency-Concurrency"></a>
The number of contacts an agent can have on a channel simultaneously.
Valid Range for `VOICE`: Minimum value of 1. Maximum value of 1.
Valid Range for `CHAT`: Minimum value of 1. Maximum value of 10.
Valid Range for `TASK`: Minimum value of 1. Maximum value of 10.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10.
Required: Yes

 ** CrossChannelBehavior **   <a name="connect-Type-MediaConcurrency-CrossChannelBehavior"></a>
Defines the cross-channel routing behavior for each channel that is enabled for this Routing Profile. For example, this allows you to offer an agent a different contact from another channel when they are currently working with a contact from a Voice channel.
Type: [CrossChannelBehavior](API_CrossChannelBehavior.md) object
Required: No

## See Also
<a name="API_MediaConcurrency_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/MediaConcurrency)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/MediaConcurrency)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/MediaConcurrency)
