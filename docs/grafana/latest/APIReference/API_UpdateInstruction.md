---
source_url: https://docs.aws.amazon.com/grafana/latest/APIReference/API_UpdateInstruction.html
---

# UpdateInstruction
<a name="API_UpdateInstruction"></a>

Contains the instructions for one Grafana role permission update in a [UpdatePermissions](https://docs.aws.amazon.com/grafana/latest/APIReference/API_UpdatePermissions.html) operation.

## Contents
<a name="API_UpdateInstruction_Contents"></a>

 ** action **   <a name="ManagedGrafana-Type-UpdateInstruction-action"></a>
Specifies whether this update is to add or revoke role permissions.
Type: String
Valid Values: `ADD | REVOKE`
Required: Yes

 ** role **   <a name="ManagedGrafana-Type-UpdateInstruction-role"></a>
The role to add or revoke for the user or the group specified in `users`.
Type: String
Valid Values: `ADMIN | EDITOR | VIEWER`
Required: Yes

 ** users **   <a name="ManagedGrafana-Type-UpdateInstruction-users"></a>
A structure that specifies the user or group to add or revoke the role for.
Type: Array of [User](API_User.md) objects
Required: Yes

## See Also
<a name="API_UpdateInstruction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/grafana-2020-08-18/UpdateInstruction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/grafana-2020-08-18/UpdateInstruction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/grafana-2020-08-18/UpdateInstruction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Grafana. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query grafana` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
