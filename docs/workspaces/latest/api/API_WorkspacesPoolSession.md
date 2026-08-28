---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_WorkspacesPoolSession.html
---

# WorkspacesPoolSession
<a name="API_WorkspacesPoolSession"></a>

Describes a pool session.

## Contents
<a name="API_WorkspacesPoolSession_Contents"></a>

 ** PoolId **   <a name="WorkSpaces-Type-WorkspacesPoolSession-PoolId"></a>
The identifier of the pool.
Type: String
Pattern: `^wspool-[0-9a-z]{9}$`
Required: Yes

 ** SessionId **   <a name="WorkSpaces-Type-WorkspacesPoolSession-SessionId"></a>
The identifier of the session.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** UserId **   <a name="WorkSpaces-Type-WorkspacesPoolSession-UserId"></a>
The identifier of the user.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 128.
Required: Yes

 ** AuthenticationType **   <a name="WorkSpaces-Type-WorkspacesPoolSession-AuthenticationType"></a>
The authentication method. The user is authenticated using a WorkSpaces Pools URL (API) or SAML 2.0 federation (SAML).
Type: String
Valid Values: `SAML`
Required: No

 ** ConnectionState **   <a name="WorkSpaces-Type-WorkspacesPoolSession-ConnectionState"></a>
Specifies whether a user is connected to the pool session.
Type: String
Valid Values: `CONNECTED | NOT_CONNECTED`
Required: No

 ** ExpirationTime **   <a name="WorkSpaces-Type-WorkspacesPoolSession-ExpirationTime"></a>
The time that the pool session ended.
Type: Timestamp
Required: No

 ** InstanceId **   <a name="WorkSpaces-Type-WorkspacesPoolSession-InstanceId"></a>
The identifier for the instance hosting the session.
Type: String
Pattern: `^i-[a-f0-9]{8}(?:[a-f0-9]{9})?$`
Required: No

 ** NetworkAccessConfiguration **   <a name="WorkSpaces-Type-WorkspacesPoolSession-NetworkAccessConfiguration"></a>
Describes the network details of the pool.
Type: [NetworkAccessConfiguration](API_NetworkAccessConfiguration.md) object
Required: No

 ** StartTime **   <a name="WorkSpaces-Type-WorkspacesPoolSession-StartTime"></a>
The time that the pool sission started.
Type: Timestamp
Required: No

## See Also
<a name="API_WorkspacesPoolSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/WorkspacesPoolSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/WorkspacesPoolSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/WorkspacesPoolSession)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
