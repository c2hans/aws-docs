---
source_url: https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/setup.html
---

# Installing and setting up the AWS Toolkit for Visual Studio
<a name="setup"></a>

The following topics describe how to download, install, set up, and uninstall the AWS Toolkit for Visual Studio.

**Topics**
+ [Prerequisites](#prereqs)
+ [Installing the AWS Toolkit](#install)
+ [Uninstalling the AWS Toolkit](#uninstall)

## Prerequisites
<a name="prereqs"></a>

The following are prerequisites for setting up supported versions of the AWS Toolkit for Visual Studio.
+ Visual Studio 19 or a later release
+ Windows 10 or a later Windows release
+ Administrator access to Windows and Visual Studio
+ Active AWS IAM Credentials

**Note**
Unsupported versions of the AWS Toolkit for Visual Studio are available for Visual Studio 2008, 2010, 2012, 2013, 2015, and 2017. To download an unsupported version, navigate to the [AWS Toolkit for Visual Studio](https://aws.amazon.com/visualstudio/) landing page and choose the version you want from the list of download links.
To learn more about IAM credentials or sign up for an account, visit the [AWS Console](https://console.aws.amazon.com) gateway.

## Installing the AWS Toolkit for Visual Studio
<a name="install"></a>

To install the AWS Toolkit for Visual Studio, find your version of Visual Studio from the following procedures and complete the necessary steps. Download links for all versions of the AWS Toolkit for Visual Studio can be found at the [AWS Toolkit for Visual Studio](https://aws.amazon.com/visualstudio/) landing page.

**Note**
If you encounter issues while installing the AWS Toolkit for Visual Studio, see the [Troubleshooting installation issues](https://docs.aws.amazon.com//toolkit-for-visual-studio/latest/user-guide/setup-troubleshoot.html) topic in this guide.

### Installing the AWS Toolkit for Visual Studio for Visual Studio 2022
<a name="install-2022"></a>

To install AWS Toolkit for Visual Studio 2022 from Visual Studio, complete the following steps:

1. From the **Main menu**, navigate to **Extensions** and choose **Manage Extensions**.

1. From the search box, search for *AWS*.

1. Choose the **Download** button for the relevant version of **Visual Studio 2022** and follow the installation prompts.
**Note**
You may need to manually close and restart Visual Studio to complete the installation process.

1. When the download and installation are complete, you can open the AWS Toolkit for Visual Studio by choosing **AWS Explorer** from the **View** menu.

### Installing the AWS Toolkit for Visual Studio for Visual Studio 2019
<a name="install-2019"></a>

To install AWS Toolkit for Visual Studio 2019 from Visual Studio, complete the following steps:

1. From the **Main menu**, navigate to **Extensions** and choose **Manage Extensions**.

1. From the search box, search for *AWS*.

1. Choose the **Download** button for **Visual Studio 2017 and 2019** and follow the prompts.
**Note**
You may need to manually close and restart Visual Studio to complete the installation process.

1. When the download and installation are complete, you can open the AWS Toolkit for Visual Studio by choosing **AWS Explorer** from the **View** menu.

## Uninstalling the AWS Toolkit for Visual Studio
<a name="uninstall"></a>

To uninstall the AWS Toolkit for Visual Studio, find your version of Visual Studio from the following procedures and complete the necessary steps.

### Uninstalling the AWS Toolkit for Visual Studio for Visual Studio 2022
<a name="uninstall-2022"></a>

To Uninstall AWS Toolkit for Visual Studio 2022 from Visual Studio, complete the following steps:

1. From the **Main menu**, navigate to **Extensions** and choose **Manage Extensions**.

1. From the **Manage Extensions** navigation menu, expand the **Installed** heading.

1. Locate the **AWS Toolkit for Visual Studio 2022** extension and choose the **Uninstall** button.
**Note**
If the AWS Toolkit for Visual Studio isn't visible from the **Installed** section of the navigation menu, you may need to restart Visual Studio.

1. Follow the onscreen prompts to complete the uninstall process.

### Uninstalling the AWS Toolkit for Visual Studio for Visual Studio 2019
<a name="uninstall-2019"></a>

To uninstall AWS Toolkit for Visual Studio 2019 from Visual Studio, complete the following steps:

1. From the **Main menu**, navigate to **Tools** and choose **Manage Extensions**.

1. From the **Manage Extensions** navigation menu, expand the **Installed** heading.

1. Locate the **AWS Toolkit for Visual Studio 2019** extension and choose the **Uninstall** button.

1. Follow the onscreen prompts to complete the uninstall process.

### Uninstalling the AWS Toolkit for Visual Studio for Visual Studio 2017
<a name="uninstall-2017"></a>

To uninstall AWS Toolkit for Visual Studio 2017 in Visual Studio, complete the following steps:

1. From the **Main** menu, navigate to **Tools** and choose **Extensions and Updates**.

1. From the **Extensions and Updates** navigation menu, expand the **Installed** heading.

1. Locate the **AWS Toolkit for Visual Studio 2017** extension and choose the **Uninstall** button.

1. Follow the onscreen prompts to complete the uninstall process.

### Uninstalling the AWS Toolkit for Visual Studio for Visual Studio 2013 or 2015
<a name="uninstall-2013-2015"></a>

To uninstall AWS Toolkit for Visual Studio 2013 or 2015, complete the following steps:

1. From your Windows Control Panel, open **Programs and Features**.
**Note**
You can open Programs and Features immediately by running `appwiz.cpl` from a Windows command prompt or the Windows **Run** dialog.

1. From the list of installed programs, open the context menu for (right-click) **AWS Tools for Windows**.

1. Choose **Uninstall** and follow the prompts to complete the uninstall process.
**Note**
Your **Samples** directory isn't deleted during the uninstall process. This directory is preserved in case you have modified samples. This directory must be manually removed.
