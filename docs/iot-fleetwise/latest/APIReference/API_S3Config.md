---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_S3Config.html
---

# S3Config
<a name="API_S3Config"></a>

The Amazon S3 bucket where the AWS IoT FleetWise campaign sends data. Amazon S3 is an object storage service that stores data as objects within buckets. For more information, see [Creating, configuring, and working with Amazon S3 buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-buckets-s3.html) in the *Amazon Simple Storage Service User Guide*.

## Contents
<a name="API_S3Config_Contents"></a>

 ** bucketArn **   <a name="iotfleetwise-Type-S3Config-bucketArn"></a>
The Amazon Resource Name (ARN) of the Amazon S3 bucket.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 100.
Pattern: `arn:(aws[a-zA-Z0-9-]*):s3:::.+`
Required: Yes

 ** dataFormat **   <a name="iotfleetwise-Type-S3Config-dataFormat"></a>
Specify the format that files are saved in the Amazon S3 bucket. You can save files in an Apache Parquet or JSON format.
+ Parquet - Store data in a columnar storage file format. Parquet is optimal for fast data retrieval and can reduce costs. This option is selected by default.
+ JSON - Store data in a standard text-based JSON file format.
Type: String
Valid Values: `JSON | PARQUET`
Required: No

 ** prefix **   <a name="iotfleetwise-Type-S3Config-prefix"></a>
Enter an S3 bucket prefix. The prefix is the string of characters after the bucket name and before the object name. You can use the prefix to organize data stored in Amazon S3 buckets. For more information, see [Organizing objects using prefixes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html) in the *Amazon Simple Storage Service User Guide*.
By default, AWS IoT FleetWise sets the prefix `processed-data/year=YY/month=MM/date=DD/hour=HH/` (in UTC) to data it delivers to Amazon S3. You can enter a prefix to append it to this default prefix. For example, if you enter the prefix `vehicles`, the prefix will be `vehicles/processed-data/year=YY/month=MM/date=DD/hour=HH/`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[a-zA-Z0-9-_:./!*'()]+`
Required: No

 ** storageCompressionFormat **   <a name="iotfleetwise-Type-S3Config-storageCompressionFormat"></a>
By default, stored data is compressed as a .gzip file. Compressed files have a reduced file size, which can optimize the cost of data storage.
Type: String
Valid Values: `NONE | GZIP`
Required: No

## See Also
<a name="API_S3Config_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/S3Config)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/S3Config)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/S3Config)
