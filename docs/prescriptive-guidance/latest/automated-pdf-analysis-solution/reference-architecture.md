---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/automated-pdf-analysis-solution/reference-architecture.html
---

# Reference architecture
<a name="reference-architecture"></a>

The following diagram shows the workflow after you apply this guide's automated solution to a daily operations report. When new files are ingested into Amazon Simple Storage Service (Amazon S3), they can be immediately visualized in an Amazon Quick Sight dashboard after they are processed.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/automated-pdf-analysis-solution/images/guide-img/689cce75-c135-4cff-9a10-7c6bc4f61a19/images/bffd2f1d-e70f-4982-91be-108fb5c56d6b.png)

The diagram shows the following four phases:

1. **PDF file ingestion** – Your application automatically ingests new PDF files with an identical format (for example, a daily operations report) into an Amazon Simple Storage Service (Amazon S3) bucket. Amazon S3 initiates an [ObjectCreated event ](https://docs.aws.amazon.com/AmazonS3/latest/userguide/NotificationHowTo.html)when new PDF files are added to the bucket and this invokes an AWS Lambda function. For more information about this, see [Using an Amazon S3 trigger to invoke a Lambda function](https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example.html) in the Amazon S3 documentation.

1. **PDF file processing** – The Lambda function sends one PDF file to Amazon Textract, which extracts the content. A post-processing script runs and parses the Amazon Textract response and uses a predefined template for this type of PDF file. This template contains the correct attributes and helps correctly extract all key-value pairs, tables, and other raw text. For more information about this, see the pattern [Automatically extract content from PDF files using Amazon Textract](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-extract-content-from-pdf-files-using-amazon-textract.html?did=pg_card&trk=pg_card) on the AWS Prescriptive Guidance website.

1. **Data storage** – The extracted and corrected data is stored in an Amazon DynamoDB table, in addition to a JSON file for each PDF file. The JSON files are stored in an S3 bucket that can be used by downstream processing and analytics services, such as [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html), [Amazon QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html), or [Amazon SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html).

1. **Analytics and visualizations** – Amazon Quick Sight analyzes the data and creates visualizations that help generate insights for all processed PDF files. After dashboards are created in Quick Sight, you can share them with your end users and business teams.

## Considerations
<a name="considerations"></a>

This guide's solution is appropriate for processing PDF files that have an identical format and a consistent layout of forms and tables. However, you must define a template and edit it in advance to fully automate the process and make extracted data available for analysis. This template is then used during processing with the Lambda function.

Although this solution can be applied to different PDF file types at the same time, you must create and define separate templates for each PDF file type and store them in an accessible location (for example, Amazon S3). We recommend that you use a unique identifier for each PDF file type, such as a PDF file name or different folders in your S3 bucket. The Lambda function can then call the appropriate template when processing the PDF file type.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
