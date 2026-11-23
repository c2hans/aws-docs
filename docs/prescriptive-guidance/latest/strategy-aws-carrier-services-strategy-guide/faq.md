---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-aws-carrier-services-strategy-guide/faq.html
---

# FAQ

## General Questions
<a name="general-questions.16095a9a-6d5f-5eb5-91aa-9a328d2d7f13"></a>

### What is AWS End User Messaging SMS?
<a name="what-is-aws-end-user-messaging-sms-.b5e2c005-425e-52eb-93bb-d41feaf00f6a"></a>

AWS End User Messaging SMS is an application-to-person (A2P) messaging service that supports SMS, MMS, and Rich Communication Services (RCS) messaging to 200\+ countries. Short Codes, 10DLC, and Toll-Free numbers are origination identities you provision within AWS End User Messaging SMS.

### What's the difference between Short Codes, 10DLC, and Long Codes?
<a name="what-s-the-difference-between-short-codes--10dlc--and-long-codes-.03e270e4-e1f6-5bce-a6d3-b91278ff35b6"></a>

Types of SMS/MMS Numbers:

**Short Codes:**

5-6 digit numbers specifically designed for business-to-consumer messaging

**Benefits**:
+ Highest throughput (100\+ messages per second)
+ High deliverability rates
+ Pre-approved by carriers for high-volume sending
+ Easily memorable for customers **Example**: 87654 (five-digit short code)

**10DLC (10-Digit Long Codes):**

Standard 10-digit phone numbers registered for business messaging

**Benefits**:
+ Moderate throughput (1-5 messages per second depending on registration)
+ Faster approval process than Short Codes
+ Uses familiar phone number format
+ Cost-effective for medium-volume messaging **Example**: (202) 555-0123

**Long Codes** Standard 10-digit phone numbers primarily intended for person-to-person communications

**Benefits**:
+ No registration required for person-to-person use
+ Can be used for both voice and SMS
+ Suitable for low-volume, conversational messaging

   **Limitations**: Limited to 1 message per second throughput

  **Example**: (301) 555-8976
**Note**
Not recommended for application-to-person messaging in the US

### How long does the entire process take from request to implementation?
<a name="how-long-does-the-entire-process-take-from-request-to-implementation-.c3012360-98c4-5307-afc5-e5c5f3615a2b"></a>

 Timeline varies by service type:
+ Short Codes: 10-14 weeks (1-2 days AWS review \+ 8-12 weeks carrier approval \+ 1-2 weeks provisioning)
+ 10DLC: 2-4 weeks total (brand registration 1-2 days \+ vetting 1-2 days \+ campaign registration up to 4 weeks \+ number request up to 10 days)
+ Connect 800 Numbers: 1-3 days for new numbers; 2-4 weeks for porting existing numbers

### What happens if my application is rejected?
<a name="what-happens-if-my-application-is-rejected-.5b6f10a4-1d68-54b7-a903-e6e681875212"></a>

 AWS will provide the rejection reason from the carrier. You can revise and resubmit your application addressing the specific concerns. The approval timeline restarts with each submission.

### What is a phone pool?
<a name="what-is-a-phone-pool-.c7243e38-7d9e-55fe-aae6-2eb5f2876f43"></a>

A phone pool is a collection of phone numbers and sender IDs with shared settings. Phone pools enable easier management, automatic failover, and consistent configuration across your messaging channels.

### What are configuration sets?
<a name="what-are-configuration-sets-.72c65a17-93ea-5832-900d-d608d065e1fc"></a>

Configuration sets are rules applied when you send messages. They enable event tracking (delivery, bounce, complaint) via CloudWatch, Firehose, or [Amazon Simple Notification Service (Amazon SNS)](https://docs.aws.amazon.com/sns/latest/dg/) for compliance and analytics.

### What are protect configurations?
<a name="what-are-protect-configurations-.9ddab46f-3c2d-5642-b66b-ccc49a43c4c5"></a>

Protect configurations define country-level rules (Allow, Block, Filter) to ensure messages only reach compliant destinations and prevent high-risk markets.

## Technical Questions
<a name="technical-questions.709eb098-e16f-5238-9106-32e826eab22b"></a>

### Can we use the same Short Code for multiple use cases or programs?
<a name="can-we-use-the-same-short-code-for-multiple-use-cases-or-programs-.5d0a8278-73a3-5926-bf44-68733f854140"></a>

No. Each distinct use case requires a separate Short Code application and approval. Attempting to use one Short Code for multiple unapproved use cases risks carrier suspension.

### How many messages can we send per second with each service type?
<a name="how-many-messages-can-we-send-per-second-with-each-service-type-.7402f0d3-b4a1-5d7a-b4bd-b4202eaea7f1"></a>

Short Codes support 100\+ messages per second; 10DLC supports 1-5 messages per second depending on registration; Long Codes are limited to 1 message per second.

### Can we send both SMS and MMS messages?
<a name="can-we-send-both-sms-and-mms-messages-.ab093dee-dd28-52f7-ad71-fdd02a8e57b8"></a>

Yes, but MMS capabilities must be specifically requested during the application process and may have different approval requirements.

## Compliance Questions
<a name="compliance-questions.1a2e1190-550b-5607-9c5c-c2760670421f"></a>

### What are the most common reasons for application rejection?
<a name="what-are-the-most-common-reasons-for-application-rejection-.d4db2734-f217-5d4f-b677-ee2f30bf4e3f"></a>

Common rejection reasons include: incomplete/inconsistent business information, unclear opt-in processes, prohibited content categories, insufficient opt-out instructions, and vague use case descriptions.

### Are there specific requirements for government agencies?
<a name="are-there-specific-requirements-for-government-agencies-.6b3e55b6-6f15-5b39-b84d-417f708ec540"></a>

Government agencies must provide official documentation confirming their status and authorization for the requested services. Federal agencies may need to provide FEIN/Tax ID verification and official letterhead authorization.

### How do we stay compliant with changing regulations?
<a name="how-do-we-stay-compliant-with-changing-regulations-.869e5133-8d54-57ab-aabc-a3f76621fb36"></a>

Work closely with your AWS account team to stay informed about regulatory changes. Schedule quarterly compliance reviews and subscribe to AWS messaging and targeting blog for updates.
