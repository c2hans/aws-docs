---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/getting-started-view-stream.html
---

# Step 5: View Your Live Stream
<a name="getting-started-view-stream"></a>

You can view your live stream with:
+ The native [IVS player SDKs](#view-stream-player-sdks).
+ The [Amazon IVS console](#view-stream-console).

## Viewing with the Amazon IVS Player SDKs
<a name="view-stream-player-sdks"></a>

1. Set up the IVS Player. Start with the [IVS Player SDK overview](player.md), then read the appropriate platform-specific Player guide(s).

1. From the [Amazon IVS console](https://console.aws.amazon.com/ivs), get the **Playback URL** that was generated when you created your channel. (See [Final Channel Creation](create-channel-console.md#getting-started-create-channel-console-record-s3) earlier in this *Getting Started* guide.)

1. Call `player.load()` with the playback URL.

## Viewing with the Amazon IVS Console
<a name="view-stream-console"></a>

1. Open the [Amazon IVS console](https://console.aws.amazon.com/ivs).

   (You can also access the Amazon IVS console through the [AWS Management Console](https://console.aws.amazon.com).)

1. On the navigation pane, choose **Live channels**. (If the nav pane is collapsed, first open it by choosing the hamburger icon.)

1. Choose the channel whose stream you want to view, to go to a details page for that channel.

   The live stream is playing in the **Live stream** section of the page.

**Note**: Playback from the console consumes resources, and you will incur live-video output costs. To learn more, see [Live Video Output Costs](https://aws.amazon.com/ivs/pricing/#Live_Video_Output_Costs) on the IVS Pricing page.

**Note**: After you start streaming, there is a short delay (up to 30 seconds, usually less) before your stream can be viewed in the console.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
