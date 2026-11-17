---
source_url: https://docs.aws.amazon.com/solutions/latest/prebid-server-deployment-on-aws/nat-gateway.html
---

# NAT gateway
<a name="nat-gateway"></a>

The solution creates each of the following alarms for each of the two NAT gateways.

## Port allocation errors
<a name="port-allocation-errors"></a>
+ The alarm changes state if there is a port allocation error in the NAT gateway within a 1-minute period.
+ This can mean that too many concurrent connections are open through the NAT gateway and it caused a port allocation error.
+ Metric: `ErrorPortAllocation` > 0

## Packets dropped count
<a name="packets-dropped-count"></a>
+ The alarm changes state if the NAT gateway drops any packets within a 1-minute period.
+ This might indicate an ongoing transient issue with the NAT gateway.
+ If the dropped packets exceed 0.01 percent of the total traffic on the NAT gateway, check the AWS Health Dashboard.
+ Metric: `PacketsDropCount` > 0
