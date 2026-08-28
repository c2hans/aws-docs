---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/set-up-emergency-calls.html
---

# Setting up emergency calling
<a name="set-up-emergency-calls"></a>

The Amazon Chime SDK provides two ways to set up emergency calls. Both methods only apply to calls made in or to the U.S.
+ **Validated addresses** – Enter and validate the physical address that calls may come from. If you choose this option, the validated address becomes available for all Amazon Chime SDK Voice Connectors and must be added to the SIP INVITE for emergency calls by following the instructions in [Using PIDF-LO in emergency calls](use-pidf-lo.md). The Amazon Chime SDK then routes calls to the nearest Public Safety Answering Point.
+ **Third-party routing** – Add emergency call routing numbers to an Amazon Chime SDK Voice Connector. If you choose this option, a third-party service of your choosing routes the calls, and you don't need to validate an address. You can use this method to make emergency calls from outside the U.S., but the calls must go to an endpoint in the U.S.

**Note**
If you don't use addresses or routing numbers, address validation may be carried out at the start of a 911 call to ensure it is routed to the appropriate Public Safety Answering Point (PSAP), meaning help may take longer to arrive.

The following sections explain how to use both options.

**Topics**
+ [Validating addresses for emergency calls](validate-emergency-addresses.md)
+ [Setting up third-party emergency routing numbers](chime-voice-connector-emergency-calling.md)
+ [Using PIDF-LO in emergency calls](use-pidf-lo.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
