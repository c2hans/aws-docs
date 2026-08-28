---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_Session.html
---

# Session
<a name="API_Session"></a>

Describes a streaming session.

## Contents
<a name="API_Session_Contents"></a>

 ** FleetName **   <a name="WorkSpacesApplications-Type-Session-FleetName"></a>
The name of the fleet for the streaming session.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** Id **   <a name="WorkSpacesApplications-Type-Session-Id"></a>
The identifier of the streaming session.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** StackName **   <a name="WorkSpacesApplications-Type-Session-StackName"></a>
The name of the stack for the streaming session.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** State **   <a name="WorkSpacesApplications-Type-Session-State"></a>
The current state of the streaming session.
Type: String
Valid Values: `ACTIVE | PENDING | EXPIRED`
Required: Yes

 ** UserId **   <a name="WorkSpacesApplications-Type-Session-UserId"></a>
The identifier of the user for whom the session was created.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 128.
Required: Yes

 ** AuthenticationType **   <a name="WorkSpacesApplications-Type-Session-AuthenticationType"></a>
The authentication method. The user is authenticated using a streaming URL (`API`) or SAML 2.0 federation (`SAML`).
Type: String
Valid Values: `API | SAML | USERPOOL | AWS_AD`
Required: No

 ** ConnectionState **   <a name="WorkSpacesApplications-Type-Session-ConnectionState"></a>
Specifies whether a user is connected to the streaming session.
Type: String
Valid Values: `CONNECTED | NOT_CONNECTED`
Required: No

 ** InstanceDrainStatus **   <a name="WorkSpacesApplications-Type-Session-InstanceDrainStatus"></a>
The drain status of the instance hosting the streaming session. This only applies to multi-session fleets.
Type: String
Valid Values: `ACTIVE | DRAINING | NOT_APPLICABLE`
Required: No

 ** InstanceId **   <a name="WorkSpacesApplications-Type-Session-InstanceId"></a>
The identifier for the instance hosting the session.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** MaxExpirationTime **   <a name="WorkSpacesApplications-Type-Session-MaxExpirationTime"></a>
The time when the streaming session is set to expire. This time is based on the `MaxUserDurationinSeconds` value, which determines the maximum length of time that a streaming session can run. A streaming session might end earlier than the time specified in `SessionMaxExpirationTime`, when the `DisconnectTimeOutInSeconds` elapses or the user chooses to end his or her session. If the `DisconnectTimeOutInSeconds` elapses, or the user chooses to end his or her session, the streaming instance is terminated and the streaming session ends.
Type: Timestamp
Required: No

 ** NetworkAccessConfiguration **   <a name="WorkSpacesApplications-Type-Session-NetworkAccessConfiguration"></a>
The network details for the streaming session.
Type: [NetworkAccessConfiguration](API_NetworkAccessConfiguration.md) object
Required: No

 ** StartTime **   <a name="WorkSpacesApplications-Type-Session-StartTime"></a>
The time when a streaming instance is dedicated for the user.
Type: Timestamp
Required: No

## See Also
<a name="API_Session_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/Session)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/Session)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/Session)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
