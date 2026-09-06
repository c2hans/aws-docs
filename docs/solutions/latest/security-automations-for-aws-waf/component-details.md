---
source_url: https://docs.aws.amazon.com/solutions/latest/security-automations-for-aws-waf/component-details.html
---

# Component details
<a name="component-details"></a>

As described in the [Architecture diagram](architecture-overview.md#architecture-diagram), four of this solution’s components use automations to inspect IP addresses and add them to the AWS WAF block list. The following sections explain each of these components in more detail.

## Log parser - Application
<a name="log-parser--application"></a>

The Application log parser helps protect against scanners and probes.

 **Application log parser flow.**

![app log parser flow](http://docs.aws.amazon.com/solutions/latest/security-automations-for-aws-waf/images/app-log-parser-flow.png)

1. When CloudFront or an ALB receives requests on behalf of your web application, it sends access logs to an Amazon S3 bucket.

   1. (Optional) If you select `Yes - Amazon Athena log parser` for the template parameters **Activate HTTP Flood Protection** and **Activate Scanner & Probe Protection**, a Lambda function moves access logs from their original folder {{<customer-bucket>}} `/AWSLogs` to a newly partitioned folder {{<customer-bucket>}} `/AWSLogs-partitioned/` {{<optional-prefix>}} `/year=` {{<YYYY>}} `/month=` {{<MM>}} `/day=` {{<DD>}} `/hour=` {{<HH>}}/ upon their arrival in Amazon S3.

   1. (Optional) If you select `yes` for the **Keep Data in Original S3 location** template parameter, logs remain in their original location and are copied to their partitioned folder, duplicating your log storage.
**Note**
For the Athena log parser, this solution only partitions new logs that arrive in your Amazon S3 bucket after you deploy this solution. If you have existing logs that you want to partition, you must manually upload those logs to Amazon S3 after you deploy this solution.

1. Based on your selection for the template parameters **Activate HTTP Flood Protection** and **Activate Scanner & Probe Protection**, this solution processes logs using one of the following:

   1.  **Lambda** - Each time a new access log is stored in the Amazon S3 bucket, the `Log Parser` Lambda function is initiated.

   1.  **Athena** - By default, every five minutes the **Scanner & Probe Protection** Athena query runs, and the output pushes to AWS WAF. This process is initiated by a CloudWatch event, which starts the Lambda function responsible for running the Athena query and pushes the result into AWS WAF.

1. The solution analyzes the log data to identify IP addresses that generated more errors than the defined quota. The solution then updates an AWS WAF IP set condition to block those IP addresses for a customer-defined period of time.

## Log parser - AWS WAF
<a name="log-parser--aws-waf"></a>

If you select `yes - AWS Lambda log parser` or `yes - Amazon Athena log parser` for **Activate HTTP Flood Protection**, this solution provisions the following components, which parse AWS WAF logs to identify and block origins that flood the endpoint with a request rate greater than the quota you defined.

 **AWS WAF log parser flow.**

![waf log parser flow](http://docs.aws.amazon.com/solutions/latest/security-automations-for-aws-waf/images/waf-log-parser-flow.png)

1. When AWS WAF receives access logs, it sends the logs to an Firehose endpoint. Firehose then delivers the logs to a partitioned bucket in Amazon S3 named {{<customer-bucket>}} `/AWSLogs/` {{<optional-prefix>}} `/year=` {{<YYYY>}} `/month=` {{<MM>}} `/day=` {{<DD>}} `/hour=` {{<HH>}} `/`

1. Based on your selection for the template parameters **Activate HTTP Flood Protection** and **Activate Scanner & Probe Protection**, this solution processes logs using one of the following:

   1.  **Lambda**: Each time a new access log is stored in the Amazon S3 bucket, the `Log Parser` Lambda function is initiated.

   1.  **Athena:** By default, every five minutes the scanner and probe Athena query is run and the output is pushed to AWS WAF. This process is initiated by an Amazon CloudWatch event, that then starts the Lambda function responsible for executing the Amazon Athena query, and pushes the result into AWS WAF.

1. The solution analyses the log data to identify IP addresses that sent more requests than the defined quota. The solution then updates an AWS WAF IP set condition to block those IP addresses for a customer-defined period of time.

## Log parser - Bad bot
<a name="log-parser--badbot"></a>

The Bad bot log parser inspects requests to the honeypot endpoint to extract their source IP address.

 **Bad bot log parser flow.**

![badbot log parser flow](http://docs.aws.amazon.com/solutions/latest/security-automations-for-aws-waf/images/badbot-log-parser-flow.png)

1. If `Bad Bot Protection` is activated and both HTTP Flood Protection and Scanner & Probe Protection features are disabled: The system will use the Log Lambda parser, which logs only bad bot requests based on [WAF label filters](https://docs.aws.amazon.com/waf/latest/developerguide/waf-labels.html).

1. The Lambda function intercepts and inspects request headers to extract the IP address of the source that accessed the trap endpoint.

1. The solution analyses the log data to identify IP addresses that sent more requests than the defined quota. The solution then updates an AWS WAF IP set condition to block those IP addresses for a customer-defined period of time.

## IP lists parser
<a name="ip-lists-parser"></a>

The `IP Lists Parser` Lambda function helps protect against known attackers identified in third-party IP reputation lists.

 **IP eputation lists parser flow.**

![ip reputation lists flow](http://docs.aws.amazon.com/solutions/latest/security-automations-for-aws-waf/images/ip-reputation-lists-flow.png)

1. An hourly Amazon CloudWatch event invokes the `IP Lists Parser` Lambda function.

1. The Lambda function gathers and parses data from three sources:
   + Spamhaus DROP and EDROP lists
   + Proofpoint Emerging Threats IP list
   + Tor exit node list

1. The Lambda function updates the AWS WAF block list with the current IP addresses.
