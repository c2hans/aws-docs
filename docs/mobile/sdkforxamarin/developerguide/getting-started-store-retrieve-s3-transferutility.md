---
source_url: https://docs.aws.amazon.com/mobile/sdkforxamarin/developerguide/getting-started-store-retrieve-s3-transferutility.html
---

The AWS Mobile SDK for Xamarin is now included in the AWS SDK for .NET. This guide references the archived version of the Mobile SDK for Xamarin.

# Store and Retrieve Files with Amazon S3
<a name="getting-started-store-retrieve-s3-transferutility"></a>

Amazon Simple Storage Service (Amazon S3) provides mobile developers with secure, durable, highly-scalable object storage. Amazon S3 is easy to use, with a simple web services interface to store and retrieve any amount of data from anywhere on the web.

The tutorial below explains how to integrate the S3 TransferUtility, a high-level utility for using S3 with your app. For more information about using S3 from Xamarin applications, see [Amazon Simple Storage Service (S3)](s3.md).

## Project Setup
<a name="project-setup"></a>

### Prerequisites
<a name="prerequisites"></a>

You must complete all of the instructions on the [Setting Up the AWS Mobile SDK for .NET and Xamarin](setup.md) before beginning this tutorial.

This tutorial also assumes you have already created an S3 bucket. To create an S3 bucket, visit the [S3 AWS Console](https://console.aws.amazon.com/s3/home).

### Set Permissions for S3
<a name="set-permissions-for-s3"></a>

The default IAM role policy grants your application access to Amazon Mobile Analytics and Amazon Cognito Sync. In order for your Cognito identity pool to access Amazon S3, you must modify the identity pool’s roles.

1. Go to the [Identity and Access Management Console](https://console.aws.amazon.com/iam/home) and click **Roles** in the left-hand pane.

1. Type your identity pool name into the search box. Two roles will be listed: one for unauthenticated users and one for authenticated users.

1. Click the role for unauthenticated users (it will have unauth appended to your identity pool name).

1. Click **Create Role Policy**, select **Policy Generator**, and then click **Select**.

1. On the **Edit Permissions** page, enter the settings shown in the following image, replacing the Amazon Resource Name (ARN) with your own. The ARN of an S3 bucket looks like `arn:aws:s3:::examplebucket/*` and is composed of the region in which the bucket is located and the name of the bucket. The settings shown below will give your identity pool full to access to all actions for the specified bucket.
![](http://docs.aws.amazon.com/mobile/sdkforxamarin/developerguide/images/edit-permissions.png)

1. Click the **Add Statement** button and then click **Next Step**.

1. The Wizard will show you the configuration that you generated. Click **Apply Policy**.

For more information on granting access to S3, see [Granting Access to an Amazon S3 Bucket](http://blogs.aws.amazon.com/security/post/Tx3VRSWZ6B3SHAV/Writing-IAM-Policies-How-to-grant-access-to-an-Amazon-S3-bucket).

### Add NuGet Package for S3 to Your Project
<a name="add-nuget-package-for-s3-to-your-project"></a>

Follow Step 4 of the instructions in [Setting Up the AWS Mobile SDK for .NET and Xamarin](setup.md) to add the S3 NuGet package to your project.

### (optional) Configure the Signature Version for S3 Requests
<a name="optional-configure-the-signature-version-for-s3-requests"></a>

Every interaction with Amazon S3 is either authenticated or anonymous. AWS uses the Signature Version 4 or Signature Version 2 algorithms to authenticate calls to the service.

All new AWS regions created after January 2014 only support Signature Version 4. However, many older regions still support Signature Version 4 and Signature Version 2 requests.

If your bucket is in one of the regions that does not support Signature Version 2 requests as listed on [this page](https://docs.aws.amazon.com/general/latest/gr/signature-version-2.html), you must set the AWSConfigsS3.UseSignatureVersion4 property to “true” like so:

```
AWSConfigsS3.UseSignatureVersion4 = true;
```

For more information on AWS Signature versions, see [Authenticating Requests (AWS Signature Version 4)](https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html).

## Initialize the S3 TransferUtility Client
<a name="initialize-the-s3-transferutility-client"></a>

Create an S3 client, passing it your AWS credentials object, and then pass the S3 client to the transfer utility, like so:

```
var s3Client = new AmazonS3Client(credentials,region);
var transferUtility = new TransferUtility(s3Client);
```

## Upload a File to Amazon S3
<a name="upload-a-file-to-amazon-s3"></a>

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

## Download a File from Amazon S3
<a name="download-a-file-from-amazon-s3"></a>

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

For more information on accessing Amazon S3 from an Xamarin application, see [Amazon Simple Storage Service (S3)](s3.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Mobile SDK for Xamarin. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mobile` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
