---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-aws-carrier-services-strategy-guide/next-steps.html
---

# Next steps

## 1. Assess Your Communication Needs
<a name="1.-assess-your-communication-needs.148ddb58-7233-5e64-a5ca-bd42aa3b4546"></a>
+ Identify your messaging use cases and volume requirements
+ Determine appropriate service type (Short Code, 10DLC, or Connect numbers)
+ Establish project timeline accounting for carrier approval processes

## 2. Prepare Your Application
<a name="2.-prepare-your-application.79cbea4e-0a2c-5803-bfea-9efa579eff43"></a>
+ Gather required documentation:
  + Agency legal name and Federal Employer Identification Number (FEIN)/Tax ID
  + Physical address and website
  + Authorized contact information
  + Use case description and message samples
+ Review the CTIA Short Code Monitoring Handbook
+ Develop compliant opt-in/opt-out processes

## 3. Set up your environment (Sandbox Testing)
<a name="3.-set-up-your-environment--sandbox-testing-.feafa706-1e74-5f2c-897d-f437fd28a678"></a>

1. Open the[**AWS End User Messaging SMS**](https://console.aws.amazon.com/sms-voice/) console

1. **Create a Phone Pool** — go to Overview → Quick start → Create pool; request a  simulator number for testing

1. **Create a Configuration Set** — set up CloudWatch/Firehose/[Amazon Simple Notification Service (Amazon SNS)](https://docs.aws.amazon.com/sns/latest/dg/) for event tracking

1.  **Create a Protect Configuration** — set country-level allow/block/filter rules. Associate with your configuration set under Protect configuration associates

1. **Send a test message** — verify delivery in CloudWatch logs **Note**: AWS End User Messaging SMS is available in 32 AWS Regions. Verify your region supports SMS/MMS before proceeding.

## 4. Request production access
<a name="4.-request-production-access9999999999999999nbsp-.c70fd0a4-5a85-5261-a767-b0da9c2d4a42"></a>

1. [Open AWS Support ](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase)

1.  Select **Service limit increase** → AWS End User Messaging SMS

1.  Provide: website URL, message type (One-Time Password/OTP/Promotional/Transactional), destination countries, opt-in process description, and sample message

1. Submit and wait for approval (typically 24–48 hours)

## 5. Submit Your Number Request
<a name="5.-submit-your-number-request.93e13606-bea2-51ec-bcc5-795518d96f74"></a>

**For Short Codes:**

1. In the same AWS Support case from Step 4, provide Short Code-specific details: CTIA compliance documentation, expected message volume, and carrier preferences

1. Once AWS processes and approves, complete the **Short Code registration form** in the End User Messaging SMS console under Registrations

1. Submit for carrier review (8–12 weeks typical)

**For 10DLC:**

1. In the End User Messaging SMS console, go to **Registrations → Create registration**

1. Register your **brand/company** (1–2 business days)

1. Apply for **external brand vetting** (recommended for higher throughput; optional but increases approval likelihood)

1. Register your **10DLC campaign** (up to 4 weeks; can start while brand vetting is in progress)

1. **Request a 10DLC phone number** and associate with your campaign (up to 10 days)

**For Amazon Connect numbers:**

1. Navigate to **Amazon Connect** in the AWS Management Console

1. Select your instance

1.  Choose **Phone numbers → Claim a number**

1. Follow the guided process

## 6. Monitor and respond
<a name="6.-monitor-and-respond.6faf5145-6358-5468-873d-e5e5a80e599b"></a>
+ Check your AWS support case regularly for updates
+ Respond promptly to any requests for additional information
+ Prepare your technical implementation while awaiting approval

## 7. Implementation and Testing
<a name="7.-implementation-and-testing.79f89b04-8ea2-5c4f-9827-83a6a4eb4e26"></a>
+ Configure AWS services to use approved numbers
+ Test with real phone numbers after production approval; verify opt-out (STOP) responses work correctly
+ Implement monitoring and compliance tracking
+ Launch your communication program

## 8. Ongoing Management
<a name="8.-ongoing-management.dc38d862-3b52-51c5-aa82-13c799a82ad5"></a>
+ Monitor delivery and engagement metrics
+ Maintain opt-in/opt-out records
+ Review compliance quarterly
+ Plan for renewals (Short Codes typically require annual renewal)
