---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_Session.html
---

# Session
<a name="API_Session"></a>

The details for the execute command session.

## Contents
<a name="API_Session_Contents"></a>

 ** sessionId **   <a name="ECS-Type-Session-sessionId"></a>
The ID of the execute command session.
Type: String
Required: No

 ** streamUrl **   <a name="ECS-Type-Session-streamUrl"></a>
A URL to the managed agent on the container that the SSM Session Manager client uses to send commands and receive output from the container.
Type: String
Required: No

 ** tokenValue **   <a name="ECS-Type-Session-tokenValue"></a>
An encrypted token value containing session and caller information. It's used to authenticate the connection to the container.
Type: String
Required: No

## See Also
<a name="API_Session_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/Session)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/Session)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/Session)
