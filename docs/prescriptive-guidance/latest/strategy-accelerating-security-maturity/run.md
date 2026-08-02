---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-accelerating-security-maturity/run.html
---

# Run stage: Optimizing your cloud security operations
<a name="run"></a>

![Icon of running person](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-accelerating-security-maturity/images/guide-img/2162f372-44e6-4f4b-80cc-427f9fca7a33/images/2ff8f77d-b39b-42d7-8186-2993825db1fd.png)

After you implement a baseline in the walk stage, your organization progresses to the run stage. This stage is focused on demonstrating the cybersecurity capabilities that are available in the cloud, many of which are not possible or are very difficult to implement with on-premises solutions. This stage brings together different security components and automates processes. Automations free up your resources so that they can focus on high-value work.

The following is the only phase in the run stage:
+ **Optimize** – How do I improve this process and add automation?

## Optimize
<a name="optimize"></a>

In the optimize phase, you automate your security operations. Like the crawl and walk stages, you can use AWS Security Hub CSPM during the run stage to achieve automation and iteration. The following image shows how Security Hub CSPM can trigger a custom [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) rule that defines automatic actions to take against specific findings and insights. For more information, see [Automations](https://docs.aws.amazon.com/securityhub/latest/userguide/automations.html) in the Security Hub CSPM documentation.

![Using AWS Security Hub and Amazon EventBridge to automate cloud security operations](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-accelerating-security-maturity/images/guide-img/2162f372-44e6-4f4b-80cc-427f9fca7a33/images/9f1e46b5-7f0d-4ec0-83a2-f0c66a668f86.png)

By using Security Hub CSPM as a central automation hub, you can also forward activities to [Splunk](https://www.splunk.com). Splunk can then detect the ones that are anomalous and trigger corresponding actions in EventBridge. This helps you automate repetitive tasks and provides more time for skilled team members to focus on higher-value activities. You can also use [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) to collect logs, take forensic snapshots, quarantine compromised servers, and replace them with a golden image. Additionally, you can use an [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) function that uses [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html) to remediate vulnerabilities across the environment and uses an [Amazon Simple Queue Service (Amazon SQS)](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html) function to validate the security of the systems. By taking this approach, it's possible to quickly contain and remediate security incidents with minimal impact to normal business operations.

The following is an example of repeated automated actions, as shown in the previous image:

1. Use Splunk to detect questionable activity.

1. Use Step Functions to collect logs, revoke access, quarantine, and take forensic snapshots.

1. Use an EventBridge rule to start a Lambda function that quarantines, takes forensic snapshots, and replaces compromised servers with a golden image.

1. Start a Lambda function that uses Systems Manager to remediate and apply patches throughout the rest of the environment.

1. Start an Amazon SQS message that uses the [Rapid7](https://www.rapid7.com/) scanner to scan and validate whether the AWS resource is secure.

For more information, see [How to automate incident response in the AWS Cloud for EC2 instances](https://aws.amazon.com/blogs/security/how-to-automate-incident-response-in-aws-cloud-for-ec2-instances/) in the AWS Security Blog.
