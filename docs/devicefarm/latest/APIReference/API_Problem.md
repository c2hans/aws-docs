---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_Problem.html
---

# Problem
<a name="API_Problem"></a>

Represents a specific warning or failure.

## Contents
<a name="API_Problem_Contents"></a>

 ** device **   <a name="devicefarm-Type-Problem-device"></a>
Information about the associated device.
Type: [Device](API_Device.md) object
Required: No

 ** job **   <a name="devicefarm-Type-Problem-job"></a>
Information about the associated job.
Type: [ProblemDetail](API_ProblemDetail.md) object
Required: No

 ** message **   <a name="devicefarm-Type-Problem-message"></a>
A message about the problem's result.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 16384.
Required: No

 ** result **   <a name="devicefarm-Type-Problem-result"></a>
The problem's result.
Allowed values include:
+ PENDING
+ PASSED
+ WARNED
+ FAILED
+ SKIPPED
+ ERRORED
+ STOPPED
Type: String
Valid Values: `PENDING | PASSED | WARNED | FAILED | SKIPPED | ERRORED | STOPPED`
Required: No

 ** run **   <a name="devicefarm-Type-Problem-run"></a>
Information about the associated run.
Type: [ProblemDetail](API_ProblemDetail.md) object
Required: No

 ** suite **   <a name="devicefarm-Type-Problem-suite"></a>
Information about the associated suite.
Type: [ProblemDetail](API_ProblemDetail.md) object
Required: No

 ** test **   <a name="devicefarm-Type-Problem-test"></a>
Information about the associated test.
Type: [ProblemDetail](API_ProblemDetail.md) object
Required: No

## See Also
<a name="API_Problem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/Problem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/Problem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/Problem)
