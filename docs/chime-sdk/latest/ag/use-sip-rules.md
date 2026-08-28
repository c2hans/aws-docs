---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/use-sip-rules.html
---

# Managing SIP rules
<a name="use-sip-rules"></a>

A SIP rule associates your SIP media application with a phone number or a Request URI hostname. You can associate a SIP rule with more than one SIP media application. Each application then runs only that rule. For an overview of how SIP rules work with SIP media applications, refer to [Understanding SIP applications and rules](understand-sip-data-models.md) in the previous section.

**Note**
To create SIP rules, you need at least one DID or toll-free phone number with a **Product Type** set to **SIP Media Application Dial-In** in your Amazon Chime SDK inventory, or at least one Request URI hostname, the name assigned to an Amazon Chime SDK Voice Connector. For more information about phone numbers, see [Managing phone numbers](https://docs.aws.amazon.com/chime/latest/ag/phone-numbers.html). For more information about Request URI hostnames, follow the steps in the next section.

**Topics**
+ [Creating a SIP rule](create-sip-rule.md)
+ [Viewing a SIP rule](view-a-rule.md)
+ [Updating a SIP rule](update-sip-rule.md)
+ [Enabling a SIP rule](enable-sip-rule.md)
+ [Disabling a SIP rule](disable-sip-rule.md)
+ [Deleting a SIP rule](delete-sip-rule.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
