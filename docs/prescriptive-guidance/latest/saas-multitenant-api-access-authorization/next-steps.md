---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/next-steps.html
---

# Next steps
<a name="next-steps"></a>

The complexity of authorization and API access control for multi-tenant SaaS applications can be overcome by adopting a standardized, language-agnostic approach to making authorization decisions. These approaches incorporate policy decision points (PDPs) and policy enforcement points (PDPs) that enforce access in a flexible and pervasive manner. Multiple approaches to access control—such as role-based access control (RBAC), attribute-based access control (ABAC), or a combination of the two—can be incorporated into a cohesive access control strategy. Removing authorization logic from an application eliminates the overhead of including ad hoc solutions in application code to address access control. The implementation and best practices discussed in this guide are intended to inform and standardize an approach to the implementation of authorization and API access control in multi-tenant SaaS applications. You can use this guidance as the first step in gathering information and designing a robust access control and authorization system for your application. **Next steps:**
+ Review your authorization and tenant isolation needs, and select an access control model for your application.
+ Build a proof of concept for testing by using either [Amazon Verified Permissions](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/getting-started-first-policy-store.html) or [Open Policy Agent (OPA),](https://www.openpolicyagent.org/docs/latest/) or by writing your own custom policy engine.
+ Identify APIs and locations in your application where PEPs should be implemented.
