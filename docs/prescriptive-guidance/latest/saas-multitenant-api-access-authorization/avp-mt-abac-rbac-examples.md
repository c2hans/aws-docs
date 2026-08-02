---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/avp-mt-abac-rbac-examples.html
---

# Example 4: Multi-tenant access control with RBAC and ABAC
<a name="avp-mt-abac-rbac-examples"></a>

To enhance the RBAC example in the previous section, you can add attributes to users to create a RBAC-ABAC hybrid approach for multi-tenant access control. This example includes the same roles from the previous example, but adds the user attribute `account_lockout_flag` and the context parameter `uses_mfa`. The example also takes a different approach to implementing multi-tenant access control by using both RBAC and ABAC, and uses one shared policy store instead of a different policy store for each tenant.

![Example of multi-tenant access control with RBAC, ABAC, Amazon Verified Permissions, and Cedar](http://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/images/guide-img/1bc1ddcc-09fb-41af-88b1-99d94e62fa1f/images/2c37b61d-2ff6-4d20-81e9-b9ecdfb648ff.png)

This example represents a multi-tenant SaaS solution in which you need to provide authorization decisions for Tenant A and Tenant B, similar to the previous example.

To implement the user lock feature, the example adds the attribute `account_lockout_flag` to the `User` entity principal in the authorization request. This flag locks user access to the system and will `DENY` all privileges to the locked out user. The `account_lockout_flag` attribute is associated with the `User` entity and is in effect for the `User` until the flag is actively revoked across multiple sessions. The example uses the `when` condition to evaluate `account_lockout_flag`.

The example also adds details about the request and session. The context information specifies that the session has been authenticated by using multi-factor authentication. To implement this validation, the example uses the `when` condition to evaluate the `uses_mfa` flag as part of the context field. For more information about best practices for adding context, see the [Cedar documentation](https://docs.cedarpolicy.com/auth/entities-syntax.html).

```
permit (
    principal in MultitenantApp::Role::"allAccessRole",
    action in [
        MultitenantApp::Action::"viewData",
        MultitenantApp::Action::"updateData"
    ],
    resource
)
when {
    principal.account_lockout_flag == false &&
    context.uses_mfa == true &&
    resource in principal.Tenant
};
```

This policy prevents access to resources unless the resource is in the same group as the requesting principal's `Tenant` attribute. This approach to maintaining tenant isolation is referred to as the *One Shared Multi-Tenant Policy Store* approach. For more information about Verified Permissions design considerations for multi-tenant SaaS applications, see the [Verified Permissions multi-tenant design considerations](avp-design-considerations.md) section.

The policy also ensures that the principal is a member of `allAccessRole` and restricts actions to `viewData` and `updateData`. Additionally, this policy verifies that `account_lockout_flag` is `false` and that the context value for `uses_mfa` evaluates to `true`.

Similarly, the following policy ensures that both the principal and resource are associated with the same tenant, which prevents cross-tenant access. This policy also ensures that the principal is a member of `viewDataRole` and restricts actions to `viewData`. Additionally, it verifies that the `account_lockout_flag` is `false` and that the context value for `uses_mfa` evaluates to `true`.

```
permit (
    principal in MultitenantApp::Role::"viewDataRole",
    action == MultitenantApp::Action::"viewData",
    resource
)
when {
    principal.account_lockout_flag == false &&
    context.uses_mfa == true &&
    resource in principal.Tenant
};
```

The third policy is similar to the previous one. The policy requires the resource to be a member of the group that corresponds to the entity that's represented by `principal.Tenant`. This ensures that both the principal and resource are associated with Tenant B, which prevents cross-tenant access. This policy ensures that the principal is a member of `updateDataRole` and restricts actions to `updateData`. Additionally, this policy verifies that the `account_lockout_flag` is `false` and that the context value for `uses_mfa` evaluates to `true`.

```
permit (
    principal in MultitenantApp::Role::"updateDataRole",
    action == MultitenantApp::Action::"updateData",
    resource
)
when {
    principal.account_lockout_flag == false &&
    context.uses_mfa == true &&
    resource in principal.Tenant
};
```

The following authorization request is evaluated by the three policies discussed earlier in this section. In this authorization request, the principal of type `User` and with a value of `Alice` makes an `updateData` request with the role `allAccessRole`. `Alice` has the attribute `Tenant` whose value is `Tenant::"TenantA"`. The action `Alice` is trying to perform is `updateData,` and the resource it will be applied to is `SampleData` of the type `Data`. `SampleData` has `TenantA` as a parent entity.

According to the first policy in the `<DATAMICROSERVICE_POLICYSTOREID>` policy store, `Alice` can perform the `updateData` action on the resource, assuming that the conditions in the `when` clause of the policy are met. The first condition requires the `principal.Tenant` attribute to evaluate to `TenantA`. The second condition requires the principal's attribute `account_lockout_flag` to be `false`. The final condition requires the context `uses_mfa` to be `true`. Because all three conditions are met, the request returns an `ALLOW` decision.

```
{
  "policyStoreId": "DATAMICROSERVICE_POLICYSTORE",
  "principal": {
      "entityType": "MultitenantApp::User",
      "entityId": "Alice"
  },
  "action": {
      "actionType": "MultitenantApp::Action",
      "actionId": "updateData"
  },
  "resource": {
      "entityType": "MultitenantApp::Data",
      "entityId": "SampleData"
  },
  "context": {
    "contextMap": {
        "uses_mfa": {
            "boolean": true
        }
    }
  },
  "entities": {
    "entityList": [
      {
        "identifier": {
            "entityType": "MultitenantApp::User",
            "entityId": "Alice"
        },
        "attributes": {
            {
                "account_lockout_flag": {
                    "boolean": false
                },
                "Tenant": {
                   "entityIdentifier": {
                        "entityType":"MultitenantApp::Tenant",
                        "entityId":"TenantA"
                   }
                }
            }
        },
        "parents": [
            {
                "entityType": "MultitenantApp::Role",
                "entityId": "allAccessRole"
            }
        ]
        },
     {
        "identifier": {
            "entityType": "MultitenantApp::Data",
            "entityId": "SampleData"
        },
        "attributes": {},
        "parents": [
            {
                "entityType": "MultitenantApp::Tenant",
                "entityId": "TenantA"
            }
        ]
      }
    ]
  }
}
```
