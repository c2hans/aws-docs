---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/devops-isolation-privacy.html
---

# Recommendations for tenant isolation and privacy of data
<a name="devops-isolation-privacy"></a>

The previous section provided several approaches for using external data with OPA and Amazon Verified Permissions to assist in making authorization decisions. Where possible, we recommend that you use the overload input approach for passing SaaS context data to OPA to make authorization decisions instead of storing data in OPA's memory. This use case doesn't apply to AWS Cloud Map, because it doesn't support storing external data in the service.

In role-based access control (RBAC) or RBAC and attribute-based access control (ABAC) hybrid models, the data provided solely by an authorization request or query might be insufficient, because roles and permissions have to be referenced to make authorization decisions. **To maintain tenant isolation and the privacy of role mapping, this data should not reside within OPA.** RBAC data should reside in an external data source such as a database or should be passed as part of claims in a JWT from an IdP. In Verified Permissions, RBAC data can be maintained as part of policies and schema in the per-tenant policy store model, because each tenant has its own logically separated policy store. However, **in the one shared multi-tenant policy store model, role mapping data should not reside within Verified Permissions to maintain tenant isolation**.

Furthermore, OPA and Verified Permissions shouldn't be used to map predefined roles to specific permissions, because this makes it difficult for tenants to define their own roles and permissions. It also makes your authorization logic rigid and in need of constant update. The exception to this guideline is the per-tenant policy store model in Verified Permissions, because this model allows each tenant to have its own policies that can be evaluated independently on a per-tenant basis.

## Amazon Verified Permissions
<a name="avp-data-storage"></a>

The only place where Verified Permissions can store potentially private RBAC data is in the schema. This is acceptable in the per-tenant policy store model, because each tenant has its own logically separated policy store. However, it could compromise tenant isolation in the one shared multi-tenant policy store model. In cases where this data is required to make an authorization decision, it should be retrieved from an external source such as DynamoDB or Amazon RDS and incorporated into the Verified Permissions authorization request.

## OPA
<a name="opa-data-storage"></a>

Secure approaches with OPA for maintaining the privacy and tenant isolation of RBAC data include using dynamic data retrieval or replication to get external data. This is because you can use the authorization service illustrated in the previous diagram to provide only tenant-specific or user-specific external data for making an authorization decision. For example, you can use a replicator to provide RBAC data or a permissions matrix to the OPA cache when a user logs in, and have the data be referenced based on a user provided in the input data . You can use a similar approach with dynamically pulled data to retrieve only the relevant data for making authorization decisions. Furthermore, in the dynamic data retrieval approach, this data doesn't have to be cached in OPA. The bundling approach isn't as effective as the dynamic retrieval approach at maintaining tenant isolation, because it updates everything in the OPA cache and can't process precise updates. The bundling model is still a good approach for updating OPA policies and non-RBAC data.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
