---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/nielsen-watermark-procedure.html
---

# Setting up Nielsen watermarks
<a name="nielsen-watermark-procedure"></a>

You can create new Nielsen watermarks on the output audio encoding. To pass through existing Nielsen watermarks or convert them to ID3, see [Converting Nielsen watermarks to ID3](feature-nielsen-id3.md).

**Note**
The information in this section assumes that you are familiar with the general steps for creating an event. It also assumes that you have already set up the audio encodes (outputs) that will contain the watermarks.

**To create Nielsen watermarks**

1. On the **Event **page of the web interface, go to the **Streams** section, then go to the specific stream that contains the audio that you want to set up with watermarking.

1. Choose the **Audio** tab. Then open the **Advanced** section. More fields appear.

1. Set **Nielsen Watermarking** to **On**. More fields appear.

1. Set the following fields to suit your requirements. For information about a field, hover on the upper-right corner of the field and choose the **?** icon.
   + Process Type
   + Distribution Type

1. Complete the remaining fields with the values you determined when [getting ready](nielsen-wmark-get-ready.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
