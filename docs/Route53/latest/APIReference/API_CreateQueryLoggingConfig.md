---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateQueryLoggingConfig.html
---

# CreateQueryLoggingConfig
<a name="API_CreateQueryLoggingConfig"></a>

Creates a configuration for DNS query logging. After you create a query logging configuration, Amazon Route 53 begins to publish log data to an Amazon CloudWatch Logs log group.

DNS query logs contain information about the queries that Route 53 receives for a specified public hosted zone, such as the following:
+ Route 53 edge location that responded to the DNS query
+ Domain or subdomain that was requested
+ DNS record type, such as A or AAAA
+ DNS response code, such as `NoError` or `ServFail`

Log Group and Resource Policy
Before you create a query logging configuration, perform the following operations.
If you create a query logging configuration using the Route 53 console, Route 53 performs these operations automatically.

1. Create a CloudWatch Logs log group, and make note of the ARN, which you specify when you create a query logging configuration. Note the following:
   + You must create the log group in the us-east-1 region.
   + You must use the same AWS account to create the log group and the hosted zone that you want to configure query logging for.
   + When you create log groups for query logging, we recommend that you use a consistent prefix, for example:

      `/aws/route53/hosted zone name `

     In the next step, you'll create a resource policy, which controls access to one or more log groups and the associated AWS resources, such as Route 53 hosted zones. There's a limit on the number of resource policies that you can create, so we recommend that you use a consistent prefix so you can use the same resource policy for all the log groups that you create for query logging.

1. Create a CloudWatch Logs resource policy, and give it the permissions that Route 53 needs to create log streams and to send query logs to log streams. You must create the CloudWatch Logs resource policy in the us-east-1 region. For the value of `Resource`, specify the ARN for the log group that you created in the previous step. To use the same resource policy for all the CloudWatch Logs log groups that you created for query logging configurations, replace the hosted zone name with `*`, for example:

    `arn:aws:logs:us-east-1:123412341234:log-group:/aws/route53/*`

   To avoid the confused deputy problem, a security issue where an entity without a permission for an action can coerce a more-privileged entity to perform it, you can optionally limit the permissions that a service has to a resource in a resource-based policy by supplying the following values:
   + For `aws:SourceArn`, supply the hosted zone ARN used in creating the query logging configuration. For example, `aws:SourceArn: arn:aws:route53:::hostedzone/hosted zone ID`.
   + For `aws:SourceAccount`, supply the account ID for the account that creates the query logging configuration. For example, `aws:SourceAccount:111111111111`.

   For more information, see [The confused deputy problem](https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html) in the * AWS IAM User Guide*.
**Note**
You can't use the CloudWatch console to create or edit a resource policy. You must use the CloudWatch API, one of the AWS SDKs, or the AWS CLI.

Log Streams and Edge Locations
When Route 53 finishes creating the configuration for DNS query logging, it does the following:
+ Creates a log stream for an edge location the first time that the edge location responds to DNS queries for the specified hosted zone. That log stream is used to log all queries that Route 53 responds to for that edge location.
+ Begins to send query logs to the applicable log stream.
The name of each log stream is in the following format:
 ` hosted zone ID/edge location code `
The edge location code is a three-letter code and an arbitrarily assigned number, for example, DFW3. The three-letter code typically corresponds with the International Air Transport Association airport code for an airport near the edge location. (These abbreviations might change in the future.) For a list of edge locations, see "The Route 53 Global Network" on the [Route 53 Product Details](http://aws.amazon.com/route53/details/) page.

Queries That Are Logged
Query logs contain only the queries that DNS resolvers forward to Route 53. If a DNS resolver has already cached the response to a query (such as the IP address for a load balancer for example.com), the resolver will continue to return the cached response. It doesn't forward another query to Route 53 until the TTL for the corresponding resource record set expires. Depending on how many DNS queries are submitted for a resource record set, and depending on the TTL for that resource record set, query logs might contain information about only one query out of every several thousand queries that are submitted to DNS. For more information about how DNS works, see [Routing Internet Traffic to Your Website or Web Application](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/welcome-dns-service.html) in the *Amazon Route 53 Developer Guide*.

Log File Format
For a list of the values in each query log and the format of each value, see [Logging DNS Queries](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/query-logs.html) in the *Amazon Route 53 Developer Guide*.

Pricing
For information about charges for query logs, see [Amazon CloudWatch Pricing](http://aws.amazon.com/cloudwatch/pricing/).

How to Stop Logging
If you want Route 53 to stop sending query logs to CloudWatch Logs, delete the query logging configuration. For more information, see [DeleteQueryLoggingConfig](https://docs.aws.amazon.com/Route53/latest/APIReference/API_DeleteQueryLoggingConfig.html).

## Request Syntax
<a name="API_CreateQueryLoggingConfig_RequestSyntax"></a>

```
POST /2013-04-01/queryloggingconfig HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<CreateQueryLoggingConfigRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <CloudWatchLogsLogGroupArn>{{string}}</CloudWatchLogsLogGroupArn>
   <HostedZoneId>{{string}}</HostedZoneId>
</CreateQueryLoggingConfigRequest>
```

## URI Request Parameters
<a name="API_CreateQueryLoggingConfig_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateQueryLoggingConfig_RequestBody"></a>

The request accepts the following data in XML format.

 ** [CreateQueryLoggingConfigRequest](#API_CreateQueryLoggingConfig_RequestSyntax) **   <a name="Route53-CreateQueryLoggingConfig-request-CreateQueryLoggingConfigRequest"></a>
Root level tag for the CreateQueryLoggingConfigRequest parameters.
Required: Yes

 ** [CloudWatchLogsLogGroupArn](#API_CreateQueryLoggingConfig_RequestSyntax) **   <a name="Route53-CreateQueryLoggingConfig-request-CloudWatchLogsLogGroupArn"></a>
The Amazon Resource Name (ARN) for the log group that you want to Amazon Route 53 to send query logs to. This is the format of the ARN:
arn:aws:logs:*region*:*account-id*:log-group:*log\_group\_name*
To get the ARN for a log group, you can use the CloudWatch console, the [DescribeLogGroups](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeLogGroups.html) API action, the [describe-log-groups](https://docs.aws.amazon.com/cli/latest/reference/logs/describe-log-groups.html) command, or the applicable command in one of the AWS SDKs.
Type: String
Required: Yes

 ** [HostedZoneId](#API_CreateQueryLoggingConfig_RequestSyntax) **   <a name="Route53-CreateQueryLoggingConfig-request-HostedZoneId"></a>
The ID of the hosted zone that you want to log queries for. You can log queries only for public hosted zones.
Type: String
Length Constraints: Maximum length of 32.
Required: Yes

## Response Syntax
<a name="API_CreateQueryLoggingConfig_ResponseSyntax"></a>

```
HTTP/1.1 201
Location: {{Location}}
<?xml version="1.0" encoding="UTF-8"?>
<CreateQueryLoggingConfigResponse>
   <QueryLoggingConfig>
      <CloudWatchLogsLogGroupArn>string</CloudWatchLogsLogGroupArn>
      <HostedZoneId>string</HostedZoneId>
      <Id>string</Id>
   </QueryLoggingConfig>
</CreateQueryLoggingConfigResponse>
```

## Response Elements
<a name="API_CreateQueryLoggingConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The response returns the following HTTP headers.

 ** [Location](#API_CreateQueryLoggingConfig_ResponseSyntax) **   <a name="Route53-CreateQueryLoggingConfig-response-Location"></a>
The unique URL representing the new query logging configuration.
Length Constraints: Maximum length of 1024.

The following data is returned in XML format by the service.

 ** [CreateQueryLoggingConfigResponse](#API_CreateQueryLoggingConfig_ResponseSyntax) **   <a name="Route53-CreateQueryLoggingConfig-response-CreateQueryLoggingConfigResponse"></a>
Root level tag for the CreateQueryLoggingConfigResponse parameters.
Required: Yes

 ** [QueryLoggingConfig](#API_CreateQueryLoggingConfig_ResponseSyntax) **   <a name="Route53-CreateQueryLoggingConfig-response-QueryLoggingConfig"></a>
A complex type that contains the ID for a query logging configuration, the ID of the hosted zone that you want to log queries for, and the ARN for the log group that you want Amazon Route 53 to send query logs to.
Type: [QueryLoggingConfig](API_QueryLoggingConfig.md) object

## Errors
<a name="API_CreateQueryLoggingConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModification **
Another user submitted a request to create, update, or delete the object at the same time that you did. Retry the request.
 ** message **

HTTP Status Code: 400

 ** InsufficientCloudWatchLogsResourcePolicy **
Amazon Route 53 doesn't have the permissions required to create log streams and send query logs to log streams. Possible causes include the following:
+ There is no resource policy that specifies the log group ARN in the value for `Resource`.
+ The resource policy that includes the log group ARN in the value for `Resource` doesn't have the necessary permissions.
+ The resource policy hasn't finished propagating yet.
+ The Key management service (KMS) key you specified doesn’t exist or it can’t be used with the log group associated with query log. Update or provide a resource policy to grant permissions for the KMS key.
+ The Key management service (KMS) key you specified is marked as disabled for the log group associated with query log. Update or provide a resource policy to grant permissions for the KMS key.
HTTP Status Code: 400

 ** InvalidInput **
The input is not valid.
 ** message **

HTTP Status Code: 400

 ** NoSuchCloudWatchLogsLogGroup **
There is no CloudWatch Logs log group with the specified ARN.
HTTP Status Code: 404

 ** NoSuchHostedZone **
No hosted zone exists with the ID that you specified.
 ** message **

HTTP Status Code: 404

 ** QueryLoggingConfigAlreadyExists **
You can create only one query logging configuration for a hosted zone, and a query logging configuration already exists for this hosted zone.
HTTP Status Code: 409

## Examples
<a name="API_CreateQueryLoggingConfig_Examples"></a>

### Example Request
<a name="API_CreateQueryLoggingConfig_Example_1"></a>

The following request creates a configuration for the hosted zone `Z1D633PJN98FT9`. DNS query logs are sent to the log group with the ARN `arn:aws:logs:us-east-1:111111111111:log-group:/aws/route53/example.com`.

```
POST /2013-04-01/queryloggingconfig HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<CreateQueryLoggingConfigRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <CloudWatchLogsLogGroupArn>arn:aws:logs:us-east-1:111111111111:log-group:/aws/route53/example.com</CloudWatchLogsLogGroupArn>
   <HostedZoneId>Z1D633PJN98FT9</HostedZoneId>
</CreateQueryLoggingConfigRequest>
```

### Example Response
<a name="API_CreateQueryLoggingConfig_Example_2"></a>

This example illustrates one usage of CreateQueryLoggingConfig.

```
HTTP/1.1 200 OK
<?xml version="1.0" encoding="UTF-8"?>
<CreateQueryLoggingConfigResponse xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <QueryLoggingConfig>
      <CloudWatchLogsLogGroupArn>arn:aws:logs:us-east-1:111111111111:log-group:/aws/route53/example.com</CloudWatchLogsLogGroupArn>
      <HostedZoneId>Z1D633PJN98FT9</HostedZoneId>
      <Id>87654321-dcba-1234-abcd-1a2b3c4d5e6f</Id>
   </QueryLoggingConfig>
</CreateQueryLoggingConfigResponse>
```

## See Also
<a name="API_CreateQueryLoggingConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/CreateQueryLoggingConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/CreateQueryLoggingConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/CreateQueryLoggingConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/CreateQueryLoggingConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/CreateQueryLoggingConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/CreateQueryLoggingConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/CreateQueryLoggingConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/CreateQueryLoggingConfig)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/CreateQueryLoggingConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/CreateQueryLoggingConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
