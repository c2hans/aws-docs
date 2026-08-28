---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/teletext.html
---

# Information for Teletext
<a name="teletext"></a>

This section provides information specific to Teletext input captions. It describes the fields that appear when you choose **SCC** in the **Source** field in the **Caption Selector** section of the event. For more context, see [Step 1: Identify the source captions that you want](identify-captions-in-the-input.md).

Teletext is a form of data that can contain several types of information, not just captions. Teletext can be present in SDI input, in MXF input, and in TS input, in which case it might be referred to as “DVB teletext.”.

You can set up to handle teletext in one of the following ways:
+ If you want to extract the entire teletext input, you must set up teletext passthrough. The entire teletext can never be converted to another format. Teletext passthrough is supported only in a TS output.
+ You can extract individual captions pages (the captions in a specific language) and convert them to another captions format.
+ You cannot extract individual captions pages (the captions in a specific language) and keep them in teletext.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
