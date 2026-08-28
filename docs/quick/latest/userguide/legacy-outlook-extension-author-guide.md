---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/legacy-outlook-extension-author-guide.html
---

# Amazon Quick Microsoft Outlook extension author guide
<a name="legacy-outlook-extension-author-guide"></a>

As an Amazon Quick author, you can deploy Quick Microsoft Outlook extensions after your admin establishes the foundational connection to your organization's Microsoft 365 tenant. Your capabilities depend on the permission level granted by your administrator.

With **limited permissions** (view, share, delete only), you can manage basic extension operations through the landing page after admin completes all setup. With **full permissions** (deploy, view, share, delete, edit), you can download manifests for deployment in the M365 admin center, rename extensions, and access all editing features.

Author capabilities for Microsoft Outlook extensions include:
+ Configure extension connections (requires access to M365 Admin Center portal).
+ Deploy extensions to your organization's Microsoft 365 tenant (requires full permissions).
+ Manage sharing and access permissions (available with limited or full permissions).
+ Customize extension settings - names, descriptions (requires full permissions).
+ Download manifest files for advanced Microsoft 365 deployment (requires full permissions).

**Note**
Before you deploy a Microsoft Outlook extension as an author, your Quick admin must [configure Amazon Quick access to Microsoft Outlook](https://docs.aws.amazon.com/quicksuite/latest/userguide/legacy-outlook-extension.html).

**Topics**
+ [Deploy Microsoft Outlook extension](#add-extensions-outlook)
+ [Edit Microsoft Outlook extension](#edit-extensions-outlook)
+ [Share Microsoft Outlook extension](#share-extensions-outlook)
+ [Delete Microsoft Outlook extension](#delete-extensions-outlook)

## Deploy Microsoft Outlook extension
<a name="add-extensions-outlook"></a>

Deploy a new Microsoft Outlook extension instance in the Quick console. This process establishes the foundation for connecting AI-powered assistance to your Microsoft Outlook environment.

**Note**
This action requires full author permissions.

1. Sign in to the Amazon Quick console.

1. In the left navigation, under **CONNECTIONS**, select **Extensions**.

1. Select **Create extension**.

1. Select **Microsoft Outlook**. Then, select **Next**.

1. Configure the following fields:
   + **Name** - A name for your extension is pre-filled for you. You can edit this and enter a descriptive name for the Microsoft Outlook extension.
   + **Description** (optional) - A description for your extension is pre-filled for you. You can edit this and enter a new description to provide additional context about this extension configuration.
   + **Installation** type - Your Microsoft Outlook extension uses manifest-only installation by default.

1. Select **Next** to save your configuration.

1. From the **Extension** summary page, navigate to the extension you just configured.

1. Then, from the **Actions** menu, navigate to the extension you just configured.

1. Select **Download manifest**. Then, from the **Complete installation for Outlook assistant** dialog box that opens, select **Download**.

   The manifest file will be downloaded to your computer.

1. From the success message, select **Install extension** to finish downloading the manifest for your extension.
**Note**
You can also navigate to the extensions summary page and download the manifest for your extension from the **Actions** menu.

1. In the screen asking for permissions to allow your Amazon Quick Outlook extension to access Outlook, select **Allow**.
**Note**
You will now continue the remainder of this procedure within the Microsoft 365 admin center.

1. In the Microsoft 365 admin center, choose **Integrated apps** from the left navigation and choose **Upload custom apps**. This will open the **Deploy New App** page.

1. Choose **Office Add-in** as your App type.

1. Paste the manifest URL link you copied in the **Provide link to manifest file** and choose **Validate**.

1. Choose the users you want to add in the **Add users** section.

1. Choose **Accept permissions** in the **Accept permissions requests** section and deploy the Add-in. Once deployment is completed, your users will be able to install the Amazon Quick Add-in in their Microsoft Outlook.

Your Outlook extension has now been successfully deployed and is available for users.

## Edit Microsoft Outlook extension
<a name="edit-extensions-outlook"></a>

As an author, you can edit the extensions you deploy to your users. Modify extension settings to update names, descriptions, or configuration options. Changes take effect immediately and apply to all users with access to the extension.

1. Sign in to the Amazon Quick console.

1. In the left navigation, under **CONNECTIONS**, select **Extensions**.

1. Select the three dot menu icon for the Microsoft Outlook extension you need to edit.

1. Select **Edit**.

1. Edit the configuration as required and select **Save** to confirm the changes.

## Share Microsoft Outlook extension
<a name="share-extensions-outlook"></a>

Share ownership and management permissions with specific users and groups, enabling multiple users to manage extensions and assist with installation. You can assign different permission levels and manage access as needed.

1. Sign in to the Amazon Quick console.

1. In the left navigation, under **CONNECTIONS**, select **Extensions**.

1. Select the three dot menu icon for the Microsoft Outlook extension you need to share.

1. Select **Share**.

1. Enter the users and groups you would like to share the extension with.

1. Select **Share** to send the access email to each group and user.

1. From the drop-down next to each name, you can edit their access levels (Viewer or Owner).

1. **Optional:** You could select **Remove access** to delete the access for the selected group or user.

## Delete Microsoft Outlook extension
<a name="delete-extensions-outlook"></a>

As an author, you can delete the extensions you deploy to your users. Permanently remove a extension from your Quick console and revoke access for all users. This action cannot be undone and requires confirmation.

1. Sign in to Amazon Quick console.

1. In the left navigation, under **CONNECTIONS**, select **Extensions**.

1. Select the three dot menu icon for the Microsoft Outlook extension you need to delete.

1. Select **Delete**.

1. Enter the word, "confirm", and select **DELETE**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
