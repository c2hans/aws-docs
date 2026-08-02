---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/opa-rbac-examples.html
---

# Example 2: Multi-tenant access control and user-defined RBAC with OPA and Rego
<a name="opa-rbac-examples"></a>

This example uses OPA and Rego to demonstrate how access control can be implemented on an API for a multi-tenant application with custom roles defined by tenant users. It also demonstrates how access can be restricted based on a tenant. This model shows how OPA can make *granular permission decisions* based on information that is provided in a high-level role.

![User-defined RBAC with OPA and Rego](http://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/images/guide-img/1bc1ddcc-09fb-41af-88b1-99d94e62fa1f/images/f65ed0f1-d92f-4e28-ba54-ab6d636e25bd.png)

The roles for the tenants are stored in external data (RBAC data) that is used to make access decisions for OPA:

```
{
    "roles": {
        "tenant_a": {
            "all_access_role": ["viewData", "updateData"]
        },
        "tenant_b": {
            "update_data_role": ["updateData"],
            "view_data_role": ["viewData"]
        }
    }
}
```

These roles, when defined by a tenant user, should be stored in an external data source or an identity provider (IdP) that can act as a source of truth when mapping tenant-defined roles to permissions and to the tenant itself.

This example uses two policies in OPA to make authorization decisions and to examine how these policies enforce tenant isolation. These policies use the RBAC data defined earlier.

```
default allowViewData = false
allowViewData = true {
    input.method == "GET"
    input.path = ["viewData", tenant_id]
    input.tenant_id == tenant_id
    role_permissions := data.roles[input.tenant_id][input.role][_]
    contains(role_permissions, "viewData")
}
```

To show how this rule will function, consider an OPA query that has the following input:

```
{
    "tenant_id": "tenant_a",
    "role": "all_access_role",
    "path": ["viewData", "tenant_a"],
    "method": "GET"
}
```

An authorization decision for this API call is made as follows, by combining the RBAC data, the OPA policies, and the OPA query input:

1. A user from `Tenant A` makes an API call to` /viewData/tenant_a`*.*

1. The Data microservice receives the call and queries the `allowViewData` rule, passing the input shown in the OPA query input example.

1. OPA uses the queried rule in OPA policies to evaluate the input provided. OPA also uses the data from RBAC data to evaluate the input. OPA does the following:

   1. Verifies that the method used to make the API call is `GET`*.*

   1. Verifies that the path requested is `viewData`*.*

   1. Checks that the `tenant_id` in the path is equal to the `input.tenant_id` associated with the user. This ensures that tenant isolation is maintained. Another tenant, even with an identical role, is unable to be authorized in making this API call.

   1. Pulls a list of role permissions from the roles' external data and assigns them to the variable `role_permissions`. This list is retrieved by using the tenant-defined role that is associated with the user in `input.role`*.*

   1. Checks `role_permissions` to see whether it contains the permission `viewData`*.*

1. OPA returns the following decision to the Data microservice:

```
{
    "allowViewData": true
}
```

This process shows how RBAC and tenant awareness can contribute to making an authorization decision with OPA. To further illustrate this point, consider an API call to `/viewData/tenant_b` with the following query input:

```
{
    "tenant_id": "tenant_b",
    "role": "view_data_role",
    "path": ["viewData", "tenant_b"],
    "method": "GET"
}
```

This rule would return the same output as *OPA query input* although it is for a different tenant who has a different role. This is because this call is for */tenant\_b* and the *view\_data\_role* in *RBAC data* still has the *viewData* permission associated with it. To enforce the same type of access control for */updateData*, you can use a similar OPA rule:

```
default allowUpdateData = false
allowUpdateData = true {
    input.method == "POST"
    input.path = ["updateData", tenant_id]
    input.tenant_id == tenant_id
    role_permissions := data.roles[input.tenant_id][input.role][_]
    contains(role_permissions, "updateData")
}
```

This rule is functionally the same as the *allowViewData* rule, but it verifies a different path and input method. The rule still ensures tenant isolation and checks that the tenant-defined role grants the API caller permission. To see how this might be enforced, examine the following query input for an API call to */updateData/tenant\_b*:

```
{
    "tenant_id": "tenant_b",
    "role": "view_data_role",
    "path": ["updateData", "tenant_b"],
    "method": "POST"
}
```

This query input, when evaluated with the *allowUpdateData *rule, returns the following authorization decision:

```
{
    "allowUpdateData": false
}
```

This call will not be authorized. Although the API caller is associated with the correct* tenant\_id* and is calling the API by using an approved method, the *input.role* is the tenant-defined *view\_data\_role*. The *view\_data\_role* doesn't have the *updateData *permission; therefore, the call to */updateData* is unauthorized. This call would have been successful for a *tenant\_b* user who has the *update\_data\_role*.
