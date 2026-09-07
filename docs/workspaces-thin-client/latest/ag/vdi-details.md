---
source_url: https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/vdi-details.html
---

End of support notice: On March 31, 2027, AWS will end support for Amazon WorkSpaces Thin Client. After March 31, 2027, you will no longer be able to access the WorkSpaces Thin Client console or WorkSpaces Thin Client resources. For more information, see [Amazon WorkSpaces Thin Client end of support](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/workspacesthinclient-end-of-support.html).

# Virtual desktop environment details
<a name="vdi-details"></a>

WorkSpaces Thin Client environments are run on a virtual desktop interface. Each interfaces has a different set of parameters that control the dedicated environment.

## Amazon WorkSpaces directory details
<a name="ws-details"></a>

WorkSpaces Thin Client environments run on Amazon WorkSpaces use directories to create and run their virtual desktops. The following table lists each element in the details and how it functions.

![WorkSpaces directory details showing ID, name, organization, type, registration, and status.](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/images/environment-details-ws.png)

| Element | Description |
| --- | --- |
| Directory ID | The Amazon WorkSpaces directory associated with this environment. |
| Directory name | The unique identifier associated with this Amazon WorkSpaces directory. |
| Organization name | The name of the organization that controls the Amazon WorkSpaces directory. |
| Directory type | The format of the Amazon WorkSpaces directory. |
| Registered | Whether this Amazon WorkSpaces directory is registered. |
| Status | Whether this Amazon WorkSpaces directory is active. |

## Amazon WorkSpaces Secure Browser portal details
<a name="wsw-details"></a>

WorkSpaces Thin Client environments run on Amazon WorkSpaces Secure Browser use web portals to create and run their virtual desktops. The following table lists each element in the details and how it functions.

![WorkSpaces Web portal details table showing name, time created, and endpoint for a custom portal.](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/images/environment-details-wsw.png)

| Element | Description |
| --- | --- |
| Name | The unique identifier associated with this WorkSpaces Secure Browser portal. |
| Time created | The date and time when this WorkSpaces Secure Browser portal was created. |
| Web portal endpoint | The url used to access your virtual desktop environment. |

## WorkSpaces Applications details
<a name="as-details"></a>

WorkSpaces Thin Client environments run on WorkSpaces Applications information stacks to create and run their virtual desktops. The following table lists each element in the details and how it functions.

![WorkSpaces Applications details table showing stack name, IdP login URL, and creation time.](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/images/environment-details-as.png)

| Element | Description |
| --- | --- |
| Stack name | The unique identifier associated with this WorkSpaces Applications stack. |
| IdP login url | The identity provider url that is used to log in and out of your WorkSpaces Applications stack. |
| Time created | The date and time when this WorkSpaces Applications stack was created. |
