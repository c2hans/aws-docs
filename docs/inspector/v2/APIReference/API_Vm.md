---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_Vm.html
---

# Vm
<a name="API_Vm"></a>

Contains details about a VM instance involved in a finding.

## Contents
<a name="API_Vm_Contents"></a>

 ** executionRole **   <a name="inspector2-Type-Vm-executionRole"></a>
The execution role of the VM instance.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** ipV4Addresses **   <a name="inspector2-Type-Vm-ipV4Addresses"></a>
The IPv4 addresses of the VM instance.
Type: Array of strings
Length Constraints: Minimum length of 7. Maximum length of 15.
Pattern: `(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])`
Required: No

 ** ipV6Addresses **   <a name="inspector2-Type-Vm-ipV6Addresses"></a>
The IPv6 addresses of the VM instance.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 47.
Required: No

 ** keyName **   <a name="inspector2-Type-Vm-keyName"></a>
The key name associated with the VM instance.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** launchedAt **   <a name="inspector2-Type-Vm-launchedAt"></a>
The date and time the VM instance was launched.
Type: Timestamp
Required: No

 ** networkId **   <a name="inspector2-Type-Vm-networkId"></a>
The network ID associated with the VM instance.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** platform **   <a name="inspector2-Type-Vm-platform"></a>
The platform of the VM instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** securityGroupIds **   <a name="inspector2-Type-Vm-securityGroupIds"></a>
The security group IDs associated with the VM instance.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Length Constraints: Minimum length of 1.
Required: No

 ** subnetIds **   <a name="inspector2-Type-Vm-subnetIds"></a>
The subnet IDs of the VM instance.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 16 items.
Length Constraints: Minimum length of 1.
Required: No

 ** type **   <a name="inspector2-Type-Vm-type"></a>
The type of the VM instance.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** vmImageReference **   <a name="inspector2-Type-Vm-vmImageReference"></a>
The image reference of the VM instance.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** vmName **   <a name="inspector2-Type-Vm-vmName"></a>
The name of the VM instance.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_Vm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/Vm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/Vm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/Vm)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
