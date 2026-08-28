---
source_url: https://docs.aws.amazon.com/solutions/latest/prebid-server-deployment-on-aws/nat-gateway.html
---

# NAT gateway
<a name="nat-gateway"></a>

## Port allocation errors
<a name="port-allocation-errors"></a>
+ The alarm changes state if there is a port allocation error in the NAT gateway.
+ The alarm returns to the `OK` state if the data is within the acceptable threshold for 5 minutes.
+ This can mean that too many concurrent connections are open through the NAT gateway and it caused a port allocation error.
+ Metric: `ErrorPortAllocation` > 0

## Packets dropped count
<a name="packets-dropped-count"></a>
+ The alarm changes state if a value greater than 0.01% is reached within a 1-minute period.
+ This might indicate an ongoing transient issue with the NAT gateway.
+ The alarm returns to the `OK` state if the data is within the acceptable threshold for 5 minutes.
+ If this value exceeds 0.01 percent of the total traffic on the NAT gateway, check the AWS Service Health dashboard.
+ Metric: `PacketsDropCount` > 0.01%

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Deploying a Prebid Server on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
