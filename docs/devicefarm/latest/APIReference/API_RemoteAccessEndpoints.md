---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_RemoteAccessEndpoints.html
---

# RemoteAccessEndpoints
<a name="API_RemoteAccessEndpoints"></a>

Represents the remote endpoints for viewing and controlling a device during a remote access session.

## Contents
<a name="API_RemoteAccessEndpoints_Contents"></a>

 ** interactiveEndpoint **   <a name="devicefarm-Type-RemoteAccessEndpoints-interactiveEndpoint"></a>
URL for viewing and interacting with the device during the remote access session.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** remoteDriverEndpoint **   <a name="devicefarm-Type-RemoteAccessEndpoints-remoteDriverEndpoint"></a>
URL for controlling the device using WebDriver-compliant clients, like Appium, during the remote access session.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

## See Also
<a name="API_RemoteAccessEndpoints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/RemoteAccessEndpoints)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/RemoteAccessEndpoints)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/RemoteAccessEndpoints)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Device Farm Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devicefarm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
