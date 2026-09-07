---
source_url: https://docs.aws.amazon.com/solutions/latest/scalable-analytics-using-apache-druid-on-aws/problem-deployment-fails-due-to-cloudformation-failure-signals.html
---

# Problem: Deployment fails due to CloudFormation FAILURE signals
<a name="problem-deployment-fails-due-to-cloudformation-failure-signals"></a>

When deploying the guidance, the deployment may fail due to CloudFormation FAILURE signals.

 **Screenshot of guidance deployment error message.**

![image8](https://docs.aws.amazon.com/solutions/latest/scalable-analytics-using-apache-druid-on-aws/images/image8.png)

## Resolution
<a name="resolution-1"></a>

The issue arises from the fact that the corresponding Druid process is unable to transition into service.

To identify the underlying cause:

1. In the primary account, navigate to the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/).

1. Choose the log group named `/aws/solutions/druid/<cluster name>`. The provided screenshot displays the log group for the example cluster **dev298**.

    **Screenshot of CloudWatch Log groups.**
![image9](https://docs.aws.amazon.com/solutions/latest/scalable-analytics-using-apache-druid-on-aws/images/image9.png)

1. Select the log stream by searching for the instance ID found in the CloudFormation console.

    **Screenshot of CloudWatch Log streams.**
![image10](https://docs.aws.amazon.com/solutions/latest/scalable-analytics-using-apache-druid-on-aws/images/image10.png)

1. Inspect the relevant logs to determine the reason the instance does not start correctly.
