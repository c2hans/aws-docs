---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/APIReference/API_S3LogConfiguration.html
---

# S3LogConfiguration
<a name="API_S3LogConfiguration"></a>

The S3 log configuration.

## Contents
<a name="API_S3LogConfiguration_Contents"></a>

 ** bucket **   <a name="workspacesweb-Type-S3LogConfiguration-bucket"></a>
The S3 bucket name where logs are delivered.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9]`
Required: Yes

 ** folderStructure **   <a name="workspacesweb-Type-S3LogConfiguration-folderStructure"></a>
The folder structure that defines the organizational structure for log files in S3.
Type: String
Valid Values: `Flat | NestedByDate`
Required: Yes

 ** logFileFormat **   <a name="workspacesweb-Type-S3LogConfiguration-logFileFormat"></a>
The format of the LogFile that is written to S3.
Type: String
Valid Values: `JSONLines | Json`
Required: Yes

 ** bucketOwner **   <a name="workspacesweb-Type-S3LogConfiguration-bucketOwner"></a>
The expected bucket owner of the target S3 bucket. The caller must have permissions to write to the target bucket.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** keyPrefix **   <a name="workspacesweb-Type-S3LogConfiguration-keyPrefix"></a>
The S3 path prefix that determines where log files are stored.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\d\w\-_/!().*']+`
Required: No

## See Also
<a name="API_S3LogConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-web-2020-07-08/S3LogConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-web-2020-07-08/S3LogConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-web-2020-07-08/S3LogConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Secure Browser. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-web` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
