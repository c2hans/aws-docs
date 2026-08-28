---
source_url: https://docs.aws.amazon.com/kinesisvideostreams/latest/APIReference/API_signaling_IceServer.html
---

# IceServer
<a name="API_signaling_IceServer"></a>

A structure for the ICE server connection data.

## Contents
<a name="API_signaling_IceServer_Contents"></a>

 ** Password **   <a name="KinesisVideo-Type-signaling_IceServer-Password"></a>
A password to login to the ICE server.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** Ttl **   <a name="KinesisVideo-Type-signaling_IceServer-Ttl"></a>
The period of time, in seconds, during which the user name and password are valid.
Type: Integer
Valid Range: Fixed value of 300.
Required: No

 ** Uris **   <a name="KinesisVideo-Type-signaling_IceServer-Uris"></a>
An array of URIs, in the form specified in the [I-D.petithuguenin-behave-turn-uris](https://tools.ietf.org/html/draft-petithuguenin-behave-turn-uris-03) spec. These URIs provide the different addresses and/or protocols that can be used to reach the TURN server.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** Username **   <a name="KinesisVideo-Type-signaling_IceServer-Username"></a>
A user name to login to the ICE server.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

## See Also
<a name="API_signaling_IceServer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-video-signaling-2019-12-04/IceServer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-video-signaling-2019-12-04/IceServer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-video-signaling-2019-12-04/IceServer)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Video Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesisvideostreams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
