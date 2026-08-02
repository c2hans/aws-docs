---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/automated-pdf-analysis-solution/storage-phase.html
---

# Data storage phase
<a name="storage-phase"></a>

Because PDF file contents typically include forms (key-value pairs), tables, and free text, the JSON file must include nested key-value pairs to represent the PDF file structure and store the extracted data. PDF files are unstructured or semi-structured data, which means they don't have a fixed schema. This means that it can be challenging to store PDF file contents in a traditional SQL database. However, a NoSQL database is ideal for storing PDF file contents because it doesn't require a predefined schema. After PDF file contents are extracted and post-processed, you can store them as one record for each PDF file in an Amazon DynamoDB table.

We recommend that you store the final extracted data as a JSON file in Amazon Simple Storage Service (Amazon S3) and as a record in a DynamoDB table. Your downstream processing and analytics applications can easily reference JSON files in Amazon S3. For example, they can use Amazon S3 as a data source for building ML models in Amazon SageMaker, [directly query the JSON file using Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-JSON.html), or use Amazon S3 as the [data source for Amazon QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/create-a-data-set-s3.html). Extracted PDF file contents stored in DynamoDB tables can be easily accessed with low-latency at any scale, which makes this approach appropriate to use as your backend database for querying and scanning.

## Best practices for the data storage phase
<a name="best-practices-for-the-data-storage-phase"></a>

Use the following two best practices to ensure a successful data storage phase:
+ Make sure that you store the final JSON file on Amazon S3 in a different output folder and use a name based on the PDF file type.
+ DynamoDB uses a primary key to uniquely identify each item in a table. The primary key can be a single key (for example, a partition key) or a composite one (for example, a partition key and a sort key). For this solution's primary key, we recommend that you use either a unique PDF file identifier (for example, the PDF file name) as the partition key or a combination of two identifiers (for example, date and warehouse name) as the partition key and sort key. For more information about this, see [Core components of Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html) in the Amazon DynamoDB documentation.
