---
source_url: https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/access-cloudwatch-logs-insights.html
---

# Access CloudWatch Logs insights
<a name="access-cloudwatch-logs-insights"></a>

This solution logs error, warning, informational, and debugging messages for the Lambda functions. To choose the type of messages to log:

1. Locate the applicable function in the AWS Lambda console.

1. Add a **POWERTOOLS\_LOG\_LEVEL** environment variable.

1. Set the variable to the applicable type of message.

For further instructions, see [Create Lambda environment variables](https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html) in the *AWS Lambda Developer Guide*.

The following table lists the types of log levels that you can choose from.

| Level | Description |
| --- | --- |
|  **ERROR**  | Logs include information on anything that causes an operation to fail. |
|  **WARNING**  | Logs include information on anything that could potentially cause inconsistencies in the function but might not necessarily cause the operation to fail. Logs also include ERROR messages. |
|  **INFO**  | Logs include high-level information about how the function is operating. Logs also include ERROR and WARNING messages. |
|  **DEBUG**  | Logs include information that might be helpful when debugging a problem with the function. Logs also include ERROR, WARNING, and INFO messages. |

Use the following procedure to add CloudWatch Logs insights to this solution.

1. Identify the relevant log groups:

   1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation).

   1. Choose your target stack.

   1. Select the **Resources** tab and search for your target Lambda functions.

   1. Sign in to the [AWS Lambda console](https://console.aws.amazon.com/lambda) and choose each of your target Lambda functions.

   1. For each of your target Lambda functions, select the **Monitor** tab and choose **View CloudWatch Logs**.

   1. Copy the names of the log groups that you want to extract insights from.

1. Navigate to the [Amazon CloudWatch console](https://console.aws.amazon.com/cloudwatch).

1. On the navigation menu, under **Logs**, choose **Logs Insights**.

1. On the **Logs Insights** page, choose the **Logs** tab.

1. Search for log group names from step 1.

1. Copy one of the following example queries and paste it into the query field:

   1. To identify all client exceptions:

      ```
      fields @message
      |filter @message like /(?i)Exception/|stats count(*) as exceptionCount by @message
      ```

   1. To retrieve count of invocations by function name:

      ```
      stats count(*) by function_name
      ```

   1. To retrieve count of invocations over five-minute intervals:

      ```
      stats count(*) as invocations by bin(5m)
      ```

   1. To retrieve all [AWS X-Ray](https://aws.amazon.com/xray/) trace IDs:

      ```
      filter @message like "XRAY TraceId"
      |parse @message "XRAY TraceId: * " as traceId|stats count(*) by traceId
      ```

   1. To retrieve logs relating to a specific X-Ray Trace ID:

      ```
      filter @message like "your-traceid-here"
      ```

   1. To retrieve unauthorized WebSocket errors:

      ```
      fields
      @ingestionTime,
      @log,
      @logStream,
      @message,
      @requestId,
      @timestamp,
      errorMessage,
      errorType
      |filter @message like /Unauthorized/ and @message like /websocket/|sort @timestamp desc
      ```

   1. To retrieve count of metrics published:

      ```
      filter @message like "CloudWatchMetrics"
      |parse @message /"Metrics":\s*\[(?<metrics>.*?)\]/|stats count(*) as metric_count by metrics
      ```
