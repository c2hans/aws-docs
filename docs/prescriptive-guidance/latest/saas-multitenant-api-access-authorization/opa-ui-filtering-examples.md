---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/opa-ui-filtering-examples.html
---

# Example 4: UI filtering with OPA and Rego
<a name="opa-ui-filtering-examples"></a>

The flexibility of OPA and Rego supports the ability to filter UI elements. The following example demonstrates how an OPA partial rule can make authorization decisions about which elements should be displayed in a UI with RBAC. This method is one of many different ways you can filter UI elements with OPA.

![UI filtering with OPA and Rego](http://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/images/guide-img/1bc1ddcc-09fb-41af-88b1-99d94e62fa1f/images/e1df957b-f5bf-4164-aff2-7e7e9546abf7.png)

In this example, a single-page web application has four buttons. Let's say that you want to filter Bob's, Shirley's, and Alice's UI so that they can see only the buttons that correspond to their roles. When the UI receives a request from the user, it queries an OPA partial rule to determine which buttons should be displayed in the UI. The query passes the following as input to OPA when Bob (with the role `viewer`) makes a request to the UI:

```
{
    "role": "viewer"
}
```

OPA uses external data structured for RBAC to make an access decision:

```
{
    "roles": {
        "viewer": ["viewUsers", "viewData"],
        "dataViewOnly": ["viewData"],
        "admin": ["viewUsers", "viewData", "updateUsers", "updateData"]
    }
}
```

The OPA partial rule uses both the external data and the input to produce a list of allowed actions:

```
user_permissions[permissions] {
    permissions := data.roles[input.role][_]
}
```

In the partial rule, OPA uses the `input.role` specified as part of the query to determine which buttons should be displayed. Bob has the role `viewer`, and the external data specifies that viewers have two permissions: `viewUsers` and `viewData`. Therefore, the output of this rule for Bob (and for any other users who have a viewer role) is as follows:

```
{
    "user_permissions": [
        "viewData",
        "viewUsers"
    ]
}
```

The output for Shirley, who has the `dataViewOnly` role, would contain a permissions button: `viewData`. The output for Alice, who has the `admin` role, would contain all of these permissions. These responses are returned to the UI when OPA is queried for `user_permissions`. The application can then use this response to hide or display the `viewUsersButton`, `viewDataButton`, `updateUsersButton`, and the `updateDataButton`.
