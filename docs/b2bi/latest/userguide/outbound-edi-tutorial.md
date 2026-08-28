---
source_url: https://docs.aws.amazon.com/b2bi/latest/userguide/outbound-edi-tutorial.html
---

# Outbound EDI tutorial
<a name="outbound-edi-tutorial"></a>

This tutorial guides you through setting up an outbound B2B Data Interchange workflow using AWS B2B Data Interchange. You'll learn how to transform JSON data into X12 EDI documents (specifically 850 Purchase Orders) for sending to your trading partners.

## Converting JSON to EDI X12 documents
<a name="outbound-use-case"></a>

Learn how to automatically convert JSON purchase orders into X12 850 EDI documents that you can send to your suppliers. This tutorial shows you how to set up an automated workflow that transforms JSON files in Amazon S3 into properly formatted EDI documents.

Here's how the workflow operates:

1. Your procurement system creates a purchase order in JSON format and uploads it to Amazon S3.

1. AWS B2B Data Interchange detects the new file and converts it to an X12 850 EDI document.

1. The converted document is saved to your output directory, ready for transmission to your supplier through Transfer Family or another EDI method.

**Note**
This tutorial covers outbound EDI (JSON to X12). For inbound EDI (X12 to JSON), see [Inbound EDI tutorial](inbound-edi-tutorial.md).

By completing this tutorial, you'll:
+ Create a business profile for your organization
+ Set up an outbound transformer to convert JSON to X12 850 EDI
+ Configure a trading capability that automates the transformation process
+ Establish a partnership with outbound EDI settings
+ Test the complete end-to-end workflow

By completing this tutorial, you'll create a business profile representing your organization, an outbound transformer that converts JSON data to X12 850 EDI documents, a trading capability that automates the transformation process, a partnership with outbound EDI configuration, and a complete end-to-end workflow for generating EDI documents.

This setup will automatically monitor your Amazon S3 input directory for JSON files and transform them into X12 EDI documents, placing the EDI output in your designated output directory for transmission to trading partners.

**Tip**
Before starting this tutorial, review the [Prerequisites](b2b-tutorials.md#tutorial-prerequisites) section.

**Topics**
+ [Converting JSON to EDI X12 documents](#outbound-use-case)
+ [Step 1: Setting up Amazon S3 buckets](outbound-tutorial-step1-s3-setup.md)
+ [Step 2: Creating your business profile](outbound-tutorial-step2-profile.md)
+ [Step 3: Creating an outbound transformer](outbound-tutorial-step3-transformer.md)
+ [Step 4: Create a trading capability](outbound-tutorial-step4-capability.md)
+ [Step 5: Create a partnership with outbound EDI configuration](outbound-tutorial-step5-partnership.md)
+ [Step 6: Test your outbound configuration](outbound-tutorial-step6-testing.md)
+ [Step 7: Monitor your outbound workflow](outbound-tutorial-step7-monitoring.md)
+ [Cleanup steps](outbound-tutorial-cleanup.md)
+ [Next steps](outbound-tutorial-conclusion.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS B2B Data Interchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query b2bi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
