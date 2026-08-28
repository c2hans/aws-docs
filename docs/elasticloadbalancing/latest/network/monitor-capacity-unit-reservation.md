---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/network/monitor-capacity-unit-reservation.html
---

# Monitor Load balancer Capacity Unit reservation for your Network Load Balancer
<a name="monitor-capacity-unit-reservation"></a>

**Reservation status**

The following are the possible status values for an LCU reservation:
+ `pending` ‐ Indicates the reservation it is in the process of provisioning.
+ `provisioned` ‐ Indicates the reserved capacity is ready and available to use.
+ `failed` ‐ Indicates the request cannot be completed at the time.
+ `rebalancing` ‐ Indicates an availability zone has been added or removed and the load balancer is rebalancing capacity.

**LCU utilization**
To determine reserved LCU utilization, you can compare the per-minute `ProcessedBytes` metric with the per-hour `Sum(ReservedLCUs)`. To convert bytes per minute to LCU per hour, use (bytes per min)\*8/60/ (10^6)/2.2.

------
#### [ Console ]

**To view the status of an LCU reservation**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. On the navigation pane, choose **Load Balancers**.

1. Select the load balancer name.

1. On the **Capacity** tab, you can view the **Reservation Status** and **Reserved LCU** value.

------
#### [ AWS CLI ]

**To monitor the status of an LCU reservation**
Use the [describe-capacity-reservation](https://docs.aws.amazon.com/cli/latest/reference/elbv2/describe-capacity-reservation.html) command.

```
aws elbv2 describe-capacity-reservation \
    --load-balancer-arn {{load-balancer-arn}}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Elastic Load Balancing. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticloadbalancing` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
