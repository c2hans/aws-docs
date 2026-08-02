---
source_url: https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/virtual-service-providers.html
---

End of support notice: On March 31, 2027, AWS will end support for Amazon WorkSpaces Thin Client. After March 31, 2027, you will no longer be able to access the WorkSpaces Thin Client console or WorkSpaces Thin Client resources. For more information, see [Amazon WorkSpaces Thin Client end of support](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/workspacesthinclient-end-of-support.html).

# Step 2: Select your virtual desktop provider
<a name="virtual-service-providers"></a>

You must have a service to provide your users access to their virtual desktop and compatible resources.

**Important**
For WorkSpaces Thin Client Administrator Console to work properly, your system must meet specific requirements. These requirements are listed in [Prerequisites and Configurations](prerequisites.md).
Make sure that your system meets these requirements before you set up your console.

## Using Amazon WorkSpaces
<a name="setting-up-ws"></a>

Amazon WorkSpaces is a fully managed desktop virtualization service for Windows that enables you to access resources from any supported device.

1. To use Amazon WorkSpaces, do one of the following:
   + Select the directory that you want to use for your environment. You can either browse through the dropdown list or you can search the directories by using the search field.
   + Create a directory by selecting the **Create WorkSpaces directory** button. For more information on creating WorkSpaces directories, see [Manage directories for WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/manage-workspaces-directory.html).

1. Select the **Create environment** button.

When you create your environment, you can still edit the details later. For more information, see [Editing an environment](editing-an-environment.md).

## Using WorkSpaces Applications
<a name="setting-up-as"></a>

WorkSpaces Applications is a fully managed, secure application streaming service that you can use to stream desktop applications from AWS to a web browser.

**Important**
In order to create an WorkSpaces Applications environment, you must have `cli_follow_urlparam` set to `false`. To achieve this, do the following:
For a default profile, run `aws configure set cli_follow_urlparam false`.
For a profile with name `ProfileName`, run `aws configure set cli_follow_urlparam false --profile ProfileName`.

1. To set up WorkSpaces Applications, do one of the following:
   + Select the stack that you want to use for your environment. You can either browse through the dropdown list or you can search the stacks by using the search field.
   + Create a stack by selecting the **Create Stack** button. For more information on creating WorkSpaces Applications stacks, see [Create a Stack](https://docs.aws.amazon.com/appstream2/latest/developerguide/set-up-stacks-fleets.html#set-up-stacks-fleets-install).

1. Enter your identity provider login and logout URL in the **IdP login URL** field. This provides users with a place to log in and out of WorkSpaces Thin Client.

1. Select the **Create environment** button.

After you create your environment, you can still edit the details later. For more information, see [Editing an environment](editing-an-environment.md).

## Using Amazon WorkSpaces Secure Browser
<a name="setting-up-wsw"></a>

Amazon WorkSpaces Secure Browser is a low-cost, fully managed WorkSpaces console that is built to deliver secure web-based workloads and software as a service (SaaS) application access to users within existing web browsers.

1. To set up Amazon WorkSpaces Secure Browser, do one of the following:
   + Select the web portal that you want to use for your environment. You can either browse through the dropdown list or you can search the web portals by using the search field.
   + Create a web portal by selecting the **Create WorkSpaces Secure Browser** button. For more information on creating WorkSpaces Secure Browser web portals, see [Setting up Amazon WorkSpaces Secure Browser](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/setting-up.html).

1. Select the **Create environment** button.

After you create your environment, you can still edit the details later. For more information, see [Editing an environment](editing-an-environment.md).
