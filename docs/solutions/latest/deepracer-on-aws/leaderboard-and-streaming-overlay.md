---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/leaderboard-and-streaming-overlay.html
---

# Leaderboard and streaming overlay
<a name="leaderboard-and-streaming-overlay"></a>

Each physical event track provides two unauthenticated spectator views. To access a spectator view, use the **Live leaderboard** or **Streaming overlay** link for a track on the event details page.

The **Live leaderboard** displays the selected track’s current rankings. The page updates as results arrive.

![Public live leaderboard showing the selected track and current rankings](https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/deepracer_public_live_leaderboard.png)

The **Streaming overlay** is a transparent browser source that you can use with Open Broadcaster Software (OBS) or similar streaming software. During a run, a panel in the bottom-left corner displays the racer’s name, a countdown, and lap-time indicators. Between runs, a panel in the top-right corner displays the top four leaderboard entries.

![Transparent overlay showing racer name](https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/deepracer_streaming_overlay_stats.png)

![Transparent overlay showing first](https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/deepracer_streaming_overlay_lb.png)

**Important**
Anyone with a spectator-view link can view that track’s race data. Share links only with your intended audience.
