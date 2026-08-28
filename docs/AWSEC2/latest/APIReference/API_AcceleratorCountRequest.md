---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AcceleratorCountRequest.html
---

# AcceleratorCountRequest
<a name="API_AcceleratorCountRequest"></a>

The minimum and maximum number of accelerators (GPUs, FPGAs, or AWS Inferentia chips) on an instance. To exclude accelerator-enabled instance types, set `Max` to `0`.

## Contents
<a name="API_AcceleratorCountRequest_Contents"></a>

 ** Max **
The maximum number of accelerators. To specify no maximum limit, omit this parameter. To exclude accelerator-enabled instance types, set `Max` to `0`.
Type: Integer
Required: No

 ** Min **
The minimum number of accelerators. To specify no minimum limit, omit this parameter.
Type: Integer
Required: No

## See Also
<a name="API_AcceleratorCountRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/AcceleratorCountRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/AcceleratorCountRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/AcceleratorCountRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
