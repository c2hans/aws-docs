---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/supported-format-outputs.html
---

# Formats supported in different types of outputs
<a name="supported-format-outputs"></a>

There are several factors that control your ability to include captions of a specific format in the outputs in a MediaLive channel:
+ **The type of input container** – A given input container can contain captions in some formats and not in others.
+ **The format of the input captions** – A given format of captions can be converted to some formats and not to others.
+ **The type of output containers** – A given output container supports some captions formats and not others.

For example, assume that your input container is an MP4 container and your output is HLS, and that you want to include WebVTT captions in the HLS output. You can implement this use case only if the MP4 container holds 608 embedded captions. You can't implement it if, for example, the MP4 container holds Ancillary captions.

For more information about all the supported combinations of input container, input format, and output container, see [Captions supported in MediaLive](supported-captions.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
