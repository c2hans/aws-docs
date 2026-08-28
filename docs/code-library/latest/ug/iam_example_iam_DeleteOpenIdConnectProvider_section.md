---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/iam_example_iam_DeleteOpenIdConnectProvider_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DeleteOpenIdConnectProvider` with a CLI
<a name="iam_example_iam_DeleteOpenIdConnectProvider_section"></a>

The following code examples show how to use `DeleteOpenIdConnectProvider`.

------
#### [ CLI ]

**AWS CLI**
**To delete an IAM OpenID Connect identity provider**
This example deletes the IAM OIDC provider that connects to the provider `example.oidcprovider.com`.

```
aws iam delete-open-id-connect-provider \
    --open-id-connect-provider-arn {{arn:aws:iam::123456789012:oidc-provider/example.oidcprovider.com}}
```
This command produces no output.
For more information, see [Creating OpenID Connect (OIDC) identity providers](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html) in the *AWS IAM User Guide*.
+  For API details, see [DeleteOpenIdConnectProvider](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-open-id-connect-provider.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example deletes the IAM OIDC provider that connects to the provider `example.oidcprovider.com`. Ensure that you update or delete any roles that reference this provider in the `Principal` element of the role's trust policy.**

```
Remove-IAMOpenIDConnectProvider -OpenIDConnectProviderArn arn:aws:iam::123456789012:oidc-provider/example.oidcprovider.com
```
+  For API details, see [DeleteOpenIdConnectProvider](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example deletes the IAM OIDC provider that connects to the provider `example.oidcprovider.com`. Ensure that you update or delete any roles that reference this provider in the `Principal` element of the role's trust policy.**

```
Remove-IAMOpenIDConnectProvider -OpenIDConnectProviderArn arn:aws:iam::123456789012:oidc-provider/example.oidcprovider.com
```
+  For API details, see [DeleteOpenIdConnectProvider](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
