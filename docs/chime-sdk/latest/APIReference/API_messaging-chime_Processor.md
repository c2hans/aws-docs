---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_Processor.html
---

# Processor
<a name="API_messaging-chime_Processor"></a>

The information about a processor in a channel flow.

## Contents
<a name="API_messaging-chime_Processor_Contents"></a>

 ** Configuration **   <a name="chimesdk-Type-messaging-chime_Processor-Configuration"></a>
The information about the type of processor and its identifier.
Type: [ProcessorConfiguration](API_messaging-chime_ProcessorConfiguration.md) object
Required: Yes

 ** ExecutionOrder **   <a name="chimesdk-Type-messaging-chime_Processor-ExecutionOrder"></a>
The sequence in which processors run. If you have multiple processors in a channel flow, message processing goes through each processor in the sequence. The value determines the sequence. At this point, we support only 1 processor within a flow.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 3.
Required: Yes

 ** FallbackAction **   <a name="chimesdk-Type-messaging-chime_Processor-FallbackAction"></a>
Determines whether to continue with message processing or stop it in cases where communication with a processor fails. If a processor has a fallback action of `ABORT` and communication with it fails, the processor sets the message status to `FAILED` and does not send the message to any recipients. Note that if the last processor in the channel flow sequence has a fallback action of `CONTINUE` and communication with the processor fails, then the message is considered processed and sent to recipients of the channel.
Type: String
Valid Values: `CONTINUE | ABORT`
Required: Yes

 ** Name **   <a name="chimesdk-Type-messaging-chime_Processor-Name"></a>
The name of the channel flow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\u0009\u000A\u000D\u0020-\u007E\u0085\u00A0-\uD7FF\uE000-\uFFFD\u10000-\u10FFFF]*`
Required: Yes

## See Also
<a name="API_messaging-chime_Processor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-messaging-2021-05-15/Processor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-messaging-2021-05-15/Processor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-messaging-2021-05-15/Processor)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
