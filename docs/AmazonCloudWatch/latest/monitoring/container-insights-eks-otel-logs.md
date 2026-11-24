---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/container-insights-eks-otel-logs.html
---

# Sending logs to Amazon CloudWatch

With OTel Container Insights, the CloudWatch agent that the Amazon CloudWatch Observability EKS add-on deploys on each node automatically uses OpenTelemetry components to collect container logs and host logs. It sends them to the CloudWatch Logs OTLP endpoint in your Region, in the log groups that are listed in [Log groups and sources](#container-insights-eks-otel-logs-groups). The agent adds Kubernetes and cloud attributes to each log record, as described in [Telemetry enrichment](eks-standard-telemetry-attributes.md).

No additional setup is required for basic log collection. Log collection is enabled by default when you follow the [Quick start](container-insights-eks-otel-quickstart.md).

**Log collection costs**
Enabling log collection ingests all container stdout and stderr from every pod in the cluster, which can significantly increase CloudWatch Logs costs. To control cost, filter logs before ingestion and set a retention policy on the log groups. For information about filtering, see [OpenTelemetry filters](eks-observability-addon-telemetry-filters.md). For information about retention policies, see [Set log retention](#container-insights-eks-otel-logs-retention).

**Correlating logs with traces**
Collecting container logs does not by itself correlate them with traces in CloudWatch Application Signals. To correlate traces with logs, instrument your application for Application Signals by using the enablement guide for your architecture, such as [Enable your applications on Amazon EKS clusters](CloudWatch-Application-Signals-Enable-EKS.md), and then configure your logging output as described in [Enable trace to log correlation](Application-Signals-TraceLogCorrelation.md).

## Prerequisites
<a name="container-insights-eks-otel-logs-prereqs"></a>

Before you configure log collection, verify that you meet the following requirements.
+ OTel Container Insights installed and the `amazon-cloudwatch-observability` add-on active on your cluster
+ IAM permissions: `logs:CreateLogGroup`, `logs:CreateLogStream`, `logs:PutLogEvents`, `logs:DescribeLogGroups`, and `logs:DescribeLogStreams` (included in the `CloudWatchAgentServerPolicy` managed policy)
+ Node access: the agent reads `/var/log` on each node. The add-on mounts it when log collection is on.

## Log groups and sources
<a name="container-insights-eks-otel-logs-groups"></a>

The following table describes the log groups that OTel Container Insights creates and the sources it collects from. In the log group names, `{{cluster-name}}` is the name of your Amazon EKS cluster.

| Log group | Source | Contents |
| --- | --- | --- |
| /aws/otel/containerinsights/{{cluster-name}}/application | /var/log/containers/\*.log | Container stdout and stderr logs, except the logs of pods whose names start with cloudwatch-agent, fluent-bit, aws-node, or kube-proxy |
| /aws/otel/containerinsights/{{cluster-name}}/host | /var/log/messages, /var/log/dmesg, and /var/log/secure | Node operating system logs |

**Note**
Dataplane logs will be available in a future release.

## Customizing log collection
<a name="container-insights-eks-otel-logs-customize"></a>

You can customize log collection by updating the add-on configuration values. The examples in this section are fragments to merge into your current configuration. For instructions on merging them, see [Configuring the add-on and the Helm chart](eks-observability-addon-configure.md). To drop the logs of some namespaces, use `otelFilters.namespaces`, as described in [OpenTelemetry filters](eks-observability-addon-telemetry-filters.md).

### Turning off log collection
<a name="container-insights-eks-otel-logs-disable"></a>

To turn off log collection and keep OTel Container Insights metrics, merge the following fragment into your configuration. The default is `true`.

```json
{
  "otelContainerInsights": {
    "enabled": true,
    "logs": { "enabled": false }
  }
}
```

### Set log retention
<a name="container-insights-eks-otel-logs-retention"></a>

By default, CloudWatch Logs retains log data indefinitely. To control storage costs, you can set a retention policy on each log group.

**To set log retention**
+ Run the following command. Replace {{cluster-name}} with the name of your Amazon EKS cluster. Replace {{30}} with the number of days to retain logs. Run it again with `host` in place of `application` for the host log group.

  ```bash
  aws logs put-retention-policy \
    --log-group-name "/aws/otel/containerinsights/{{cluster-name}}/application" \
    --retention-in-days {{30}}
  ```

## Verification
<a name="container-insights-eks-otel-logs-verify"></a>

To verify that log collection is working, check that the expected log groups exist and contain data.

**To verify log collection**
+ Run the following command. Replace {{cluster-name}} with the name of your Amazon EKS cluster.

  ```bash
  aws logs describe-log-groups \
    --log-group-name-prefix "/aws/otel/containerinsights/{{cluster-name}}" \
    --query "logGroups[].{Name:logGroupName,StoredBytes:storedBytes}" \
    --output table
  ```

  The output displays the log group names and the number of stored bytes. A non-zero value for `StoredBytes` confirms that the agent is delivering logs.

## Troubleshooting
<a name="container-insights-eks-otel-logs-troubleshoot"></a>

Use the following guidance to resolve common log collection issues.

### Log groups not created after 5 minutes
<a name="container-insights-eks-otel-logs-ts-no-loggroup"></a>

**Symptom:** The `/aws/otel/containerinsights/{{cluster-name}}/application` log group does not appear in CloudWatch Logs after 5 minutes.

**Cause:** The collector does not have the required IAM permissions to create log groups and log streams.

**Solution:** Verify that the IAM role associated with the collector has the `CloudWatchAgentServerPolicy` managed policy attached. This policy includes the `logs:CreateLogGroup` and `logs:CreateLogStream` permissions.

### Application log group exists but is empty
<a name="container-insights-eks-otel-logs-ts-empty"></a>

**Symptom:** The application log group exists in CloudWatch Logs, but it contains no log streams or log events.

**Cause:** This issue occurs when containers are not writing to stdout or stderr, or the filelog receiver cannot access `/var/log/containers/` on the node.

**Solution:** Complete the following steps to resolve this issue.

1. Verify that your application containers write logs to stdout or stderr.

1. Run the following command to check that the CloudWatch agent DaemonSet has a volume mount for `/var/log`.

   ```bash
   kubectl get daemonset cloudwatch-agent -n amazon-cloudwatch -o yaml | grep "mountPath: /var/log$"
   ```

1. If the mount is missing, check that `otelContainerInsights.logs.enabled` isn't `false` in the add-on configuration.

1. Check the collector logs for file access errors.

   ```bash
   kubectl logs -n amazon-cloudwatch -l app.kubernetes.io/name=cloudwatch-agent --tail=50 | grep -i "error\|permission"
   ```

### High CloudWatch Logs costs
<a name="container-insights-eks-otel-logs-ts-costs"></a>

**Symptom:** CloudWatch Logs ingestion or storage costs are higher than expected.

**Cause:** High-volume namespaces (such as load testing or monitoring namespaces) generate large volumes of logs.

**Solution:** Drop the logs of those namespaces with `otelFilters.namespaces`, and set a retention policy on the log groups to automatically delete older logs. For instructions on filtering, retention, and turning off log collection, see [OpenTelemetry filters](eks-observability-addon-telemetry-filters.md), [Set log retention](#container-insights-eks-otel-logs-retention), and [Turning off log collection](#container-insights-eks-otel-logs-disable).
