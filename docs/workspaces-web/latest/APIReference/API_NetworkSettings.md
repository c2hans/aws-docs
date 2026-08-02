---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/APIReference/API_NetworkSettings.html
---

# NetworkSettings
<a name="API_NetworkSettings"></a>

A network settings resource that can be associated with a web portal. Once associated with a web portal, network settings define how streaming instances will connect with your specified VPC.

## Contents
<a name="API_NetworkSettings_Contents"></a>

 ** networkSettingsArn **   <a name="workspacesweb-Type-NetworkSettings-networkSettingsArn"></a>
The ARN of the network settings.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=\/,.@-]+:[a-zA-Z0-9\-]+:[a-zA-Z0-9\-]*:[a-zA-Z0-9]{1,12}:[a-zA-Z]+(\/[a-fA-F0-9\-]{36})+`
Required: Yes

 ** associatedPortalArns **   <a name="workspacesweb-Type-NetworkSettings-associatedPortalArns"></a>
A list of web portal ARNs that this network settings is associated with.
Type: Array of strings
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=\/,.@-]+:[a-zA-Z0-9\-]+:[a-zA-Z0-9\-]*:[a-zA-Z0-9]{1,12}:[a-zA-Z]+(\/[a-fA-F0-9\-]{36})+`
Required: No

 ** securityGroupIds **   <a name="workspacesweb-Type-NetworkSettings-securityGroupIds"></a>
One or more security groups used to control access from streaming instances to your VPC.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+\-]+`
Required: No

 ** subnetIds **   <a name="workspacesweb-Type-NetworkSettings-subnetIds"></a>
The subnets in which network interfaces are created to connect streaming instances to your VPC. At least two of these subnets must be in different availability zones.
Type: Array of strings
Array Members: Minimum number of 2 items. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `subnet-([0-9a-f]{8}|[0-9a-f]{17})`
Required: No

 ** vpcId **   <a name="workspacesweb-Type-NetworkSettings-vpcId"></a>
The VPC that streaming instances will connect to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `vpc-[0-9a-z]*`
Required: No

## See Also
<a name="API_NetworkSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-web-2020-07-08/NetworkSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-web-2020-07-08/NetworkSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-web-2020-07-08/NetworkSettings)
