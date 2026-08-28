---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/feature-nielsen-watermark.html
---

# Inserting Nielsen watermarks
<a name="feature-nielsen-watermark"></a>

Starting with Elemental Live version 2.22.0, you can set up to create new Nielsen watermarks and insert them into your audio. Typically, only content and distribution providers use Nielsen watermarks. If you're not working with The Nielsen Company to implement watermarks, you don't need to read this section.

If your content already contains watermarks, you might choose to convert them to ID3 metadata and include that metadata in the output. For information about conversion to ID3, see [Converting Nielsen watermarks to ID3](feature-nielsen-id3.md).

The Nielsen watermark feature requires the license (the Nielsen Audio Watermark Package). Contact your AWS sales manager.

**Topics**
+ [Audio requirements](nielsen-wmark-requirements.md)
+ [Getting ready](nielsen-wmark-get-ready.md)
+ [Setting up Nielsen watermarks](nielsen-watermark-procedure.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
