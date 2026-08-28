---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/sdk-use-pstn-service.html
---

# Using the Amazon Chime SDK PSTN audio service
<a name="sdk-use-pstn-service"></a>

**Note**
This section describes the Chime SDK PSTN audio service, which was previously referred to as “SIP Media Applications (SMA)” in prior versions of the documentation and some blog posts. Going forward, when we refer to “SIP Media Applications,” we are referring to the configuration items in the Amazon Chime SDK console and the AWS SDK that are associated with the PSTN audio service.

This section explains how to use the Amazon Chime SDK Public Switched Telephone Network (PSTN) Audio service. With the PSTN audio service, developers can build custom telephony applications using the agility and operational simplicity of a serverless AWS Lambda function.

Your AWS Lambda functions control the behavior of phone calls, such as playing voice prompts, collecting digits, recording calls, routing calls to the PSTN and Session Initiation Protocol (SIP) devices using the Amazon Chime SDK Voice Connector. The following topics provide an overview and architectural information about the PSTN audio service, including how to build AWS Lambda functions to control calls.

**Note**
The topics in this section assume that you understand the AWS Lambda service. For more information about AWS Lambda, see [Getting started with AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html). Also, to use this section of the Amazon Chime SDK successfully, an Amazon Chime SDK administrator must create at least one SIP rule and one SIP media application. For more information about completing those tasks, see [Managing SIP media applications](https://docs.aws.amazon.com/chime-sdk/latest/ag/manage-sip-applications.html) in the *Amazon Chime SDK Administrator Guide*.

**Topics**
+ [Migrating to the Amazon Chime SDK voice namespace](voice-namespace-migration.md)
+ [Understanding phone numbers, SIP rules, SIP media applications, and AWS Lambda functions for Amazon Chime SDK PSTN audio](using-lambda.md)
+ [Understanding the Amazon Chime SDK PSTN audio service programming model](pstn-model.md)
+ [Routing calls and events to AWS Lambda functions for Amazon Chime SDK PSTN audio](route-calls-events.md)
+ [Routing calls to AWS Lambda functions for Amazon Chime SDK PSTN audio (AWS CLI)](route-calls-events-cli.md)
+ [Learn about using Amazon Chime SDK PSTN audio service call legs](call-architecture.md)
+ [Understanding call flow for Amazon Chime SDK PSTN audio](call-flow.md)
+ [Building AWS Lambda functions for the Amazon Chime SDK PSTN audio service](writing-lambdas.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
