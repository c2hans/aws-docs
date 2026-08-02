---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/enable-contactlens-integration.html
---

# Enable Connect Customer Contact Lens integration
<a name="enable-contactlens-integration"></a>

After you create a Contact Lens connector, you need to enable the integration by assigning users security profile permissions so they can access it on the Connect Customer admin website.

1. Log in to the Connect Customer admin website at https://*instance name*.my.connect.aws/ using an Admin account.

1. On the navigation bar, choose **Security profiles**. On the **Manage security profiles** page, choose **Admin**, **Edit**.

1. On the **Edit security profile** page, choose **Channels and Flows** - **AnalyticsConnectors** - **View** and **Edit** permissions, and then choose **Save**.
**Important**
If you don't see the Contact Lens connectors permission under **Channels and Flows**, request service quota increases for the following quotas in your Connect Customer account:
Contact Lens connectors per account
Maximum active recording sessions from external voice systems per instance

1. Assign this permission to the security profiles for users who you want to access the Contact Lens connectors.
**Note**
You can only delete the last Contact Lens connector in your Connect Customer instance when the access to the Contact Lens connector is removed from the users of that instance.
If you attempt to delete the last Contact Lens connector without first removing the Contact Lens connectors access from the users of that instance, the following error message is displayed: **error - Failed to delete connector {connector-name} with error: An analytics connector permissions is being used in a security profile**.

1. After you apply the permission, users who have it will be able to see the **Contact Lens connectors** option in the Connect Customer admin website left navigation menu, as shown in the following image.
![The left menu on the Connect Customer admin website, the Contact Lens option.](http://docs.aws.amazon.com/connect/latest/adminguide/images/contact-lens-connector-menuitem.png)

1. You're done enabling the Contact Lens connector. Continue to the next step: [associate a Contact Lens connector with a flow](associate-contactlens-integration.md).
