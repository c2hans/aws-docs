---
source_url: https://docs.aws.amazon.com/comprehend/latest/dg/pii.html
---

# Personally identifiable information (PII)
<a name="pii"></a>

You can use the Amazon Comprehend console or APIs to detect *personally identifiable information (PII)* in English or Spanish text documents. PII is a textual reference to personal data that could be used to identify an individual. PII examples include addresses, bank account numbers, and phone numbers.

With PII detection, you have the choice of locating the PII entities or redacting the PII entities in the text. To locate PII entities, you can use real-time analysis or an asynchronous batch job. To redact the PII entities, you must use an asynchronous batch job.

You can use Amazon S3 Object Lambda Access Points for personally identifiable information (PII) to control the retrieval of documents from your Amazon S3 bucket. You can control access to documents that contain PII and redact personally identifiable information from the documents. For more information, see [Using Amazon S3 object Lambda access points for personally identifiable information (PII)](using-access-points.md).

**Topics**
+ [Detecting PII entities](how-pii.md)
+ [Labeling PII entities](how-pii-labels.md)
+ [PII real-time analysis (Console)](realtime-pii-console.md)
+ [PII asynchronous analysis jobs (Console)](async-pii-console.md)
+ [PII real-time analysis (API)](realtime-pii-api.md)
+ [PII asynchronous analysis jobs (API)](get-started-api-pii.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Comprehend. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query comprehend` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
