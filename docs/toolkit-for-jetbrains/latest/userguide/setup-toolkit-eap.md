---
source_url: https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/setup-toolkit-eap.html
---

# Installing AWS Toolkit for JetBrains Early Access Program (EAP) and custom builds
<a name="setup-toolkit-eap"></a>

Early Access Program (EAP) builds of the AWS Toolkit for JetBrains contain previews of new and experimental features.

**Note**
To run the AWS Toolkit for JetBrains version 3.0 through 4.0.251, you must also install AWS Core from the JetBrains Marketplace. Starting with version 4.0.261, the AWS Core plugin is no longer required.

To configure your toolkit for EAP builds, complete the following procedure:

1. From the JetBrains main menu, open your **Preferences** menu (expand **File** choose **Settings**, for Windows users).

1. From the **Preferences**/**Settings** menu, choose **Plugins** to open the **Plugins** menu.

1. From the **Plugins** menu navigation, expand the **Settings (Manage Repositories, Configure Proxy or Install Plugin from Disk)** icon and choose **Manage Plugin Repositories**.

1. From the **Manage Plugin Repositories** menu choose the **\+ (Add)** icon and enter **https://plugins.jetbrains.com/plugins/eap/aws.toolkit** into the **EAP repository for the AWS Toolkit** field.

1. Choose **OK** to start the EAP installation.

1. JetBrains prompts you to restart the IDE when the installation is complete.

## Removing AWS Toolkit for JetBrains EAP and custom repository references
<a name="setup-toolkit-eap-remove"></a>

It may be necessary to remove an EAP or custom repository reference in order to use a specific version of the AWS Toolkit for JetBrains. To remove a repository reference, complete the following procedure.

**Note**
After completing this procedure it may still be necessary to uninstall your current version of the AWS Toolkit for JetBrains before updating or installing a different version.

**To remove an EAP repository reference**

1. From the JetBrains main menu, open your **Preferences** menu (expand **File** choose **Settings**, for Windows users).

1. From the **Preferences**/**Settings** menu, choose **Plugins** to open the **Plugins** menu.

1. From the **Plugins** menu navigation, expand the **Settings (Manage Repositories, Configure Proxy or Install Plugin from Disk)** icon and choose **Manage Plugin Repositories**.

1. From the **Manage Plugin Repositories** menu choose the **- (Remove)** icon and confirm the removal.
