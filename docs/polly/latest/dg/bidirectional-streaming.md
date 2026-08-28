---
source_url: https://docs.aws.amazon.com/polly/latest/dg/bidirectional-streaming.html
---

# Synthesizing speech with bidirectional streaming
<a name="bidirectional-streaming"></a>

Amazon Polly provides a `StartSpeechSynthesisStream` operation that establishes an HTTP/2 connection with bidirectional communication between your application and the service. Text flows from your application to Amazon Polly while synthesized audio flows back. You send text as it becomes available, and Amazon Polly returns audio as it synthesizes, without either side waiting for the other to finish.

This is useful when text is produced progressively rather than all at once. For example, a customer service chatbot powered by a foundation model on Amazon Bedrock generates its response token by token. With bidirectional streaming, your application can forward each text chunk to Amazon Polly as the model produces it and begin playing audio back to the caller while the model is still generating the rest of the response.

This operation requires the generative engine and an AWS SDK that supports HTTP/2 event streams. The audio arrives as a sequence of chunks that your application accumulates into a complete audio output. Speech marks are not supported by this operation.

**Note**
The AWS CLI (v1 and v2), AWS Tools for PowerShell (v4 and v5), Python, and .NET v3 are not supported. You can use the bidirectional streaming API with the following SDKs: AWS SDK for Java 2.x, JavaScript v3, .NET v4, C\+\+, Go v2, Kotlin, PHP v3, Ruby v3, Rust, and Swift.

**Topics**
+ [SynthesizeSpeech and StartSpeechSynthesisStream compared](bidirectional-streaming-choosing.md)
+ [Sending text and receiving audio](bidirectional-streaming-lifecycle.md)
+ [Code examples](bidirectional-streaming-examples.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Polly. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query polly` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
