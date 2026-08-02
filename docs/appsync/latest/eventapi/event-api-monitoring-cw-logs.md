---
source_url: https://docs.aws.amazon.com/appsync/latest/eventapi/event-api-monitoring-cw-logs.html
---

# Configuring CloudWatch Logs on Event APIs
<a name="event-api-monitoring-cw-logs"></a>

You can configure two types of logging on any new or existing API: request-level logs and and handler logs.

**Request-level logs**

When request-level logging is configured for an API, the following information is logged.
+ The number of tokens consumed
+ The request and response HTTP headers
+ The overall operation summary

**Handler logs**

When handler logging is configured for an API, the following information is logged.
+ Generated request mapping with source and arguments for each field
+ The transformed response mapping for each field, which includes the data as a result of resolving that field
+ Tracing information for each field

If you turn on logging, AWS AppSync manages the CloudWatch Logs. The process includes creating log groups and log streams, and reporting to the log streams with these logs.

When you turn on logging on an AWS AppSync API and make requests, AWS AppSync creates a log group and log streams under the log group. The log group is named following the `/aws/appsync/apis/{api_id}` format. Within each log group, the logs are further divided into log streams. These are ordered by **Last Event Time** as logged data is reported.

Every log event is tagged with the **x-amzn-RequestId** of that request. This helps you filter log events in CloudWatch to get all logged information about that request. You can get the RequestId from the response headers of every AWS AppSync request.

The field-level logging is configured with the following log levels:
+  **None - No handler logs are captured.**
+
** **Error** - Logs the following information *only* for the fields that are in error:**
  + The error section in the server response
  + Handler errors and `console.error` logging from handlers
  + The generated request/response functions that got resolved for error fields
+
** **All** - Logs the following information for *all* fields in the query:**
  + Custom logging from handlers
  + The generated request/response functions that got resolved for each field

## Using token counts to optimize your requests
<a name="aws-appsync-using-token-counts-to-optimize-requests"></a>

Requests that consume less than or equal to 1,500 KB-seconds of memory and vCPU time are allocated one token. Requests with resource consumption greater than 1,500 KB-seconds receive additional tokens. For example, if a request consumes 3,350 KB-seconds, AWS AppSync allocates three tokens (rounded up to the next integer value) to the request. By default, AWS AppSync allocates a maximum of 5,000 or 10,000 request tokens per second to the APIs in your account, depending upon the AWS Region in which it's deployed. If your APIs each use an average of two tokens per second, you'll be limited to 2,500 or 5,000 requests per second, respectively. If you need more tokens per second than the allotted amount, you can submit a request to increase the default quota for the rate of request tokens. For more information, see [AWS AppSync endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/appsync.html#limits_appsync) in the *AWS General Reference guide* and [Requesting a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) in the *Service Quotas User Guide*.

A high per-request token count could indicate that there's an opportunity to optimize your requests and improve the performance of your API. Factors that can increase your per-request token count include:
+ The complexity of your handlers
+ The amount of data returned from your handlers
+ Logging configuration, and the amount of custom logging in your handlers

**Note**
In addition to AWS AppSync metrics and logs, clients can access the number of tokens consumed in a request via the response header `x-amzn-appsync-TokensConsumed`.

**Log size limits**

By default, if logging has been enabled, AWS AppSync will send up to 1 MB of logs per request.
