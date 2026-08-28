---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/access-control-types.html
---

# Types of access control
<a name="access-control-types"></a>

You can use two broadly defined models to implement access control: role-based access control (RBAC) and attribute-based access control (ABAC). Each model has advantages and disadvantages, which are briefly discussed in this section. The model you should use depends on your specific use case. The architecture discussed in this guide supports both models.

## RBAC
<a name="rbac"></a>

Role-based access control (RBAC) determines access to resources based on a role that usually aligns with business logic. Permissions are associated with the role as appropriate. For instance, a *marketing* role would authorize a user to perform *marketing* activities within a restricted system. This is a relatively simple access control model to implement because it aligns well to easily recognizable business logic.

The RBAC model is less effective when:
+ You have unique users whose responsibilities encompass several roles.
+ You have complex business logic that makes roles difficult to define.
+ Scaling up to a large size requires constant administration and mapping of permissions to new and existing roles.
+ Authorizations are based on dynamic parameters.

## ABAC
<a name="abac"></a>

Attribute-based access control (ABAC) determines access to resources based on attributes. Attributes can be associated with a user, resource, environment, or even application state. Your policies or rules reference attributes and can use basic Boolean logic to determine whether a user is permitted to perform an action. Here's a basic example of permissions:

*In the payments system, all users in the Finance department are allowed to process payments at the API endpoint *`/payments`* during business hours. *

Membership in the Finance department is a user attribute that determines access to `/payments`. There is also a resource attribute associated with the `/payments` API endpoint that permits access only during business hours. In ABAC, whether or not a user can process a payment is determined by a policy that includes the Finance department membership as a user attribute, and the time as a resource attribute of `/payments`.

The ABAC model is very flexible in allowing dynamic, contextual, and granular authorization decisions. However, the ABAC model is difficult to implement initially. Defining rules and policies as well as enumerating attributes for all relevant access vectors require a significant upfront investment to implement.

## RBAC-ABAC hybrid approach
<a name="hybrid"></a>

Combining RBAC and ABAC can provide some of the advantages of both models. RBAC, being aligned so closely to business logic, is simpler to implement than ABAC. To provide an additional layer of granularity when making authorization decisions, you can combine ABAC with RBAC. This hybrid approach determines access by combining a user's role (and its assigned permissions) with additional attributes to make access decisions. Using both models enables simple administration and assignment of permissions while also permitting increased flexibility and granularity pertaining to authorization decisions.

## Access control model comparison
<a name="comparison"></a>

The following table compares the three access control models discussed previously. This comparison is meant to be informative and high-level. Using an access model in a specific situation might not necessarily correlate to the comparisons made in this table.

|
|
| Factor | RBAC | ABAC | Hybrid |
| --- |--- |--- |--- |
| **Flexibility** | Medium  | High | High |
| **Simplicity** | High | Low | Medium |
| **Granularity** | Low | High | Medium |
| **Dynamic decisions and rules** | No | Yes | Yes |
| **Context-aware** | No | Yes | Somewhat |
| **Implementation effort** | Low | High | Medium |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
