---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/legacy-word-extension-author-guide.html
---

# Amazon Quick Microsoft Word extension author guide
<a name="legacy-word-extension-author-guide"></a>

As an Amazon Quick author, you can deploy Quick Microsoft Word extensions after your admin establishes the foundational connection to your organization's Microsoft 365 tenant. Your capabilities depend on the permission level granted by your administrator.

With **limited permissions** (view, share, delete only), you can manage basic extension operations through the landing page after admin completes all setup. With **full permissions** (deploy, view, share, delete, edit), you can download manifests for deployment in the M365 admin center, rename extensions, and access all editing features.

Author capabilities for Microsoft Word extensions include:
+ Configure extension connections (requires access to M365 Admin Center portal).
+ Deploy extensions to your organization's Microsoft 365 tenant (requires full permissions).
+ Customize extension settings - names, descriptions (requires full permissions).
+ Download manifest files for advanced Microsoft 365 deployment (requires full permissions).
+ Manage sharing and access permissions (available with limited or full permissions).

**Note**
Before you deploy a Microsoft Word extension as an author, your Quick admin must [configure Amazon Quick access to Microsoft Word](https://docs.aws.amazon.com/quicksuite/latest/userguide/legacy-word-extension.html).

**Topics**
+ [Deploy Microsoft Word extension](#add-extensions-word)
+ [Edit Microsoft Word extension](#edit-extensions-word)
+ [Share Microsoft Word extensions](#word-authors-share)
+ [Delete Microsoft Word Extensions](#word-authors-delete)

## Deploy Microsoft Word extension
<a name="add-extensions-word"></a>

Deploy a new Microsoft Word extension instance in the Amazon Quick console. This process establishes the foundation for connecting AI-powered assistance to your Microsoft Word environment.

**Note**
This action requires full author permissions.

Use this procedure to create and configure a new Microsoft Word extension for your organization.

1. Sign in to the Amazon Quick console.

1. In the left navigation, under **CONNECTIONS**, select **Extensions**.

1. Select **Create extension**.

1. Select **Microsoft Word**. Then, select **Next**.

1. Configure the following fields:
   + **Name** - A name for your extension is pre-filled for you. You can edit this and enter a descriptive name for the Microsoft Word extension.
   + **Description** (optional) - A description for your extension is pre-filled for you. You can edit this and enter a new description to provide additional context about this extension configuration.
   + **Installation** type - Your Microsoft Word extension uses manifest-only installation by default.

1. Select **Next** to save the details and download the manifest file to your computer.

**Note**
You will now continue the remainder of this procedure within the Microsoft 365 admin center.

1. In the Microsoft 365 admin center, choose **Integrated apps** from the left navigation and choose **Upload custom apps**. This will open the **Deploy New App** page.

1. Choose **Office Add-in** as your App type.

1. Choose **Upload manifest file (.xml) from device**, select **Choose from file**, select the downloaded manifest xml file and choose **Next**.

1. Choose the users you want to add in the **Add users** section.

1. Choose **Accept permissions** in the **Accept permissions requests** section and deploy the Add-in. Once deployment is completed, your users will be able to install the Amazon Quick Add-in in their Microsoft Word.

Your Microsoft Word extension is now created and ready for deployment to users in your organization.

## Edit Microsoft Word extension
<a name="edit-extensions-word"></a>

**Note**
This action requires full author permissions.

As an author, you can edit the extensions you deploy to your users. Modify existing Microsoft Word extension configurations to update settings, change descriptions, or adjust deployment parameters as your organizational needs evolve.

Use this procedure to modify settings and configuration for an existing Microsoft Word extension.

1. Sign in to the Amazon Quick console.

1. In the left navigation, under **CONNECTIONS**, select **Extensions**.

1. Select the three dot menu icon for the Microsoft Word extension you need to edit.

1. Select **Edit**.

1. Enter your changes and select **Save** to confirm the new configuration.

Your changes are now applied and will be reflected in the extension configuration for all users.

## Share Microsoft Word extensions
<a name="word-authors-share"></a>

Share ownership and management permissions with specific users and groups, enabling multiple users to manage extensions and assist with installation. You can assign different permission levels and manage access as needed.

Use this procedure to share your Microsoft Word extension with other users and manage their access permissions.

1. Sign in to Amazon Quick console.

1. In the left navigation, under **CONNECTIONS**, select **Extensions**.

1. Select the three dot menu icon for the Microsoft Word extension you need to share.

1. Select **Share**.

1. Enter the users and groups you would like to share the extension with.

1. Select **Share** to send the access email to each group and user.

1. From the drop-down next to each name, you can edit their access levels (**Viewer** or **Owner**).

1. **Optional **You could select, **Remove access** to delete the access for the selected group or user.

The specified users and groups now have access to your Microsoft Word extension with the permissions you assigned.

## Delete Microsoft Word Extensions
<a name="word-authors-delete"></a>

As an author, you can delete the extensions you deploy to your users.

Use this procedure to permanently remove a Microsoft Word extension from your organization.

1. Sign in to Amazon Quick console

1. In the left navigation, under **CONNECTIONS**, select **Extensions**

1. Select the three dot menu icon for the Microsoft Word extension you need to delete

1. Select **Delete**

1. Enter, confirm and **DELETE** to delete the Extension

The Microsoft Word extension has been permanently removed and is no longer accessible to users in your organization.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
