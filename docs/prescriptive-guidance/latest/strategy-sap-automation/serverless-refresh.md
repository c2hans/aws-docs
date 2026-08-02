---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-sap-automation/serverless-refresh.html
---

# Example: Automating SAP serverless refresh
<a name="serverless-refresh"></a>

Another example of automation for SAP on AWS is *SAP serverless refresh*. Many enterprises require regular refreshes of their SAP systems in order to support testing and production operations. The manual refresh process can be time-consuming, costly, and tedious for SAP administrators. As an alternative to the manual process, you can use an automation that consists of serverless AWS services that collectively perform the system refresh process for you. You can use this capability to refresh an SAP system's test data from another system. This solution currently supports SAP systems using the SAP HANA database management system. The following are the benefits of this automation:
+ Maintains the SAP system configuration
+ Increases productivity, agility, and innovation
+ Reduces downtime to several minutes
+ Reduces human resource involvement
+ Reduces the risk of human error
+ Reduces the refresh process from weeks to days

The following image and process describe how the automation for SAP serverless refreshes works:

1. A user starts a state machine in AWS Step Functions. For more information about state machines, see [States](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-states.html) (Step Functions documentation).

1. The state machine uses an Amazon Simple Notification Service (Amazon SNS) topic to notify the end user that the process has started.

1. A Lambda function starts Systems Manager documents that launch an Amazon Elastic Compute Cloud (Amazon EC2) instance from an Amazon Machine Image (AMI).

1. A Lambda function restores the backup by copying the backup files from an Amazon Simple Storage Service (Amazon S3) bucket to the EC2 instances that host the SAP database. The Lambda function also references Parameter Store, a capability of Systems Manager, to retrieve values of required variables, such as the target hostname, target IP address, and target SAP system identifier.

1. After the database restoration is complete, a Lambda function performs post-copy tasks, such as transport import and logical system name conversion.

1. The state machine uses the Amazon SNS topic to notify the end user that the refresh was successful.

1. The Lambda functions use an Amazon DynamoDB table to track the progress of each step in the state machine.

![Architecture diagram showing how you can use automation to perform a serverless refresh.](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-sap-automation/images/guide-img/029e7e61-9fe5-41b5-83f4-177d03384b91/images/02b1e527-edd7-44b6-bb0d-0c58c93a2290.png)
