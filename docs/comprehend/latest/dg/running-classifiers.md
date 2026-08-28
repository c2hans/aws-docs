---
source_url: https://docs.aws.amazon.com/comprehend/latest/dg/running-classifiers.html
---

# Running asynchronous jobs
<a name="running-classifiers"></a>

After you train a custom classifier, you can use asynchronous jobs to analyze large documents or multiple documents in one batch.

Custom classification accepts a variety of input document types. For details, see [Inputs for asynchronous custom analysis](idp-inputs-async.md).

If you plan to analyze image files or scanned PDF documents, your IAM policy must grant permissions to use two Amazon Textract API methods (DetectDocumentText and AnalyzeDocument). Amazon Comprehend invokes these methods during text extraction. For an example policy, see [Permissions required to perform document analysis actions](security_iam_id-based-policy-examples.md#security-iam-based-policy-perform-cmp-actions).

For classification of semi-structured documents (image, PDF, or Docx files) using a plain-text model, use the `one document per file` input format. Also, include the `DocumentReaderConfig` parameter in your [StartDocumentClassificationJob](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StartDocumentClassificationJob.html) request.

**Topics**
+ [File formats for async analysis](class-inputs-async.md)
+ [Analysis jobs for custom classification (console)](analysis-jobs-custom-classifier.md)
+ [Analysis jobs for custom classification (API)](analysis-jobs-custom-class-api.md)
+ [Outputs for asynchronous analysis jobs](outputs-class-async.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Comprehend. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query comprehend` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
