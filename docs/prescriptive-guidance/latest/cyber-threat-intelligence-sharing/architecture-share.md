---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/cyber-threat-intelligence-sharing/architecture-share.html
---

# Sharing CTI
<a name="architecture-share"></a>

The community that you send cyber threat intelligence (CTI) to is usually the same one that you receive CTI from. However, you can choose to share to more. For example, you might choose to share with government or regulatory organizations that you trust, such as your national cybersecurity center or Information Sharing and Analysis Centers (ISACs). The goal is to rapidly propagate and implement CTI by pooling findings from multiple organizations. Your threat intelligence platform manages the API integrations for sharing with multiple feeds.

Sending CTI to the trust community happens at the same time as implementing preventative and detective controls. You use logs to help identify security events. Then, you centralize events and findings so that you can quickly get an overview of the security posture of your AWS accounts. Then, your security teams, such as your cyber analysts, can identify any information that might be valuable. Because you already have findings in AWS Security Hub CSPM, you can convert these findings into the format used by the threat feed, such as JSON or STIX. Then, you send the CTI to the feed provider. Their threat intelligence platforms ingest, anonymize, and validate the CTI that you provide. Then, your CTI is shared with an even wider community.

The following image shows how you can use AWS services to generate CTI and then share it with your trust community, including cyber authorities and other community members.

![Workflow for generating CTI and sharing it with your trust community.](https://docs.aws.amazon.com/prescriptive-guidance/latest/cyber-threat-intelligence-sharing/images/guide-img/65270b8a-43a4-49d2-8123-9467febf488a/images/110864b9-ec92-4376-b14b-ab46d1af66f6.png)

This diagram shows the following workflow:

1. Findings are created in AWS Security Hub CSPM.

1. An AWS Lambda function retrieves the findings from Security Hub CSPM and converts them into a sharable format, such as JSON or STIX.

1. The Lambda function stores the findings in an Amazon DynamoDB table.

1. The third-party threat intelligence platform, which is running on Amazon Elastic Compute Cloud (Amazon EC2) or Amazon Elastic Container Service (Amazon ECS), retrieves the findings from the DynamoDB table.

1. A cyber analyst reviews the CTI in the threat intelligence platform.

1. The threat intelligence platform publishes the CTI to the trust community, which consists of other CTI producers and consumers.
