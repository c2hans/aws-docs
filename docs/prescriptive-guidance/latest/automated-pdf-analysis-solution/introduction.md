---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/automated-pdf-analysis-solution/introduction.html
---

# Designing an automated solution to analyze PDF files on the AWS Cloud
<a name="introduction"></a>

*Tianxia Jia and Yanyan Zhang, Amazon Web Services*

Organizations regularly use PDF files to store and transfer different data types, including text, tables, and forms. However, it can be challenging to automatically aggregate and analyze data from different PDF files. For example, an organization's business application might regularly ingest different PDF files with an identical format but that users must individually open and read. This means that users find it difficult to generate useful insights from those PDF files and must manually extract relevant data and use third-party tools for further analysis.

On the AWS Cloud, [Amazon Textract](https://docs.aws.amazon.com/textract/latest/dg/what-is.html) automatically extracts information (for example, printed text, forms, and tables) from PDF files and produces a JSON-formatted file that contains information from the original PDF file. During post-processing, the extracted data is stored in [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) and you can generate business insights using analytics and visualizations in [Amazon QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html).

This guide provides a serverless, automated PDF file analysis solution in four phases:
+ [Ingestion phase ](ingestion-phase.md)– Prepare a PDF file type that your organization continuously generates (for example, a daily operations report) and that you need to regularly extract data from.
+ [Processing phase ](processing-phase.md)– Extract the data values required by your downstream applications from the PDF files.
+ [Data storage phase ](storage-phase.md)– Store the extracted data as a JSON file in [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) and as a record in a DynamoDB table.
+ [Analysis phase ](analysis-phase.md)– Create dashboards in Amazon Quick Sight to visualize and help analyze the data.

The guide uses [Amazon S3](https://docs.aws.amazon.com/amazonglacier/latest/dev/introduction.html) to store the raw and processed data, [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) for compute, [Amazon](https://docs.aws.amazon.com/textract/latest/dg/what-is.html)

[Textract](https://docs.aws.amazon.com/textract/latest/dg/what-is.html) to extract content from PDF files, [DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) to store the processed data, and [Amazon](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html)

[QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html) for analysis and visualizations. This guide is intended for data scientists, machine learning (ML) engineers, and solutions architects who want to automatically extract information and generate insights from PDF files.

## Targeted business outcomes
<a name="targeted-business-outcomes"></a>

You should expect the following three outcomes after designing an automated solution to analyze PDF files on the AWS Cloud:
+ Automatically process raw data from multiple PDF files at scale by using an automated solution that refreshes when new data becomes available.
+ Downstream modeling and analytics applications (for example, ML modeling in [Amazon SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html)) can access the extracted PDF file content.
+ Data dashboards that show all PDF file contents to your end users in Amazon Quick Sight.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
