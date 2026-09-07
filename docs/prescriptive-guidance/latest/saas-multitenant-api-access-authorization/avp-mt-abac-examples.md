---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/avp-mt-abac-examples.html
---

# Example 3: Multi-tenant access control with RBAC
<a name="avp-mt-abac-examples"></a>

To elaborate on the previous RBAC example, you can expand your requirements to include SaaS multi-tenancy, which is a common requirement for SaaS providers. In multi-tenant solutions, resource access is always provided on behalf of a given tenant. That is, users of Tenant A cannot view the data of Tenant B, even if that data is logically or physically collocated in a system. The following example illustrates how you can implement tenant isolation by using multiple [Verified Permissions policy stores](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/policy-stores.html), and how you can employ user roles to define permissions within the tenant.

Using the Per Tenant Policy Store design pattern is a best practice for maintaining tenant isolation while implementing access control with Verified Permissions. In this scenario, Tenant A and Tenant B user requests are verified against separate policy stores, `DATAMICROSERVICE_POLICYSTORE_A` and `DATAMICROSERVICE_POLICYSTORE_B`, respectively. For more information about Verified Permissions design considerations for multi-tenant SaaS applications, see the [Verified Permissions multi-tenant design considerations](avp-design-considerations.md) section.

![Example of multi-tenant access control with RBAC, Amazon Verified Permissions, and Cedar](https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/images/guide-img/1bc1ddcc-09fb-41af-88b1-99d94e62fa1f/images/d4bab8ae-41ac-4206-978a-741397a733dd.png)

The following policy resides in the `DATAMICROSERVICE_POLICYSTORE_A` policy store. It verifies that the principal will be a part of the group `allAccessRole` of type `Role`. In this case, the principal will be allowed to perform the `viewData` and `updateData` actions on all resources that are associated with Tenant A.

```
permit (
    principal in MultitenantApp::Role::"allAccessRole",
    action in [
        MultitenantApp::Action::"viewData",
        MultitenantApp::Action::"updateData"
    ],
    resource
);
```

The following policies reside in the `DATAMICROSERVICE_POLICYSTORE_B` policy store. The first policy verifies that the principal is part of the `updateDataRole` group of type `Role`. Assuming that is the case, it gives permission to principals to perform the `updateData` action on resources that are associated with Tenant B.

```
permit (
    principal in MultitenantApp::Role::"updateDataRole",
    action == MultitenantApp::Action::"updateData",
    resource
);
```

This second policy mandates that principals that are a part of the `viewDataRole` group of type `Role` should be allowed to perform the `viewData` action on resources that are associated with Tenant B.

```
permit (
    principal in MultitenantApp::Role::"viewDataRole",
    action == MultitenantApp::Action::"viewData",
    resource
);
```

The authorization request made from Tenant A needs to be sent to the `DATAMICROSERVICE_POLICYSTORE_A` policy store and verified by the policies that belong to that store. In this case, it's verified by the first policy discussed earlier as part of this example. In this authorization request, the principal of type `User` with a value of `Alice` is requesting to perform the `viewData` action*. *The principal belongs to the group `allAccessRole` of type `Role`. Alice is trying to perform the `viewData` action on the `SampleData` resource*. *Because Alice has the `allAccessRole` role, this evaluation results in an `ALLOW` decision.

```
{
  "policyStoreId": "DATAMICROSERVICE_POLICYSTORE_A",
  "principal": {
      "entityType": "MultitenantApp::User",
      "entityId": "Alice"
  },
  "action": {
      "actionType": "MultitenantApp::Action",
      "actionId": "viewData"
  },
  "resource": {
      "entityType": "MultitenantApp::Data",
      "entityId": "SampleData"
  },
  "entities": {
    "entityList": [
      {
        "identifier": {
            "entityType": "MultitenantApp::User",
            "entityId": "Alice"
        },
        "attributes": {},
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
        "parents": []
      }
    ]
  }
}
```

If, instead, you view a request made from Tenant B by `User Bob`, you will see something like the following authorization request. The request is sent to the `DATAMICROSERVICE_POLICYSTORE_B` policy store because it originates from Tenant B. In this request, the principal `Bob` wants to perform the action `updateData` on the resource `SampleData`. However, `Bob` is not a part of a group that has access to the action `updateData` on that resource. Therefore, the request results in a `DENY` decision.

```
{
  "policyStoreId": "DATAMICROSERVICE_POLICYSTORE_B",
  "principal": {
      "entityType": "MultitenantApp::User",
      "entityId": "Bob"
  },
  "action": {
      "actionType": "MultitenantApp::Action",
      "actionId": "updateData"
  },
  "resource": {
      "entityType": "MultitenantApp::Data",
      "entityId": "SampleData"
  },
  "entities": {
    "entityList": [
      {
        "identifier": {
            "entityType": "MultitenantApp::User",
            "entityId": "Bob"
        },
        "attributes": {},
        "parents": [
            {
                "entityType": "MultitenantApp::Role",
                "entityId": "viewDataRole"
            }
        ]
      },
      {
        "identifier": {
            "entityType": "MultitenantApp::Data",
            "entityId": "SampleData"
        },
        "attributes": {},
        "parents": []
      }
    ]
  }
}
```

In this third example, `User Alice `tries to perform the `viewData` action on the resource `SampleData`. This request is directed to the `DATAMICROSERVICE_POLICYSTORE_A` policy store because the principal `Alice` belongs to Tenant A. `Alice` is a part of the group `allAccessRole` of the type `Role`, which permits her to perform the `viewData` action on resources. As such, the request results in an `ALLOW` decision.

```
{
  "policyStoreId": "DATAMICROSERVICE_POLICYSTORE_A",
  "principal": {
      "entityType": "MultitenantApp::User",
      "entityId": "Alice"
  },
  "action": {
      "actionType": "MultitenantApp::Action",
      "actionId": "viewData"
  },
  "resource": {
      "entityType": "MultitenantApp::Data",
      "entityId": "SampleData"
  },
  "entities": {
    "entityList": [
      {
        "identifier": {
            "entityType": "MultitenantApp::User",
            "entityId": "Alice"
        },
        "attributes": {},
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
        "parents": []
      }
    ]
  }
}
```
