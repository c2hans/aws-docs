---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cognito-identity_example_cognito-identity_SetIdentityPoolRoles_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `SetIdentityPoolRoles` with a CLI
<a name="cognito-identity_example_cognito-identity_SetIdentityPoolRoles_section"></a>

The following code examples show how to use `SetIdentityPoolRoles`.

------
#### [ CLI ]

**AWS CLI**
**To set identity pool roles**
The following `set-identity-pool-roles` example sets an identity pool role.

```
aws cognito-identity set-identity-pool-roles \
    --identity-pool-id {{"us-west-2:11111111-1111-1111-1111-111111111111"}} \
    --roles authenticated="arn:aws:iam::111111111111:role/Cognito_MyIdentityPoolAuth_Role"
```
+  For API details, see [SetIdentityPoolRoles](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/set-identity-pool-roles.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: Configures the specific Identity Pool to have an unauthenticated IAM role.**

```
Set-CGIIdentityPoolRole -IdentityPoolId us-east-1:0de2af35-2988-4d0b-b22d-EXAMPLEGUID1 -Role @{ "unauthenticated" = "arn:aws:iam::123456789012:role/CommonTests1Role" }
```
+  For API details, see [SetIdentityPoolRoles](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: Configures the specific Identity Pool to have an unauthenticated IAM role.**

```
Set-CGIIdentityPoolRole -IdentityPoolId us-east-1:0de2af35-2988-4d0b-b22d-EXAMPLEGUID1 -Role @{ "unauthenticated" = "arn:aws:iam::123456789012:role/CommonTests1Role" }
```
+  For API details, see [SetIdentityPoolRoles](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
