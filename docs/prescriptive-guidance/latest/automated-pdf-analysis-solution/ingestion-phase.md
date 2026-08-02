---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/automated-pdf-analysis-solution/ingestion-phase.html
---

# Ingestion phase
<a name="ingestion-phase"></a>

Your organization identifies a PDF file type that is continuously generated (for example, a daily operations report), has an identical format, and that you need to automatically and regularly extract data from. To ingest this PDF file, you need an Amazon Simple Storage Service (Amazon S3) bucket and we recommend that you create a dedicated S3 bucket. However, you can also use an existing S3 bucket. For more information about this, see [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html) in the Amazon S3 documentation.

The S3 bucket invokes an AWS Lambda function when the new PDF file is ingested. For more information about this, see [Using an Amazon S3 trigger to invoke a Lambda function](https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example.html) in the AWS Lambda documentation.

The Lambda function then processes the PDF file. This process is described in the [Processing phase ](processing-phase.md)section of this guide.

## Best practices for the ingestion phase
<a name="best-practices-ingestion"></a>

Use the following four best practices to ensure a successful PDF file ingestion:
+ Use bulk ingestion for historical PDF files and continuous ingestion for new PDF files.
+ For bulk ingestion, use bulk dump (for example, uploading PDF files from a local drive). If you have more than one PDF file type, we recommend that you use different folders to hold each type of PDF file. We also recommend using a unique and descriptive naming standard for the files, such as warehouse\_<wharehouse\_number>\_<mmddyy>\_<PDF\_file\_type>.pdf.
+ To continuously ingest new PDF files, your source system must connect to your S3 bucket. For example, you can set up a daily dump from your source system to the S3 bucket.
+ Make sure that your PDF files are of good quality and clearly readable. We recommend using native PDF files, but you can also use scanned documents that are converted to a PDF format if the individual words are clear. For more information about this, see [PDF file preprocessing with Amazon Textract: Visuals detection and removal](https://aws.amazon.com/blogs/machine-learning/process-text-and-images-in-pdf-documents-with-amazon-textract/) on the AWS Machine Learning Blog.
