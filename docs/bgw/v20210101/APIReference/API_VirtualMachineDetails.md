---
source_url: https://docs.aws.amazon.com/bgw/v20210101/APIReference/API_VirtualMachineDetails.html
---

# VirtualMachineDetails
<a name="API_VirtualMachineDetails"></a>

Your `VirtualMachine` objects, ordered by their Amazon Resource Names (ARNs).

## Contents
<a name="API_VirtualMachineDetails_Contents"></a>

 ** HostName **   <a name="bgw-Type-VirtualMachineDetails-HostName"></a>
The host name of the virtual machine.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]*`
Required: No

 ** HypervisorId **   <a name="bgw-Type-VirtualMachineDetails-HypervisorId"></a>
The ID of the virtual machine's hypervisor.
Type: String
Required: No

 ** LastBackupDate **   <a name="bgw-Type-VirtualMachineDetails-LastBackupDate"></a>
The most recent date a virtual machine was backed up, in Unix format and UTC time.
Type: Timestamp
Required: No

 ** Name **   <a name="bgw-Type-VirtualMachineDetails-Name"></a>
The name of the virtual machine.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]*`
Required: No

 ** Path **   <a name="bgw-Type-VirtualMachineDetails-Path"></a>
The path of the virtual machine.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[^\x00]+`
Required: No

 ** ResourceArn **   <a name="bgw-Type-VirtualMachineDetails-ResourceArn"></a>
The Amazon Resource Name (ARN) of the virtual machine. For example, `arn:aws:backup-gateway:us-west-1:0000000000000:vm/vm-0000ABCDEFGIJKL`.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 500.
Pattern: `arn:(aws|aws-cn|aws-us-gov):backup-gateway(:[a-zA-Z-0-9]+){3}\/[a-zA-Z-0-9]+`
Required: No

 ** VmwareTags **   <a name="bgw-Type-VirtualMachineDetails-VmwareTags"></a>
These are the details of the VMware tags associated with the specified virtual machine.
Type: Array of [VmwareTag](API_VmwareTag.md) objects
Required: No

## See Also
<a name="API_VirtualMachineDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-gateway-2021-01-01/VirtualMachineDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-gateway-2021-01-01/VirtualMachineDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-gateway-2021-01-01/VirtualMachineDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Backup gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bgw` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
