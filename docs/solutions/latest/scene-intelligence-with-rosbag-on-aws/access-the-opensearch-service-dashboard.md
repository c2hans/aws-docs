---
source_url: https://docs.aws.amazon.com/solutions/latest/scene-intelligence-with-rosbag-on-aws/access-the-opensearch-service-dashboard.html
---

# Access the OpenSearch Service dashboard
<a name="access-the-opensearch-service-dashboard"></a>

The solution sends the metadata to OpenSearch Service. The solution provides a proxy to access the OpenSearch Service dashboard. To access the proxy securely, the solution uses AWS Systems Manager and tunnel to the instance and leverage port-forwarding to the dashboard.

**Note**
To use this feature, you must have the [AWS Systems Manager CLI extension](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-install-plugin.html) installed.

Complete the following instructions to access the OpenSearch Service dashboard.

1. Obtain the proxy instance name, either by using the AWS Management Console or the AWS CLI.
   + Using the AWS Management Console:\*

     1. Sign in to the [Amazon EC2 console](https://console.aws.amazon.com/ec2).

     1. Choose **Instances** from the navigation menu.

     1. Find and copy the instance name that starts with addf-aws-solutions.

    **Using the AWS CLI:**

   \+

   ```
   $ aws ec2 describe-instances \
    --filter "Name=tag:Name,Values=addf-aws-solutions-integration- opensearch-tunnel/OSTunnel" \
    --query "Reservations[].Instances[?State.Name == 'running'].InstanceId[]" \
    --output text
   ```

1. Establish a tunnel by using the AWS CLI. This solution defaults the port to `3333`.

   The following is an example where you replace {{<instance-name>}} with the instance name:

   ```
   $ aws ssm start-session --target <instance-name> \
    --document-name AWS-StartPortForwardingSession \
    --parameters '{"portNumber": ["3333"], "localPortNumber": ["3333"]}'
   ```

   The following is an example where the instance name is `i-123456789c45166cb`:

   ```
   $ aws ssm start-session --target i-123456789c45166cb \
    --document-name AWS-StartPortForwardingSession \
    --parameters '{"portNumber": ["3333"], "localPortNumber": ["3333"]}'
   ```

1. Use the following URL to open the dashboard: [http://localhost:3333/_dashboards](http://localhost:3333/_dashboards). This securely tunnels to the OpenSearch Service dashboard.

1. Add a new filter to discover your data. The partitions begin with `rosbag`, so we recommend selecting `rosbag-*` as a starting filter.

 **Example OpenSearch dashboard displaying indexed roasbag data.**

![filtered rosbag data](http://docs.aws.amazon.com/solutions/latest/scene-intelligence-with-rosbag-on-aws/images/filtered-rosbag-data.png)
