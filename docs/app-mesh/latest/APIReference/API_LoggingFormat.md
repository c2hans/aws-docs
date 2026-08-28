---
source_url: https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_LoggingFormat.html
---

# LoggingFormat
<a name="API_LoggingFormat"></a>

An object that represents the format for the logs.

## Contents
<a name="API_LoggingFormat_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** json **   <a name="appmesh-Type-LoggingFormat-json"></a>
The logging format for JSON.
Type: Array of [JsonFormatRef](API_JsonFormatRef.md) objects
Required: No

 ** text **   <a name="appmesh-Type-LoggingFormat-text"></a>
The logging format for text.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

## See Also
<a name="API_LoggingFormat_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/LoggingFormat)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/LoggingFormat)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/LoggingFormat)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Mesh. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query app-mesh` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
