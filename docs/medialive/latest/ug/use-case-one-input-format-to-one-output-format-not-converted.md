---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/use-case-one-input-format-to-one-output-format-not-converted.html
---

# Use case A: One input format to one output and not converted
<a name="use-case-one-input-format-to-one-output-format-not-converted"></a>

In this use case for including captions in a MediaLive output, the input is set up with one format of captions and two or more languages. Assume that you want to maintain the format in the output, and that you want to produce only one type of output and to include all the languages in that output.

For example, the input has embedded captions in English and French. You want to produce HLS output that includes embedded captions in both English and French.

![Diagram showing input captions in English and French flowing to output captions and HLS output.](http://docs.aws.amazon.com/medialive/latest/ug/images/captions_INembed_OUTembed_hls.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
