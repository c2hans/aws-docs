---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/acxd-accessing-workspace.html
---

# Accessing an Agentic CX Designer workspace
<a name="acxd-accessing-workspace"></a>

Agentic CX Designer is accessed through Amazon Connect Customer and organized into workspaces.

A workspace is a standalone environment where teams build and manage conversational AI applications. Each workspace has its own applications, flows, integrations, knowledge bases, guardrails, analytics, users, roles, and settings.

Because workspaces are separate, resources and permissions are not shared automatically across them. Changes made in one workspace do not affect another workspace.

## Access from Connect Customer
<a name="acxd-accessing-workspace-connect"></a>

Access to Agentic CX Designer starts from Connect Customer.
+ Select your Connect Customer instance.
+ From your instance, select Agentic CX Designer.

Users can launch Agentic CX Designer from the Connect Customer console. Account administrators can access the Admin Hub in Agentic CX Designer to create one or more workspaces and assign users to those workspaces.

When adding users, Account Administrators select from user profiles already available in the connected Connect Customer instance.

After a user profile is added to a workspace, the Account Administrator assigns that user a workspace role. The role determines what the user can view, create, edit, or manage inside that workspace.

**To access Agentic CX Designer**

1. Open the Amazon Connect Customer console.

1. Select Agentic CX Designer.

If a user cannot access the expected workspace, they should contact an Account Administrator to confirm that their Connect Customer user profile has been added to the workspace and assigned the correct role.

## Workspace resources
<a name="acxd-accessing-workspace-resources"></a>

Inside a workspace, users can create and manage resources such as:

|  |  |
| --- |--- |
| **Applications** | The conversational AI experiences users interact with. |
| **Flows** | The conversation paths that guide users through tasks. |
| **Canvas** | The visual builder used to create and connect flow nodes. |
| **Integrations** | Connections to external tools, APIs, and services. |
| **Knowledge bases** | Trusted content the AI can use to answer questions. |
| **Variables** | Dynamic values captured, remembered, or referenced during a conversation. |
| **Guardrails** | Safety, brand, and compliance controls. |
| **Analytics** | Performance data used to monitor and improve experiences. |
| **Roles and permissions** | Access controls that determine what each person can view or manage within that workspace. |

## Switching workspaces
<a name="acxd-accessing-workspace-switching"></a>

If you are an Account Administrator or have been assigned a role in more than one workspace, you can switch between workspaces from the workspace dropdown in the upper-left corner of an Agentic CX Designer workspace.

When you switch workspaces, you are changing which set of resources you are viewing and editing.

Only workspaces you have permission to access appear in the dropdown.

Each workspace is separate.

This means:
+ Applications in one workspace do not appear in another workspace.
+ Flows, integrations, knowledge bases, guardrails, and analytics are managed independently.
+ Users must be assigned to each workspace where they need access.
+ A role in one workspace does not automatically grant the same role in another workspace.
+ Changes made in one workspace do not affect resources in another workspace.

Workspace separation helps teams organize work safely and keep resources permissioned appropriately.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
