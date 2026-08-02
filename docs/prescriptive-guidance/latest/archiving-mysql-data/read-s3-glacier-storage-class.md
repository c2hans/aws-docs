---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/archiving-mysql-data/read-s3-glacier-storage-class.html
---

# Reading archived S3 objects with S3 Glacier storage classes
<a name="read-s3-glacier-storage-class"></a>

Amazon S3 Glacier classes are special storage classes with inexpensive pricing but high retrieval time. Unlike S3 Standard objects, S3 Glacier objects can't be read as AWS Glue tables. To make the data available for analytical queries or reporting, you first restore the S3 Glacier objects. The restoration is an asynchronous process that happens over time and has a retention period. After the objects are restored, they can be copied to a different location as S3 Standard objects. Beyond the retention period, the restored objects transition back to Amazon S3 Glacier.

## Using S3 Batch Operations
<a name="using-s3-batch-operations.029c4daf-d3a3-5982-95aa-168808982ff5"></a>

S3 Batch Operations enables large-scale batch operations on Amazon S3 in the order of billions of objects containing exabytes of data. Amazon S3 tracks progress, sends notifications, and stores a detailed completion report of all actions, providing a fully managed, auditable, and serverless experience.

S3 Batch Operations supports the [Restore](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-initiate-restore-object.html) operation, which initiates S3 object restore for the following storage tiers:
+ Objects archived in the S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive storage classes
+ Objects archived through the S3 Intelligent-Tiering storage class in the Archive Access or Deep Archive Access tiers

The batch operation can be invoked both programmatically and on the Amazon S3 console. For input, it requires a .csv manifest file that contains the list objects to restore.

You can use an [Amazon S3 Inventory](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-inventory.html) report as an input for the batch work. The inventory report is configured for a bucket and can be limited to objects under specific prefixes. It is an automated report and gets generated either weekly or daily in either CSV, ORC, or Parquet format.

For more information about configuring an inventory report, see the [Amazon S3 documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/configure-inventory.html#configure-inventory-console). For information about using Boto3 to create an S3 Batch Operations job, see the [Boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3control.html#S3Control.Client.create_job).
