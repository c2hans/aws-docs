---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_NetworkConnectionAction.html
---

# NetworkConnectionAction
<a name="API_NetworkConnectionAction"></a>

Provided if `ActionType` is `NETWORK_CONNECTION`. It provides details about the attempted network connection that was detected.

## Contents
<a name="API_NetworkConnectionAction_Contents"></a>

 ** Blocked **   <a name="securityhub-Type-NetworkConnectionAction-Blocked"></a>
Indicates whether the network connection attempt was blocked.
Type: Boolean
Required: No

 ** ConnectionDirection **   <a name="securityhub-Type-NetworkConnectionAction-ConnectionDirection"></a>
The direction of the network connection request (`IN` or `OUT`).
Type: String
Pattern: `.*\S.*`
Required: No

 ** LocalPortDetails **   <a name="securityhub-Type-NetworkConnectionAction-LocalPortDetails"></a>
Information about the port on the EC2 instance.
Type: [ActionLocalPortDetails](API_ActionLocalPortDetails.md) object
Required: No

 ** Protocol **   <a name="securityhub-Type-NetworkConnectionAction-Protocol"></a>
The protocol used to make the network connection request.
Length Constraints: Minimum length of 1. Maximum length of 64.
Type: String
Pattern: `.*\S.*`
Required: No

 ** RemoteIpDetails **   <a name="securityhub-Type-NetworkConnectionAction-RemoteIpDetails"></a>
Information about the remote IP address that issued the network connection request.
Type: [ActionRemoteIpDetails](API_ActionRemoteIpDetails.md) object
Required: No

 ** RemotePortDetails **   <a name="securityhub-Type-NetworkConnectionAction-RemotePortDetails"></a>
Information about the port on the remote IP address.
Type: [ActionRemotePortDetails](API_ActionRemotePortDetails.md) object
Required: No

## See Also
<a name="API_NetworkConnectionAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/NetworkConnectionAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/NetworkConnectionAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/NetworkConnectionAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
