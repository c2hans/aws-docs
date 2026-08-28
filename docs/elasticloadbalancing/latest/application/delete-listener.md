---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/application/delete-listener.html
---

# Delete a listener for your Application Load Balancer
<a name="delete-listener"></a>

Before you delete a listener, consider the impact on your application:
+ The load balancer immediately stops accepting new connections on the listener port.
+ Active connections are closed. Any requests in progress when the listener is deleted will likely fail.

------
#### [ Console ]

**To delete a listener**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. On the navigation pane, choose **Load Balancers**.

1. Select the load balancer.

1. On the **Listeners and rules** tab, select the check box for the listener and choose **Manage listener**, **Delete listener**.

1. When prompted for confirmation, enter **confirm** and then choose **Delete**.

------
#### [ AWS CLI ]

**To delete a listener**
Use the [delete-listener](https://docs.aws.amazon.com/cli/latest/reference/elbv2/delete-listener.html) command.

```
aws elbv2 delete-listener \
    --listener-arn {{listener-arn}}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Elastic Load Balancing. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticloadbalancing` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
