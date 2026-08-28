---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/adminguide/monitoring-logging.html
---

# User activity logging in Amazon WorkSpaces Secure Browser
<a name="monitoring-logging"></a>

Amazon WorkSpaces Secure Browser enables customers to log session events related to user activities in the Secure browser sessions.

WorkSpaces Secure Browser offers two options for logging user activity and security-related events:
+ Session Logger captures a wide range of session events. These logs are delivered to an Amazon S3 bucket in your account, enabling easy integration with your preferred SIEM platform.
+ User Access Logging captures the most critical session events. These logs are streamed to an Amazon Kinesis stream for real-time processing and analysis.

For more information about how to set up these options, see [Setting up Session Logger for Amazon WorkSpaces Secure Browser](session-logger.md) and [Setting up User Access logging for Amazon WorkSpaces Secure Browser](user-access-logging.md).

**Topics**
+ [Session events in Session Logger for Amazon WorkSpaces Secure Browser](session-events-session-logger.md)
+ [Session events in User Access logging for Amazon WorkSpaces Secure Browser](session-events-logging.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Secure Browser. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-web` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
