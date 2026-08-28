---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_AcceleratorCountRange.html
---

# AcceleratorCountRange
<a name="API_AcceleratorCountRange"></a>

Defines the maximum and minimum number of GPU accelerators required for a worker instance..

## Contents
<a name="API_AcceleratorCountRange_Contents"></a>

 ** min **   <a name="deadlinecloud-Type-AcceleratorCountRange-min"></a>
The minimum number of GPU accelerators in the worker host.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: Yes

 ** max **   <a name="deadlinecloud-Type-AcceleratorCountRange-max"></a>
The maximum number of GPU accelerators in the worker host.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: No

## See Also
<a name="API_AcceleratorCountRange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/AcceleratorCountRange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/AcceleratorCountRange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/AcceleratorCountRange)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
