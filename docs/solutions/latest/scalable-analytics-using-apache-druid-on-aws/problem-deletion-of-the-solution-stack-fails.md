---
source_url: https://docs.aws.amazon.com/solutions/latest/scalable-analytics-using-apache-druid-on-aws/problem-deletion-of-the-solution-stack-fails.html
---

# Problem: Deletion of the guidance stack fails
<a name="problem-deletion-of-the-solution-stack-fails"></a>

When deleting the guidance stack, you may see the following error from AWS CloudFormation console.

 **Screenshot of delete guidance stack - error message.**

![troubleshooting1](http://docs.aws.amazon.com/solutions/latest/scalable-analytics-using-apache-druid-on-aws/images/troubleshooting1.png)

## Resolution
<a name="resolution"></a>

This issue may occur when subnet and security group dependencies are not properly deleted.

To delete the stack completely:

1. In the primary account, navigate to the [Amazon EC2 console](https://console.aws.amazon.com/ec2/). In the primary account, navigate to the [Amazon VPC Console](https://console.aws.amazon.com/vpc/)

1. Navigate to the Databases page and select the RDS databases belonging to the guidance.

1. Select **Actions**, and **Delete**.

1. Wait for the selected databases to stop.

1. Navigate to the [CloudFormation console](https://console.aws.amazon.com/cloudformation/), and delete the stack again.
