---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/call-and-bridge.html
---

# CallAndBridge
<a name="call-and-bridge"></a>

Creates an outbound call to a PSTN phone number, or to a SIP trunk configured as an Amazon Chime SDK Voice Connector or Amazon Chime SDK Voice Connector Group, and then bridges it with an existing call. You use `PSTN` when calling a phone number, and `AWS` when calling a SIP trunk.

An existing call can be an outbound call created by using the [CreateSIPMediaApplicationCall](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_CreateSipMediaApplicationCall.html) API, or an inbound call created by a SIP rule that invokes the AWS Lambda function with a `NewInboundCall` event. When you implement a `CallAndBridge` action to a Voice Connector or Voice Connector Group endpoint, you must specify the Amazon Resource Number (ARN) of the Voice Connector or Voice Connector Group.

You can also add custom SIP headers to outbound calls and AWS Lambda functions. Custom headers allow you to pass values such as floor numbers and zip codes. For more information about custom headers, refer to [Using SIP headers in the Amazon Chime SDK PTSN audio service](sip-headers.md).

When using the call and bridge function it is important to note that each call is counted towards your active concurrent call count used to calculate SMA Active Call Limits. With this in mind, when managing your SMA Active Call Limits for call and bridge, you should count 2 calls for every 1 call and bridge action. For more information, see [SIP trunking and voice quotas](https://docs.aws.amazon.com/general/latest/gr/chime-sdk.html#chm-sdk-pstn-quotas) in the *AWS General Reference*.

The following example code shows a typical action that bridges to a PSTN endpoint.

```
{
    "SchemaVersion": "1.0",
    "Actions": [{
            "Type": "{{CallAndBridge}}",
            "Parameters": {
                "CallTimeoutSeconds": {{30}},
                "CallerIdNumber": "{{e164PhoneNumber}}", // required
                "Endpoints": [{
                    "BridgeEndpointType": "PSTN", // required
                    "Uri": "{{e164PhoneNumber}}", // required
                }],
            }
        }
    ]
}
```

The following example shows a typical action that uses a Voice Connector or Voice Connector Group, plus a custom SIP header.

```
{
   "SchemaVersion":"1.0",
   "Actions":[
      {
         "Type":"CallAndBridge",
         "Parameters":{
            "CallTimeoutSeconds":{{30}},
            "CallerIdNumber": "{{e164PhoneNumber}}", // required
            "RingbackTone": { // optional
                    "Type": "S3",
                    "BucketName": "{{s3_bucket_name}}",
                    "Key": "{{audio_file_name}}"
                },
            "Endpoints":[
               {
                  "BridgeEndpointType":"AWS", // enum type, required
                  "Arn":"arn:aws:{{chime:us-east-1}}:{{0123456789101}}:vc/{{abcdefg1hijklm2nopq3rs}}" //VC or VCG ARN, required for AWS endpoints
                  "Uri":"{{ValidString}}", // required, see description below
               }
            ],
            "SipHeaders": {
                "x-{{String}}":"{{String}}"
            }
         }
      }
   ]
}
```

**CallTimeoutSeconds**
*Description* – The interval before a call times out. The timer starts at call setup.
*Allowed values* – Between 1 and 120, inclusive
*Required* – No
*Default value* – 30

**CallerIdNumber**
*Description* – A number belonging to the customer, or the From number of the A Leg
*Allowed values* – A valid phone number in the E.164 format
*Required* – Yes
*Default value* – None

**Endpoints**
*Description* – The endpoints of a call
*Allowed values*:
+ `BridgeEndpointType` – `AWS` for Voice Connectors and Voice Connector Groups, otherwise `PSTN`.
+ `Arn` – The ARN of a Voice Connector or Voice Connector Group. Only required when you use `AWS` as the `BridgeEndpointType`.
+ `Uri` – The URI value depends on the type of endpoint.

  For `PSTN` endpoints, the URI must be a valid E.164 phone number.

  For `AWS` endpoints, the URI value sets the `user` part of the `Request-URI`. You must use [Augmented Backus-Naur Format](https://datatracker.ietf.org/doc/html/rfc2234). Required length: between 1 and 36, inclusive. Use the following values: `a-z, A-Z, 0-9, &, =, +, $, /, %, -, _, !, ~, *, `(`,`), (`.`)

  The host value of the `Request-URI` is derived from the Inbound routes of the target Voice Connector. The following example shows a `CallAndBridge` action with an `AWS` endpoint.

  ```
  {
     "SchemaVersion":"1.0",
     "Actions":[
        {
           "Type":"CallAndBridge",
           "Parameters":{
              "CallTimeoutSeconds":{{30}},
              "CallerIdNumber": "{{+18005550122}}",
              "Endpoints":[
                 {
                    "BridgeEndpointType":"AWS",
                    "Arn":"arn:aws:{{chime:us-east-1}}:{{0123456789101}}:vc/{{abcdefg1hijklm2nopq3rs}}",
                    "Uri":"{{5550}}"
                 }
              ],
              "SipHeaders": {
                  "x-{{String}}":"{{String}}"
              }
           }
        }
     ]
  }
  ```

  For more information about Inbound routes and Voice Connectors, refer to [Editing Amazon Chime SDK Voice Connector settings](https://docs.aws.amazon.com/chime-sdk/latest/ag/edit-voicecon.html).
*Required* – Yes
*Default value* – None

**SipHeaders**
*Description* – Enables you to pass additional values. Use only with the `AWS` endpoint type.
*Allowed values* – Valid SIP header
*Required* – No
*Default value* – None

The following example shows a successful `CallAndBridge` action that uses a PSTN endpoint:

```
{
   "SchemaVersion": "1.0",
   "Sequence": 3,
   "InvocationEventType": "ACTION_SUCCESSFUL",
   "ActionData": {
      "Type": "CallAndBridge",
      "Parameters": {
         "CallTimeoutSeconds": {{30}},
         "CallerIdNumber": "{{e164PhoneNumber}}",
         "Endpoints":[
            {
               "BridgeEndpointType": "PSTN",
               "Uri": "{{e164PhoneNumber}}"
            }
         ],
         "CallId": "{{call-id-1}}"
      }
   },
   "CallDetails":{
      .....
      .....
      "Participants":[
         {
            "CallId": "{{call-id-1}}",
            "ParticipantTag": "LEG-A",
            .....
            "Status": "Connected"
         },
         {
            "CallId": "{{call-id-2}}",
            "ParticipantTag": "LEG-B",
            .....
            "Status": "Connected"
         }
      ]
   }
}
```

The following example shows a failed `CallAndBridge` action.

```
{
   "SchemaVersion": "1.0",
   "Sequence":2,
   "InvocationEventType": "ACTION_FAILED",
      "ActionData":{
      "Type": "CallAndBridge",
      "Parameters":{
         "CallTimeoutSeconds": {{30}},
         "CallerIdNumber": "{{e164PhoneNumber}}",
         "Endpoints": [
            {
               "BridgeEndpointType": "PSTN",
               "Uri": "{{e164PhoneNumber}}"
            }
         ],
         "CallId": "{{call-id-1}}"
      },
      "ErrorType": "CallNotAnswered",
      "ErrorMessage": "Call not answered"
   },
   "CallDetails":{
      .....
      .....
      "Participants":[
         {
            "CallId": "{{call-id-1}}",
            "ParticipantTag": "LEG-A",
            .....
         }
      ]
   }
}
```

## Call flows
<a name="call-bridge-flows"></a>

The `CallAndBridge` action provides a different call signaling and audio experience for an existing call leg, depending on the parameters and whether the leg is connected.

The following diagram shows show the call flows with different parameters when an inbound call leg A is already connected.

![The flow of an answered call through the CallAndBridge action.](http://docs.aws.amazon.com/chime-sdk/latest/dg/images/call-bridge-ans-2.png)

The following diagram shows the call flow for an unanswered call.

![The flow of an unanswered call through the CallAndBridge action.](http://docs.aws.amazon.com/chime-sdk/latest/dg/images/SMA_Bridging_NotAns.png)

**Additional Details**
Remember these facts about the `CallAndBridge` action.
+ `CallTimeoutSeconds` – This timer starts when the SIP invitation is sent on the B-Leg. You can set a desired target value, but this value can be ignored by upstream carriers.
+ `CallerIdNumber` – This phone number must belong to the customer, or be the From number of an A-Leg.
+ **Hang-up behavior and edge cases** – If one call leg hangs up, the other call leg does not automatically hang up the call. When a `Hangup` event is sent to the AWS Lambda function, the remaining leg must be disconnected independently. If a call leg is left hanging, the call is billed until it is hung up. For example, the following scenario may lead to unexpected charges:
  + You try to bridge to a destination phone number. The destination is busy and sends the call straight to voicemail. From the Audio Service's perspective, going to voicemail is an answered call. The A-Leg hangs up, but the B-Leg continues listening for the voicemail message. While the B-Leg listens, you get billed.
  + As a best practice, use the AWS Lambda function, or the party on the other end of the call, to hang up each call leg independently.
+ **Billing** – You're billed for the following when using `CallAndBridge`:
  + Active call minutes for each call leg created (A-Leg, B-Leg, etc.) to the PSTN.
  + Audio Service usage minutes.

See working examples on GitHub:
+ [https://github.com/aws-samples/amazon-chime-sma-bridging](https://github.com/aws-samples/amazon-chime-sma-bridging)
+ [https://github.com/aws-samples/amazon-chime-sma-call-forwarding](https://github.com/aws-samples/amazon-chime-sma-call-forwarding)
+ [https://github.com/aws-samples/amazon-chime-sma-on-demand-recording](https://github.com/aws-samples/amazon-chime-sma-on-demand-recording)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
