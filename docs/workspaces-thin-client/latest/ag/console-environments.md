---
source_url: https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/console-environments.html
---

End of support notice: On March 31, 2027, AWS will end support for Amazon WorkSpaces Thin Client. After March 31, 2027, you will no longer be able to access the WorkSpaces Thin Client console or WorkSpaces Thin Client resources. For more information, see [Amazon WorkSpaces Thin Client end of support](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/workspacesthinclient-end-of-support.html).

# Environments
<a name="console-environments"></a>

Each WorkSpaces Thin Client device uses an individual virtual desktop environment to access its online resources. Users access this environment by using one of the following virtual desktop providers:
+ [Amazon WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces.html)
+ [WorkSpaces Applications](https://docs.aws.amazon.com/appstream2/latest/developerguide/what-is-appstream.html)
+ [Amazon WorkSpaces Secure Browser](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/what-is-workspaces-secure-browser.html)

## Environment list
<a name="environment-list"></a>

There are a number of parameters for your environment for you to review as well as some actions you can take.

![Environments table showing name, virtual desktop service, activation code, device count, and time created columns.](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/images/environment-list.png)

### Environment list details
<a name="environment-list-details"></a>

The parameters for your environment are listed for your review. The following table lists each element in the summary and how it functions.

| Element | Description |
| --- | --- |
| Name | The unique identifier associated with this environment. |
| Virtual desktop service | The virtual desktop provider that this environment uses. |
| Virtual desktop service ID | The unique identifier that the virtual desktop service provider assigns to this environment. |
| Activation code | The code that is used by end users to access the virtual desktop environment. |
| Device count | The number of WorkSpaces Thin Client devices that are accessing this environment. |
| Time Created | The date and time that the environment was created. |

### Environment list actions
<a name="environment-list-actions"></a>

There are a number of actions you can perform from here. Select any of these to perform the corresponding action.

| Element | Description |
| --- | --- |
| Search | Searches all environments that you manage. |
| Refresh | Refreshes the environment list. |
| View details | Displays [Environment details](environment-details.md). |
| Actions | Opens a dropdown list where you can [Edit](editing-an-environment.md) or [Delete](deleting-an-environment.md) an environment. |
| Create environment | Starts the process of [creating an environment](creating-an-environment.md). |

**Topics**
+ [Environment list](#environment-list)
+ [Environment Details](environment-details.md)
+ [Creating an environment](creating-an-environment.md)
+ [Editing an environment](editing-an-environment.md)
+ [Deleting an environment](deleting-an-environment.md)
