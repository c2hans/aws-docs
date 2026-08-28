---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetails.html
---

# AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetails
<a name="API_AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetails"></a>

 The minimum and maximum number of accelerators (GPUs, FPGAs, or AWS Inferentia chips) on an Amazon EC2 instance.

## Contents
<a name="API_AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetails_Contents"></a>

 ** Max **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetails-Max"></a>
 The maximum number of accelerators. If this parameter isn't specified, there's no maximum limit. To exclude accelerator-enabled instance types, set `Max` to `0`.
Type: Integer
Required: No

 ** Min **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetails-Min"></a>
 The minimum number of accelerators. If this parameter isn't specified, there's no minimum limit.
Type: Integer
Required: No

## See Also
<a name="API_AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
