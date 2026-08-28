---
source_url: https://docs.aws.amazon.com/streams/latest/dev/tutorial-stock-data-kplkcl2-download.html
---

# Download and build the code
<a name="tutorial-stock-data-kplkcl2-download"></a>

This topic provides sample implementation code for the sample stock trades ingestion into the data stream (*producer*) and the processing of this data (*consumer*).

**To download and build the code**

1. Download the source code from the [https://github.com/aws-samples/amazon-kinesis-learning](https://github.com/aws-samples/amazon-kinesis-learning) GitHub repo to your computer.

1. Create a project in your IDE with the source code, adhering to the provided directory structure.

1. Add the following libraries to the project:
   + Amazon Kinesis Client Library (KCL)
   + AWS SDK
   + Apache HttpCore
   + Apache HttpClient
   + Apache Commons Lang
   + Apache Commons Logging
   + Guava (Google Core Libraries For Java)
   + Jackson Annotations
   + Jackson Core
   + Jackson Databind
   + Jackson Dataformat: CBOR
   + Joda Time

1. Depending on your IDE, the project might be built automatically. If not, build the project using the appropriate steps for your IDE.

If you complete these steps successfully, you are now ready to move to the next section, [Implement the producer](tutorial-stock-data-kplkcl2-producer.md).

## Next steps
<a name="tutorial-stock-data-kplkcl2-download-next"></a>

[[Implement the producer](tutorial-stock-data-kplkcl2-producer.md)](tutorial-stock-data-kplkcl2-producer.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query streams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
