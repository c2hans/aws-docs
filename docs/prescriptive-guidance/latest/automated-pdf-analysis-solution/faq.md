---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/automated-pdf-analysis-solution/faq.html
---

# FAQ
<a name="faq"></a>

This section provides answers to commonly raised questions about designing an automated solution to analyze PDF files on the AWS Cloud.

## Can I use this guide's solution to process different PDF file types?
<a name="can-i-use-this-guide9999999999999999apos-s-solution-to-process-different-pdf-file-types-.b405b6ef-80a4-5b38-afe9-2588a28ab4c3"></a>

Yes, you can process different PDF file types if you define a separate template for each PDF file type. This template is used by the Lambda function during processing and you can use a single Lambda function to process different PDF file types.

## Can I process multipage PDF files?
<a name="can-i-process-multipage-pdf-files-.6eabf685-0311-5643-b370-e34abe55fc66"></a>

Yes, you can use the Amazon Textract asynchronous API in your Lambda function to process multipage PDF files.

## Can I use other business intelligence tools to create dashboards instead of Quick?
<a name="can-i-use-other-business-intelligence-tools-to-create-dashboards-instead-of-9999999999999999qs--.20ca9dfb-11b1-5e60-af3b-271f3554ba4b"></a>

Yes, you can connect Amazon Simple Storage Service (Amazon S3) to your preferred business intelligence tool and then create dashboards.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
