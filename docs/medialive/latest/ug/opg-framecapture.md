---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/opg-framecapture.html
---

# Creating a Frame capture output group
<a name="opg-framecapture"></a>

When you create a AWS Elemental MediaLive channel, you might want to include a Frame capture output group. A Frame capture output is a supplement to streaming; it isn't itself a streaming output. This type of output might be useful for your workflow. For example, you might use a Frame capture output to create thumbnails of the content. (You can also create thumbnails by using the [thumbnails feature](thumbnails.md).)

**Topics**
+ [Organize encodes in a Frame capture output group](design-framecapture-package.md)
+ [Coordinate with the downstream system](framecapture-op-origin-server-s3.md)
+ [Create a Frame capture output group](creating-framecapture-output-group.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
