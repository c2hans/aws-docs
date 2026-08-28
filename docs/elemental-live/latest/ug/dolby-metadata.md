---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/dolby-metadata.html
---

# Working with Dolby metadata
<a name="dolby-metadata"></a>

Audio encoded with a Dolby codec always includes Dolby metadata, as per the ATSC A/52 2012 standard. This Dolby metadata is used by AWS Elemental Live in two ways when the stream is encoded with Dolby codec:
+ It is used to manipulate the audio just before encoding the output.
+ It is included in the metadata for the output stream.

This document describes how to set up an Elemental Live profile or event to use Dolby metadata in these ways.

Dolby metadata is supported in the output only when the audio codec for the output is Dolby Digital (also known as AC3) or Dolby Digital Plus (also known as Enhanced AC3).

**Topics**
+ [Categories of metadata: Delivered and encoder control](dolby-metadata-categories.md)
+ [Source of Elemental Live metadata](dolby-metadata-source.md)
+ [Impact of the metadata on the output audio](dolby-metadata-impact.md)
+ [Combinations of input and output codec](dolby-metadata-impact-combination-input-output-codec.md)
+ [Setting up the profile or event using the web interface](dolby-metadata-setup.md)
+ [Output with the Dolby Digital codec](dolby-metadata-output-dolby-digital-codec.md)
+ [Output with Dolby Digital Plus (EC2, EAC3) codec](dolby-metadata-output-dolby-digital-plus-codec.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
