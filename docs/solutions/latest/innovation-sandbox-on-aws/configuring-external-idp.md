---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/configuring-external-idp.html
---

# Configuring an external identity provider (Optional)
<a name="configuring-external-idp"></a>

## Group Management
<a name="group-management"></a>

Innovation Sandbox on AWS uses three different user groups that align with the different personas. These groups must be created following your normal process within the external provider. The group names must be exactly the same as they are specified in the IDC CloudFormation Stack parameters.

Personas and corresponding groups:

| Persona | Default Group Name | Responsibility |
| --- | --- | --- |
| Admin | <namespace>\_IsbAdminsGroup | The Admin persona is responsible for deploying and managing the solution and managing the AWS accounts used in the solution. |
| Manager | <namespace>\_IsbManagersGroup | The Manager persona is responsible for the creation and management of the Lease Templates (Sandbox thresholds and actions) and the Leases (active Sandbox accounts). |
| User | <namespace>\_IsbUsersGroup | The User persona is responsible for requesting and using Leases (Sandbox Accounts) |

## User Management
<a name="user-management"></a>

Users will be managed according to your normal process within your provider by adding the appropriate users into the one of the 3 ISB user groups.

Requirements:
+  **Email**: Ensure that the primary email field in the provider is populated with the correct email address.
  + Microsoft Entra: `mail`
  + Okta: `email`
+ The primary email field must be configured within your provider to be passed to IAM Identity Center.

You can confirm that a user’s email attribute has been successfully mapped and passed to the correct field in IAM Identity Center by running the following command in the **IDC Account** (Management or delegated account):

```
aws identitystore list-users --identity-store-id $(aws sso-admin list-instances --query "Instances[0].IdentityStoreId" --output text)
```

You can confirm that the correct email address is populated in the Emails array as shown below. The Email value should be correct and Primary should be set to true.

```
"Emails": [
    {
       "Value": "user@example.com",
       "Type": "work",
       "Primary": true
    }
]
```

## Attribute mapping examples
<a name="attribute-mapping-examples"></a>

The attribute mappings within your provider must be configured to map the user’s primary email field (from provider) to `emails[type eq "work"]` (to IAM Identity Center).

| External identity provider | Provider attribute | IAM Identity Center attribute |
| --- | --- | --- |
| Microsoft Entra | mail | emails[type eq "work"] |
| Okta | email | emails[type eq "work"] |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Innovation Sandbox on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
