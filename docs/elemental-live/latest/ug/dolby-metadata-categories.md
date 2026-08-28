---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/dolby-metadata-categories.html
---

# Categories of metadata: Delivered and encoder control
<a name="dolby-metadata-categories"></a>

There are two categories of parameters in the Dolby metadata, characterized by how Elemental Live uses it:
+ Delivered: Elemental Live does not read these parameters, so they have no effect on the audio produced by Elemental Live. Instead, they are included as metadata in the output in order to **deliver ** them to the downstream decoder.

  “Delivered” metadata is also called *Consumer* metadata because it is intended to be used by the end consumer’s home decoder.
+ Encoder Control: Elemental Live uses these parameters to manipulate the audio just before encoding the stream and producing the output. They provide a mechanism for Elemental Live to control the transcoding performed by Elemental Live. These parameters are never included in the output metadata.

  “Encoder Control” metadata is also called *Professional* metadata because it is intended to be used by a professional device – in our case Elemental Live. It is never intended for the end consumer's home decoder.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
