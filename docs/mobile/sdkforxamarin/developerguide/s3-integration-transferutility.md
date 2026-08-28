---
source_url: https://docs.aws.amazon.com/mobile/sdkforxamarin/developerguide/s3-integration-transferutility.html
---

The AWS Mobile SDK for Xamarin is now included in the AWS SDK for .NET. This guide references the archived version of the Mobile SDK for Xamarin.

# Using the S3 Transfer Utility
<a name="s3-integration-transferutility"></a>

The S3 Transfer Utility makes it easier to upload and download files to S3 from your Xamarin application.

## Initialize the TransferUtility
<a name="initialize-the-transferutility"></a>

Create an S3 client, passing it your AWS credentials object, and then pass the S3 client to the transfer utility, like so:

```
var s3Client = new AmazonS3Client(credentials,region);
var transferUtility = new TransferUtility(s3Client);
```

## (optional) Configure the TransferUtility
<a name="optional-configure-the-transferutility"></a>

There are three optional properties that you can configure:
+  **ConcurrentServiceRequests** - Determines how many active threads or the number of concurrent asynchronous web requests will be used to upload/download the file. The default value is 10.
+  **MinSizeBeforePartUpload** - Gets or sets the minimum part size for upload parts in bytes. The default is 16 MB. Decreasing the minimum part size causes multipart uploads to be split into a larger number of smaller parts. Setting this value too low has a negative effect on transfer speeds, causing extra latency and network communication for each part.
+  **NumberOfUploadThreads** - Gets or sets the number of executing threads. This property determines how many active threads will be used to upload the file. The default value is 10 threads.

To configure the S3 TransferUtility client, create a config object, set your properties, and pass the object to to your TransferUtility constructor like so:

```
var config = new TransferUtilityConfig();

config.ConcurrentServiceRequests = 10;
config.MinSizeBeforePartUpload=16*1024*1024;
config.NumberOfUploadThreads=10;

var s3Client = new AmazonS3Client(credentials);
var utility = new TransferUtility(s3Client,config);
```

## Download a File
<a name="download-a-file"></a>

To download a file from S3, call `Download` on the Transfer Utility object, passing the following parameters:
+  `file` - String name of the file that you want to download
+  `bucketName` - String name of the S3 bucket from which you want to download the file
+  `key` - A string representing the name of the S3 object (a file in this case) to download

```
transferUtility.Download(
  Path.Combine(Environment.SpecialFolder.ApplicationData,"file"),
  "bucketName",
  "key"
);
```

## Upload a File
<a name="upload-a-file"></a>

To upload a file to S3, call `Upload` on the Transfer Utility object, passing the following parameters:
+  `file` - String name of the file that you want to upload
+  `bucketName` - String name of the S3 bucket to store the file

```
transferUtility.Upload(
  Path.Combine(Environment.SpecialFolder.ApplicationData,"file"),
  "bucketName"
);
```

The code above assumes that there is a file in the directory Environment.SpecialFolder.ApplicationData. Uploads automatically use S3’s multi-part upload functionality on large files to enhance throughput.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Mobile SDK for Xamarin. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mobile` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
