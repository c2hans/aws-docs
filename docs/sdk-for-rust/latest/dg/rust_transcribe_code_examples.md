---
source_url: https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_transcribe_code_examples.html
---

# Amazon Transcribe examples using SDK for Rust
<a name="rust_transcribe_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Rust with Amazon Transcribe.

*Scenarios* are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Scenarios](#scenarios)

## Scenarios
<a name="scenarios"></a>

### Convert text to speech and back to text
<a name="cross_Telephone_rust_topic"></a>

The following code example shows how to:
+ Use Amazon Polly to synthesize a plain text (UTF-8) input file to an audio file.
+ Upload the audio file to an Amazon S3 bucket.
+ Use Amazon Transcribe to convert the audio file to text.
+ Display the text.

**SDK for Rust**
 Use Amazon Polly to synthesize a plain text (UTF-8) input file to an audio file, upload the audio file to an Amazon S3 bucket, use Amazon Transcribe to convert that audio file to text, and display the text.
 For complete source code and instructions on how to set up and run, see the full example on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/rustv1/cross_service#code-examples).

**Services used in this example**
+ Amazon Polly
+ Amazon S3
+ Amazon Transcribe

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Rust. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-rust` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
