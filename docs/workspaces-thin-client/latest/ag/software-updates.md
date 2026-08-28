---
source_url: https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/software-updates.html
---

End of support notice: On March 31, 2027, AWS will end support for Amazon WorkSpaces Thin Client. After March 31, 2027, you will no longer be able to access the WorkSpaces Thin Client console or WorkSpaces Thin Client resources. For more information, see [Amazon WorkSpaces Thin Client end of support](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/workspacesthinclient-end-of-support.html).

# Software updates
<a name="software-updates"></a>

WorkSpaces Thin Client requires software updates periodically to introduce new functionality and apply security patches. These updates are represented by a versioned **Software set**.

A **Software set** can contain updates for software applications or the operating system of the WorkSpaces Thin Client device. From this console, you can choose to update the software immediately or schedule an automatic update during the maintenance window for the environments.

There are two types of Software sets:
+ Software sets that introduce new functionality, fix defects, and make general improvements. These are released monthly.
+ Software sets that contain security patches and fixes for critical issues. These are released as needed.

As an administrator, if you haven’t enabled automatic software updates on your environment, devices registered to that environment won’t receive software updates until you manually push the update.

As new Software sets are released, older Software sets expire. Starting from the date of release of a Software set with new functionality, you have 40 days before prior Software sets expire.

To ensure the security posture of the device remains intact, the service automatically updates devices if it detects expired software. This type of update can interrupt active sessions because it won’t honor the maintenance window or allow end users to delay the update. To avoid this, we recommend updating Software sets at least once every 30 days.

**Note**
If a Software set with security patches or a critical update is released, all prior Software sets will be set to expire in 3 days. To ensure your device remains secure and minimize disruption to daily operations, we recommend updating these Software sets immediately.

Refer to [ WorkSpaces Thin Client environment software sets](environment-software-sets.md) for the list of released Software Sets.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Thin Client. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-thin-client` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
