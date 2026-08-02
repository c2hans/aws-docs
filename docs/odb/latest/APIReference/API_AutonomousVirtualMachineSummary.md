---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_AutonomousVirtualMachineSummary.html
---

# AutonomousVirtualMachineSummary
<a name="API_AutonomousVirtualMachineSummary"></a>

A summary of an Autonomous Virtual Machine (VM) within an Autonomous VM cluster.

## Contents
<a name="API_AutonomousVirtualMachineSummary_Contents"></a>

 ** autonomousVirtualMachineId **   <a name="odb-Type-AutonomousVirtualMachineSummary-autonomousVirtualMachineId"></a>
The unique identifier of the Autonomous VM.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 64.
Pattern: `[a-zA-Z0-9_~.-]+`
Required: No

 ** clientIpAddress **   <a name="odb-Type-AutonomousVirtualMachineSummary-clientIpAddress"></a>
The IP address used by clients to connect to this Autonomous VM.
Type: String
Required: No

 ** cloudAutonomousVmClusterId **   <a name="odb-Type-AutonomousVirtualMachineSummary-cloudAutonomousVmClusterId"></a>
The unique identifier of the Autonomous VM cluster containing this Autonomous VM.
Type: String
Required: No

 ** cpuCoreCount **   <a name="odb-Type-AutonomousVirtualMachineSummary-cpuCoreCount"></a>
The number of CPU cores allocated to this Autonomous VM.
Type: Integer
Required: No

 ** dbNodeStorageSizeInGBs **   <a name="odb-Type-AutonomousVirtualMachineSummary-dbNodeStorageSizeInGBs"></a>
The amount of storage allocated to this Autonomous Virtual Machine, in gigabytes (GB).
Type: Integer
Required: No

 ** dbServerDisplayName **   <a name="odb-Type-AutonomousVirtualMachineSummary-dbServerDisplayName"></a>
The display name of the database server hosting this Autonomous VM.
Type: String
Required: No

 ** dbServerId **   <a name="odb-Type-AutonomousVirtualMachineSummary-dbServerId"></a>
The unique identifier of the database server hosting this Autonomous VM.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 64.
Pattern: `[a-zA-Z0-9_~.-]+`
Required: No

 ** memorySizeInGBs **   <a name="odb-Type-AutonomousVirtualMachineSummary-memorySizeInGBs"></a>
The amount of memory allocated to this Autonomous VM, in gigabytes (GB).
Type: Integer
Required: No

 ** ocid **   <a name="odb-Type-AutonomousVirtualMachineSummary-ocid"></a>
The Oracle Cloud Identifier (OCID) of the Autonomous VM.
Type: String
Required: No

 ** ociResourceAnchorName **   <a name="odb-Type-AutonomousVirtualMachineSummary-ociResourceAnchorName"></a>
The name of the Oracle Cloud Infrastructure (OCI) resource anchor associated with this Autonomous VM.
Type: String
Required: No

 ** status **   <a name="odb-Type-AutonomousVirtualMachineSummary-status"></a>
The current status of the Autonomous VM.
Type: String
Valid Values: `AVAILABLE | FAILED | PROVISIONING | TERMINATED | TERMINATING | UPDATING | MAINTENANCE_IN_PROGRESS`
Required: No

 ** statusReason **   <a name="odb-Type-AutonomousVirtualMachineSummary-statusReason"></a>
Additional information about the current status of the Autonomous VM, if applicable.
Type: String
Required: No

 ** vmName **   <a name="odb-Type-AutonomousVirtualMachineSummary-vmName"></a>
The name of the Autonomous VM.
Type: String
Required: No

## See Also
<a name="API_AutonomousVirtualMachineSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/AutonomousVirtualMachineSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/AutonomousVirtualMachineSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/AutonomousVirtualMachineSummary)
