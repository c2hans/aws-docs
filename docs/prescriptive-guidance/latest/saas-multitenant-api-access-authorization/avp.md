---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/avp.html
---

# Implementing a PDP by using Amazon Verified Permissions
<a name="avp"></a>

Amazon Verified Permissions is a scalable, fine-grained permissions management and authorization service that you can use to implement a policy decision point (PDP). As a policy engine, it can help your application verify user actions in real time and highlight permissions that are overly privileged or invalid. It helps your developers build more secure applications faster by externalizing authorization and centralizing policy management and administration. By separating authorization logic from application logic, Verified Permissions supports *policy decoupling. *

By using Verified Permissions to implement a PDP and implementing least privilege and continual verification within applications, developers can align their application access with [Zero Trust](https://aws.amazon.com/security/zero-trust/) principles. Additionally, security and audit teams can better analyze and audit who has access to which resources within an application. Verified Permissions uses [Cedar](https://www.cedarpolicy.com/en), which is a purpose-built and security-first, open source policy language, to define policy-based access controls based on role-based access control (RBAC) and attribute-based access control (ABAC) for more granular, context-aware access control.

Verified Permissions provides some useful features for SaaS applications, such as the ability to enable multi-tenant authorization by using multiple identity providers such as Amazon Cognito, Google, and Facebook. Another Verified Permissions feature that is particularly helpful for SaaS applications is support for custom roles on a per-tenant basis. If you're designing a customer relationship management (CRM) system, one tenant might define granularity of access by sales opportunities based on one particular set of criteria. Another tenant might have another definition. The underlying permissions systems in Verified Permissions can support these variations, which makes it an excellent candidate for SaaS use cases. Verified Permissions also supports the ability to write policies that apply to all tenants, so it is straightforward to apply guardrail policies to prevent unauthorized access as a SaaS provider.

![Using Amazon Verified Permissions to implement a PDP](https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/images/guide-img/1bc1ddcc-09fb-41af-88b1-99d94e62fa1f/images/760153f4-fc01-435a-9f20-8eea3eb12508.png)

**Why use Verified Permissions?**

Use Verified Permissions with an identity provider such as [Amazon Cognito](https://aws.amazon.com/cognito/) for a more dynamic, policy-based access management solution for your applications. You can build applications that help users share information and collaborate while maintaining the security, confidentiality, and privacy of their data. Verified Permissions helps reduce operational costs by providing you with a fine-grained authorization system to enforce access based on the roles and attributes of your identities and resources. You can define your policy model, create and store policies in a central location, and evaluate access requests in milliseconds.

In Verified Permissions, you can express permissions by using a simple, human-readable declarative language called Cedar. Policies that are written in Cedar can be shared across teams regardless of the programming language used by each team's application.

**What to consider when you use Verified Permissions**

In Verified Permissions, you can create policies and automate them as part of provisioning. You can also create policies at runtime as part of application logic. As a best practice, you should use a continuous integration and continuous deployment (CI/CD) pipeline to administer, modify, and track policy versions when you create policies as part of tenant onboarding and provisioning. Alternatively, an application can administer, modify, and track policy versions; however, application logic doesn't inherently perform this functionality. To support these capabilities in your application, you must explicitly design your application to implement this functionality.

If it's necessary to provide external data from other sources to reach an authorization decision, this data must be retrieved and provided to Verified Permissions as part of the authorization request. Additional context, entities, and attributes are not retrieved by default with this service.
