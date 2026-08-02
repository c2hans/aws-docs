---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_Topic.html
---

# Topic
<a name="API_Topic"></a>

An interest group, theme, or label within a list. Lists can have multiple topics.

## Contents
<a name="API_Topic_Contents"></a>

 ** DefaultSubscriptionStatus **   <a name="SES-Type-Topic-DefaultSubscriptionStatus"></a>
The default subscription status to be applied to a contact if the contact has not noted their preference for subscribing to a topic.
Type: String
Valid Values: `OPT_IN | OPT_OUT`
Required: Yes

 ** DisplayName **   <a name="SES-Type-Topic-DisplayName"></a>
The name of the topic the contact will see.
Type: String
Required: Yes

 ** TopicName **   <a name="SES-Type-Topic-TopicName"></a>
The name of the topic.
Type: String
Required: Yes

 ** Description **   <a name="SES-Type-Topic-Description"></a>
A description of what the topic is about, which the contact will see.
Type: String
Required: No

## See Also
<a name="API_Topic_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/Topic)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/Topic)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/Topic)
