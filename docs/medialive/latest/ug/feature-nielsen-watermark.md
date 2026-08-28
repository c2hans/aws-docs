---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/feature-nielsen-watermark.html
---

# Creating and inserting Nielsen watermarks
<a name="feature-nielsen-watermark"></a>

You can set up MediaLive to create new Nielsen watermarks and insert them in the output audio. Typically, only content and distribution providers use Nielsen watermarks. If you're not working with The Nielsen Company to implement watermarks, you don't need to read this section.

If your content already contains watermarks, you might choose to convert them to ID3 metadata and include that metadata in the output. For more information about passthrough and conversion to ID3, see [Converting Nielsen watermarks to ID3](feature-nielsen-id3.md).

**Topics**
+ [Audio requirements](supportedaudio.md)
+ [Getting ready](nielsen-watermark-getready.md)
+ [Setting up Nielsen watermarks in a MediaLive channel](watermark-procedure.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
