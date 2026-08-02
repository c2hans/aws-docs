---
source_url: https://docs.aws.amazon.com/appsync/latest/eventapi/event-api-monitoring.html
---

# Using CloudWatch to monitor and log Event API data
<a name="event-api-monitoring"></a>

You can log and debug your Event API using CloudWatch metrics and CloudWatch logs. These tools enable developers to monitor performance, troubleshoot issues, and optimize their AWS AppSync API operations effectively.

CloudWatch metrics is a tool that provides a wide range of metrics to monitor API performance and usage. These metrics fall into two main categories:

1. **HTTP API Metrics for Publish**: These include `4XXError` and `5XXError` for tracking client and server errors, `Latency` for measuring response times, `Requests` for monitoring total API calls, `TokensConsumed` for tracking resource usage, and *Events* related to metrics for tracking event publishing performance.

1. **Real-time Subscription Metrics**: These metrics focus on WebSocket connections and subscription activities. They include metrics for connection requests, successful connections, subscription registrations, message publishing, and active connections and subscriptions.

CloudWatch Logs is a tool that enables logging capabilities for your Eent APIs. Logs can be set at two levels of the API:

1. **Request-level Logs**: These capture overall request information, including HTTP headers, operation summaries, and subscription registrations.

1. **Handler-level Logs**: These provide detailed information about handler evaluation, including request and response mappings, and tracing information for each field.

You can configure logging, interpret log entries, and use log data for troubleshooting and optimization. AWS AppSync provides various log types that provide insight into your API's behavior.

## Setting up and configuring logging on an Event API
<a name="setup-and-configuration"></a>

Us the following instruction to turn on automatic logging on a Event API using the AWS AppSync console.

1. Sign in to the AWS Management Console and open the [AppSync console](https://console.aws.amazon.com/appsync/).

1. On the **APIs** page, choose the name of an Event API.

1. On the API's homepage, in the navigation pane, choose **Settings**.

1. Under **Logging**, do the following:

   1. Turn on **Enable Logs**.

   1. (Optional) For **Log level**, choose your preferred field-level logging level (**None**, **Error**, or **All**).

   1. The procedure for adding a service role varies depending on whether you want to create a new role or use an existing one.
      + To create a new role:

        1. For **Create or use an existing role**, choose **New role**. This creates a new IAM role that allows AWS AppSync to write logs to CloudWatch.
      + To use an existing role:

        1. Choose **Existing role**.

        1. In the service role list, select the ARN of an existing IAM role in your AWS account.

           For information about the configuration of the IAM role, see [Manually creating an IAM role with CloudWatch Logs permissions](#manual-role-configuration).

1. Choose **Save**.

### Manually creating an IAM role with CloudWatch Logs permissions
<a name="manual-role-configuration"></a>

If you choose to use an existing IAM role, the role must grant AWS AppSync the required permissions to write logs to CloudWatch. To configure this manually, you must provide a service role ARN so that AWS AppSync can assume the role when writing the logs.

In the [IAM console](https://console.aws.amazon.com/iam), create a new policy with the name `AWSAppSyncPushToCloudWatchLogsPolicy` that has the following definition:

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "*"
        }
    ]
}
```

------

Next, create a new role with the name **AWSAppSyncPushToCloudWatchLogsRole**, and attach the newly created policy to the role. Edit the trust relationship for this role to the following:

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
        "Effect": "Allow",
        "Principal": {
            "Service": "appsync.amazonaws.com"
        },
        "Action": "sts:AssumeRole"
        }
    ]
}
```

------

Copy the role ARN and use it when setting up logging for an AWS AppSync Event API.
