---
source_url: https://docs.aws.amazon.com/comprehend/latest/dg/idp.html
---

# Document processing
<a name="idp"></a>

Amazon Comprehend supports one-step document processing for custom classification and custom entity recognition. For example, you can input a mix of plain text documents and semi-structured documents (such as PDF documents, Microsoft Word documents, and images) to a custom analysis job.

For input files that require text extraction, Amazon Comprehend automatically performs the text extraction before running the analysis. To extract the text content, Amazon Comprehend uses an internal parser for native semi-structured documents and uses Amazon Textract APIs for images and scanned documents.

Amazon Comprehend document processing is available in each of the Amazon Comprehend [Supported Regions](guidelines-and-limits.md#limits-regions), except Asia Pacific (Tokyo) and AWS GovCloud (US-West) support only plain-text models for custom classification.

The following topics provide details about the input document types that Amazon Comprehend supports for custom analysis.

**Topics**
+ [Inputs for real-time custom analysis](idp-inputs-sync.md)
+ [Inputs for asynchronous custom analysis](idp-inputs-async.md)
+ [Setting text extraction options](idp-set-textract-options.md)
+ [Best practices for images](idp-images-bp.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Comprehend. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query comprehend` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
