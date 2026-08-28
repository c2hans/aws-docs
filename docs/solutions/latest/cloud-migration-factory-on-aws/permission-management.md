---
source_url: https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/permission-management.html
---

# Permission management
<a name="permission-management"></a>

The Cloud Migration Factory on AWS solution provides granular role-based access control to the data and automation functions available in the solution, underlying this is Amazon Cognito, providing the user directory and authentication engine.

The following table shows the various elements that make up the access control framework within the Cloud Migration Factory on AWS solution and where each element is managed from.

| Access control element | Management interface | Description |
| --- | --- | --- |
| User | Amazon Cognito and Cloud Migration Factory on AWS | Users are created, deleted, and updated in Amazon Cognito, where the users' profile can be established as well as multi-factor authentication (MFA) if required. Within the AWS CMF user interface, you can add and remove users from groups only. |
| Group | Cloud Migration Factory on AWS | You can create or delete groups from within the AWS CMF user interface. |
| Role | Cloud Migration Factory on AWS | A Role is mapped to one or many Groups, changing the groups a Role is assigned to is performed in the AWS CMF administration section. Any user that is a member of a group assigned to a role will be assigned all policies that are mapped to the role.<br />One or many policies can be assigned to a role. |
| Policy | Cloud Migration Factory on AWS | A policy contains the detailed rights that are assigned to any user to which the policy applies (via group membership). A single policy can include data access rights for multiple entities or a single entity, along with access rights to run automation jobs and other actions within the AWS CMF user interface. These policies also apply when a user is interacting with the AWS CMF APIs. |

## Policies
<a name="policies"></a>

A policy provides the most granular permissions possible in Cloud Migration Factory on AWS, it holds the tasks level definition of what rights are provided to a user. Within a policy there are two main permission types that can be granted to a user group, **Metadata Permissions** and **Automation Action Permissions**. Metadata permissions allow an administrator to control the level of access a group has to individual schemas and their attributes, specifying rights to create, read, update and/or delete as required. Automation Action permissions grant users access to run specific automation actions, such as the AWS MGN integration action.

### Metadata permissions
<a name="metadata-permissions"></a>

For each schema or entity within AWS CMF an administrator can define a policy that allows users access to specific attributes and also define the level of access they have to those attributes. On creation of a new policy, the default rights for all schemas are no access. The first thing that should be set is the level of access required for this policy at the item/record level. Below is a table describing the record level access permissions available.

| Access level | Description |
| --- | --- |
| Create | When selected, a user where this policy applies will have the ability to Add new records/items of this type to the metadata store. When create is selected but no other rights are allowed the user will have the ability to create records and set only required attributes to a value regardless of the selected attributes. |
| Read |  **Not yet implemented** <br />When selected, a user will have read rights to all records/items for this entity type, when not selected they will not see the data items in the UI or the API. |
| Update | When selected, a user where this policy applies will have the ability to update records/items of this type to the metadata store, but only for the attributes specified in the Attribute level access list. When update is selected at least one Attribute has to be selected or an error will be show on saving. |
| Delete | When selected, a user where this policy applies will have the ability to delete records/items of this type from the metadata store. |

## Roles
<a name="roles"></a>

Roles allow one or more policies to be assigned to one or more groups. The combination of all policies assigned to a role provides access permissions. Roles can be created based on job roles or functions within the project or organization.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Cloud Migration Factory on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
