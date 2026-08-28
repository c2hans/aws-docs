---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_Ec2ScanModeState.html
---

# Ec2ScanModeState
<a name="API_Ec2ScanModeState"></a>

The state of your Amazon EC2 scan mode configuration.

## Contents
<a name="API_Ec2ScanModeState_Contents"></a>

 ** scanMode **   <a name="inspector2-Type-Ec2ScanModeState-scanMode"></a>
The scan method that is applied to the instance.
Type: String
Valid Values: `EC2_SSM_AGENT_BASED | EC2_HYBRID`
Required: No

 ** scanModeStatus **   <a name="inspector2-Type-Ec2ScanModeState-scanModeStatus"></a>
The status of the Amazon EC2 scan mode setting.
Type: String
Valid Values: `SUCCESS | PENDING`
Required: No

## See Also
<a name="API_Ec2ScanModeState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/Ec2ScanModeState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/Ec2ScanModeState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/Ec2ScanModeState)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
