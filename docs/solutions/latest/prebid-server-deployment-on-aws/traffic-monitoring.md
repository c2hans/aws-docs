---
source_url: https://docs.aws.amazon.com/solutions/latest/prebid-server-deployment-on-aws/traffic-monitoring.html
---

# Traffic monitoring and troubleshooting
<a name="traffic-monitoring"></a>

This section provides traffic monitoring and troubleshooting instructions for deploying and using the solution. If this information don’t help address your issue, [Contact Support](contact-aws-support.md) provides instructions for opening an AWS Support case for this solution.

## Amazon CloudWatch alarms
<a name="amazon-cloudwatch-alarms"></a>

Amazon CloudWatch alarms monitor specific metrics in real time and proactively notify AWS Management Console users when predefined conditions are met. This solution has several CloudWatch alarms to help monitor its health and performance. In this section, each of the solution’s alarms are listed with details on what metrics they track and what can invoke the alarms.

These alarms are enabled automatically when the AWS CDK stack is deployed. There are no further actions required to review the alarms.

**Note**
There are no subscriptions to alarm notifications by default. Add your team’s email alias, paging address, or connection to an operational dashboard to be notified when an alarm changes state.

The following diagram shows the conceptual relationship between cloud resources created by this solution and pre-configured CloudWatch monitoring alarms.

 **Diagram showing overview of resources and their related CloudWatch alarms**

![aws solution for prebid server cloudwatch alarms](https://docs.aws.amazon.com/solutions/latest/prebid-server-deployment-on-aws/images/aws-solution-for-prebid-server-cloudwatch-alarms.png)

Network traffic flow is monitored by ALB, CloudFront, NAT gateway, and AWS WAF alarms. ECS alarms focus on problems related to creating new instances. EFS alarms monitor throughput problems. Glue alarms change state on failures of the periodic AWS Glue job. The customer is responsible for subscribing to these alarms to a notification mechanism, such as email or text message.
