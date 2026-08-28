---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_Session.html
---

# Session
<a name="API_Session"></a>

Information about a Session Manager connection to a managed node.

## Contents
<a name="API_Session_Contents"></a>

 ** AccessType **   <a name="systemsmanager-Type-Session-AccessType"></a>
 `Standard` access type is the default for Session Manager sessions. `JustInTime` is the access type for [Just-in-time node access](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-just-in-time-node-access.html).
Type: String
Valid Values: `Standard | JustInTime`
Required: No

 ** Details **   <a name="systemsmanager-Type-Session-Details"></a>
Reserved for future use.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** DocumentName **   <a name="systemsmanager-Type-Session-DocumentName"></a>
The name of the Session Manager SSM document used to define the parameters and plugin settings for the session. For example, `SSM-SessionManagerRunShell`.
Type: String
Pattern: `^[a-zA-Z0-9_\-.]{3,128}$`
Required: No

 ** EndDate **   <a name="systemsmanager-Type-Session-EndDate"></a>
The date and time, in ISO-8601 Extended format, when the session was terminated.
Type: Timestamp
Required: No

 ** MaxSessionDuration **   <a name="systemsmanager-Type-Session-MaxSessionDuration"></a>
The maximum duration of a session before it terminates.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4.
Pattern: `^([1-9]|[1-9][0-9]|[1-9][0-9][0-9]|1[0-4][0-3][0-9]|1440)$`
Required: No

 ** OutputUrl **   <a name="systemsmanager-Type-Session-OutputUrl"></a>
Reserved for future use.
Type: [SessionManagerOutputUrl](API_SessionManagerOutputUrl.md) object
Required: No

 ** Owner **   <a name="systemsmanager-Type-Session-Owner"></a>
The ID of the Amazon Web Services user that started the session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** Reason **   <a name="systemsmanager-Type-Session-Reason"></a>
The reason for connecting to the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^.{1,256}$`
Required: No

 ** SessionId **   <a name="systemsmanager-Type-Session-SessionId"></a>
The ID of the session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 96.
Required: No

 ** StartDate **   <a name="systemsmanager-Type-Session-StartDate"></a>
The date and time, in ISO-8601 Extended format, when the session began.
Type: Timestamp
Required: No

 ** Status **   <a name="systemsmanager-Type-Session-Status"></a>
The status of the session. For example, "Connected" or "Terminated".
Type: String
Valid Values: `Connected | Connecting | Disconnected | Terminated | Terminating | Failed`
Required: No

 ** Target **   <a name="systemsmanager-Type-Session-Target"></a>
The managed node that the Session Manager session connected to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 400.
Required: No

## See Also
<a name="API_Session_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/Session)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/Session)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/Session)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
