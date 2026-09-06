---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/opa-design-isolation.html
---

# Tenant isolation with the OPA document model
<a name="opa-design-isolation"></a>

OPA uses documents to make decisions. These documents can contain tenant-specific data, so you must consider how to maintain tenant data isolation. OPA documents consist of base documents and virtual documents. Base documents contain data from the the outside world. This includes data provided to OPA directly, data about the OPA request, and data that might be passed to OPA as input. Virtual documents are computed by policy and include OPA policies and rules. For more information, see the[ OPA documentation](https://www.openpolicyagent.org/docs/latest/philosophy/).

To design a document model in OPA for a multi-tenant application, you must first consider what type of base documents you will need to make a decision in OPA. If these base documents contain tenant-specific data, you must take measures to ensure that this data isn't accidentally exposed to cross-tenant access. Fortunately, in many cases, tenant-specific data isn't required to make a decision in OPA. The following example shows a hypothetical OPA document model that allows access to an API based on which tenant owns the API, and whether the user is a member of the tenant, as indicated in the input document.

![Basic OPA document model](http://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/images/guide-img/1bc1ddcc-09fb-41af-88b1-99d94e62fa1f/images/fafb55e1-6add-43a8-a222-26a77fee87dc.png)

In this approach, OPA doesn't have access to any tenant-specific data except for information about which tenants own an API. In this case, there is no concern over OPA facilitating cross-tenant access, because the only information OPA uses to make an access decision is a user's association with a tenant and the tenant's association with APIs. You could apply this type of OPA document model to a siloed SaaS model, because each tenant would have ownership of independent resources.

However, in many RBAC authorization approaches, there is the potential for cross-tenant exposure of information. In the following example, a hypothetical OPA document model allows access to an API based on whether a user is a member of a tenant, and whether the user has the correct role to access the the API.

![OPA document model for cross-tenant use case](http://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/images/guide-img/1bc1ddcc-09fb-41af-88b1-99d94e62fa1f/images/2bc5bde5-9f55-4121-8879-c673c7e9f88f.png)

This model introduces a risk of cross-tenant access, because multiple tenants' roles and permissions in `data.tenant1.user_roles` and `data.tenant2.user_roles` must now be made accessible to OPA to make authorization decisions. To maintain tenant isolation and the privacy of role mapping, this data should not reside within OPA. RBAC data should reside in an external data source such as a database. Furthermore, OPA should not be used to map predefined roles to specific permissions, because this makes it difficult for tenants to define their own roles and permissions. It also makes your authorization logic rigid and in need of constant update. For guidance on how to safely incorporate RBAC data into the OPA decision-making process, see the section [Recommendations for tenant isolation and data privacy](devops-isolation-privacy.md) later in this guide.

You can easily maintain tenant isolation in OPA by not storing any tenant-specific data as an asynchronous base document. An asynchronous base document is data that is stored in memory and can be periodically updated, in OPA. Other base documents, such as OPA input, are passed synchronously and are available only at decision time. For example, providing tenant-specific data as part of OPA input to a query would not constitute a breach of tenant isolation, because that data is available only synchronously during the process of making a decision.
