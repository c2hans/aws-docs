---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_ErrorDetails.html
---

# ErrorDetails
<a name="API_ErrorDetails"></a>

Describes in-depth details about the error. These details include the possible causes of the error and troubleshooting information.

## Contents
<a name="API_ErrorDetails_Contents"></a>

 ** ErrorCode **   <a name="WorkSpaces-Type-ErrorDetails-ErrorCode"></a>
Indicates the error code returned.
Type: String
Valid Values: `OutdatedPowershellVersion | OfficeInstalled | PCoIPAgentInstalled | WindowsUpdatesEnabled | AutoMountDisabled | WorkspacesBYOLAccountNotFound | WorkspacesBYOLAccountDisabled | DHCPDisabled | DiskFreeSpace | AdditionalDrivesAttached | OSNotSupported | DomainJoined | AzureDomainJoined | FirewallEnabled | VMWareToolsInstalled | DiskSizeExceeded | IncompatiblePartitioning | PendingReboot | AutoLogonEnabled | RealTimeUniversalDisabled | MultipleBootPartition | Requires64BitOS | ZeroRearmCount | InPlaceUpgrade | AntiVirusInstalled | UEFINotSupported | UnknownError | AppXPackagesInstalled | ReservedStorageInUse | AdditionalDrivesPresent | WindowsUpdatesRequired | SysPrepFileMissing | UserProfileMissing | InsufficientDiskSpace | EnvironmentVariablesPathMissingEntries | DomainAccountServicesFound | InvalidIp | RemoteDesktopServicesDisabled | WindowsModulesInstallerDisabled | AmazonSsmAgentEnabled | UnsupportedSecurityProtocol | MultipleUserProfiles | StagedAppxPackage | UnsupportedOsUpgrade | InsufficientRearmCount | ProtocolOSIncompatibility | MemoryIntegrityIncompatibility | RestrictedDriveLetterInUse`
Required: No

 ** ErrorMessage **   <a name="WorkSpaces-Type-ErrorDetails-ErrorMessage"></a>
The text of the error message related the error code.
Type: String
Required: No

## See Also
<a name="API_ErrorDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/ErrorDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/ErrorDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/ErrorDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
