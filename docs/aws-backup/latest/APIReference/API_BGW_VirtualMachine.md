---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_BGW_VirtualMachine.html
---

# VirtualMachine
<a name="API_BGW_VirtualMachine"></a>

A virtual machine that is on a hypervisor.

## Contents
<a name="API_BGW_VirtualMachine_Contents"></a>

 ** HostName **   <a name="Backup-Type-BGW_VirtualMachine-HostName"></a>
The host name of the virtual machine.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]*`
Required: No

 ** HypervisorId **   <a name="Backup-Type-BGW_VirtualMachine-HypervisorId"></a>
The ID of the virtual machine's hypervisor.
Type: String
Required: No

 ** LastBackupDate **   <a name="Backup-Type-BGW_VirtualMachine-LastBackupDate"></a>
The most recent date a virtual machine was backed up, in Unix format and UTC time.
Type: Timestamp
Required: No

 ** Name **   <a name="Backup-Type-BGW_VirtualMachine-Name"></a>
The name of the virtual machine.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]*`
Required: No

 ** Path **   <a name="Backup-Type-BGW_VirtualMachine-Path"></a>
The path of the virtual machine.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[^\x00]+`
Required: No

 ** ResourceArn **   <a name="Backup-Type-BGW_VirtualMachine-ResourceArn"></a>
The Amazon Resource Name (ARN) of the virtual machine. For example, `arn:aws:backup-gateway:us-west-1:0000000000000:vm/vm-0000ABCDEFGIJKL`.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 500.
Pattern: `arn:(aws|aws-cn|aws-us-gov):backup-gateway(:[a-zA-Z-0-9]+){3}\/[a-zA-Z-0-9]+`
Required: No

## See Also
<a name="API_BGW_VirtualMachine_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-gateway-2021-01-01/VirtualMachine)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-gateway-2021-01-01/VirtualMachine)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-gateway-2021-01-01/VirtualMachine)
