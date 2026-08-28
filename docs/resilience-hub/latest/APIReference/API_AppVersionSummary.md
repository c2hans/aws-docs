---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_AppVersionSummary.html
---

# AppVersionSummary
<a name="API_AppVersionSummary"></a>

Version of an application.

## Contents
<a name="API_AppVersionSummary_Contents"></a>

 ** appVersion **   <a name="resiliencehub-Type-AppVersionSummary-appVersion"></a>
Version of an application.
Type: String
Pattern: `\S{1,50}`
Required: Yes

 ** creationTime **   <a name="resiliencehub-Type-AppVersionSummary-creationTime"></a>
Creation time of the application version.
Type: Timestamp
Required: No

 ** identifier **   <a name="resiliencehub-Type-AppVersionSummary-identifier"></a>
Identifier of the application version.
Type: Long
Required: No

 ** versionName **   <a name="resiliencehub-Type-AppVersionSummary-versionName"></a>
Name of the application version.
Type: String
Pattern: `\S{1,50}`
Required: No

## See Also
<a name="API_AppVersionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/AppVersionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/AppVersionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/AppVersionSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
