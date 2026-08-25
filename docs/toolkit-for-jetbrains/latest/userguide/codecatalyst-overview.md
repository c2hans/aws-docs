---
source_url: https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/codecatalyst-overview.html
---

# Working with Amazon CodeCatalyst in JetBrains Gateway
<a name="codecatalyst-overview"></a>

You can launch a virtual computing environment, known as a Dev Environment, from JetBrains. Dev Environments are customizable cloud-development environments that you can copy and share among different team members in your Space. For more information about Dev Environments and how you can access them from CodeCatalyst, see the [Dev Environments](https://docs.aws.amazon.com/codecatalyst/latest/userguide/devenvironment.html) section in the *Amazon CodeCatalyst* User Guide.

The following sections describe how to create, open, and work with Dev Environments from JetBrains Gateway.

## Opening a Dev Environment
<a name="codecatalyst-overview-open"></a>

To open an existing Dev Environment from JetBrains Gateway, complete the following steps.

1. From the **Connections** explorer, choose the **Amazon CodeCatalyst** plugin.

1. From the **Remote Development** wizard body, navigate to the parent Space and project for the Dev Environment that you want to open.

1. Choose the Dev Environment that you want to open.

1. Confirm the opening process for your Dev Environment to continue.
**Note**
JetBrains displays the progress in a new status window, when the opening process is complete, your Dev Environment opens in a new window.

## Creating a Dev Environment
<a name="codecatalyst-overview-creating"></a>

To create a new Dev Environment:

1. From the **Connections** explorer, choose the **CodeCatalyst** plugin.

1. From the **Remote Development** wizard header section, choose the **Create a Dev Environment** link to open the **New CodeCatalyst Dev Environment** view.

1. From the **New CodeCatalyst Dev Environment** view, use the following fields to configure your Dev Environment preferences.
   + **IDE**: Select your preferred JetBrains IDE to launch in your Dev Environment.
   + **CodeCatalyst Project**: Choose a CodeCatalyst Space and project for your Dev Environment.
   + **Dev Environment Alias**: Enter an alternate name for your Dev Environment.
   + **Compute**: Choose the virtual hardware configuration for your Dev Environment.
   + **Persistent storage**: Choose the amount of persistent storage for your Dev Environment.
   + **Inactivity timeout**: Choose the system idle time that passes before your Dev Environment enters into standby.

1. To create your Dev Environment, choose **Create Dev Environment**.
**Note**
When you choose **Create Dev Environment**, the **New Dev Environment** view closes and the process to create your Dev Environment starts. The process can take several minutes and you can't use other JetBrains Gateway features until your Dev Environment is created.
JetBrains displays the progress in a new status window, and, when the process is complete, your Dev Environment opens in a new window.

## Creating a Dev Environment from a third-party repository
<a name="codecatalyst-overview-creating-source-repo"></a>

You can create Dev Environments from a third-party repository by linking to the repository as a source.

Linking to a third-party repository as a source is handled at the project level in CodeCatalyst. For instructions and additional details on how to connect a third-party repository to your Dev Environment, see the [Linking a source repository](https://docs.aws.amazon.com/codecatalyst/latest/userguide/source-repositories-link.html) topic in the *Amazon CodeCatalyst User Guide*.

## Configuring Dev Environment settings
<a name="codecatalyst-overview-configure"></a>

To change the settings for an existing Dev Environment from JetBrains Gateway, complete the following steps.

**Note**
You can't modify the amount of storage assigned to your Dev Environment after it has been created.

1. From the **Connections** explorer, choose the **Amazon CodeCatalyst** plugin.

1. From the **Remote Development** wizard body, navigate to the parent Space and project for the Dev Environment that you want to configure.

1. Choose the **Settings** icon, next to the Dev Environment that you want to configure, to open the **Configure Dev Environment:** settings.

1. From **Configure Dev Environment:** settings menu, configure your Dev Environment by changing the following options:
   + **Dev Environment Alias**: Optional field to specify and alternate name for your Dev Environment.
   + **IDE:** choose the JetBrains IDE you want to launch inside of your Dev Environment.
   + **Compute**: Choose the virtual hardware configuration for your Dev Environment.
   + **Inactivity timeout**: Choose the system idle time that passes before your Dev Environment enters into standby.

## Pausing a Dev Environment
<a name="codecatalyst-overview-pause"></a>

The activity in your Dev Environment is stored persistently. This means that you can pause and resume your Dev Environment without losing your work.

To pause your Dev Environment, complete the following steps.

1. From the **Connections** explorer, choose the **Amazon CodeCatalyst** plugin.

1. From the **Remote Development** wizard body, navigate to the parent Space and project for the Dev Environment that you want to pause.

1. Choose the **Pause** icon next to your active Dev Environment to open the **Confirm Pause** dialog.

1. Choose **Yes** to close the **Confirm Pause** dialog and initialize the pause process.
**Note**
JetBrains displays the progress of the pause process in a new status window. When the Dev Environment has stopped, the **Pause ** icon is removed from the user interface.

## Resuming a Dev Environment
<a name="codecatalyst-overview-resume"></a>

The activity in your Dev Environment is stored persistently. This means that you can resume a paused Dev Environment without losing your previous work.

To resume a paused Dev Environment, complete the following steps.

1. From the **Connections** explorer, choose the **Amazon CodeCatalyst** plugin.

1. From the **Remote Development** wizard body, navigate to the parent Space and project for the Dev Environment that you want to resume.

1. Choose the Dev Environment you want to resume.
**Note**
JetBrains displays the progress of the resume process in a new status window. When the Dev Environment has resumed, a **Pause ** icon is added next to the Dev Environment **Settings** icon.

## Deleting a Dev Environment
<a name="codecatalyst-overview-delete"></a>

To delete your Dev Environment, complete the following steps:

1. From the **Connections** explorer, choose the **Amazon CodeCatalyst** plugin.

1. From the **Remote Development** wizard body, navigate to the parent Space and project for the Dev Environment that you want to delete.

1. Choose the **X** icon button next to your Dev Environment to open the **Confirm Deletion** dialog.

1. Choose **Yes** to close the dialog and delete your Dev Environment.
**Important**
After you choose **Yes**, your Dev Environment is deleted and can't be retrieved. Before deleting a Dev Environment, make sure to commit and push your code changes to the original source repository. Otherwise, your unsaved changes will be permanently lost.
After a Dev Environment is deleted, the **Remote Development** wizard updates and the Dev Environment is no longer listed in your resources.

## Configuring Dev Environments defaults
<a name="codecatalyst-overview-default"></a>

You can configure your Dev Environment default settings in the `devfile` of your Dev Environment. The `devfile` specification is an open standard, which you can update in a YAML document.

For more information about how to define and configure your `devfile`, see [devfile.io](https://devfile.io/).

To open and edit your `devfile` from your JetBrains Gateway Dev Environment instance, complete the following steps.

1. From the **Navigation bar** in your active JetBrains Dev Environment, expand the **Amazon CodeCatalyst Dev Environment** node to open the **Backend Status Details** menu.

1. Choose the **Configure Dev Environment** tab, then choose **Open Devfile** to open your `devfile` in the JetBrains **Editor**.

1. From the **Editor**, make changes to your `devfile` and save your work.

1. Upon saving your changes, the **Amazon CodeCatalyst Dev Environment** node displays an alert indicating that your Dev Environment requires a rebuild.

1. Expand the **Amazon CodeCatalyst Dev Environment** node and choose the **Rebuild Dev Environment** node from the **Configure Dev Environment** tab.
