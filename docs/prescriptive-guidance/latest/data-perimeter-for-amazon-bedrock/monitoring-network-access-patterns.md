---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/data-perimeter-for-amazon-bedrock/monitoring-network-access-patterns.html
---

# Monitoring network access patterns
<a name="monitoring-network-access-patterns"></a>

## Control objective
<a name="control-objective.59ffe723-856f-5d42-b485-0a25e8e93b73"></a>

***Network perimeter**** – My identities can access resources only from expected networks / My resources can only be accessed from expected networks*

AI workloads can generate unexpected network traffic patterns due to their dynamic nature. Implement comprehensive monitoring that detects anomalous network behavior, such as unusual data volumes, unexpected destination endpoints, or traffic patterns that suggest data exfiltration attempts.

**Amazon VPC Flow Logs configuration**

Configure Amazon VPC Flow Logs for the Amazon VPC containing your AI workloads using this configuration:

```
{
  "FlowLogConfiguration": {
    "ResourceType": "VPC",
    "ResourceId": "vpc-12345678",
    "TrafficType": "ALL",
    "LogDestinationType": "cloud-watch-logs",
    "LogGroupName": "/aws/vpc/bedrock-flowlogs",
    "DeliverLogsPermissionArn": "arn:aws:iam::123456789012:role/flowlogsRole",
    "Tags": [
      {
        "Key": "Purpose",
        "Value": "BedrockNetworkMonitoring"
      }
    ]
  }
}
```
+ **VPC Flow Logs** – Captures all network traffic metadata for the Amazon VPC containing AI workloads, enabling detection of anomalous traffic patterns and potential data exfiltration attempts

### CloudWatch Insights queries for anomaly detection:
<a name="cloud-watch-insights-queries-for-anomaly-detection"></a>

These queries analyze Amazon VPC Flow Logs to detect unusual network behavior. The first query identifies sources generating high traffic volumes to Amazon Bedrock endpoints, which could indicate data exfiltration or misconfigured applications. The second query detects connections from AI workload subnets to external (non-private) IP addresses, which violates the network perimeter.

```
-- Detect unusual traffic volumes to Bedrock endpoints
fields @timestamp, srcaddr, dstaddr, bytes
| filter dstaddr like /bedrock/
| stats sum(bytes) as total_bytes by srcaddr
| sort total_bytes desc
| limit 20

-- Identify connections to unexpected external endpoints
fields @timestamp, srcaddr, dstaddr, dstport
| filter srcaddr like /10\.0\.1[01]\./
| filter not (dstaddr like /10\./ or dstaddr like /172\.16\./ or dstaddr like /192\.168\./)
| stats count() as connection_count by dstaddr, dstport
| sort connection_count desc
```

**Query explanation:**
+ **Traffic volume query** – Identifies sources generating high traffic to Amazon Bedrock endpoints, helping detect potential data exfiltration or misconfigured applications
+ **External connection query** – Detects AI workload subnets connecting to non-private IP addresses, indicating potential network perimeter violations
