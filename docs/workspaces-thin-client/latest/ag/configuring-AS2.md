---
source_url: https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/configuring-AS2.html
---

End of support notice: On March 31, 2027, AWS will end support for Amazon WorkSpaces Thin Client. After March 31, 2027, you will no longer be able to access the WorkSpaces Thin Client console or WorkSpaces Thin Client resources. For more information, see [Amazon WorkSpaces Thin Client end of support](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/workspacesthinclient-end-of-support.html).

# Configuring WorkSpaces Applications for Amazon WorkSpaces Thin Client
<a name="configuring-AS2"></a>

WorkSpaces Applications instances will be listed based on Stack names and will require an IdP login URL to be configured on the create environment page. Because SAML authentication for WorkSpaces Applications only supports initiated authentication, the administrator will have to enter the correct login URL manually.

**Note**
Configurations must be made before using the console for the first time. It is not recommended that you modify any prerequisite features after you start using the console.

## Step 1: Verify that your system meets WorkSpaces Applications required features
<a name="appstream-prequisites"></a>

For WorkSpaces Thin Client administrator console to work with WorkSpaces Applications properly, your system must meet the following specific requirements. This table lists all of these supported features and their requirements.

| Feature | Requirement |
| --- | --- |
| Identity Provider | Go to [Setting Up SAML](https://docs.aws.amazon.com/appstream2/latest/developerguide/external-identity-providers-setting-up-saml.html) in the [WorkSpaces Applications Administrator Guide](https://docs.aws.amazon.com/appstream2/latest/developerguide/what-is-appstream.html) to create an Identity Provider.<br />When prompted to **Create env console**, enter your IDP Login URL. |
| Operating system | Windows |
| Platform Type | Windows Server (2012 R2, 2016 or 2019) |
| Clipboard | Disable<br />Configured at WorkSpaces Applications stack level |
| File transfer | Disable<br />Configured at WorkSpaces Applications stack level |
| Print to local device | Disable<br />Configured at WorkSpaces Applications stack level |

The screen lock requirement through SAML authentication on WorkSpaces Applications is also supported. The **User Pool** and **Programmatic** authentication mechanisms are not supported on WorkSpaces Thin Client.

## Step 2: Set up your WorkSpaces Applications stacks
<a name="setting-up-as2"></a>

To stream your applications, WorkSpaces Applications requires an environment that includes a fleet that is associated with a stack, and at least one application image. Follow these steps to set up a fleet and stack and give users access to the stack. If you haven't already done so, we recommend that you try the procedures in [ Get Started with WorkSpaces Applications: Set Up With Sample Applications](https://docs.aws.amazon.com/appstream2/latest/developerguide/getting-started.html).

If you want to create an image to use, see [ Tutorial: Create a Custom AppStream 2.0 Image by Using the AppStream 2.0 Console](https://docs.aws.amazon.com/appstream2/latest/developerguide/tutorial-image-builder.html).

If you plan to join a fleet to an Active Directory domain, configure your Active Directory domain before completing the following steps. For more information, see [ Using Active Directory with AppStream 2.0](https://docs.aws.amazon.com/appstream2/latest/developerguide/active-directory.html).

**Tasks**
+ [ Create a Fleet](https://docs.aws.amazon.com/appstream2/latest/developerguide/set-up-stacks-fleets.html#set-up-stacks-fleets-create)
+ [ Create a Stack](https://docs.aws.amazon.com/appstream2/latest/developerguide/set-up-stacks-fleets.html#set-up-stacks-fleets-install)
+ [ Provide Access to Users](https://docs.aws.amazon.com/appstream2/latest/developerguide/set-up-stacks-fleets.html#set-up-stacks-fleets-add)
+ [ Clean Up Resources](https://docs.aws.amazon.com/appstream2/latest/developerguide/set-up-stacks-fleets.html#set-up-stacks-fleets-finish)
