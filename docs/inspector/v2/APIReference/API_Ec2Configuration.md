---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_Ec2Configuration.html
---

# Ec2Configuration
<a name="API_Ec2Configuration"></a>

Enables agent-based scanning, which scans instances that are not managed by SSM.

## Contents
<a name="API_Ec2Configuration_Contents"></a>

 ** scanMode **   <a name="inspector2-Type-Ec2Configuration-scanMode"></a>
The scan method that is applied to the instance.
Type: String
Valid Values: `EC2_SSM_AGENT_BASED | EC2_HYBRID`
Required: Yes

 ** activateVMScanner **   <a name="inspector2-Type-Ec2Configuration-activateVMScanner"></a>
Whether to activate Amazon Inspector VM scanner for Amazon EC2 scanning.
Type: Boolean
Required: No

## See Also
<a name="API_Ec2Configuration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/Ec2Configuration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/Ec2Configuration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/Ec2Configuration)
