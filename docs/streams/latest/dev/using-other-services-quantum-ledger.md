---
source_url: https://docs.aws.amazon.com/streams/latest/dev/using-other-services-quantum-ledger.html
---

# Write to Kinesis Data Streams using Amazon Quantum Ledger Database (Amazon QLDB)
<a name="using-other-services-quantum-ledger"></a>

You can create a stream in Amazon QLDB that captures every document revision that is committed to your journal and delivers this data to Amazon Kinesis Data Streams in real time. A QLDB stream is a continuous flow of data from your ledger's journal to a Kinesis data stream resource. Then, you can use the Kinesis streaming platform or the Kinesis Client Library to consume your stream, process the data records, and analyze the data contents. A QLDB stream writes your data to Kinesis Data Streams in three types of records: `control`, `block summary`, and `revision details`.

For more information, see [Streams](https://docs.aws.amazon.com/qldb/latest/developerguide/streams.html) in the *Amazon QLDB developer Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query streams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
