---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/use-case-one-input-format-to-different-output-formats.html
---

# Use case B: One input format converted to one different format in one output
<a name="use-case-one-input-format-to-different-output-formats"></a>

In this use case for including captions in a MediaLive output, the input is set up with one format of captions and two or more languages. You want to convert the captions to a different format in the output. You want to produce only one type of output and include all the languages in that output.

For example, the input has embedded captions in German and French. You want to convert the captions to DVB-Sub and include these captions in both languages in a UDP output.

![Diagram showing input captions in German and French converting to DVB-Sub output formats.](http://docs.aws.amazon.com/medialive/latest/ug/images/captions_INembed_OUTdvb_udp.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
