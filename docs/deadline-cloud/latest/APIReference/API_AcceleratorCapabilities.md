---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_AcceleratorCapabilities.html
---

# AcceleratorCapabilities
<a name="API_AcceleratorCapabilities"></a>

Provides information about the GPU accelerators used for jobs processed by a fleet.

**Important**
Accelerator capabilities cannot be used with wait-and-save fleets. If you specify accelerator capabilities, you must use either spot or on-demand instance market options.

**Note**
Each accelerator type maps to specific EC2 instance families:
 `t4`: Uses G4dn instance family
 `a10g`: Uses G5 instance family
 `l4`: Uses G6 and Gr6 instance families
 `l40s`: Uses G6e instance family
 `rtx-pro-server-6000`: Uses G7e instance family

## Contents
<a name="API_AcceleratorCapabilities_Contents"></a>

 ** selections **   <a name="deadlinecloud-Type-AcceleratorCapabilities-selections"></a>
A list of accelerator capabilities requested for this fleet. Only Amazon Elastic Compute Cloud instances that provide these capabilities will be used. For example, if you specify both L4 and T4 chips, AWS Deadline Cloud will use Amazon EC2 instances that have either the L4 or the T4 chip installed.
+ You must specify at least one accelerator selection.
+ You cannot specify the same accelerator name multiple times in the selections list.
+ All accelerators in the selections must use the same runtime version.
Type: Array of [AcceleratorSelection](API_AcceleratorSelection.md) objects
Required: Yes

 ** count **   <a name="deadlinecloud-Type-AcceleratorCapabilities-count"></a>
The number of GPU accelerators specified for worker hosts in this fleet.
You must specify either `acceleratorCapabilities.count.max` or `allowedInstanceTypes` when using accelerator capabilities. If you don't specify a maximum count, AWS Deadline Cloud uses the instance types you specify in `allowedInstanceTypes` to determine the maximum number of accelerators.
Type: [AcceleratorCountRange](API_AcceleratorCountRange.md) object
Required: No

## See Also
<a name="API_AcceleratorCapabilities_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/AcceleratorCapabilities)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/AcceleratorCapabilities)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/AcceleratorCapabilities)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
