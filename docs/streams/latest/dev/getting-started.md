---
source_url: https://docs.aws.amazon.com/streams/latest/dev/getting-started.html
---

# Use the AWS CLI to perform Amazon Kinesis Data Streams operations
<a name="getting-started"></a>

This section shows you how to perform basic Amazon Kinesis Data Streams operations using the AWS Command Line Interface. You will learn fundamental Kinesis Data Streams data flow principles and the steps necessary to put and get data from an Kinesis data stream.

 If you are new to Kinesis Data Streams, start by becoming familiar with the concepts and terminology presented in [Amazon Kinesis Data Streams Terminology and concepts](key-concepts.md).

**Topics**
+ [Tutorial: Install and configure the AWS CLI for Kinesis Data Streams](kinesis-tutorial-cli-installation.md)
+ [Tutorial: Perform basic Kinesis Data Streams operations using the AWS CLI](fundamental-stream.md)

For CLI access, you need an access key ID and a secret access key. Use temporary credentials instead of long-term access keys when possible. Temporary credentials include an access key ID, a secret access key, and a security token that indicates when the credentials expire. For more information, see [ Using temporary credentials with AWS resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html) in the *IAM User Guide*.

You can find detailed step-by-step IAM and security key set up instructions at [Create an IAM User](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/get-set-up-for-amazon-ec2.html#create-an-iam-user).

In this section, the specific commands discussed are given verbatim, except where specific values are necessarily different for each run. Also, the examples are using the US West (Oregon) region, but the steps in this section work in any of [the regions where Kinesis Data Streams is supported](https://docs.aws.amazon.com/general/latest/gr/rande.html#ak_region).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query streams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
