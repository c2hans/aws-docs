---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/elbproxy/monitoring-logs.html
---

# Proxy logs

Each proxy publishes its Envoy process logs to CloudWatch Logs using its proxy role. These are application logs about the proxy process, such as startup, configuration, and connection errors. They are separate from the per-request access logs, which you export with a network access logger in your Envoy configuration. Because the proxy uses its proxy role to publish the application logs, the proxy role must grant permission to write to CloudWatch Logs. For more information, see [Create a proxy role](setting-up.md#setting-up-proxy-role).

The VPC of the proxy must have network access to CloudWatch Logs, through an internet gateway or a VPC endpoint.

A proxy publishes its logs to the log group `/aws/elb-proxy/{{proxy-name}}`. Within that log group, each log stream is named for a proxy elastic network interface (ENI) ID, for example `eni-0123456789abcdef0`. Because these are the network interfaces in the proxy's VPC, the stream name identifies which proxy interface produced the log. By default, the proxy logs at the `warn` level.

## If logs are missing
<a name="monitoring-logs-missing"></a>

If a proxy publishes no logs, or you can't find the logs that you expect, check the following.

1. **Account, Region, and stream** – Look in the proxy's account and Region, in the log group `/aws/elb-proxy/{{proxy-name}}`. Choose the log stream for the ENI that you want, and a time range that covers the event.

1. **Proxy role permissions** – The role in `roleArn` must allow `logs:CreateLogGroup`, `logs:CreateLogStream`, and `logs:PutLogEvents` on the proxy log groups and streams. Its trust policy must allow `elasticloadbalancing.amazonaws.com`. Check for denies in permissions boundaries and AWS Organizations service control policies. For the proxy role and its policy, see [Create a proxy role](setting-up.md#setting-up-proxy-role). The role must allow the following actions.

   ```
   logs:CreateLogGroup
   logs:CreateLogStream
   logs:PutLogEvents
   ```

1. **VPC connectivity** – The proxy subnets must reach CloudWatch Logs over HTTPS (TCP 443), with working DNS, routes, security groups, and network ACLs. Use a CloudWatch Logs interface VPC endpoint, or a route to the public endpoint, for example a NAT gateway for private subnets. For more information, see [Using CloudWatch Logs with interface VPC endpoints](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/cloudwatch-logs-and-interface-VPC.html).

1. **Log level** – ELB for Envoy emits logs at or above the configured level, which is `warn` by default, so a quiet proxy might emit nothing. A missing log group or stream by itself is not proof of a permissions or connectivity problem, because groups and streams are created as records are published. For more information about log levels, see [Set the Envoy log level](monitoring-log-level.md).
