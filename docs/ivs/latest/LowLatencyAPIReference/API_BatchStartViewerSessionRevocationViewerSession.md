---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_BatchStartViewerSessionRevocationViewerSession.html
---

# BatchStartViewerSessionRevocationViewerSession
<a name="API_BatchStartViewerSessionRevocationViewerSession"></a>

A viewer session to revoke in the call to [BatchStartViewerSessionRevocation](API_BatchStartViewerSessionRevocation.md).

## Contents
<a name="API_BatchStartViewerSessionRevocationViewerSession_Contents"></a>

 ** channelArn **   <a name="ivs-Type-BatchStartViewerSessionRevocationViewerSession-channelArn"></a>
The ARN of the channel associated with the viewer session to revoke.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:channel/[a-zA-Z0-9-]+`
Required: Yes

 ** viewerId **   <a name="ivs-Type-BatchStartViewerSessionRevocationViewerSession-viewerId"></a>
The ID of the viewer associated with the viewer session to revoke. Do not use this field for personally identifying, confidential, or sensitive information.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 40.
Required: Yes

 ** viewerSessionVersionsLessThanOrEqualTo **   <a name="ivs-Type-BatchStartViewerSessionRevocationViewerSession-viewerSessionVersionsLessThanOrEqualTo"></a>
An optional filter on which versions of the viewer session to revoke. All versions less than or equal to the specified version will be revoked. Default: 0.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_BatchStartViewerSessionRevocationViewerSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-2020-07-14/BatchStartViewerSessionRevocationViewerSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-2020-07-14/BatchStartViewerSessionRevocationViewerSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-2020-07-14/BatchStartViewerSessionRevocationViewerSession)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
