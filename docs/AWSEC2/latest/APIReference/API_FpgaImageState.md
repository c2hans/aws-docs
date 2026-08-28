---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_FpgaImageState.html
---

# FpgaImageState
<a name="API_FpgaImageState"></a>

Describes the state of the bitstream generation process for an Amazon FPGA image (AFI).

## Contents
<a name="API_FpgaImageState_Contents"></a>

 ** code **
The state. The following are the possible values:
+  `pending` - AFI bitstream generation is in progress.
+  `available` - The AFI is available for use.
+  `failed` - AFI bitstream generation failed.
+  `unavailable` - The AFI is no longer available for use.
Type: String
Valid Values: `pending | failed | available | unavailable`
Required: No

 ** message **
If the state is `failed`, this is the error message.
Type: String
Required: No

## See Also
<a name="API_FpgaImageState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/FpgaImageState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/FpgaImageState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/FpgaImageState)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
