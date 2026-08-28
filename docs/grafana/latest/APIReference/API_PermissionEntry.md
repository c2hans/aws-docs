---
source_url: https://docs.aws.amazon.com/grafana/latest/APIReference/API_PermissionEntry.html
---

# PermissionEntry
<a name="API_PermissionEntry"></a>

A structure containing the identity of one user or group and the `Admin`, `Editor`, or `Viewer` role that they have.

## Contents
<a name="API_PermissionEntry_Contents"></a>

 ** role **   <a name="ManagedGrafana-Type-PermissionEntry-role"></a>
Specifies whether the user or group has the `Admin`, `Editor`, or `Viewer` role.
Type: String
Valid Values: `ADMIN | EDITOR | VIEWER`
Required: Yes

 ** user **   <a name="ManagedGrafana-Type-PermissionEntry-user"></a>
A structure with the ID of the user or group with this role.
Type: [User](API_User.md) object
Required: Yes

## See Also
<a name="API_PermissionEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/grafana-2020-08-18/PermissionEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/grafana-2020-08-18/PermissionEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/grafana-2020-08-18/PermissionEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Grafana. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query grafana` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
