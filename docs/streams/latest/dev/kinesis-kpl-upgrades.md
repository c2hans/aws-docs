---
source_url: https://docs.aws.amazon.com/streams/latest/dev/kinesis-kpl-upgrades.html
---

# Transition to Amazon Trust Services (ATS) certificates for the KPL
<a name="kinesis-kpl-upgrades"></a>

On February 9, 2018, at 9:00 AM PST, Amazon Kinesis Data Streams installed ATS certificates. To continue to be able to write records to Kinesis Data Streams using the Amazon Kinesis Producer Library (KPL), you must upgrade your installation of the KPL to [version 0.12.6](http://search.maven.org/#artifactdetails|com.amazonaws|amazon-kinesis-producer|0.12.6|jar) or later. This change affects all AWS Regions.

For information about the move to ATS, see [How to Prepare for AWS’s Move to Its Own Certificate Authority](https://aws.amazon.com/blogs/security/how-to-prepare-for-aws-move-to-its-own-certificate-authority/).

If you encounter problems and need technical support, [create a case](https://console.aws.amazon.com/support/v1#/case/create) with the AWS Support Center.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query streams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
