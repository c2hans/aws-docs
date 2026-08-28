---
source_url: https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_FileAccessLog.html
---

# FileAccessLog
<a name="API_FileAccessLog"></a>

An object that represents an access log file.

## Contents
<a name="API_FileAccessLog_Contents"></a>

 ** path **   <a name="appmesh-Type-FileAccessLog-path"></a>
The file path to write access logs to. You can use `/dev/stdout` to send access logs to standard out and configure your Envoy container to use a log driver, such as `awslogs`, to export the access logs to a log storage service such as Amazon CloudWatch Logs. You can also specify a path in the Envoy container's file system to write the files to disk.
The Envoy process must have write permissions to the path that you specify here. Otherwise, Envoy fails to bootstrap properly.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** format **   <a name="appmesh-Type-FileAccessLog-format"></a>
The specified format for the logs. The format is either `json_format` or `text_format`.
Type: [LoggingFormat](API_LoggingFormat.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_FileAccessLog_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/FileAccessLog)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/FileAccessLog)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/FileAccessLog)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Mesh. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query app-mesh` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
