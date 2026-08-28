---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/automated-pdf-analysis-solution/analysis-phase.html
---

# Analysis
<a name="analysis-phase"></a>

By processing PDF files, you extract content that can be used for further processing and analysis. For example, you can identify cost trends by using the cost fields of daily operations reports or generate insights by aggregating key performance indicator (KPIs) for business operations. You can also combine extracted content with other data sources, including data lakes, data warehouses, third-party data, or customer relationship management (CRM) data to perform in-depth business analytics.

[Amazon QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html) is a serverless business intelligence service that connects to the Amazon Simple Storage Service (Amazon S3) bucket that contains your extracted PDF file data. Your business analysts can then create a dashboard to analyze, visualize, and directly generate insights from the JSON files in the S3 bucket. The dashboard connects to the S3 bucket and automatically updates after new PDF files are processed. You can also [share the dashboard with different users](https://docs.aws.amazon.com/quicksight/latest/user/sharing-a-dashboard.html) and users can also [subscribe to the dashboard](https://docs.aws.amazon.com/quicksight/latest/user/subscribing-to-reports.html) to view it on a mobile device. For more information about this, see [Creating a dataset using Amazon S3 files](https://docs.aws.amazon.com/quicksight/latest/user/create-a-data-set-s3.html) in the Amazon QuickSight documentation.

Most PDF files also contain rich text content inside forms and tables or in a free text paragraph. After the text content is extracted, the rich text content can be used by other AWS artificial intelligence and machine learning (AI/ML) services that can handle natural-language processing (NLP), such as [Amazon Comprehend](https://docs.aws.amazon.com/comprehend/latest/dg/comprehend-general.html) or [Amazon Translate](https://docs.aws.amazon.com/translate/latest/dg/what-is.html). You can also use [Amazon Kendra](https://docs.aws.amazon.com/kendra/latest/dg/what-is-kendra.html) for indexing and searching documents extracted from a large database of PDF files.

Your data scientists and ML engineers can also use Amazon SageMaker to directly access the extracted data in the S3 bucket or Amazon DynamoDB table and then implement advanced ML modeling and prediction.

## Best practices for the analysis phase
<a name="best-practices-analysis-phase"></a>

You can use the following two best practices to ensure a successful analytics phase:
+ Create a manifest file to use an S3 bucket as a data source for Amazon QuickSight. For more information about this, see [Create an analysis using your own Amazon S3 data](https://docs.aws.amazon.com/quicksight/latest/user/getting-started-create-analysis-s3.html) in the Quick documentation.
+ Automatically update your dataset to capture any new data added to Amazon S3 and refresh your dashboard. For more information about this, see [Refreshing a dataset on a schedule](https://docs.aws.amazon.com/quicksight/latest/user/refreshing-imported-data.html#schedule-data-refresh) in the Quick documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
