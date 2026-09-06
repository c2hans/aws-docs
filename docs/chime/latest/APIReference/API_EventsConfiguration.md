---
source_url: https://docs.aws.amazon.com/chime/latest/APIReference/API_EventsConfiguration.html
---

**End of support notice**: On February 20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/). **Note:** This does not impact the availability of the [Amazon Chime SDK service](https://aws.amazon.com/chime/chime-sdk/).

# EventsConfiguration
<a name="API_EventsConfiguration"></a>

The configuration that allows a bot to receive outgoing events. Can be either an HTTPS endpoint or a Lambda function ARN.

## Contents
<a name="API_EventsConfiguration_Contents"></a>

 ** BotId **   <a name="chime-Type-EventsConfiguration-BotId"></a>
The bot ID.
Type: String
Required: No

 ** LambdaFunctionArn **   <a name="chime-Type-EventsConfiguration-LambdaFunctionArn"></a>
Lambda function ARN that allows a bot to receive outgoing events.
Type: String
Required: No

 ** OutboundEventsHTTPSEndpoint **   <a name="chime-Type-EventsConfiguration-OutboundEventsHTTPSEndpoint"></a>
HTTPS endpoint that allows a bot to receive outgoing events.
Type: String
Required: No

## See Also
<a name="API_EventsConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-2018-05-01/EventsConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-2018-05-01/EventsConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-2018-05-01/EventsConfiguration)
