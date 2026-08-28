---
source_url: https://docs.aws.amazon.com/comprehend/latest/dg/running-class-sync.html
---

# Running real-time analysis
<a name="running-class-sync"></a>

After you train a custom classifier, you can classify documents using real-time analysis. Real-time analysis takes a single document as input and returns the results synchronously. Custom classification accepts a variety of document types as inputs for real-time analysis. For details, see [Inputs for real-time custom analysis](idp-inputs-sync.md).

If you plan to analyze image files or scanned PDF documents, your IAM policy must grant permissions to use two Amazon Textract API methods (DetectDocumentText and AnalyzeDocument). Amazon Comprehend invokes these methods during text extraction. For an example policy, see [Permissions required to perform document analysis actions](security_iam_id-based-policy-examples.md#security-iam-based-policy-perform-cmp-actions).

You must create an endpoint to run real-time analysis using a custom classification model.

**Topics**
+ [Real-time analysis for custom classification (console)](custom-sync.md)
+ [Real-time analysis for custom classification (API)](class-sync-api.md)
+ [Outputs for real-time analysis](outputs-class-sync.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Comprehend. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query comprehend` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
