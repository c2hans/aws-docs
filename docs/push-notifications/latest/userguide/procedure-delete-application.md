---
source_url: https://docs.aws.amazon.com/push-notifications/latest/userguide/procedure-delete-application.html
---

# Deleting an application
<a name="procedure-delete-application"></a>

This procedure removes the application from your account and all resources in the application.

## Contextual
<a name="procedure-delete-application"></a>

**Application**
An application is a storage container for all of your AWS End User Messaging Push settings. The application also stores your Amazon Pinpoint channels, campaigns, and journeys settings.

## Procedure
<a name="procedure-delete-application"></a>

1. Open the AWS End User Messaging Push console at [https://console.aws.amazon.com/push-notifications/](https://console.aws.amazon.com/push-notifications/).

1. Choose an application and then choose **Delete**.

1. In the **Delete application** window enter **delete** and then choose **Delete**.
**Important**
Any Amazon Pinpoint channels, campaigns, journeys, or segments are also deleted.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging Push. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query push-notifications` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
