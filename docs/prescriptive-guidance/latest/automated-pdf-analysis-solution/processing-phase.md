---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/automated-pdf-analysis-solution/processing-phase.html
---

# Processing phase
<a name="processing-phase"></a>

Amazon Textract extracts PDF file contents as strings that cannot be directly used by downstream applications (for example, to generate statistics by aggregating numbers). Correctly identified and transformed data values are required because they can be more easily used by your downstream applications (for example, to plot cost trends as a time series). To implement PDF file processing, one PDF file from each new PDF file type must be processed one-time through Amazon Textract, which then generates a JSON-formatted Template file.

After the AWS Lambda function is initiated in the [Ingestion phase](ingestion-phase.md), it runs the steps shown in the following diagram.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/automated-pdf-analysis-solution/images/guide-img/689cce75-c135-4cff-9a10-7c6bc4f61a19/images/46fec87a-b1a6-48a1-bb16-5de50578c62c.png)

The diagram shows the Lambda function implementing the following steps:

1. Calls Amazon Textract to process the PDF file, extract the content, and return a JSON-formatted file.

1. Takes the JSON file and parses out forms and tables by using a predefined Template JSON file that has the correct key name and value type for each field. This process provides a parsed JSON file.

1. Applies the post-processing rules and uses the Template JSON file to correct each value in the parsed JSON file. This produces the Final JSON file. The predefined Template JSON file can be stored in the S3 bucket.

1. Stores the Final JSON file in Amazon DynamoDB as one record for each PDF file, in addition to one JSON file for each PDF file in an S3 output bucket.

For a step-by-step workflow that uses Amazon Textract to automatically extract content from PDF files and process it into a clean output, see the pattern [Automatically extract content from PDF files using Amazon Textract](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-extract-content-from-pdf-files-using-amazon-textract.html) on the AWS Prescriptive Guidance website. The pattern uses a template matching technique to correctly identify the required field, key name, and tables, and then applies post-processing corrections to each data type.

## Best practices for the processing phase
<a name="best-practices-processing"></a>

Use the following four best practices to ensure a successful processing phase:
+ Create a template JSON file for each PDF file type that you want to process. You can store these different template JSON files in an S3 bucket that is called by the Lambda function. If you want to process different PDF file types in one Lambda function, you should use a unique identifier for each PDF file type (for example, the PDF file type's folder name in the S3 bucket). After the Lambda function is invoked, it retrieves the appropriate template JSON file and processes it.
+ Set up a mechanism to accurately track the status of each step in the Lambda function. For example, you could add Success statuses for after the Amazon Textract call, when the final JSON file is saved to an Amazon DynamoDB table, or when the PDF files are saved to an S3 bucket. You can also create a separate DynamoDB table to track the status of each PDF file in the different steps, which provides visibility into the process.
+ Manage throttling and dropped connections by automatically retrying failed operations when you batch process many PDF files. Throttling can occur in Amazon Textract if your connection drops or you exceed the maximum number of transactions per second (TPS). For more information and steps to automatically retry failed operations, see [Handling throttled calls and dropped connections](https://docs.aws.amazon.com/textract/latest/dg/handling-errors.html) in the Amazon Textract documentation.
+ If you have PDF files with multiple pages, you can either use an asynchronous operation to process the entire file or break up the PDF file into an individual page, use a synchronous operation to process each page, and then combine each page's results. For a complete code implementation of an asynchronous operation, see [Detecting and analyzing text in multipage documents](https://docs.aws.amazon.com/textract/latest/dg/async-analyzing-with-sqs.html) in the Amazon Textract documentation. For more information about using a synchronous operation, see [Detecting and analyzing text in single-page documents](https://docs.aws.amazon.com/textract/latest/dg/sync.html) in the Amazon Textract documentation.
