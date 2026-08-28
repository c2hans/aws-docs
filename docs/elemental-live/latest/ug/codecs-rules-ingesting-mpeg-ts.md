---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/codecs-rules-ingesting-mpeg-ts.html
---

# Rules for ingesting MPEG-TS programs
<a name="codecs-rules-ingesting-mpeg-ts"></a>

For video, each AWS Elemental Live event can extract only one video from only one program. Elemental Live will not reject MPTS inputs, but it will handle only one program. There are fields in the event that specify which video to extract.

For audio, each Elemental Live event can extract audio that is in the same program as the video. It can extract more than one audio from that program. It cannot extract audio from another program. There are fields in the event that specify which audio to extract.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
