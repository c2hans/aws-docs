---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/broadcast-ios.html
---

# IVS Broadcast SDK: iOS Guide \| Low-Latency Streaming
<a name="broadcast-ios"></a>

The IVS Low-Latency Streaming iOS Broadcast SDK provides the interfaces required to broadcast to Amazon IVS on iOS.

The `AmazonIVSBroadcast` module implements the interface described in this document. The following operations are supported:
+ Set up (initialize) a broadcast session.
+ Manage broadcasting.
+ Attach and detach input devices.
+ Manage a composition session.
+ Receive events.
+ Receive errors.

**Latest version of iOS broadcast SDK:** 1.46.0 ([Release Notes](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/release-notes.html#aug27-26-broadcast-mobile-ll))

**Reference documentation:** For information on the most important methods available in the Amazon IVS iOS broadcast SDK, see the reference documentation at [https://aws.github.io/amazon-ivs-broadcast-docs/1.46.0/ios/](https://aws.github.io/amazon-ivs-broadcast-docs/1.46.0/ios/).

**Sample code: **See the iOS sample repository on GitHub: [https://github.com/aws-samples/amazon-ivs-broadcast-ios-sample](https://github.com/aws-samples/amazon-ivs-broadcast-ios-sample).

**Platform requirements:** iOS 14\+

## How iOS Chooses Camera Resolution and Frame Rate
<a name="ios-publish-subscribe-resolution-framerate"></a>

The camera managed by the broadcast SDK optimizes its resolution and frame rate (frames-per-second, or FPS) to minimize heat production and energy consumption. This section explains how the resolution and frame rate are selected to help host applications optimize for their use cases.

When attaching an `IVSCamera` to an `IVSBroadcastSession`, the camera is optimized for a frame rate of `IVSVideoConfiguration.targetFramerate` and a resolution of `IVSVideoConfiguration.size`. These values are provided to the `IVSBroadcastSession` on initialization.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
