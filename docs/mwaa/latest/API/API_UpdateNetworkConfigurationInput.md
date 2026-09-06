---
source_url: https://docs.aws.amazon.com/mwaa/latest/API/API_UpdateNetworkConfigurationInput.html
---

# UpdateNetworkConfigurationInput
<a name="API_UpdateNetworkConfigurationInput"></a>

Defines the VPC networking components used to secure and enable network traffic between the AWS resources for your environment. For more information, refer to [About networking on Amazon MWAA](https://docs.aws.amazon.com/mwaa/latest/userguide/networking-about.html).

## Contents
<a name="API_UpdateNetworkConfigurationInput_Contents"></a>

 ** SecurityGroupIds **   <a name="mwaa-Type-UpdateNetworkConfigurationInput-SecurityGroupIds"></a>
A list of security group IDs. A security group must be attached to the same VPC as the subnets. For more information, refer to [Security in your VPC on Amazon MWAA](https://docs.aws.amazon.com/mwaa/latest/userguide/vpc-security.html).
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `sg-[a-zA-Z0-9\-._]+`
Required: Yes

## See Also
<a name="API_UpdateNetworkConfigurationInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mwaa-2020-07-01/UpdateNetworkConfigurationInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mwaa-2020-07-01/UpdateNetworkConfigurationInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mwaa-2020-07-01/UpdateNetworkConfigurationInput)
