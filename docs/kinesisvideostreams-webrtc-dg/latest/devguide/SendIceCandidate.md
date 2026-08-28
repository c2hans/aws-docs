---
source_url: https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/SendIceCandidate.html
---

# SendIceCandidate
<a name="SendIceCandidate"></a>

Sends the ICE candidate to the target recipient. The prerequisite is that the client must be already connected to the WebSocket endpoint obtained from the `GetSignalingChannelEndpoint` API.

If the sender type is a viewer, then it sends the ICE candidate to a master. Also, it is not necessary to specify the `RecipientClientId` and any specified value for `RecipientClientId` is ignored. If the sender type is master, the ICE candidate is sent to the target specified by the `RecipientClientId`. `RecipientClientId` is a required input in this case.

A master client app is allowed to send an ICE candidate to any viewer, whereas a viewer client app is only allowed to send an ICE candidate to a master client app. If a viewer client app attempts to send an ICE candidate to another viewer client app, the request will NOT be honored.

## Request
<a name="SendIceCandidate-request"></a>

```
{
    "action": "ICE_CANDIDATE",
    "recipientClientId": "string",
    "messagePayload": "string",
    "correlationId": "string"
}
```
+ **action** - Type of the message that is being sent.
  + Type: ENUM
  + Valid values: `SDP_OFFER`, `SDP_ANSWER`, `ICE_CANDIDATE`
  + Length constraints: Minimum length of 1. Maximum length of 256.
  + Pattern: `[a-zA-Z0-9_.-]+`
  + Required: Yes
+ **recipientClientId** - A unique identifier for the recipient.
  + Type: String
  + Length constraints: Minimum length of 1. Maximum length of 256.
  + Pattern: `[a-zA-Z0-9_.-]+`
  + Required: No
+ **messagePayload** - The base64-encoded message content.
  + Type: String
  + Length constraints: Minimum length of 1. Maximum length of 10K.
  + Required: Yes
+ **correlationId** - A unique identifier for the message.
  + Type: String
  + Length constraints: Minimum length of 1. Maximum length of 256.
  + Pattern: `[a-zA-Z0-9_.-]+`
  + Required: No

## Response
<a name="SendIceCandidate-response"></a>

No response is returned if the message is successfully received by the signaling backend. If the service encounters an error and if the `correlationId` is specified in the request, the error details are returned as a `STATUS_RESPONSE` message. For more information, see [Asynchronous message reception](async-message-reception-api.md).

## Errors
<a name="SendIceCandidate-errors"></a>
+ InvalidArgumentException

  A specified parameter exceeds its restrictions, is not supported, or cannot be used. For more information, see the returned message.

  HTTP Status Code: 400
+ ClientLimitExceededException

  When the API is invoked at a rate that is too high. For more information, see [Amazon Kinesis Video Streams with WebRTC service quotas](kvswebrtc-limits.md) and [Error Retries and Exponential Backoff in AWS](https://docs.aws.amazon.com/general/latest/gr/api-retries.html).

  HTTP Status Code: 400

## Limits/Throttling
<a name="SendIceCandidate-limits"></a>

This API is throttled at an account level if the API is invoked at too high a rate. An error returned when throttled with `ClientLimitExceededException`.

## Idempotent
<a name="SendIceCandidate-idempotent"></a>

This API is not idempotent.

## Retry behavior
<a name="SendIceCandidate-retry"></a>

This is counted as a new API call.

## Concurrent calls
<a name="SendIceCandidate-concurrent"></a>

Concurrent calls are allowed. An offer is sent once per each call.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Kinesis Video Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesisvideostreams-webrtc-dg` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
