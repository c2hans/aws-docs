---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/ips-create-inputs-tips.html
---

# Create the inputs
<a name="ips-create-inputs-tips"></a>

This section is a supplement to the information in [Working with inputs](creating-input.md). It provides information that applies specifically to creating inputs for use in a MediaLive channel that contains multiple input attachments.

Follow the steps in [Creating an input](create-input.md)for creating a channel, with the following notes.
+ Create the inputs that you identified in the previous steps in this section.
+ Make sure that you set up each input as the correct type (static live, static file, or dynamic file).

  There are no special steps for creating a static live input or static file input.

  To create a dynamic input, you must enter a variable in the URL for the file source. When this variable is present, MediaLive recognizes the input as a dynamic input. For more information, see [Setting up dynamic inputs](dynamic-inputs.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
