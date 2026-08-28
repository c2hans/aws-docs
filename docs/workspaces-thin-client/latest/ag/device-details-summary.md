---
source_url: https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/device-details-summary.html
---

End of support notice: On March 31, 2027, AWS will end support for Amazon WorkSpaces Thin Client. After March 31, 2027, you will no longer be able to access the WorkSpaces Thin Client console or WorkSpaces Thin Client resources. For more information, see [Amazon WorkSpaces Thin Client end of support](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/workspacesthinclient-end-of-support.html).

# Summary
<a name="device-details-summary"></a>

The Summary section provides a high-level overview of the key features of the WorkSpaces Thin Client device. The following table lists each element in the summary and how it functions.

![Summary section showing device details, enrollment status, and software information.](http://docs.aws.amazon.com/workspaces-thin-client/latest/ag/images/device-details-summary.png)

| Element | Description |
| --- | --- |
| Device serial number | The identification number assigned to an individual device. |
| ARN | The unique identifier for the device in Amazon Resource Name (ARN) format. |
| Device name | The name that you give to a device. If you have not created a name, you can name it, or it will get a default name. |
| Device type | The type of end user device that is linked to the account. |
| Activity status | The current status of this device. The two status states are:+ Active<br />+ Inactive |
| Environment ID | The identification number of the environment that the device uses. |
| Enrollment status | Confirmation that a device has been set up, is associated with this AWS account, and is part of a specific environment. It can be in one of the following four states:+ **Registered** – This is the default status.<br />+ **Deregistering** – The device is in the Reset and Deregister process.<br />+ **Deregistered** – The device has been successfully deregistered. You can only delete the device if it’s in either a Deregistered or Archived status.<br />+ **Archived** – This device has been marked by the administrator as not currently in service. |
| Enrolled since | The date the device was activated. |
| Last logged in | The date and time of the most recent login. |
| Last posture checked at | The date and time of the most recent device check-in. |
| Current software version | The software version that this device is currently using. |
| Scheduled for software update | The scheduled software version on the device. |
| Software compliance | Confirmation that the software set is valid. There are two status states:+ Compliant<br />+ Not Compliant |
| Last used by | The identification number of the user accessing the device. Only available when using WorkSpaces Personal. |

## User log
<a name="device-details-user-log"></a>

![User activity details showing 5 device access timestamps from August 24 to August 28, 2023.](http://docs.aws.amazon.com/workspaces-thin-client/latest/ag/images/device-details-user-log.png)

| Element | Description |
| --- | --- |
| Last device access | The date and time when this device was last used. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Thin Client. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-thin-client` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
