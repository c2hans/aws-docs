---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/ad-avail-blanking-and-blackout.html
---

# Ad avail blanking and blackout
<a name="ad-avail-blanking-and-blackout"></a>

You can turn on one or both of the following features to blank out the content associated with a SCTE-35 event:
+ “**Blackout**”: Blank out the content for other types of SCTE-35 messages such as chapters and programs.
+ “**Ad avail blanking**”: Blank out the content for a SCTE-35 message that is considered an “ad avail” (according to the mode, [Getting ready: Setting the ad avail mode](getting-ready-setting-the-ad-avail-mode.md)).

In both features, the handling is one of the following.
+ Replace the video content associated with the event with an image you specify or with a black image.
+ Remove the audio associated with the event.
+ Remove the closed captions associated with the event.

**Topics**
+ [Blanking is global](blanking-is-global.md)
+ [Scope of blackout of SCTE-35 messages](scope-of-blackout.md)
+ [Scope of ad avail blanking of SCTE-35 messages](scope-of-ad-avail-blanking.md)
+ [Procedure to enable ad avail blanking](procedure-to-enable-ad-avail-blanking.md)
+ [Procedure to enable blackout](procedure-to-enable-blackout.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
