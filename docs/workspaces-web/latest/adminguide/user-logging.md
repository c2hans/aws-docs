---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/adminguide/user-logging.html
---

# Setting up user activity logging in Amazon WorkSpaces Secure Browser
<a name="user-logging"></a>

WorkSpaces Secure Browser offers two options for logging user activity and security-related events:
+ Session Logger captures a wide range of session events. These logs are delivered to an Amazon S3 bucket in your account, enabling easy integration with your preferred SIEM platform.
+ User Access Logging captures the most critical session events. These logs are streamed to an Amazon Kinesis stream for real-time processing and analysis.

Both logging options are configured at the portal level. You must set up each option individually for every portal where you want logging to be active. You can enable either option or both, depending on your requirements for each portal.

You are responsible for complying with any requirements that apply to the logging or monitoring of user activity when using this feature, including logging or monitoring of employee activity.

**Topics**
+ [Setting up Session Logger for Amazon WorkSpaces Secure Browser](session-logger.md)
+ [Setting up User Access logging for Amazon WorkSpaces Secure Browser](user-access-logging.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Secure Browser. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-web` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
