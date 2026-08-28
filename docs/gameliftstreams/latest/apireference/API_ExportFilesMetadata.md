---
source_url: https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ExportFilesMetadata.html
---

# ExportFilesMetadata
<a name="API_ExportFilesMetadata"></a>

Provides details about the stream session's exported files.

## Contents
<a name="API_ExportFilesMetadata_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** OutputUri **   <a name="gameliftstreams-Type-ExportFilesMetadata-OutputUri"></a>
 The S3 bucket URI where Amazon GameLift Streams uploaded the set of compressed exported files for a stream session. Amazon GameLift Streams generates a ZIP file name based on the stream session metadata. Alternatively, you can provide a custom file name with a `.zip` file extension.
 Example 1: If you provide an S3 URI called `s3://amzn-s3-demo-destination-bucket/MyGame_Session1.zip`, then Amazon GameLift Streams will save the files at that location.
 Example 2: If you provide an S3 URI called `s3://amzn-s3-demo-destination-bucket/MyGameSessions_ExportedFiles/`, then Amazon GameLift Streams will save the files at `s3://amzn-s3-demo-destination-bucket/MyGameSessions_ExportedFiles/YYYYMMDD-HHMMSS-appId-sg-Id-sessionId.zip` or another similar name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `s3://.*(/|\.zip|\.ZIP)`
Required: No

 ** Status **   <a name="gameliftstreams-Type-ExportFilesMetadata-Status"></a>
The result of the [ExportStreamSessionFiles](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ExportStreamSessionFiles.html) operation.
Type: String
Valid Values: `SUCCEEDED | FAILED | PENDING`
Required: No

 ** StatusReason **   <a name="gameliftstreams-Type-ExportFilesMetadata-StatusReason"></a>
A short description of the reason the export is in `FAILED` status.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## See Also
<a name="API_ExportFilesMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gameliftstreams-2018-05-10/ExportFilesMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gameliftstreams-2018-05-10/ExportFilesMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gameliftstreams-2018-05-10/ExportFilesMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftstreams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
