---
source_url: https://docs.aws.amazon.com/streams/latest/dev/server-side-encryption.html
---

# Data protection in Amazon Kinesis Data Streams
<a name="server-side-encryption"></a>

Server-side encryption using AWS Key Management Service (AWS KMS) keys makes it easy for you to meet strict data management requirements by encrypting your data at rest within Amazon Kinesis Data Streams.

**Note**
If you require FIPS 140-2 validated cryptographic modules when accessing AWS through a command line interface or an API, use a FIPS endpoint. For more information about the available FIPS endpoints, see [Federal Information Processing Standard (FIPS) 140-2](https://aws.amazon.com/compliance/fips/).

**Topics**
+ [What is server-side encryption for Kinesis Data Streams?](what-is-sse.md)
+ [Costs, Regions, and performance considerations](costs-performance.md)
+ [How do I get started with server-side encryption?](getting-started-with-sse.md)
+ [Create and use user-generated KMS keys](creating-using-sse-master-keys.md)
+ [Permissions to use user-generated KMS keys](permissions-user-key-KMS.md)
+ [Verify and Troubleshoot KMS key permissions](sse-troubleshooting.md)
+ [Use Amazon Kinesis Data Streams with interface VPC endpoints](vpc.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query streams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
