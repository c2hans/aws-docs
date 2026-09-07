---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/avp-design-shared-store.html
---

# One shared multi-tenant policy store
<a name="avp-design-shared-store"></a>

The one shared multi-tenant policy store design model uses a single multi-tenant policy store in Amazon Verified Permissions for all tenants in the SaaS solution. The primary benefit of this approach is simplified management and operations, particularly because you don't have to create additional policy stores during tenant onboarding. The disadvantages of this approach include an increased scope of impact from any failure or mistakes in policy updates or deployments, and a greater exposure to [noisy neighbor](https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/noisy-neighbor.html) effects. Furthermore, we don't recommend this approach if your solution requires unique policies for each tenant. In this case, use the per-tenant policy store model instead to guarantee that the policies of the correct tenant are used.

The one shared multi-tenant policy store approach is similar to the SaaS [pooled isolation](https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/pool-isolation.html) model. It can provide a pooled approach to tenant isolation, if your SaaS application requires it. You can also use this model if your SaaS solution applies [siloed isolation](https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/silo-isolation.html) to its microservices. When you choose a model, you should evaluate the requirements for tenant data isolation and the structure of Verified Permissions policies that are necessary for a SaaS application independently.

To enforce a consistent way of sharing the tenant identifier across your entire SaaS solution, it's a good practice to map the identifier to the user's SaaS identity during user registration, as discussed previously. You can provide this mapping to a SaaS application by maintaining it as part of an IdP or in an external data source such as DynamoDB. We also recommend that you map the shared policy store ID to users. Although the ID isn't used as part of tenant isolation, this is a good practice because it facilitates future changes.

The following example shows how the API endpoint sends a JWT for the users `Alice` and `Bob`, who belong to different tenants but share the policy store with the policy store ID `store-multi-tenant` for authorization. Because all tenants share a single policy store, you don't need to maintain the policy store ID in a token or database. Because all tenants share a single policy store ID, you can provide the ID as an environment variable that your application can use to make calls to the policy store.

![Amazon Verified Permissions shared design model](https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/images/guide-img/1bc1ddcc-09fb-41af-88b1-99d94e62fa1f/images/5d09c1a4-884a-4478-b9df-75e9be5dc45d.png)

The following sample policy illustrates the one shared multi-tenant policy design paradigm. In this policy, the principal `MultiTenantApp::User` that has the parent `MultiTenantApp::Role` `Admin` has permissions to view the data of all resources.

```
permit (
    principal in MultiTenantApp::Role::"Admin",
    action == MultiTenantApp::Action::"viewData",
    resource
);
```

Because a single policy store is in use, the Verified Permissions policy store must ensure that a tenancy attribute that's associated with the principal matches the tenancy attribute that's associated with the resource. This can be accomplished by including the following policy in the policy store, to ensure that all authorization requests that don't have matching tenancy attributes on the resource and principal are rejected.

```
forbid(
    principal,
    action,
    resource
)
unless {
    resource.Tenant == principal.Tenant
};
```

For an authorization request that uses a one shared multi-tenant policy store model, the policy store ID is the identifier of the shared policy store. In the following request, the `User` `Alice` is allowed access because she has a `Role` of `Admin`, and the `Tenant` attributes associated with the resource and principal are both `TenantA`.

```
{
   "policyStoreId":"store-multi-tenant",
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
         {
            "identifier":{
               "entityType":"MultiTenantApp::User",
               "entityId":"Alice"
            },
            "attributes": {
                {
                    "Tenant": {
                        "entityIdentifier": {
                            "entityType":"MultitenantApp::Tenant",
                            "entityId":"TenantA"
                        }
                    }
                }
            },
            "parents":[
               {
                  "entityType":"MultiTenantApp::Role",
                  "entityId":"Admin"
               }
            ]
         },
         {
            "identifier":{
               "entityType":"MultiTenantApp::Data",
               "entityId":"my_example_data"
            },
            "attributes": {
                {
                    "Tenant": {
                        "entityIdentifier": {
                            "entityType":"MultitenantApp::Tenant",
                            "entityId":"TenantA"
                        }
                    }
                }
            },
            "parents":[]
         }
      ]
   }
}
```

With Verified Permissions, it is possible, but not required, to integrate an IdP with a policy store. This integration allows for policies to explicitly reference the principal in the identity store as the policies' principal. For more information about how to integrate with Amazon Cognito as an IdP for Verified Permissions, see the [Verified Permissions documentation](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/identity-providers.html) and [Amazon Cognito documentation](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-authorization-with-avp.html).

When you integrate a policy store with an IdP,you can use only one [identity source](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/identity-providers.html) per policy store. For example, if you choose to integrate Verified Permissions with Amazon Cognito, you have to mirror the strategy used for tenant isolation of Verified Permissions policy stores and Amazon Cognito user pools. The policy stores and user pools also have to be in the same AWS account.

![Integrating Verified Permissions with Amazon Cognito in shared design model](https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/images/guide-img/1bc1ddcc-09fb-41af-88b1-99d94e62fa1f/images/c9231b42-f0bf-4089-bc48-f87efcb6aa78.png)

From operational and audit perspectives, the one shared multi-tenant policy store model has a disadvantage in that the [logged activity in AWS CloudTrail](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/monitoring-overview.html) requires more involved queries to filter out individual activity on the tenant, because each logged CloudTrail call uses the same policy store. In this scenario, it is helpful to log additional custom metrics on a per-tenant dimension to Amazon CloudWatch to ensure an appropriate level of observability and audit capability.

The one shared multi-tenant policy store approach also requires close attention to [Verified Permissions quotas](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/quotas.html) to ensure that they don't interfere with the operations of your SaaS solution. In particular, we recommend that you monitor the *IsAuthorized requests per second per Region per account* quota to ensure that its limitations are not exceeded. You can request an increase to this quota.
