---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/avp-ui-filtering-examples.html
---

# Example 5: UI filtering with Verified Permissions and Cedar
<a name="avp-ui-filtering-examples"></a>

You can also use Verified Permissions to implement RBAC filtering of UI elements based on authorized actions. This is extremely valuable for applications that have context-sensitive UI elements that might be associated with specific users or tenants in the case of a multi-tenant SaaS application.

In the following example, `Users` of the `Role` `viewer` are not allowed to perform updates. For these users, the UI should not render any update buttons.

![Example of UI filtering with Amazon Verified Permissions and Cedar](http://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-api-access-authorization/images/guide-img/1bc1ddcc-09fb-41af-88b1-99d94e62fa1f/images/38d54b9a-3a03-470e-9b9a-1353b63e3bd5.png)

In this example, a single-page web application has four buttons. Which buttons are visible depends on the `Role` of the user who is currently logged in to the application. As the single-page web application renders the UI, it queries Verified Permissions to determine which actions the user is authorized to perform, and then generates the buttons based on the authorization decision.

The following policy specifies that the type `Role` with a value of `viewer` can view both users and data. An `ALLOW` authorization decision for this policy requires a `viewData` or `viewUsers` action, and also requires a resource to be associated with the type `Data` or `Users`. An `ALLOW` decision permits the UI to render two buttons: `viewDataButton` and `viewUsersButton`.

```
permit (
    principal in GuiAPP::Role::"viewer",
    action in [GuiAPP::Action::"viewData", GuiAPP::Action::"viewUsers"],
    resource
)
when {
   resource in [GuiAPP::Type::"Data", GuiAPP::Type::"Users"]
};
```

The following policy specifies that the type `Role` with a value of `viewerDataOnly` can only view data. An `ALLOW` authorization decision for this policy requires a `viewData` action, and also requires a resource to be associated with the type `Data`. An `ALLOW` decision permits the UI to render the button `viewDataButton`.

```
permit (
    principal in GuiApp::Role::"viewerDataOnly",
    action in [GuiApp::Action::"viewData"],
    resource in [GuiApp::Type::"Data"]
);
```

The following policy specifies that the type `Role` with a value of `admin` can edit and view data and users. An `ALLOW` authorization decision for this policy requires an action of `updateData`, `updateUsers`, `viewData,` or `viewUsers`, and also requires a resource to be associated with the type `Data` or `Users`. An `ALLOW` decision permits the UI to render all four buttons: `updateDataButton`, `updateUsersButton`, `viewDataButton`, and `viewUsersButton`.

```
permit (
    principal in GuiApp::Role::"admin",
    action in [
        GuiApp::Action::"updateData",
        GuiApp::Action::"updateUsers",
        GuiApp::Action::"viewData",
        GuiApp::Action::"viewUsers"
       ],
    resource
)
when {
   resource in [GuiApp::Type::"Data", GuiApp::Type::"Users"]
};
```
