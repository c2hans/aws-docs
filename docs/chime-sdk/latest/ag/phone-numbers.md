---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/phone-numbers.html
---

# Managing phone numbers in Amazon Chime SDK
<a name="phone-numbers"></a>

The topics in this section explain how to manage phone numbers for use with the Amazon Chime SDK.

You can obtain numbers in the following ways:
+ Provision numbers by ordering them from a pool of numbers provided by the Amazon Chime SDK. You can only do this in countries that don't have identification requirements.
+ Port existing numbers over from another carrier into the Amazon Chime SDK.
+ Order international phone numbers.

The provisioning and porting processes add the numbers to your inventory. You then use the numbers with Amazon Chime SDK Voice Connectors, Amazon Chime SDK Voice Connector groups or Amazon Chime SDK SIP media applications.

**Note**
You can port toll-free numbers for use with Amazon Chime SDK Voice Connectors, and with Amazon Chime SIP media applications. Amazon Chime Business Calling doesn't support toll-free numbers. For more information, see [Porting existing phone numbers](porting.md), later in this guide.

To use a phone number with an Amazon Chime SDK Voice Connector or Amazon Chime SDK Voice Connector group you use the Amazon Chime SDK console to assign the number. For information about Voice Connectors, see [Managing Amazon Chime SDK Voice Connectors](voice-connectors.md). For information about assigning numbers to Voice Connectors, see [Assigning numbers to a Voice Connector or Voice Connector group](assign-to-cvc.md).

**Note**
You also use Voice Connectors to enable emergency calling from Amazon Chime. However, the Amazon Chime SDK doesn’t offer emergency calling services outside of the United States. To modify the emergency calling services that the Amazon Chime SDK provides for the United States, you can obtain an emergency call routing number from a third-party emergency service provider, give that number to the Amazon Chime SDK, then assign the number to an Amazon Chime SDK Voice Connector. For more information, see [Setting up third-party emergency routing numbers](chime-voice-connector-emergency-calling.md).

To use a phone number with a SIP media application, you add it to the SIP rule associated with the application. For more information about SIP media applications, see [Using SIP media applications](use-sip-apps.md). For more information about adding phone numbers to SIP rules, see [Creating a SIP rule](create-sip-rule.md).

**Note**
Amazon Chime SDK Voice Connectors, and Amazon Chime SDK SIP media applications have bandwidth requirements. For more information, see [Bandwidth requirements](network-config.md#bandwidth).

**Topics**
+ [Provisioning phone numbers](provision-phone.md)
+ [Requesting international phone numbers](request-intl-numbers.md)
+ [Porting existing phone numbers](porting.md)
+ [Managing phone number inventory](phone-inventory.md)
+ [Deleting phone numbers](delete-phone.md)
+ [Restoring deleted phone numbers](restore-phone.md)
+ [Optimize your outbound calling reputation](optimize-outbound-calling.md)
+ [STIR/SHAKEN for Amazon Chime SDK](stir-shaken.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
