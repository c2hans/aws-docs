---
source_url: https://docs.aws.amazon.com/streams/latest/dev/kinesis-kpl-supported-plats.html
---

# KPL supported platforms
<a name="kinesis-kpl-supported-plats"></a>

The Amazon Kinesis Producer Library (KPL) is written in C\+\+ and runs as a child process to the main user process. Precompiled 64-bit native binaries are bundled with the Java release and are managed by the Java wrapper.

The Java package runs without the need to install any additional libraries on the following operating systems:
+ Linux distributions with kernel 2.6.18 (September 2006) and later
+ Apple iOS X 10.9 and later
+ Windows Server 2008 and later
**Important**
Windows Server 2008 and later is supported for all KPL versions up to version 0.14.0.
The Windows platform is NOT supported starting with KPL version 0.14.0 or higher.

Note that the KPL is 64-bit only.

## Source code
<a name="kinesis-kpl-supported-plats-source-code"></a>

If the binaries provided in the KPL installation are not sufficient for your environment, the core of the KPL is written as a C\+\+ module. The source code for the C\+\+ module and the Java interface are released under the Amazon Public License and are available on GitHub at [Amazon Kinesis Producer Library](https://github.com/awslabs/amazon-kinesis-producer). Although the KPL can be used on any platform for which a recent standards-compliant C\+\+ compiler and JRE are available, Amazon doesn't officially support any platform that is not on the supported platforms list.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query streams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
