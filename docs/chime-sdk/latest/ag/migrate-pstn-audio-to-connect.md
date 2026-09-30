---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/migrate-pstn-audio-to-connect.html
---

# Migrating Amazon Chime SDK PSTN Audio to Amazon Connect
<a name="migrate-pstn-audio-to-connect"></a>

**Note**
Amazon Chime SDK SIP media applications will no longer be open to new customers starting October 29, 2026. If you would like to use SIP media applications, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [Amazon Chime SDK SIP media applications availability change](sip-applications-maintenance-mode.md).

The following topics explain how to migrate your Amazon Chime SDK PSTN Audio workloads to Amazon Connect.

## Overview
<a name="migrate-pstn-overview"></a>

This guide provides step-by-step instructions for migrating workloads from the Amazon Chime SDK PSTN Audio service to Amazon Connect. It shows how to map your existing SIP media application Lambda logic to Amazon Connect contact flows. It also identifies the equivalent Amazon Connect capability for each PSTN Audio feature.

Plan for about 20 hours of migration effort per application. The actual effort varies by complexity.

## Prerequisites
<a name="migrate-pstn-prerequisites"></a>

Before you start your migration, make sure that you have the following:
+ An AWS account with permissions to create Amazon Connect resources.
+ Access to your existing PSTN Audio configuration, including the following:
  + Your SIP media application Lambda function code
  + The phone numbers associated with your SIP rules
  + Any Amazon S3 buckets used for audio prompts or recordings
  + Any other AWS services used in your application
+ Familiarity with Amazon Connect basics. To learn more, review the [Amazon Connect Administrator Guide](https://docs.aws.amazon.com/connect/latest/adminguide/what-is-amazon-connect.html).

## Architecture comparison
<a name="migrate-pstn-architecture"></a>

The following table compares PSTN Audio concepts with their Amazon Connect equivalents.

**PSTN Audio and Amazon Connect architecture comparison**

| Concept | PSTN Audio | Amazon Connect |
| --- | --- | --- |
| Call flow logic | AWS Lambda function (code) | Contact flow (visual designer or JSON) |
| Call routing trigger | SIP rule to SIP media application | Phone number to contact flow |
| Audio prompts | Amazon S3 bucket (WAV files) | Prompts library (WAV or MP3), or text-to-speech |
| DTMF collection | `PlayAudioAndGetDigits` or `ReceiveDigits` action | **Get customer input** or **Store customer input** block |
| Call transfer | `CallAndBridge` action | **Transfer to phone number** block |
| Recording | `RecordAudio` action | **Set recording and analytics behavior** block |
| Text-to-speech | `Speak` or `SpeakAndGetDigits` action | **Play prompt** block with text-to-speech |
| External data lookup | Direct in Lambda | **Invoke AWS Lambda function** block |
| Outbound calling | `CreateSipMediaApplicationCall` API | Amazon Connect outbound campaigns, or **Call phone number** block |
| Call state and context | `TransactionAttributes` | Contact attributes |
| Call events | Lambda invocation events, such as `NEW_INBOUND_CALL` | Contact flow entry points and event flows |

## Step 1: Set up your Amazon Connect instance
<a name="migrate-pstn-step1-instance"></a>

Follow the Amazon Connect documentation to create and configure your instance. For instructions, see [Set up your instance](https://docs.aws.amazon.com/connect/latest/adminguide/tutorial1-set-up-your-instance.html).

When you configure your instance, set the following options:
+ For *Identity management*, choose your preferred directory.
+ For *Administrator*, create an admin user.
+ For *Telephony*, enable inbound and outbound calling.
+ For *Data storage*, configure Amazon S3 for recordings, logs, and exported reports.

After you create the instance, sign in to your Amazon Connect admin interface.

## Step 2: Port or claim phone numbers
<a name="migrate-pstn-step2-numbers"></a>

You have two options for getting phone numbers into Amazon Connect.

*Option A: Port your existing numbers*
+ Open a support case with AWS Support that references "Phone number port from Chime SDK to Connect".
+ Provide the phone numbers and your Amazon Connect instance ARN.
+ Allow two to four weeks for porting.

*Option B: Claim new numbers*

**To claim a new number**

1. In your Amazon Connect instance, choose **Channels**, then choose **Phone numbers**.

1. Choose **Claim a number**.

1. Select your country and number type, either toll-free or DID.

1. Associate the number with the contact flow that you create in the next step.

## Step 3: Convert your Lambda logic to a contact flow
<a name="migrate-pstn-step3-contact-flow"></a>

This step is the core of the migration. The following topics map each PSTN Audio action to its Amazon Connect equivalent, and explain how to bring external data lookups into your contact flow.

### Action-to-block mapping
<a name="migrate-pstn-action-mapping"></a>

The following sections show the Amazon Connect block that replaces each PSTN Audio action.

#### PlayAudio to Play prompt
<a name="map-playaudio"></a>

In PSTN Audio, you play an audio file with the `PlayAudio` action.

```
{
    "Type": "PlayAudio",
    "Parameters": {
        "CallId": "call-id-1",
        "AudioSource": {
            "Type": "S3",
            "BucketName": "my-bucket",
            "Key": "welcome.wav"
        }
    }
}
```

In Amazon Connect, do the following:

1. Upload your WAV file to the Amazon Connect **Prompts** library. Choose **Routing**, choose **Prompts**, then choose **Create new prompt**.

1. Add a **Play prompt** block to your contact flow.

1. Select the uploaded audio file, or use text-to-speech.

#### PlayAudioAndGetDigits to Get customer input
<a name="map-playaudioandgetdigits"></a>

In PSTN Audio, you play a prompt and collect digits with the `PlayAudioAndGetDigits` action.

```
{
    "Type": "PlayAudioAndGetDigits",
    "Parameters": {
        "CallId": "call-id-1",
        "AudioSource": {
            "Type": "S3",
            "BucketName": "my-bucket",
            "Key": "enter-pin.wav"
        },
        "FailureAudioSource": {
            "Type": "S3",
            "BucketName": "my-bucket",
            "Key": "invalid-entry.wav"
        },
        "MinNumberOfDigits": 4,
        "MaxNumberOfDigits": 4,
        "TerminatorDigits": ["#"],
        "InBetweenDigitsDurationInMilliseconds": 5000,
        "Repeat": 3,
        "RepeatDurationInMilliseconds": 10000
    }
}
```

In Amazon Connect, do the following:

1. Add a **Get customer input** block for menu-style DTMF, or a **Store customer input** block for free-form digits.

1. For **Prompt**, select your audio file or enter text-to-speech text.

1. For the DTMF options, set the digit timeout and the number of digits.

1. To handle errors, configure retry behavior with a **Loop** block.

Note the following key differences:
+ The **Get customer input** block is designed for menu choices, such as press 1 for one option and press 2 for another.
+ The **Store customer input** block is designed for free-form numeric entry, such as account numbers and PINs.
+ For retry logic, wrap the block in a **Loop** block instead of using the `Repeat` parameter.

#### Speak and SpeakAndGetDigits to Play prompt with text-to-speech
<a name="map-speak"></a>

In PSTN Audio, you convert text to speech with the `Speak` and `SpeakAndGetDigits` actions.

```
{
    "Type": "Speak",
    "Parameters": {
        "CallId": "call-id-1",
        "Text": "Your account balance is 500 dollars",
        "Engine": "neural",
        "LanguageCode": "en-US",
        "TextType": "text",
        "VoiceId": "Joanna"
    }
}
```

In Amazon Connect, do the following:

1. Add a **Play prompt** block.

1. Select **Text-to-speech or chat text**.

1. For **Text**, enter your message. The block supports SSML.

1. For **Interpret as**, choose text or SSML.

1. To set the voice, add a **Set voice** block before the **Play prompt** block, then choose a language and an Amazon Polly voice.

To insert dynamic values, use `$.Attributes.VariableName` or `$.External.VariableName`.

#### CallAndBridge to Transfer to phone number
<a name="map-callandbridge"></a>

In PSTN Audio, you transfer a call to a PSTN endpoint with the `CallAndBridge` action.

```
{
    "Type": "CallAndBridge",
    "Parameters": {
        "CallTimeoutSeconds": 30,
        "CallerIdNumber": "+15551234567",
        "Endpoints": [{
            "BridgeEndpointType": "PSTN",
            "Uri": "+15559876543"
        }]
    }
}
```

In Amazon Connect, do the following:

1. Add a **Transfer to phone number** block.

1. For **Phone number**, enter the destination number in E.164 format.

1. For **Caller ID**, select the outbound caller ID number.

1. For **Timeout**, set the transfer timeout.

Note the following key differences:
+ In Amazon Connect, the contact is complete when the transferred call ends. You do not manage hang-up separately.
+ For whisper announcements before connecting, use a **Set whisper flow** block.

#### RecordAudio to Set recording and analytics behavior
<a name="map-recordaudio"></a>

In PSTN Audio, you record a call with the `RecordAudio` action.

```
{
    "Type": "RecordAudio",
    "Parameters": {
        "CallId": "call-id-1",
        "DurationInSeconds": "10",
        "SilenceDurationInSeconds": 3,
        "RecordingTerminators": ["#"],
        "RecordingDestination": {
            "Type": "S3",
            "BucketName": "my-recordings",
            "Prefix": "calls/"
        }
    }
}
```

In Amazon Connect, do the following:

1. Add a **Set recording and analytics behavior** block.

1. For **Call recording**, choose agent and customer, or customer only.

Amazon Connect stores recordings in the Amazon S3 bucket that you configured for your instance. Note the following key differences:
+ Amazon Connect records the entire call, or from the point the block is triggered. It does not record fixed-duration segments.
+ For voicemail-style use cases, consider the Amazon Connect voicemail feature or a Lambda-based solution.
+ Recordings are automatically available in the Amazon Connect contact trace record.

#### ReceiveDigits to Store customer input
<a name="map-receivedigits"></a>

In PSTN Audio, you collect digits with the `ReceiveDigits` action.

```
{
    "Type": "ReceiveDigits",
    "Parameters": {
        "CallId": "call-id-1",
        "InputDigitsRegex": "^\\d{4}$",
        "InBetweenDigitsDurationInMilliseconds": 5000,
        "FlushDigitsDurationInMilliseconds": 10000
    }
}
```

In Amazon Connect, do the following:

1. Add a **Store customer input** block.

1. For **Prompt**, play audio or text-to-speech while you wait for input.

1. For **Maximum digits**, set your expected input length.

1. For sensitive data, such as credit cards or SSNs, select **Encrypt input**.

Amazon Connect stores the entered digits in `$.StoredCustomerInput`.

#### SendDigits to a limited equivalent
<a name="map-senddigits"></a>

In PSTN Audio, you send DTMF digits with the `SendDigits` action.

```
{
    "Type": "SendDigits",
    "Parameters": {
        "CallId": "call-id-1",
        "Digits": "1,,,,2"
    }
}
```

In Amazon Connect, the **Transfer to phone number** block includes a **Send digits** option. This option sends DTMF to dial extensions after connecting. For more complex DTMF scenarios, you might need architecture changes.

#### Hangup to Disconnect / hang up
<a name="map-hangup"></a>

In PSTN Audio, you end a call with the `Hangup` action.

```
{
    "Type": "Hangup",
    "Parameters": {
        "CallId": "call-id-1",
        "SipResponseCode": "0"
    }
}
```

In Amazon Connect, add a **Disconnect / hang up** block. This block terminates the contact.

#### Pause to Wait
<a name="map-pause"></a>

In PSTN Audio, you pause a call with the `Pause` action.

```
{
    "Type": "Pause",
    "Parameters": {
        "CallId": "call-id-1",
        "DurationInMilliseconds": "3000"
    }
}
```

In Amazon Connect, add a **Wait** block, then configure the timeout duration.

#### JoinChimeMeeting has no direct equivalent
<a name="map-joinchimemeeting"></a>

In PSTN Audio, you join a Amazon Chime SDK meeting from a call with the `JoinChimeMeeting` action.

```
{
    "Type": "JoinChimeMeeting",
    "Parameters": {
        "CallId": "call-id-1",
        "JoinToken": "meeting-join-token",
        "MeetingId": "meeting-id"
    }
}
```

Amazon Connect has no direct equivalent for joining a Amazon Chime SDK meeting from a phone call. Note the following:
+ This use case falls under the exception process for maintenance mode.
+ If you use PSTN Audio only for meeting dial-in or dial-out, contact AWS Support to request continued access.

#### TransactionAttributes to Set contact attributes
<a name="map-transactionattributes"></a>

In PSTN Audio, you store call context with the `TransactionAttributes` action.

```
{
    "Type": "TransactionAttributes",
    "Parameters": {
        "key1": "value1",
        "key2": "value2"
    }
}
```

In Amazon Connect, do the following:

1. Add a **Set contact attributes** block.

1. For **Namespace**, choose user defined.

1. For **Attribute**, enter your key name.

1. For **Value**, set the value manually or dynamically.

Reference the attribute later as `$.Attributes.key1`.

#### StartBotConversation to Get customer input with a Lex bot
<a name="map-startbotconversation"></a>

In PSTN Audio, you start a bot conversation with the `StartBotConversation` action.

```
{
    "Type": "StartBotConversation",
    "Parameters": {
        "CallId": "call-id-1",
        "BotAliasArn": "arn:aws:lex:us-east-1:123456789:bot-alias/BOTID/ALIASID",
        "LocaleId": "en_US"
    }
}
```

In Amazon Connect, do the following:

1. Add a **Get customer input** block.

1. Select **Amazon Lex** as the input type.

1. Configure your Amazon Lex bot and alias.

1. Branch the flow based on the intents that the bot returns.

### External data lookups
<a name="migrate-pstn-external-lambda"></a>

If your PSTN Audio Lambda function calls external APIs or databases, you can bring that same logic into Amazon Connect.

1. Recreate your AWS Lambda function, or create a trimmed version.

1. Add the function to your Amazon Connect instance. Choose **Instance settings**, choose **Flows**, choose **AWS Lambda**, then add the function.

1. In your contact flow, add an **Invoke AWS Lambda function** block.

1. Pass parameters using contact attributes.

1. Use the response in later blocks through `$.External.keyName`.

Be aware of the following limits:
+ The Lambda timeout in Amazon Connect is 8 seconds.
+ The sequential Lambda chain limit is 20 seconds total.
+ Add **Play prompt** blocks between Lambda calls to avoid silence.

## Step 4: Migrate audio prompts
<a name="migrate-pstn-step4-prompts"></a>

To move your audio prompts into Amazon Connect, do the following.

**To migrate audio prompts**

1. Download your WAV files from Amazon S3.

1. In Amazon Connect, choose **Routing**, choose **Prompts**, then choose **Create new prompt**.

1. Upload each WAV file. We recommend 16-bit, 8 kHz, mono WAV files for Amazon Connect.

1. Alternatively, replace audio files with text-to-speech in your contact flows.

## Step 5: Set up outbound calling
<a name="migrate-pstn-step5-outbound"></a>

If you use `CreateSipMediaApplicationCall` for outbound calls, choose one of the following approaches.

*For programmatic call control (primary)*

1. Use the Amazon Connect [StartOutboundVoiceContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_StartOutboundVoiceContact.html) API to start calls programmatically.

1. The contact flow that you specify handles the call.

1. Your flow logic replaces the Lambda event-driven model.

*For high-volume outbound notifications or IVR (secondary)*

1. Use the Amazon Connect outbound campaigns feature.

1. Associate an outbound whisper flow with a **Call phone number** block for call logic.

## Step 6: Test your migration
<a name="migrate-pstn-step6-test"></a>

To validate your migration, do the following.

1. Claim a test phone number in Amazon Connect, then associate it with your new contact flow.

1. Call the test number and verify the following:
   + Audio prompts play correctly.
   + DTMF input is collected properly.
   + Transfers connect to the right destination.
   + Recordings are captured.
   + Lambda integrations return data correctly.

1. Test the following edge cases:
   + The caller hangs up mid-flow.
   + Invalid input triggers the retry behavior.
   + A transfer times out or is not answered.

1. Compare the results against your PSTN Audio behavior. Call your existing SIP media application number and your new Amazon Connect number side by side.

## Step 7: Cut over production traffic
<a name="migrate-pstn-step7-cutover"></a>

To move production traffic to Amazon Connect, do the following.

1. Port your phone numbers from Amazon Chime SDK to Amazon Connect. Submit a porting request through AWS Support.

1. Alternatively, update your DNS or routing to point to your Amazon Connect numbers.

1. Monitor the first 24 to 72 hours:
   + Check contact trace records for errors.
   + Review flow logs with a **Set logging behavior** block.
   + Monitor CloudWatch metrics for your instance.

## Step 8: Decommission PSTN Audio resources
<a name="migrate-pstn-step8-decommission"></a>

After you confirm that your migration is stable, do the following.

1. Delete your SIP rules.

1. Delete your SIP media applications.

1. Release any phone numbers that remain in Amazon Chime SDK.

1. (Optional) Delete or archive your PSTN Audio Lambda function.

## Common migration patterns
<a name="migrate-pstn-patterns"></a>

The following patterns show how common PSTN Audio designs map to Amazon Connect.

### Pattern 1: Simple call forwarding
<a name="pattern-call-forwarding"></a>

The following PSTN Audio Lambda function forwards a call.

```
exports.handler = async (event) => {
    return {
        SchemaVersion: "1.0",
        Actions: [{
            Type: "CallAndBridge",
            Parameters: {
                CallTimeoutSeconds: 30,
                CallerIdNumber: event.CallDetails.Participants[0].From,
                Endpoints: [{ BridgeEndpointType: "PSTN", Uri: "+15559876543" }]
            }
        }]
    };
};
```

The Amazon Connect equivalent is a two-block flow:

1. A **Transfer to phone number** block to \+15559876543.

1. A **Disconnect** block on the error branch.

### Pattern 2: IVR menu
<a name="pattern-ivr-menu"></a>

In PSTN Audio, the Lambda function plays a prompt, collects digits, branches on the input, then transfers or plays more prompts.

The Amazon Connect equivalent is the following flow:

1. A **Play prompt** block that says "Press 1 for sales, 2 for support".

1. A **Get customer input** block for DTMF, with options 1 and 2.

1. For option 1, a **Transfer to queue** block to the sales queue.

1. For option 2, a **Transfer to queue** block to the support queue.

1. For the default or error branch, a **Play prompt** block that says "Invalid selection", which loops back.

### Pattern 3: Outbound notification with response
<a name="pattern-outbound-notification"></a>

In PSTN Audio, you call `CreateSipMediaApplicationCall`, speak a message, collect digits with `PlayAudioAndGetDigits`, then process the response.

The Amazon Connect equivalent uses the [StartOutboundVoiceContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_StartOutboundVoiceContact.html) API with a contact flow that does the following:

1. A **Play prompt** block with text-to-speech delivers the notification message.

1. A **Store customer input** block captures the confirmation digit.

1. An **Invoke AWS Lambda function** block processes the response.

1. A **Disconnect** block ends the contact.

## Limitations and known gaps
<a name="migrate-pstn-limitations"></a>

The following table lists capabilities that differ between PSTN Audio and Amazon Connect.

**PSTN Audio and Amazon Connect limitations and known gaps**

| Capability | PSTN Audio | Amazon Connect | Notes |
| --- | --- | --- | --- |
| SIP header access | Full SIP header control | Not available | If you rely on custom SIP headers, you might need architecture changes. |
| Join Amazon Chime SDK meeting | `JoinChimeMeeting` action | Not available | The exception process applies. Continue using PSTN Audio. |
| Per-minute cost (forwarding) | About $0.0068 per minute | About $0.0251 per minute | Amazon Connect includes a managed platform. Total cost depends on your use case. |
| Raw call leg control | Full leg management | Abstracted | Amazon Connect manages call legs. |
| Programmatic DTMF send | `SendDigits` to any leg | Limited | You might need architecture changes for complex DTMF automation. |

## Getting help
<a name="migrate-pstn-getting-help"></a>

Use the following resources for help with your migration:
+ AWS Support. Open a case that references "PSTN Audio to Connect Migration".
+ Amazon Connect documentation. See the [Amazon Connect Administrator Guide](https://docs.aws.amazon.com/connect/latest/adminguide/what-is-amazon-connect.html).
+ Amazon Connect API reference. See the [Amazon Connect API Reference](https://docs.aws.amazon.com/connect/latest/APIReference/Welcome.html).
+ Sample contact flows. Every new Amazon Connect instance includes samples under **Routing** and **Flows**.
