---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_TestCase.html
---

# TestCase
<a name="API_TestCase"></a>

 Information about a test case created using a framework such as NUnit or Cucumber. A test case might be a unit test or a configuration test.

## Contents
<a name="API_TestCase_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** durationInNanoSeconds **   <a name="CodeBuild-Type-TestCase-durationInNanoSeconds"></a>
 The number of nanoseconds it took to run this test case.
Type: Long
Required: No

 ** expired **   <a name="CodeBuild-Type-TestCase-expired"></a>
 The date and time a test case expires. A test case expires 30 days after it is created. An expired test case is not available to view in CodeBuild.
Type: Timestamp
Required: No

 ** message **   <a name="CodeBuild-Type-TestCase-message"></a>
 A message associated with a test case. For example, an error message or stack trace.
Type: String
Required: No

 ** name **   <a name="CodeBuild-Type-TestCase-name"></a>
 The name of the test case.
Type: String
Required: No

 ** prefix **   <a name="CodeBuild-Type-TestCase-prefix"></a>
 A string that is applied to a series of related test cases. CodeBuild generates the prefix. The prefix depends on the framework used to generate the tests.
Type: String
Required: No

 ** reportArn **   <a name="CodeBuild-Type-TestCase-reportArn"></a>
 The ARN of the report to which the test case belongs.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** status **   <a name="CodeBuild-Type-TestCase-status"></a>
 The status returned by the test case after it was run. Valid statuses are `SUCCEEDED`, `FAILED`, `ERROR`, `SKIPPED`, and `UNKNOWN`.
Type: String
Required: No

 ** testRawDataPath **   <a name="CodeBuild-Type-TestCase-testRawDataPath"></a>
 The path to the raw data file that contains the test result.
Type: String
Required: No

 ** testSuiteName **   <a name="CodeBuild-Type-TestCase-testSuiteName"></a>
The name of the test suite that the test case is a part of.
Type: String
Required: No

## See Also
<a name="API_TestCase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/TestCase)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/TestCase)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/TestCase)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
