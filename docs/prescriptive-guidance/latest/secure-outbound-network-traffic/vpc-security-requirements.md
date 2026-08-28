---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/secure-outbound-network-traffic/vpc-security-requirements.html
---

# Determining your VPC's security requirements
<a name="vpc-security-requirements"></a>

**Important**
It's a best practice to design and test your VPC's outbound traffic security architecture in a test environment. Testing architecture changes in a development environment mitigates the risk of pushing unintended system behaviors live.

Before making changes to your network's outbound traffic patterns, it's important to understand the traffic patterns that your application needs to operate as intended. This information can help you identify which traffic patterns to allow and which ones to deny when rearchitecting your network.

To analyze your VPC's existing outbound traffic patterns, first turn on [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html). Then, use a test environment to run your application through various usage scenarios and analyze the simulated traffic in the flow logs.

VPC Flow Logs record your VPC's inbound and outbound IP traffic. Amazon VPC then sends the logs to either Amazon Simple Storage Service (Amazon S3) or Amazon CloudWatch. You can view and analyze the logs by using either of the following tools:
+ (For Amazon S3) Amazon Athena
+ (For CloudWatch) CloudWatch Logs Insights

For more information and example queries, see the following:
+ [Querying Amazon VPC flow logs](https://docs.aws.amazon.com/athena/latest/ug/vpc-flow-logs.html) (*Amazon Athena User Guide*)
+ [How can I use CloudWatch Logs Insights queries with my VPC flow log?](https://aws.amazon.com/premiumsupport/knowledge-center/vpc-flow-logs-and-cloudwatch-logs-insights/) (*AWS Knowledge Center*)
+ [CloudWatch Logs Insights query syntax](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax.html) (*Amazon CloudWatch Logs User Guide*)

For details on the types of information that VPC Flow Logs capture, see [Flow log record examples](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs-records-examples.html) in the *Amazon VPC User Guide*.

**Note**
VPC Flow Logs don't capture application layer (layer 7) information, such as DNS hostnames. If your security requirements call for the analysis of application layer data, you can deploy [AWS Network Firewall](https://aws.amazon.com/network-firewall/) to capture the required details. For more information, see the **Restricting a VPC's outbound traffic by using AWS Network Firewall and DNS hostnames** section of this guide.

## Best practices for analyzing your VPC's outbound traffic when using VPC Flow Logs
<a name="best-practices-outbound-traffic-analysis"></a>

When analyzing your VPC flow logs by using either Amazon Athena or CloudWatch Logs Insights queries, make sure that you do the following:
+ Identify and analyze the inbound and outbound traffic flowing through the [elastic network interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) attached to the resources that your application uses.
+ Identify and analyze the application traffic flowing through the network interface that's attached to the NAT gateway.
+ Make sure that you capture all outbound traffic for a network interface by making the source address in your query the network interface's private IP address.
+ Write your queries to focus on unexpected traffic patterns only. (For example, if your application communicates with third-party entities like an HTTPS API endpoint, then you can construct your queries to not include those entities.)
+ Investigate the validity of each port and destination IP address. (For example, an outbound destination port 22 could be normal for a bastion host, or a host that clones repositories from Git by using SSH.)

**Note**
If you're working with Amazon Athena for the first time, make sure that you configure a query result location. For instructions, see [Specifying a query result location using the Athena console](https://docs.aws.amazon.com/athena/latest/ug/querying.html#query-results-specify-location-console) in the *Amazon Athena User Guide*.

### Amazon Athena query examples
<a name="amazon-athena-query-examples.4c87b8f3-3c81-5133-a98f-9d63664706d1"></a>

**Example Athena query that returns outbound admin traffic from a specific network interface**

The following Athena query returns the first 200 lines of outbound admin traffic from a network interface with the IP address of **10.100.0.10**:

```
SELECT * FROM "<vpc_flow_logs_table_name>"

WHERE interface_id = 'eni-1234567890000000' AND srcaddr LIKE '10.100.0.10' AND dstport < 1024

LIMIT 200;
```

**Output example**

|  |
| --- |
| \# | 1 |
| --- |--- |
| **version** | 2 |
| **account\_id** | <account-id> |
| **interface\_id** | eni-123456789000000 |
| **srcaddr** | 10.32.0.10 |
| **dstaddr** | 11.22.33.44 |
| **srcport** | 36952 |
| **dstport** | 443 |
| **protocol** | 6 |
| **packets** | 25 |
| **bytes** | 5445 |
| **start** | 1659310200 |
| **end** | 1659310225 |
| **action** | ACCEPT |
| **log\_status** | OK |
| **date** | 2022-07-16 |

**Note**
The output in this pattern is formatted for presentation purposes and may appear differently on your system.

**Example Athena query that returns external IP addresses that receive the most traffic from a specific VPC**

The following Athena query returns the external IP addresses and ports that receive the most outbound traffic from a VPC with a CIDR block starting with **'10.32'**:

```
SELECT dstport, dstaddr,

count(*) AS count

FROM "<vpc_flow_logs_table_name>"

WHERE dstaddr not like '10.32%' AND interface_id = 'eni-1234567890000000'

GROUP BY dstport, dstaddr

ORDER BY count desc

LIMIT 200;
```

**Output example**

|
|
| \# | Dstport | Dstaddr | count |
| --- |--- |--- |--- |
| 1 | 443 | 52.x.x.x | 1442 |
| 2 | 443 | 63.x.x.x | 1201 |
| 3 | 443 | 102.x.x.x | 887 |

**Example Athena query that returns rejected outbound traffic from a specific VPC**

The following Athena query returns the rejected outbound traffic from a VPC with a CIDR block starting with **'10.32'**:

```
SELECT *

FROM "<vpc_flow_logs_table_name>"

WHERE srcaddr like '10.32%' AND action LIKE 'REJECT'
```

**Output example**

|  |
| --- |
| \# | 1 |
| --- |--- |
| **version** | 2 |
| **account\_id** | <account-id> |
| **interface\_id** | eni-123456789000000 |
| **srcaddr** | 10.32.0.10 |
| **dstaddr** | 11.22.33.44 |
| **srcport** | 36952 |
| **dstport** | 443 |
| **protocol** | 6 |
| **packets** | 25 |
| **bytes** | 5445 |
| **start** | 1659310200 |
| **end** | 1659310225 |
| **action** | REJECT |
| **log\_status** | OK |
| **date** | 2022-07-16 |

**Note**
The output in this pattern is formatted for presentation purposes and may appear differently on your system.

For more information about how to interpret Athena query results, see [Flow log records](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html#flow-log-records) in the *Amazon VPC User Guide*.

### CloudWatch Logs Insights query examples
<a name="cloudwatch-logs-insights-query-examples.460761c5-df5b-5058-9b70-0ff64c7039eb"></a>

**CloudWatch Logs Insights query example that returns outbound admin traffic from a specific network interface**

The following CloudWatch Logs Insights query returns the first 200 results of outbound admin traffic from a network interface with the IP address of **10.100.0.10**:

```
fields @timestamp, @message

| filter interfaceId = 'eni-1234567890000000'

| filter srcAddr = '10.100.0.10'

| filter dstPort < 1024

| limit 200
```

**Output example**

|
|
| Field | Value |
| --- |--- |
| @ingestionTime | 1659310250813 |
| @log | <account-id>:/aws/vpc/flowlogs |
| @logStream | eni-123456789000000-all |
| @message | 2 <account-id> eni-123456789000000 10.100.0.10 11.22.33.44 36952 443 6 25 5445 1659310200 1659310225 ACCEPT OK |
| @timestamp | 1659310200000 |
| accountId | <account-id> |
| action | ACCEPT |
| bytes | 5445 |
| dstAddr | 11.22.33.44 |
| dstPort | 443 |
| end | 1659310225 |
| interfaceId | eni-123456789000000 |
| logStatus | OK |
| packets | 25 |
| protocol | 6 |
| srcAddr | 10.100.0.10 |
| srcPort | 36952 |
| start | 1659310200 |
| version | 2 |

**Example CloudWatch Logs Insights query that returns external IP addresses that receive the most traffic from a specific VPC**

The following CloudWatch Logs Insights query returns the external IP addresses and ports that receive the most outbound traffic from a VPC with a CIDR block starting with **'10.32'**:

```
filter @logstream = 'eni-1234567890000000'

| stats count(*) as count by dstAddr, dstPort

| filter dstAddr not like '10.32'

| order by count desc

| limit 200
```

**Output example**

|
|
| \# | dstAddr | dstPort | count |
| --- |--- |--- |--- |
| 1 | 52.x.x.x | 443 | 439 |
| 2 | 51.79.x.x | 63.x.x.x | 25 |

**Example CloudWatch Logs Insights query that returns rejected outbound traffic from a specific VPC**

The following CloudWatch Logs Insights query returns the rejected outbound traffic from a VPC with a CIDR block starting with **'10.32'**:

```
filter @logstream = 'eni-0123456789000000'

| fields @timestamp, @message

| filter action='REJECT'
```

**Output example**

|
|
| Field | Value |
| --- |--- |
| @ingestionTime | 1666991000899 |
| @log | <account-id>:/aws/vpc/flowlogs |
| @logStream | eni-0123456789000000-all |
| @message | 2 <account-id> 'eni-0123456789000000' 185.x.x.x 10.10.2.222 55116 11211 17 1 43 1666990939 1666990966 REJECT OK |
| @timestamp | 1666990939000 |
| accountId | <account-id> |
| action | REJECT |
| bytes | 43 |
| dstAddr | 10.10.2.222 |
| dstPort | 11211 |
| end | 1666990966 |
| interfaceId | 'eni-0123456789000000' |
| logStatus | OK |
| packets | 1 |
| protocol | 17 |
| srcAddr | 185.x.x.x |
| srcPort | 55116 |
| start | 1666990939 |
| version | 2 |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
