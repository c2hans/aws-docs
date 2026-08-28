---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/outbound-call-restrictions.html
---

# Outbound calling restrictions
<a name="outbound-call-restrictions"></a>

## China
<a name="china-restrictions"></a>

Chinese carriers are increasingly blocking international routes into China. The Amazon Chime SDK continues to support our existing customers, but all customers approved to call China must meet the following conditions:

### Eligibility criteria
<a name="eligibility-china"></a>

**Unsupported use cases**
+ Short duration calls and alerting of less than 15 seconds.
+ High volume of calls, especially over a short period of time, using the same outbound caller ID (more than 5 calls per minute).
+ Any form of cold calling.
+ Any calls to invalid phone numbers. All numbers called must be validated as accurate.
+ Repeated calls using the same FROM and/or TO numbers.
+ Attempts to call China from any number that has not been pre-approved.

**Supported use cases**
+ Direct calls to known business entities, such as a hotel or IT support function.
+ Calling users who attempt to engage with your business, such as university placement schemes or product purchases.

### Data required for setup
<a name="required-data-china"></a>

Follow these steps to obtain permission to call Chinese telephone numbers (\+86):
+ Provide an exact and complete list of phone numbers used to call China.
  + The number must be a DID provided by the Amazon Chime SDK. No other number is acceptable.
  + The number cannot be a DID provided by Hong Kong, Macau, Taiwan, China, or Singapore.
**Note**
The above list may change at any time.
+ For each number, you must record an announcement that identifies the name of your business so that anyone calling the number will hear the recording and know what company is placing the call.
+ You must provide AWS with a detailed description of your use case for calling China, and you must confirm that you meet the eligibility criteria described in this topic.

### Consequences of violating the criteria
<a name="consequences-china"></a>

The Amazon Chime SDK has a zero-tolerance policy for calling into China. Amazon will suspend your Amazon Chime SDK account if you use the service for any of the restricted use cases listed above. Your Amazon Chime SDK administrators must communicate this policy to other members of your organization so that they are also aware of these restrictions. Ignorance of the rules is not an acceptable reason for a breach.

### Service assurance
<a name="service-assurance-china"></a>

If Chinese carriers block major international routes without prior warning and impact the ability to call China, the exclusions in the [ Amazon Chime SDK Service Level Agreement](https://aws.amazon.com/chime/chime-sdk/sla/) take effect.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
