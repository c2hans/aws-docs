---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_NetworkConfigurationInfo.html
---

# NetworkConfigurationInfo

The network access controls for your Identity Center instance. These controls restrict which networks can reach your instance and applications.

## Contents
<a name="API_NetworkConfigurationInfo_Contents"></a>

 ** VpceAccessRequired **   <a name="singlesignon-Type-NetworkConfigurationInfo-VpceAccessRequired"></a>
Specifies whether access to your Identity Center instance and to applications must originate from a VPC endpoint. When this value is `true` and no other field is specified, access is allowed from any VPC in your organization, or from any VPC in the AWS account for an account instance, and applies to all applications. When this value is `false`, no network access control is enforced and the values of `RestrictSourceVpcs`, `AllowSourceIps`, and `ExcludeApplicationArns` are cleared.
Type: Boolean
Required: Yes

 ** AllowSourceIps **   <a name="singlesignon-Type-NetworkConfigurationInfo-AllowSourceIps"></a>
Allows access from the IPv4 or IPv6 CIDR blocks that you specify, in addition to the VPCs allowed by `RestrictSourceVpcs`. If you don't specify this value, no additional IP address ranges are allowed.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 2. Maximum length of 43.
Pattern: `((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\/(3[0-2]|[1-2][0-9]|[0-9]))?|(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:(:[0-9a-fA-F]{1,4}){1,6}|:((:[0-9a-fA-F]{1,4}){1,7}|:))(\/(12[0-8]|1[0-1][0-9]|[1-9][0-9]|[0-9]))?)`
Required: No

 ** ExcludeApplicationArns **   <a name="singlesignon-Type-NetworkConfigurationInfo-ExcludeApplicationArns"></a>
Exempts the applications that you specify from the network access control, so that access to them is unchanged. You can specify both AWS managed applications and customer managed applications, and you can use wildcards. These applications are not restricted by `RestrictSourceVpcs` or `AllowSourceIps`. If you don't specify this value, the controls apply to all applications.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:[a-z0-9-]+:[a-z0-9-*]*:[0-9]{12}:[-a-zA-Z0-9./:_*]+`
Required: No

 ** RestrictSourceVpcs **   <a name="singlesignon-Type-NetworkConfigurationInfo-RestrictSourceVpcs"></a>
Limits access to the VPC endpoints in the VPCs that you specify. These VPCs must be in your organization, or in the AWS account for an account instance. If you don't specify this value, access is allowed from any VPC in your organization or AWS account.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 43. Maximum length of 128.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:ec2:[a-z0-9-]+:[0-9]{12}:vpc/vpc-([0-9a-f]){8}(([0-9a-f]){9})?`
Required: No

## See Also
<a name="API_NetworkConfigurationInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/NetworkConfigurationInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/NetworkConfigurationInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/NetworkConfigurationInfo)
