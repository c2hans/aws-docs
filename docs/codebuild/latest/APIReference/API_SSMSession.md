---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_SSMSession.html
---

# SSMSession
<a name="API_SSMSession"></a>

Contains information about the Session Manager session.

## Contents
<a name="API_SSMSession_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** sessionId **   <a name="CodeBuild-Type-SSMSession-sessionId"></a>
The ID of the session.
Type: String
Required: No

 ** streamUrl **   <a name="CodeBuild-Type-SSMSession-streamUrl"></a>
A URL back to SSM Agent on the managed node that the Session Manager client uses to send commands and receive output from the node.
Type: String
Required: No

 ** tokenValue **   <a name="CodeBuild-Type-SSMSession-tokenValue"></a>
An encrypted token value containing session and caller information.
Type: String
Required: No

## See Also
<a name="API_SSMSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/SSMSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/SSMSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/SSMSession)
