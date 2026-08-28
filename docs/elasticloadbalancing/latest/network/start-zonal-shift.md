---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/network/start-zonal-shift.html
---

# Start a zonal shift for your Network Load Balancer
<a name="start-zonal-shift"></a>

Zonal shift in ARC enables you to temporarily move traffic for supported resources away from an Availability Zone so that your application can continue to operate normally with other Availability Zones in an AWS Region.

**Prerequisite**
Before you begin, verify that you [enabled zonal shift](enable-zonal-shift.md#enable-zonal-shift.title) for the load balancer.

------
#### [ Console ]

This procedure explains how to start a zonal shift using the Amazon EC2 console. For steps to start a zonal shift using the ARC console, see [Starting a zonal shift](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.start-cancel.html) in the *Amazon Application Recovery Controller (ARC) Developer Guide*.

**To start a zonal shift**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. On the navigation pane, under **Load Balancing**, choose **Load Balancers**.

1. Select the Network Load Balancer.

1. On the **Integrations** tab, expand **Amazon Application Recovery Controller (ARC)** and choose **Start zonal shift**.

1. Select the Availability Zone that you want to move traffic away from.

1. Choose or enter an expiration for the zonal shift. A zonal shift can initially be set from 1 minute up to three days (72 hours).

   All zonal shifts are temporary. You must set an expiration, but you can update active shifts later to set a new expiration.

1. Enter a comment. You can update the zonal shift later to edit the comment.

1. Select the check box to acknowledge that starting a zonal shift reduces capacity for your application by shifting traffic away from the Availability Zone.

1. Choose **Confirm**.

------
#### [ AWS CLI ]

**To start a zonal shift**
Use the Amazon Application Recovery Controller (ARC) [start-zonal-shift](https://docs.aws.amazon.com/cli/latest/reference/arc-zonal-shift/start-zonal-shift.html) command.

```
aws arc-zonal-shift start-zonal-shift \
    --resource-identifier {{load-balancer-arn}} \
    --away-from {{use2-az2}} \
    --expires-in {{2h}} \
    --comment "{{zonal shift due to scheduled maintenance}}"
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Elastic Load Balancing. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticloadbalancing` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
