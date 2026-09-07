---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/cyber-threat-intelligence-sharing/architecture-automate-controls.html
---

# Automating security controls
<a name="architecture-automate-controls"></a>

After cyber threat intelligence (CTI) has been ingested in to the threat intelligence platform, you can automate the process of making configuration changes in response to the data. Threat intelligence platforms help you manage cyber threat intelligence and observe your environment. They provide capability to structure, store, organize and visualize technical and non-technical information about cyber threats. They can help you build a threat picture and combine a range of intelligence sources to profile and track threats, such as [advanced persistent threats (APTs)](https://en.wikipedia.org/wiki/Advanced_persistent_threat).

Automation can reduce the time between receiving threat intelligence and implementing configuration changes in the environment. Not all CTI responses can be automated. However, automating as many responses as possible helps your security team prioritize and assess the remaining CTI in a timelier fashion. Each organization must determine which types of CTI responses can be automated and which require manual analysis. Make this decision based on organizational context, such as risks, assets, and resources. For example, some organizations might choose to automate blocks for known bad domains or IP addresses, but they might require analyst investigation before blocking internal IP addresses.

This section provides examples of how to set up automated CTI responses in [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html), [AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html), and [Amazon Route 53 Resolver DNS Firewall](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall.html). You can implement these examples independently of each other. Let your organization's security requirements and needs guide your decisions. You can automate configuration changes for AWS services through an [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) workflow (also called a *state machine*). When an [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) function finishes converting the CTI to JSON format, it triggers an [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) event that starts the Step Functions workflow.

The following diagram shows a sample architecture. Step Functions workflows automatically update the threat list in GuardDuty, the domain list in Route 53 Resolver DNS Firewall, and the rule group in Network Firewall.

![An EventBridge event initiates Step Functions workflows that update the AWS security services.](https://docs.aws.amazon.com/prescriptive-guidance/latest/cyber-threat-intelligence-sharing/images/guide-img/65270b8a-43a4-49d2-8123-9467febf488a/images/8698999b-6963-4a69-abe9-29de36c9eefb.png)

The figure shows the following workflow:

1. An EventBridge event is initiated on a regular schedule. This event starts an AWS Lambda function.

1. The Lambda function retrieves CTI data from the external threat feed.

1. The Lambda function writes the retrieved CTI data to an Amazon DynamoDB table.

1. Writing data to the DynamoDB table initiates a change data capture stream event that starts a Lambda function.

1. If changes occurred, a Lambda function initiates a new event in EventBridge. If no changes occurred, then the workflow completes.

1. If the CTI relates to IP address records, then EventBridge starts an Step Functions workflow that automatically updates the threat list in Amazon GuardDuty. For more information, see [Amazon GuardDuty](#architecture-automate-controls-guardduty) in this section.

1. If the CTI relates to IP address or domain records, then EventBridge starts a Step Functions workflow that automatically updates the rule group in AWS Network Firewall. For more information, see [AWS Network Firewall](#architecture-automate-controls-network-firewall) in this section.

1. If the CTI relates to domain records, then EventBridge starts a Step Functions workflow that automatically updates the domain list in Amazon Route 53 Resolver DNS Firewall. For more information, see [Amazon Route 53 Resolver DNS Firewall](#architecture-automate-controls-route53) in this section.

## Amazon GuardDuty
<a name="architecture-automate-controls-guardduty"></a>

[Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html) is a threat detection service that continuously monitors your AWS accounts and workloads for unauthorized activity and delivers detailed security findings for visibility and remediation. By automatically updating the GuardDuty threat list from CTI feeds, you can gain insights into threats that might be accessing your workloads. GuardDuty improves your detective control capabilities.

**Tip**
GuardDuty natively integrates with [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html). Security Hub CSPM provides a comprehensive view of your security state in AWS and helps you to check your environment against security industry standards and best practices. When you integrate GuardDuty with Security Hub CSPM, your GuardDuty findings are automatically sent to Security Hub CSPM. Security Hub CSPM can then include those findings in its analysis of your security posture. For more information, see [Integrating with AWS Security Hub CSPM](https://docs.aws.amazon.com/guardduty/latest/ug/securityhub-integration.html) in the GuardDuty documentation. In Security Hub CSPM, you can use [automations](https://docs.aws.amazon.com/securityhub/latest/userguide/automations.html) to improve your detective and responsive security control capabilities.

The following image shows how a Step Functions workflow can use CTI from a threat feed to update the threat list in GuardDuty. When a Lambda function finishes converting the CTI to JSON format, it triggers an EventBridge event that starts the workflow.

![A Step Functions workflow uses CTI to automatically update the threat list in GuardDuty.](https://docs.aws.amazon.com/prescriptive-guidance/latest/cyber-threat-intelligence-sharing/images/guide-img/65270b8a-43a4-49d2-8123-9467febf488a/images/73305c6d-0f11-4953-880b-32d124e8ac3d.png)

The diagram shows the following steps:

1. If the CTI relates to IP address records, then EventBridge starts the Step Functions workflow.

1. A Lambda function retrieves the threat list, which is stored as an object in an Amazon Simple Storage Service (Amazon S3) bucket.

1. A Lambda function updates the threat list with the IP address changes in the CTI. It saves the threat list as a new version of the object in the original Amazon S3 bucket. The object name is unchanged.

1. A Lambda function uses API calls to retrieve the GuardDuty detector ID and threat intel set ID. It uses these IDs to update GuardDuty to refer to the new version of the threat list.
**Note**
You can't retrieve a specific GuardDuty detector and IP address list because they are retrieved as an array. Therefore, we recommend that you have only one of each in the target AWS account. If you more that one, then you need to make sure that the correct data is extracted in the final Lambda function in this workflow.

1. The Step Functions workflow ends.

## Amazon Route 53 Resolver DNS Firewall
<a name="architecture-automate-controls-route53"></a>

[Amazon Route 53 Resolver DNS Firewall](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall.html) helps you filter and regulate outbound DNS traffic for your virtual private cloud (VPC). In DNS Firewall, you create a rule group that blocks the domain addresses that are identified by the CTI feed. You configure a Step Functions workflow to automatically add and remove domains from this rule group.

The following image shows how a Step Functions workflow can use CTI from a threat feed to update the domain list in Amazon Route 53 Resolver DNS Firewall. When a Lambda function finishes converting the CTI to JSON format, it triggers an EventBridge event that starts the workflow.

![A Step Functions workflow uses CTI to automatically update the domain list in DNS Firewall.](https://docs.aws.amazon.com/prescriptive-guidance/latest/cyber-threat-intelligence-sharing/images/guide-img/65270b8a-43a4-49d2-8123-9467febf488a/images/d8864bac-7b5a-49c5-873e-40c09833155d.png)

The diagram shows the following steps:

1. If the CTI relates to domain records, then EventBridge starts the Step Functions workflow.

1. A Lambda function retrieves the domain list data for the firewall. For more information about creating this Lambda function, see [get\_firewall\_domain\_list](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/get_firewall_domain_list.html) in the AWS SDK for Python (Boto3) documentation.

1. A Lambda function uses the CTI and the retrieved data to update the domain list. For more information about creating this Lambda function, see [update\_firewall\_domains](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53resolver/client/update_firewall_domains.html) in the Boto3 documentation. The Lambda function can add, remove, or replace domains.

1. The Step Functions workflow ends.

We recommend the following best practices:
+ We recommend that you use both Route 53 Resolver DNS Firewall and AWS Network Firewall. DNS Firewall filters DNS traffic, and Network Firewall filters all other traffic.
+ We recommend that you enable logging for DNS Firewall. You can create detective controls that monitor the log data and alert you if a restricted domain tries to send traffic through the firewall. For more information, see [Monitoring Route 53 Resolver DNS Firewall rule groups with Amazon CloudWatch](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/monitoring-resolver-dns-firewall-with-cloudwatch.html).

## AWS Network Firewall
<a name="architecture-automate-controls-network-firewall"></a>

[AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html) is a stateful, managed, network firewall and intrusion detection and prevention service for VPCs in the AWS Cloud. It filters traffic at the perimeter of your VPC, helping you block threats. Using threat intelligence feeds to automatically update Network Firewall rule groups can help protect your organization's cloud workloads and data from malicious actors.

The following image shows how a Step Functions workflow can use CTI from a threat feed to update one or more rule groups in Network Firewall. When a Lambda function finishes converting the CTI to JSON format, it triggers an EventBridge event that starts the workflow.

![A Step Functions workflow uses CTI to automatically update a rule group in Network Firewall.](https://docs.aws.amazon.com/prescriptive-guidance/latest/cyber-threat-intelligence-sharing/images/guide-img/65270b8a-43a4-49d2-8123-9467febf488a/images/150718fa-df05-4883-91c7-5bde36d1aadc.png)

The diagram shows the following steps:

1. If the CTI relates to IP address or domain records, then EventBridge starts a Step Functions workflow that automatically updates the rule group in Network Firewall.

1. A Lambda function retrieves the rule group data from Network Firewall.

1. A Lambda function uses the CTI to update the rule group. It adds or removes IP addresses or domains.

1. The Step Functions workflow ends.

We recommend the following best practices:
+ Network Firewall can have multiple rule groups. Create separate rule groups for domains and IP addresses.
+ We recommend that you enable logging for Network Firewall. You can create detective controls that monitor the log data and alert you if a restricted domain or IP address tries to send traffic through the firewall. For more information, see [Logging network traffic from AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-logging.html).
+ We recommend that you use both Route 53 Resolver DNS Firewall and AWS Network Firewall. DNS Firewall filters DNS traffic, and Network Firewall filters all other traffic.
