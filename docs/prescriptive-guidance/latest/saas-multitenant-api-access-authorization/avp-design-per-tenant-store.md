---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/avp-design-per-tenant-store.html
---

# Per-tenant policy store
<a name="avp-design-per-tenant-store"></a>

The per-tenant policy store design model in Amazon Verified Permissions associates each tenant in a SaaS application with its own policy store. This model is similar to the SaaS [silo isolation](https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/silo-isolation.html) model. Both models mandate the creation of tenant-specific infrastructure and have similar benefits and disadvantages. The primary benefits of this approach are infrastructure-enforced tenant isolation, support for unique authorization models on a per-tenant basis, elimination of [noisy neighbor](https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/noisy-neighbor.html) concerns, and a reduced scope of impact for failure in policy updates or deployments. The disadvantages of this approach include more complex tenant onboarding processes, deployments, and operations. Per-tenant policy store is the recommended approach if the solution has unique policies per tenant.

The per-tenant policy store model can provide a highly siloed approach to tenant isolation, if your SaaS application requires it. You can also use this model with [pool isolation](https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/pool-isolation.html), but your Verified Permissions implementation won't share the standard benefits of the broader pool isolation model such as simplified management and operations.

In a per-tenant policy store, tenant isolation is achieved by mapping a tenant's policy store identifier to the SaaS Identity of the user during the user registration process, as discussed earlier. This approach strongly ties the tenant's policy store to the user principal and provides a consistent way to share the mapping throughout the entire SaaS solution. You can provide the mapping to a SaaS application by maintaining it as part of an IdP or in an external data source such as DynamoDB. This also ensures that the principal is part of the tenant and that the policy store of the tenant is used.

This example shows how the JWT that contains the `policyStoreId` and `tenant` of a user is passed from the an API endpoint to the policy evaluation point in an AWS Lambda authorizer, which routes the request to the correct policy store.

![Per-tenant policy store model in Amazon Verified Permissions](https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/images/guide-img/1bc1ddcc-09fb-41af-88b1-99d94e62fa1f/images/c9e5139c-6a62-4793-9266-2ef50f30449b.png)

The following sample policy illustrates the per-tenant policy store design paradigm. The user `Alice` belongs to `TenantA.` The policyStoreId `store-a` is also mapped to the tenant identity of `Alice,` and enforces the use of the correct policy store. This ensures that the policies of `TenantA` are used.

**Note**
The per-tenant policy store model isolates the policies of tenants. Authorization enforces the actions users are allowed to perform on their data. The resources involved in any hypothetical application that uses this model should be isolated by using other isolation mechanisms, as defined in the [AWS Well-Architected Framework, SaaS Lens documentation](https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/core-isolation-concepts.html).

In this policy, `Alice` has permissions to view the data of all resources.

```
permit (
    principal == MultiTenantApp::User::"Alice",
    action == MultiTenantApp::Action::"viewData",
    resource
);
```

To make an authorization request and start an evaluation with a Verified Permissions policy, you need to provide the policy store ID that corresponds to the unique ID mapped to the tenant, `store-a`.

```
{
   "policyStoreId":"store-a",
   "principal":{
      "entityType":"MultiTenantApp::User",
      "entityId":"Alice"
   },
   "action":{
      "actionType":"MultiTenantApp::Action",
      "actionId":"viewData"
   },
   "resource":{
      "entityType":"MultiTenantApp::Data",
      "entityId":"my_example_data"
   },
   "entities":{
      "entityList":[
         [
            {
               "identifier":{
                  "entityType":"MultiTenantApp::User",
                  "entityId":"Alice"
               },
               "attributes":{},
               "parents":[]
            },
            {
               "identifier":{
                  "entityType":"MultiTenantApp::Data",
                  "entityId":"my_example_data"
               },
               "attributes":{},
               "parents":[]
            }
         ]
      ]
   }
}
```

The user `Bob` belongs to Tenant B, and the policyStoreId `store-b` is also mapped to the tenant identity of `Bob`, which enforces the use of the correct policy store. This ensures that the polices of Tenant B are used.

In this policy, `Bob` has permissions to customize the data of all resources. In this example, `customizeData` might be an action that is specific only to Tenant B, so the policy would be unique for Tenant B. The per-tenant policy store model inherently supports custom policies on a per-tenant basis.

```
permit (
    principal == MultiTenantApp::User::"Bob",
    action == MultiTenantApp::Action::"customizeData",
    resource
);
```

To make an authorization request and start an evaluation with a Verified Permissions policy, you need to provide the policy store ID that corresponds to the unique ID mapped to the tenant, `store-b`.

```
{
   "policyStoreId":"store-b",
   "principal":{
      "entityType":"MultiTenantApp::User",
      "entityId":"Bob"
   },
   "action":{
      "actionType":"MultiTenantApp::Action",
      "actionId":"customizeData"
   },
   "resource":{
      "entityType":"MultiTenantApp::Data",
      "entityId":"my_example_data"
   },
   "entities":{
      "entityList":[
         [
            {
               "identifier":{
                  "entityType":"MultiTenantApp::User",
                  "entityId":"Bob"
               },
               "attributes":{},
               "parents":[]
            },
            {
               "identifier":{
                  "entityType":"MultiTenantApp::Data",
                  "entityId":"my_example_data"
               },
               "attributes":{},
               "parents":[]
            }
         ]
      ]
   }
}
```

With Verified Permissions, it is possible, but not required, to integrate an IdP with a policy store. This integration allows for policies to explicitly reference the principal in the identity store as the policies' principal. For more information about how to integrate with Amazon Cognito as an IdP for Verified Permissions, see the [Verified Permissions documentation](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/identity-providers.html) and [Amazon Cognito documentation](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-authorization-with-avp.html).

When you integrate a policy store with an IdP, you can use only one [identity source](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/identity-providers.html) per policy store. For example, if you choose to integrate Verified Permissions with Amazon Cognito, you have to mirror the strategy used for tenant isolation of Verified Permissions policy stores and Amazon Cognito user pools. The policy stores and user pools also have to be in the same AWS account.

![Integrating Verified Permissions with Amazon Cognito in per-tenant design model](https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/images/guide-img/1bc1ddcc-09fb-41af-88b1-99d94e62fa1f/images/57860d3b-f683-4c62-9099-2138621e4faa.png)

On an operational level, the per-tenant policy store has an audit advantage, because you can easily query the [logged activity in ](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/monitoring-overview.html)AWS CloudTrail independently for each tenant. However, we still recommend that you log additional custom metrics on a per-tenant dimension to Amazon CloudWatch.

The per-tenant policy store approach also requires close attention to two [Verified Permissions quotas](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/quotas.html) to ensure that they don't interfere with the operations of your SaaS solution. These quotas are *Policy stores per Region per account* and *IsAuthorized requests per second per Region per account*. You can request increases for both quotas.

For a more detailed example of how to implement the per-tenant policy store model, see the AWS blog post [SaaS access control using Amazon Verified Permissions with a per-tenant policy store](https://aws.amazon.com/blogs/security/saas-access-control-using-amazon-verified-permissions-with-a-per-tenant-policy-store/).
