---
source_url: https://docs.aws.amazon.com/translate/latest/dg/processing.html
---

# Translation processing modes
<a name="processing"></a>

When translating documents, you can use two different translation processing modes: real-time translation or asynchronous batch processing. The mode you use is based on the size and type of the target documents and affects how you submit the translation job and view its results.
+ [Real-time translation](sync.md) – You make a synchronous request to translate a small amount of text (or a text file) and Amazon Translate responds immediately with the translated text.
+ [Asynchronous batch processing](async.md) – You put a collection of documents in an Amazon Simple Storage Service (Amazon S3) location and start an asynchronous processing job to translate them. Amazon Translate sends the translated output documents to a specified Amazon S3 location.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Translate. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query translate` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
