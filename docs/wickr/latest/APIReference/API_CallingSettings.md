---
source_url: https://docs.aws.amazon.com/wickr/latest/APIReference/API_CallingSettings.html
---

# CallingSettings
<a name="API_CallingSettings"></a>

Defines the calling feature permissions and settings for users in a security group, controlling what types of calls users can initiate and participate in.

## Contents
<a name="API_CallingSettings_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** canStart11Call **   <a name="wickr-Type-CallingSettings-canStart11Call"></a>
Specifies whether users can start one-to-one calls.
Type: Boolean
Required: No

 ** canVideoCall **   <a name="wickr-Type-CallingSettings-canVideoCall"></a>
Specifies whether users can make video calls (as opposed to audio-only calls). Valid only when audio call(canStart11Call) is enabled.
Type: Boolean
Required: No

 ** forceTcpCall **   <a name="wickr-Type-CallingSettings-forceTcpCall"></a>
When enabled, forces all calls to use TCP protocol instead of UDP for network traversal.
Type: Boolean
Required: No

## See Also
<a name="API_CallingSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wickr-2024-02-01/CallingSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wickr-2024-02-01/CallingSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wickr-2024-02-01/CallingSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wickr. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wickr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
