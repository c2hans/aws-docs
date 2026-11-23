---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-aws-carrier-services-strategy-guide/best-practices.html
---

# Best practices

## Strategic Planning
<a name="strategic-planning.3148196f-0130-5c93-b282-0236f88ade46"></a>
+ **Timeline Management**: Build realistic project timelines that account for 8-12 week carrier approval processes for short codes
+ **Contingency Planning**: Include buffer time (1.5-2x estimated approval time) for potential revisions or rejections
+ **Service Selection**: Choose the appropriate service type based on use case, volume, and urgency:
  + Short Codes: High-volume, consistent messaging (8-12 week approval)
  + 10DLC: Medium-volume messaging with faster approval (2-4 weeks)
  + Toll-Free Numbers: Voice communications and lower-volume messaging

## AWS End User Messaging SMS Configuration
<a name="aws-end-user-messaging-sms-configuration.c1fb89bd-615a-511a-924b-25e6c2c83eeb"></a>
+ **Phone pool setup and management: **Create phone pools to group phone numbers and sender IDs with shared settings; enables easier failover and consistent configuration across messaging channels
+ **Configuration sets for event tracking**: Set up configuration sets with [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html), [Amazon Data Firehose,](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html) or [SNS](https://aws.amazon.com/sns/) event destinations to capture delivery, bounce, complaint, and opt-out events for compliance auditing
+ **Protect configurations for country compliance: **Define country-level rules (Allow, Block, Filter) to ensure messages only reach compliant destinations and prevent high-risk or restricted markets
+ **SMS simulator for testing**: Use the SMS simulator in [AWS End User Messaging](https://aws.amazon.com/end-user-messaging/) SMS console to test message flows without carrier costs; simulator numbers are free and don't require registration

## Application Preparation
<a name="application-preparation.fa67b2f8-22fe-5870-9798-ee86c0a8984b"></a>
+ **Documentation Accuracy**: Ensure all application information is complete, accurate, and consistent with official agency records
+ **Use Case Clarity**: Provide detailed descriptions of messaging purpose, content examples, and frequency
+ **Compliance Review**: Conduct internal review of use cases against CTIA guidelines before submission
+ **Single Point of Contact**: Designate one responsible individual to manage carrier communications

## Implementation Requirements
<a name="implementation-requirements.65826dfa-232e-589e-875b-f16995d0dbce"></a>
+ **Opt-In Mechanisms**: Implement and document clear consent processes with records retention
+ **Opt-Out Handling**: Include standard opt-out keywords (STOP, CANCEL) in all messages
+ **Message Content**: Ensure all messages include:
  + Agency/program identification
  + Clear purpose
  + Opt-out instructions
  + Support contact method
+ **Testing Protocol**: Develop comprehensive testing plan for all message flows before launch
+ **Character Limits**: SMS has 160-character limit per segment; longer messages incur additional charges
+ **Personalization**: Use customer data to personalize messages and improve recipient engagement
+ **Timing**: Send messages during business hours in recipient's timezone
+ **Avoid Spam Triggers**: Do not use excessive caps, special characters, or suspicious URLs

## Compliance Maintenance
<a name="compliance-maintenance.289d8252-0324-5ac4-826c-3c672cff43ca"></a>
+ **Regular Audits**: Conduct quarterly reviews of messaging practices against current regulations
+ **Content Monitoring**: Implement approval workflows for new message templates
+ **Consent Management**: Maintain auditable records of all opt-ins and opt-outs
+ **Feedback Loops**: Monitor delivery rates, opt-out rates, and engagement metrics
+ **Event Destination Setup**: Enable Amazon CloudWatch, Amazon Data Firehose, or Amazon Simple Notification Service to capture all SMS events
+ **Delivery Rate Monitoring**: Target >95% for transactional messages; investigate failures
+ **Cost Optimization**: Review usage reports monthly; identify high-cost destinations
+ **TCPA Compliance**: Respect [Do Not Call registry](https://consumer.ftc.gov/articles/national-do-not-call-registry-faqs); maintain consent records for 4\+ years
+ **General Data Protection Regulation (GDPR) Compliance**: For EU recipients, ensure GDPR-compliant consent and data handling
+ **Regional Restrictions**: Verify SMS support in target countries (AWS End User Messaging SMS supports 200\+ countries)

## Two-Way SMS Management
<a name="two-way-sms-management.1f495f89-cffc-5241-ac2d-c7622c0455ca"></a>
+ **Inbound Message Handling**: Configure [Amazon Simple Notification Service](https://docs.aws.amazon.com/sns/latest/dg/) topics or [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) functions to process incoming messages
+ **Auto-Responses**: Set up automatic responses for common keywords (HELP, INFO, STOP)
+ **Opt-Out Processing**: Automatically add STOP responses to opt-out lists within 24 hours
