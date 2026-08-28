---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-opentext-teamsite/cost-and-licenses.html
---

# Cost and licenses
<a name="cost-and-licenses"></a>

When assessing the costs and licenses required to migrate OpenText TeamSite, LiveSite, and Media Management workloads to the AWS Cloud, we assume that you have development, QA, and production environments to migrate. Your DevOps toolset should also include the following AWS services:
+ [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) and [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) for monitoring and logging
+ [Amazon Simple Storage Service Glacier ](https://docs.aws.amazon.com/amazonglacier/latest/dev/introduction.html)for archiving
+ [AWS CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html) for software deployment automation
+ [Amazon Simple Notification Service (Amazon SNS)](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) for application-to-application and application-toperson communication
+ [AWS Config ](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html)for recording and evaluating the configurations of your AWS resources

Your remaining environments should use the following AWS products and services:
+ Amazon Elastic Compute Cloud (Amazon EC2) instances for OpenText Media Management, TeamSite, and Livesite
+ Amazon Relational Database Service (Amazon RDS) instances for OpenText TeamSite and Media Management databases
+ [Application Load Balancers ](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html)to distribute requests across multiple OpenText LiveSite servers

For more information about costs, see [this estimate ](https://calculator.aws/?id=109c6f7bda67e38c02c99d31423b5a72f04561b6#/estimate) from AWS Pricing Calculator.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
