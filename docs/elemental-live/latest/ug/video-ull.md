---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/video-ull.html
---

# Setting up for ultra-low latency
<a name="video-ull"></a>

If you are sending output to an HTTP server or to AWS Elemental MediaStore, you can produce ultra-low latency outputs if you create a DASH output and enable chunked encoding and chunked transfer.

With chunked encoding and transfer Elemental Live delivers more quickly, without any decrease in quality. When you enable chunked encoding and transfer, Elemental Live divides the video into fragments, with several fragments in each segment. Elemental Live delivers the fragments before the entire segment is complete. Delivery of smaller chunks more frequently can speed up handling by the downstream system, assuming that the downstream system can handle the frequency.

From the Elemental Live side, this feature works with any downstream system that can accept DASH. But you should always discuss your requirements with the downstream system administrator, to make sure that they are prepared to accept the output.

**Setup**
**Note**
The information in this section assumes that you are familiar with the general steps for creating an event.

To produce an ultra-low latency DASH output, create a DASH output group in the usual way, with these additions:

1. Enable **Chunked Encoding**.

1. Change **Fragment Length** and **Segment Length** if necessary. For information about these fields, choose the ? icon that appears when you hover over the field name.

1. In **HTTP Push Dialect**, choose the appropriate option. The **Chunked Transfer** field appears.

1. Enable **Chunked Transfer**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
