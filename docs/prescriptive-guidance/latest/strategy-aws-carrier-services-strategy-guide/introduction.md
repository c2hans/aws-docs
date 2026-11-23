---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-aws-carrier-services-strategy-guide/introduction.html
---

# AWS Carrier Services: Implementing Short Codes, 10DLC, and Toll-Free  Solutions

*Olga Shepeleva and Don Vecchioni, Amazon Web Services*

## Welcome to the AWS Carrier-Dependent Service. This resource provides essential information for implementing carrier-dependent services such as AWS End User Messaging SMS (supporting Short Codes, 10-Digit Long Code (10DLC), Long Codes) and Amazon Connect (Caller ID 800 numbers).
<a name="welcome-to-the-aws-carrier-dependent-service.-this-resource-provides-essential-information-for-implementing-carrier-dependent-services-such-as-9999999999999999pinsmslong---supporting-short-codes--10-digit-long-code--10dlc---long-codes--and-9999999999999999connectportfoliolong---caller-id-800-numbers-..0e5ed419-bcdf-507c-9d1c-09a5a0fa9c15"></a>

Carrier-dependent services require coordination between AWS, telecommunications carriers, and regulatory bodies. This guide outlines the processes, timelines, and best practices to ensure successful implementation of these services for your agency's communication needs, including phone pools, configuration sets, and compliance controls.

Understanding the unique requirements and extended timelines associated with carrier approvals is critical for project planning. This guide will help you navigate the complexities of the telecommunications landscape while using AWS services to achieve your communication objectives.

### Overview
<a name="overview"></a>

In today's digital landscape, effective communication between organizations and their customers, users, or constituents is essential for delivering critical services, notifications, and information. AWS carrier-dependent services—including Short Codes, 10DLC, Long Codes, and [Amazon Connect](https://aws.amazon.com/products/connect/customer/?trk=25b81a8c-c9b1-4866-9ba5-f9cb1c5e792a&sc_channel=ps&ef_id=CjwKCAjw1vXTBhB-EiwAEKr_k4eSCLI5hTRbJYkhTQ0jd4l6WjCHBk839h4U28Por0vvoMB9PbwifBoCAesQAvD_BwE&gclid=CjwKCAjw1vXTBhB-EiwAEKr_k4eSCLI5hTRbJYkhTQ0jd4l6WjCHBk839h4U28Por0vvoMB9PbwifBoCAesQAvD_BwE) toll-free numbers—provide the infrastructure needed for these communications, but they operate within a complex telecommunications environment governed by carriers, regulatory bodies, and industry associations.

#### Why This Guide Is Necessary
<a name="why-this-guide-is-necessary.161d8d2e-7fff-5d06-87f8-b148e96fa02e"></a>

Implementing carrier-dependent services presents unique challenges that differ significantly from standard AWS service deployments:

1. **Multi-Party Approval Process**: Unlike most AWS services that can be provisioned immediately, carrier-dependent services require approval from external telecommunications carriers who maintain strict compliance standards.

1. **Extended Timelines**: The approval process can extend from several days to several months, requiring careful project planning and stakeholder management.

1. **Regulatory Complexity**: These services operate under telecommunications regulations (Federal Communications Commission (FCC), Telephone Consumer Protection Act (TCPA)) and industry guidelines (Cellular Telecommunications Industry Association (CTIA))

    that govern content, consent, and usage patterns.

1. **High Compliance Standards**: Carriers enforce strict requirements to protect consumers from spam, fraud, and unwanted messages, resulting in rigorous application reviews.

1. **Technical Limitations**: Each service type has specific throughput limits, content restrictions, and implementation requirements that must be understood before selection.

#### Intended Audience
<a name="intended-audience.a7db17f0-f342-56b9-8471-6799abcab626"></a>

This guide is designed for:
+ Technical architects and solution designers implementing carrier-dependent services
+ Program managers overseeing communication infrastructure projects
+ Compliance officers ensuring regulatory adherence
+ Federal agency leaders evaluating AWS messaging and voice solutions

This guide applies to federal agencies and any enterprise organization implementing carrier-dependent services at scale.

#### Industry Practices and Standards
<a name="industry-practices-and-standards.4a634e1a-4754-5caa-8937-c3908f551391"></a>

The telecommunications industry has established several key practices to maintain the integrity of messaging and voice channels:

1. **Explicit Consent**: The industry standard requires documented, clear opt-in processes before sending messages to consumers, with specific requirements for sensitive use cases.

1. **Sender Identification**: All communications must clearly identify the sending organization and provide opt-out mechanisms.

1. **Content Governance**: Carriers prohibit certain content categories and require pre-approval of messaging use cases to prevent misuse.

1. **Registration Systems**: The industry has implemented registration databases for business messaging to improve transparency and reduce spam.

1. **Throughput Management**: Carriers apply different throughput limits based on the type of number and registration status to prevent network abuse.

#### Benefits of Following This Guide
<a name="benefits-of-following-this-guide.ff780647-f1a4-5e69-bd2c-af74a3d797ab"></a>

Organizations that follow the guidelines and best practices outlined in this document will:

1. **Reduce Approval Delays**: Properly prepared applications with complete documentation experience fewer rejections and faster approvals.

1. **Improve Deliverability**: Compliant messaging practices result in higher delivery rates and fewer blocked messages.

1. **Build Customer Trust**: Properly identified, consent-based communications build trust in your organization's communications.

1. **Minimize Compliance Risk**: Following established guidelines reduces the risk of regulatory violations and potential penalties.

1. **Optimize Resource Allocation**: Understanding realistic timelines allows for better project planning and resource management.

1. **Enable Scalable Communications**: Properly implemented carrier-dependent services provide reliable, high-volume communication channels that can scale during emergencies or peak periods.

1. **Support Multi-Channel Strategy**: Integration of voice and messaging capabilities creates a cohesive citizen communication experience.

This guide serves as a roadmap through the complex landscape of carrier-dependent services, helping organizations and federal agencies navigate the approval process, implement compliant practices, and leverage AWS communication tools effectively to fulfill their mission of serving citizens. **Service Limitations Disclaimer**: Some AWS services aren't available in all AWS Regions. For Region availability, see the [Service endpoints and quotas page](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html) in the AWS documentation, and choose the link for the service.

### Attachments
<a name="attachments-59fe4557-e7c1-4103-aa65-72bfb33b10b9"></a>

To access additional content that is associated with this document, download and unzip the following file:

[attachment.zip](samples/attachment.zip)
