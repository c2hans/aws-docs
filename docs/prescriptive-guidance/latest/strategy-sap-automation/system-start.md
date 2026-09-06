---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-sap-automation/system-start.html
---

# Example: Automating startup and shutdown of SAP systems
<a name="system-start"></a>

A typical productive SAP system consists of multiple Amazon EC2 instances that host several critical SAP components, such as SAP database servers, SAP application servers, SAP Central Services and SAP enqueue replication services. SAP customers also integrate their core SAP systems with other mission-critical solutions, such as archiving engines, tax management solutions, content servers, and job management systems. The startup and shutdown procedure for such a complex and tightly integrated SAP solution requires following a specific sequence of tasks.

You can automate startup and shutdown of SAP systems by using AWS services. This consistent and controlled process requires significantly less human intervention because it automates the monotonous, repetitive tasks and follows the sequence designed by SAP administrators. You can optionally add scheduling, notification, and alerts by using AWS services built for the cloud. In addition, this automation is capable of defining and handling dependencies between multiple SAP and non-SAP applications. For more information, see the blog post [Automate Start or Stop of Distributed SAP HANA systems using AWS Systems Manager](https://aws.amazon.com/blogs/awsforsap/automate-start-or-stop-of-distributed-sap-hana-systems-using-aws-systems-manager/). In addition, see the blog post [Start/Stop SAP systems with Slack using AWS Chatbot](https://aws.amazon.com/blogs/awsforsap/start-stop-sap-systems-with-slack-using-aws-chatbot/), which describes how to automate this process by using Slack and AWS services, such as AWS Chatbot, Lambda, Systems Manager, and CloudWatch. The following are the benefits of this automation:
+ Significantly reduces costs by reducing the need for manual operational efforts
+ Reduces the risk of human error and the need for expensive corrective activities

The following image and process describe how you can automate startup and shutdown of SAP systems:

1. A time-based event causes an Amazon EventBridge rule to start a Systems Manager document. For more information, see [Systems Manager documents](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-ssm-docs.html).

1. Systems Manager connects to the target EC2 instances and stops or starts the SAP application and its associated instances.

1. After the SAP system has stopped or started, another EventBridge rule responds to the change in the EC2 instance state and uses a Lambda function handler to notify the stakeholders of the change.

![Architecture diagram showing how you can automate startup or shutdown procedures for complex SAP systems.](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-sap-automation/images/guide-img/029e7e61-9fe5-41b5-83f4-177d03384b91/images/01641ff2-c243-4ea7-bff2-8b7df8a12684.png)
