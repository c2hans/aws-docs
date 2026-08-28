---
source_url: https://docs.aws.amazon.com/workspaces-thin-client/latest/ug/defer-software-update.html
---

End of support notice: On March 31, 2027, AWS will end support for Amazon WorkSpaces Thin Client. After March 31, 2027, you will no longer be able to access the WorkSpaces Thin Client console or WorkSpaces Thin Client resources. For more information, see [Amazon WorkSpaces Thin Client end of support](https://docs.aws.amazon.com/workspaces-thin-client/latest/ug/workspacesthinclient-end-of-support.html).

# Deferring software updates
<a name="defer-software-update"></a>

Your WorkSpaces Thin Client device requires periodic updates. These updates are managed by your IT administrator. When an update is ready, the administrator will release it to your device. If you need to, you can defer, or postpone, these updates. When you receive the update, your screen will show a pop-up notification, like the image below.

You have three options.
+ Install now

  If you choose **Install now**, your device will install the update immediately. This disconnects you from your current session and you will need to log in again after the update. We recommend that you restart your device after an update.
+ Install in one hour

  If you choose **Install in one hour**, the update will be deferred for one hour. After that, you will receive the pop-up notification again.

  If you restart your device before then, the updates will install at that time. You will not see the pop-up notification again.
+ Install during your maintenance window

  If you choose **Install during next maintenance window**, the update will be deferred until the next scheduled maintenance window. Maintenance window times are managed by your administrator. For more information, please contact your IT administrator.

  For example, your IT administrator sets up a maintenance window time of 10:00 pm on Sunday night of each week. You defer your update to install during the maintenance window. So, on 10:00 pm that next Sunday night, your device will receive the pop-up notification again. Or, if your administrator sets up maintenance windows on Monday, Wednesday, and Friday of each week. You defer the update on Monday. On Wednesday, your device will receive the pop-up notification again. In either case, if you do not defer again, the update will install after five minutes.

  If you restart your device before then, the updates will install at that time. You will not see the pop-up notification again.

**Note**
If you do not make any selection within five minutes, your device will automatically begin to install the update.

![WorkSpaces Thin Client software update notification with installation options.](http://docs.aws.amazon.com/workspaces-thin-client/latest/ug/images/defer-ss-popup.png)

If you selected **Install in one hour** or **Install during next maintenance window**, a notification related to the update will appear in the **Notifications** section of **Settings**. For an example of this, refer to the image below.

The notification will tell you the name of the updated software, the version number, and when you will receive the pop-up notification again. If you want to install the update immediately, select **Install now**.

![Settings page showing software update notification for Software set 2.6.0 scheduled for Jun 25, 2024.](http://docs.aws.amazon.com/workspaces-thin-client/latest/ug/images/settings-install-now.png)

You can continue deferring updates. After a certain point, however, your device will be considered behind schedule. If this happens, the updates will install automatically.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Thin Client. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-thin-client` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
