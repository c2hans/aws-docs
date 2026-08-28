---
source_url: https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_JavaScriptSourceMaps.html
---

# JavaScriptSourceMaps
<a name="API_JavaScriptSourceMaps"></a>

 A structure that contains the configuration for how an app monitor can unminify JavaScript error stack traces using source maps.

## Contents
<a name="API_JavaScriptSourceMaps_Contents"></a>

 ** Status **   <a name="cloudwatchrum-Type-JavaScriptSourceMaps-Status"></a>
 Specifies whether JavaScript error stack traces should be unminified for this app monitor. The default is for JavaScript error stack trace unminification to be `DISABLED`.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

 ** S3Uri **   <a name="cloudwatchrum-Type-JavaScriptSourceMaps-S3Uri"></a>
 The S3Uri of the bucket or folder that stores the source map files. It is required if status is ENABLED.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `s3://[a-z0-9][-.a-z0-9]{1,62}(?:/[-!_*'().a-z0-9A-Z]+(?:/[-!_*'().a-z0-9A-Z]+)*)?/?`
Required: No

## See Also
<a name="API_JavaScriptSourceMaps_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rum-2018-05-10/JavaScriptSourceMaps)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rum-2018-05-10/JavaScriptSourceMaps)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rum-2018-05-10/JavaScriptSourceMaps)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for CloudWatch RUM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudwatchrum` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
