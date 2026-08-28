---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_S3Location.html
---

# S3Location
<a name="API_S3Location"></a>

The location in Amazon S3 where build or script files are stored for access by Amazon GameLift Servers.

## Contents
<a name="API_S3Location_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Bucket **   <a name="gameliftservers-Type-S3Location-Bucket"></a>
An Amazon S3 bucket identifier. Thename of the S3 bucket.
Amazon GameLift Servers doesn't support uploading from Amazon S3 buckets with names that contain a dot (.).
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** Key **   <a name="gameliftservers-Type-S3Location-Key"></a>
The name of the zip file that contains the build files or script files.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** ObjectVersion **   <a name="gameliftservers-Type-S3Location-ObjectVersion"></a>
The version of the file, if object versioning is turned on for the bucket. Amazon GameLift Servers uses this information when retrieving files from an S3 bucket that you own. Use this parameter to specify a specific version of the file. If not set, the latest version of the file is retrieved.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** RoleArn **   <a name="gameliftservers-Type-S3Location-RoleArn"></a>
The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html)) for an IAM role that allows Amazon GameLift Servers to access the S3 bucket.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_S3Location_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/S3Location)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/S3Location)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/S3Location)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
