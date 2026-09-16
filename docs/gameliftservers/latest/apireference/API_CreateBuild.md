---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_CreateBuild.html
---

# CreateBuild
<a name="API_CreateBuild"></a>

 **This API works with the following fleet types:** EC2, Anywhere

Creates a new Amazon GameLift Servers build resource for your game server binary files. Combine game server binaries into a zip file for use with Amazon GameLift Servers.

**Important**
When setting up a new game build for Amazon GameLift Servers, we recommend using the AWS CLI command ** [upload-build](https://docs.aws.amazon.com/cli/latest/reference/gamelift/upload-build.html) **. This helper command combines two tasks: (1) it uploads your build files from a file directory to an Amazon GameLift Servers Amazon S3 location, and (2) it creates a new build resource.

You can use the `CreateBuild` operation in the following scenarios:
+ Create a new game build with build files that are in an Amazon S3 location under an AWS account that you control. To use this option, you give Amazon GameLift Servers access to the Amazon S3 bucket. With permissions in place, specify a build name, operating system, and the Amazon S3 storage location of your game build.
+ Upload your build files to a Amazon GameLift Servers Amazon S3 location. To use this option, specify a build name and operating system. This operation creates a new build resource and also returns an Amazon S3 location with temporary access credentials. Use the credentials to manually upload your build files to the specified Amazon S3 location. For more information, see [Uploading Objects](https://docs.aws.amazon.com/AmazonS3/latest/dev/UploadingObjects.html) in the *Amazon S3 Developer Guide*. After you upload build files to the Amazon GameLift Servers Amazon S3 location, you can't update them.

If successful, this operation creates a new build resource with a unique build ID and places it in `INITIALIZED` status. A build must be in `READY` status before you can create fleets with it.

 **Learn more**

 [Uploading Your Game](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-build-intro.html)

 [ Create a Build with Files in Amazon S3](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-build-cli-uploading.html#gamelift-build-cli-uploading-create-build)

 [All APIs by task](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets)

## Request Syntax
<a name="API_CreateBuild_RequestSyntax"></a>

```
{
   "Name": "{{string}}",
   "OperatingSystem": "{{string}}",
   "ServerSdkVersion": "{{string}}",
   "StorageLocation": {
      "Bucket": "{{string}}",
      "Key": "{{string}}",
      "ObjectVersion": "{{string}}",
      "RoleArn": "{{string}}"
   },
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "Version": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateBuild_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Name](#API_CreateBuild_RequestSyntax) **   <a name="gameliftservers-CreateBuild-request-Name"></a>
A descriptive label that is associated with a build. Build names do not need to be unique. You can change this value later.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [OperatingSystem](#API_CreateBuild_RequestSyntax) **   <a name="gameliftservers-CreateBuild-request-OperatingSystem"></a>
The operating system that your game server binaries run on. This value determines the type of fleet resources that you use for this build. If your game build contains multiple executables, they all must run on the same operating system. You must specify a valid operating system in this request. There is no default value. You can't change a build's operating system later.
Amazon Linux 2 (AL2) will reach end of support on 6/30/2026. See more details in the [Amazon Linux 2 FAQs](http://aws.amazon.com/amazon-linux-2/faqs/). For game servers that are hosted on AL2 and use server SDK version 4.x for Amazon GameLift Servers, first update the game server build to server SDK 5.x, and then deploy to AL2023 instances. See [ Migrate to server SDK version 5.](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-serversdk5-migration.html)
Windows Server 2016 will reach end of support on 1/12/2027. For game servers that are hosted on Windows Server 2016 and use server SDK version 4.x for Amazon GameLift Servers, first update the game server build to server SDK 5.x, and then deploy to Windows Server 2022 instances. See [ Migrate to server SDK version 5.](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-serversdk5-migration.html)
Type: String
Valid Values: `WINDOWS_2012 | AMAZON_LINUX | AMAZON_LINUX_2 | WINDOWS_2016 | AMAZON_LINUX_2023 | WINDOWS_2022`
Required: No

 ** [ServerSdkVersion](#API_CreateBuild_RequestSyntax) **   <a name="gameliftservers-CreateBuild-request-ServerSdkVersion"></a>
A server SDK version you used when integrating your game server build with Amazon GameLift Servers. For more information see [Integrate games with custom game servers](https://docs.aws.amazon.com/gamelift/latest/developerguide/integration-custom-intro.html). By default Amazon GameLift Servers sets this value to `4.0.2`.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `^\d+\.\d+\.\d+$`
Required: No

 ** [StorageLocation](#API_CreateBuild_RequestSyntax) **   <a name="gameliftservers-CreateBuild-request-StorageLocation"></a>
Information indicating where your game build files are stored. Use this parameter only when creating a build with files stored in an Amazon S3 bucket that you own. The storage location must specify an Amazon S3 bucket name and key. The location must also specify a role ARN that you set up to allow Amazon GameLift Servers to access your Amazon S3 bucket. The S3 bucket and your new build must be in the same Region.
If a `StorageLocation` is specified, the size of your file can be found in your Amazon S3 bucket. Amazon GameLift Servers will report a `SizeOnDisk` of 0.
Type: [S3Location](API_S3Location.md) object
Required: No

 ** [Tags](#API_CreateBuild_RequestSyntax) **   <a name="gameliftservers-CreateBuild-request-Tags"></a>
A list of labels to assign to the new build resource. Tags are developer defined key-value pairs. Tagging AWS resources are useful for resource management, access management and cost allocation. For more information, see [ Tagging AWS Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the * AWS General Reference*. Once the resource is created, you can use [TagResource](https://docs.aws.amazon.com/gamelift/latest/apireference/API_TagResource.html), [UntagResource](https://docs.aws.amazon.com/gamelift/latest/apireference/API_UntagResource.html), and [ListTagsForResource](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ListTagsForResource.html) to add, remove, and view tags. The maximum tag limit may be lower than stated. See the AWS General Reference for actual tagging limits.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** [Version](#API_CreateBuild_RequestSyntax) **   <a name="gameliftservers-CreateBuild-request-Version"></a>
Version information that is associated with a build or script. Version strings do not need to be unique. You can change this value later.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_CreateBuild_ResponseSyntax"></a>

```
{
   "Build": {
      "BuildArn": "string",
      "BuildId": "string",
      "CreationTime": number,
      "Name": "string",
      "OperatingSystem": "string",
      "ServerSdkVersion": "string",
      "SizeOnDisk": number,
      "Status": "string",
      "Version": "string"
   },
   "StorageLocation": {
      "Bucket": "string",
      "Key": "string",
      "ObjectVersion": "string",
      "RoleArn": "string"
   },
   "UploadCredentials": {
      "AccessKeyId": "string",
      "SecretAccessKey": "string",
      "SessionToken": "string"
   }
}
```

## Response Elements
<a name="API_CreateBuild_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Build](#API_CreateBuild_ResponseSyntax) **   <a name="gameliftservers-CreateBuild-response-Build"></a>
The newly created build resource, including a unique build IDs and status.
Type: [Build](API_Build.md) object

 ** [StorageLocation](#API_CreateBuild_ResponseSyntax) **   <a name="gameliftservers-CreateBuild-response-StorageLocation"></a>
Amazon S3 location for your game build file, including bucket name and key.
Type: [S3Location](API_S3Location.md) object

 ** [UploadCredentials](#API_CreateBuild_ResponseSyntax) **   <a name="gameliftservers-CreateBuild-response-UploadCredentials"></a>
This element is returned only when the operation is called without a storage location. It contains credentials to use when you are uploading a build file to an Amazon S3 bucket that is owned by Amazon GameLift Servers. Credentials have a limited life span. To refresh these credentials, call [RequestUploadCredentials](https://docs.aws.amazon.com/gamelift/latest/apireference/API_RequestUploadCredentials.html).
Type: [AwsCredentials](API_AwsCredentials.md) object

## Errors
<a name="API_CreateBuild_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.

HTTP Status Code: 400

 ** InternalServiceException **
The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.
HTTP Status Code: 500

 ** InvalidRequestException **
One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.
HTTP Status Code: 400

 ** TaggingFailedException **
The requested tagging operation did not succeed. This may be due to invalid tag format or the maximum tag limit may have been exceeded. Resolve the issue before retrying.
HTTP Status Code: 400

 ** UnauthorizedException **
The client failed authentication. Clients should not retry such requests.
HTTP Status Code: 400

## Examples
<a name="API_CreateBuild_Examples"></a>

### Create a build with files in your own S3 bucket
<a name="API_CreateBuild_Example_1"></a>

This example creates a custom game build resource. It uses zipped files that are stored in an S3 location in an AWS account that you control. This example assumes that you've already created an IAM role that gives Amazon GameLift Servers permission to access the S3 location. The request must specify a valid operating system value.

#### Sample Request
<a name="API_CreateBuild_Example_1_Request"></a>

```
{
    "Name": "MegaFrogRaceServer.NA",
    "Version": "12345.678",
    "OperatingSystem": "WINDOWS_2022",
    "StorageLocation": {
        "Bucket": "MegaFrogRaceServer_NA_build_files",
        "Key": "MegaFrogRaceServer_build_123.zip",
        "RoleArn": "arn:aws:iam::111122223333:role/GameLiftAccess"
    }
}
```

#### Sample Response
<a name="API_CreateBuild_Example_1_Response"></a>

```
{
    "Build": {
        "BuildArn": "arn:aws:gamelift:us-west-2::build/build-1111aaaa-22bb-33cc-44dd-5555eeee66ff",
        "BuildId": "build-1111aaaa-22bb-33cc-44dd-5555eeee66ff",
        "CreationTime": 1496708916.18,
        "Name": "MegaFrogRaceServer.NA",
        "OperatingSystem": "WINDOWS_2022",
        "SizeOnDisk": 0,
        "Status": "READY",
        "Version": "12345.678"
    },
    "StorageLocation": {
        "Bucket": "MegaFrogRaceServer_NA_build_files",
        "Key": "MegaFrogRaceServer_build_123.zip"
    }
}
```

### Create a game build resource for manually uploading files to Amazon GameLift Servers
<a name="API_CreateBuild_Example_2"></a>

This example creates a new build resource. It also gets a storage location and temporary credentials that allow you to manually upload your game build to the Amazon GameLift Servers location in Amazon S3. When you specify a storage location, Amazon GameLift Servers reports the `SizeOnDisk` as `0`. You can find the actual size in Amazon S3. After you upload your build, Amazon GameLift Servers validates the build and updates the new build's status. The request must specify a valid operating system value.

#### Sample Request
<a name="API_CreateBuild_Example_2_Request"></a>

```
{
    "Name": "MegaFrogRaceServer.NA",
    "Version": "12345.678",
    "OperatingSystem": "AMAZON_LINUX_2023"
}
```

#### Sample Response
<a name="API_CreateBuild_Example_2_Response"></a>

```
{
    "Build": {
        "BuildArn": "arn:aws:gamelift:us-west-2::build/build-1111aaaa-22bb-33cc-44dd-5555eeee66ff",
        "BuildId": "build-1111aaaa-22bb-33cc-44dd-5555eeee66ff",
        "CreationTime": 1496708916.18,
        "Name": "MegaFrogRaceServer.NA",
        "OperatingSystem": "AMAZON_LINUX_2023",
        "SizeOnDisk": 0,
        "Status": "READY",
        "Version": "12345.678"
    },
    "StorageLocation": {
        "Bucket": "gamelift-builds-us-west-2",
        "Key": "123456789012/build-1111aaaa-22bb-33cc-44dd-5555eeee66ff"
    },
    "UploadCredentials": {
        "AccessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "SecretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
        "SessionToken": "AgoGb3JpZ2luENz...EXAMPLETOKEN=="
    }
}
```

## See Also
<a name="API_CreateBuild_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/CreateBuild)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/CreateBuild)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/CreateBuild)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/CreateBuild)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/CreateBuild)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/CreateBuild)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/CreateBuild)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/CreateBuild)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/CreateBuild)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/CreateBuild)
