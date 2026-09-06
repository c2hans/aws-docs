---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/avp-design-onboarding-registration.html
---

# Tenant onboarding and user tenant registration
<a name="avp-design-onboarding-registration"></a>

SaaS applications observe the concept of[ SaaS identities](https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/saas-identity.html) and follow the general best practice of [binding a user identity to a tenant identity](https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/general-design-principles.html). Binding involves storing a tenant identifier as a claim or attribute for the user in the identity provider. This shifts the responsibility of mapping identities to tenants from each application to the user registration process. Each authenticated user then has the correct tenant identity as part of the JSON Web Token (JWT).

Similarly, the selection of the correct policy store for an authorization request should not be determined by application logic. To determine which policy store a particular authorization request should use, maintain a mapping of users to policy stores, or tenants to policy stores. These mappings are typically maintained in a data store such as Amazon DynamoDB or Amazon Relational Database Service (Amazon RDS) that your application references. You can also provide or supplement these mappings by data in an identity provider (IdP). The relationship between tenants, users, and policy stores is then usually provided to a user through a JWT that contains all the relationships that are necessary for an authorization request.

This example shows how the JWT might appear for the user `Alice`, who belongs to the tenant `TenantA` and uses the policy store with the policy store ID `ps-43214321` for authorization.

```
{
   "sub":"1234567890",
   "name":"Alice",
   "tenant":"TenantA",
   "policyStoreId":"ps-43214321"
}
```
