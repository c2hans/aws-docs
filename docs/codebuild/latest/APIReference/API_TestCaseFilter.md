---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_TestCaseFilter.html
---

# TestCaseFilter
<a name="API_TestCaseFilter"></a>

A filter used to return specific types of test cases. In order to pass the filter, the report must meet all of the filter properties.

## Contents
<a name="API_TestCaseFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** keyword **   <a name="CodeBuild-Type-TestCaseFilter-keyword"></a>
A keyword that is used to filter on the `name` or the `prefix` of the test cases. Only test cases where the keyword is a substring of the `name` or the `prefix` will be returned.
Type: String
Required: No

 ** status **   <a name="CodeBuild-Type-TestCaseFilter-status"></a>
The status used to filter test cases. A `TestCaseFilter` can have one status. Valid values are:
+  `SUCCEEDED`
+  `FAILED`
+  `ERROR`
+  `SKIPPED`
+  `UNKNOWN`
Type: String
Required: No

## See Also
<a name="API_TestCaseFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/TestCaseFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/TestCaseFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/TestCaseFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
