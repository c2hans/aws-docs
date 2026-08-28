---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_ErrorInfo.html
---

# ErrorInfo
<a name="API_ErrorInfo"></a>

 Provides details in the event of a failed flow, including the failure count and the related error messages.

## Contents
<a name="API_ErrorInfo_Contents"></a>

 ** executionMessage **   <a name="appflow-Type-ErrorInfo-executionMessage"></a>
 Specifies the error message that appears if a flow fails.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `[\s\w/!@#+=.-]*`
Required: No

 ** putFailuresCount **   <a name="appflow-Type-ErrorInfo-putFailuresCount"></a>
 Specifies the failure count for the attempted flow.
Type: Long
Required: No

## See Also
<a name="API_ErrorInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/ErrorInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/ErrorInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/ErrorInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AmazonAppFlow. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appflow` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
