---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_StopCisMessageProgress.html
---

# StopCisMessageProgress
<a name="API_StopCisMessageProgress"></a>

The stop CIS message progress.

## Contents
<a name="API_StopCisMessageProgress_Contents"></a>

 ** errorChecks **   <a name="inspector2-Type-StopCisMessageProgress-errorChecks"></a>
The progress' error checks.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 65536.
Required: No

 ** failedChecks **   <a name="inspector2-Type-StopCisMessageProgress-failedChecks"></a>
The progress' failed checks.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 65536.
Required: No

 ** informationalChecks **   <a name="inspector2-Type-StopCisMessageProgress-informationalChecks"></a>
The progress' informational checks.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 65536.
Required: No

 ** notApplicableChecks **   <a name="inspector2-Type-StopCisMessageProgress-notApplicableChecks"></a>
The progress' not applicable checks.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 65536.
Required: No

 ** notEvaluatedChecks **   <a name="inspector2-Type-StopCisMessageProgress-notEvaluatedChecks"></a>
The progress' not evaluated checks.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 65536.
Required: No

 ** successfulChecks **   <a name="inspector2-Type-StopCisMessageProgress-successfulChecks"></a>
The progress' successful checks.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 65536.
Required: No

 ** totalChecks **   <a name="inspector2-Type-StopCisMessageProgress-totalChecks"></a>
The progress' total checks.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 65536.
Required: No

 ** unknownChecks **   <a name="inspector2-Type-StopCisMessageProgress-unknownChecks"></a>
The progress' unknown checks.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 65536.
Required: No

## See Also
<a name="API_StopCisMessageProgress_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/StopCisMessageProgress)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/StopCisMessageProgress)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/StopCisMessageProgress)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
