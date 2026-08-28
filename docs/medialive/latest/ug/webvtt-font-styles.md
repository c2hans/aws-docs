---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/webvtt-font-styles.html
---

# Font styles for WebVTT
<a name="webvtt-font-styles"></a>

This section applies if you are [setting up a MediaLive channel with WebVTT captions](output-sidecar-and-smptett-mss.md) from source captions that are embedded or Teletext captions. You can optionally pass through some of the style information.

1. In the output that has the WebVTT captions, display the section for the captions.

1. Set **Style control**:
   + **NO\_STYLE\_DATA**: Includes only text and timestamp information for the caption encode.
   + **Passthrough**: Passes through position and color style data from the source, and includes the text and timestamp information.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
