---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/update-idle-timeout.html
---

# Update the TCP idle timeout for your Gateway Load Balancer listener
<a name="update-idle-timeout"></a>

For each TCP request made through a Gateway Load Balancer, the state of that connection is tracked. If no data is sent through the connection by either the client or target for longer than the idle timeout, the connection is closed. The default idle timeout value for TCP flows is 350 seconds, but can be updated to any value between 60-6000 seconds.
+ If you set the idle timeout higher than 350 seconds, verify that your targets' ENI connection tracking idle timeout (`TcpEstablishedTimeout`) is equal to or greater than the Gateway Load Balancer idle timeout value. On Nitro V6\+ instances, the default connection tracking timeout is 350 seconds. A mismatch causes the target's network interface to silently drop connection state before the load balancer closes the connection. For more information, see [Best Practices for TCP Connection Management on EC2](https://aws.amazon.com/blogs/networking-and-content-delivery/best-practices-for-tcp-connection-management-on-ec2/).

**To update the TCP idle timeout using the console**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, under **Load Balancing**, choose **Load Balancers**.

1. Select the Gateway Load Balancer.

1. On the listeners tab choose **Actions**, **View listener details**.

1. On the listener details page, in the **Attributes** tab, select **Edit**.

1. On the **Edit listener attributes** page, in the **Listener attributes** section, enter a value for **TCP idle timeout**.

1. Choose **Save changes**

**To update the TCP idle timeout using the AWS CLI**
Use the [modify-listener-attributes](https://docs.aws.amazon.com/cli/latest/reference/elbv2/modify-listener-attributes.html) command with the `tcp.idle_timeout.seconds` attribute.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Elastic Load Balancing. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticloadbalancing` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
