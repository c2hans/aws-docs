---
source_url: https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-action-installDistributorPackageOnAzure.html
---

# `aws:installDistributorPackageOnAzure` – Install a package on an Azure VM

The `aws:installDistributorPackageOnAzure` action installs, uninstalls, or updates an Systems Manager Distributor package on a Microsoft Azure virtual machine (VM) that a Cloud Connector reaches. The public runbook `AWS-InstallDistributorPackageOnAzure` uses this action.

**Note**
The `aws:installDistributorPackageOnAzure` action is available in the AWS Regions where Cloud Connector is available.

**Input**
The action takes the following inputs.

------
#### [ YAML ]

```yaml
action: aws:installDistributorPackageOnAzure
inputs:
  CloudConnector: {{The Cloud Connector ID}}
  AzureVmResourceId: {{The ARM resource ID of the VM}}
  PackageName: {{The Distributor package name}}
  Action: {{Install or Uninstall}}
  InstallationType: {{Uninstall and reinstall, or In-place update}}
  Version: {{The package version}}
  AdditionalArguments: {{A map of extra arguments}}
```

------
#### [ JSON ]

```json
{
  "action": "aws:installDistributorPackageOnAzure",
  "inputs": {
    "CloudConnector": "{{The Cloud Connector ID}}",
    "AzureVmResourceId": "{{The ARM resource ID of the VM}}",
    "PackageName": "{{The Distributor package name}}",
    "Action": "{{Install or Uninstall}}",
    "InstallationType": "{{Uninstall and reinstall, or In-place update}}",
    "Version": "{{The package version}}",
    "AdditionalArguments": {}
  }
}
```

------

CloudConnector
The ID of the Cloud Connector that reaches the Azure VM. For example, `a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`.
Type: String
Required: Yes

AzureVmResourceId
The Azure Resource Manager (ARM) resource ID of the VM. For example, `/subscriptions/11111111-2222-3333-4444-555555555555/resourceGroups/my-resource-group/providers/Microsoft.Compute/virtualMachines/my-vm`.
Type: String
Required: Yes

PackageName
The name of the Distributor package to install.
Type: String
Required: Yes

Action
Whether to install or uninstall the package. Valid values are `Install` and `Uninstall`.
Type: String
Required: No

InstallationType
How to apply an update. Valid values are `Uninstall and reinstall` and `In-place update`.
Type: String
Required: No

Version
The version of the package to install. If you don't specify a version, the action installs the default version.
Type: String
Required: No

AdditionalArguments
A map of additional arguments to pass to the installation.
Type: StringMap
Required: No

**Outputs**
The action returns the following outputs.

Status
The status of the operation.

Action
The action that was run.

PackageName
The name of the package.

PackageVersion
The version of the package.

Installed
Whether the package is installed.

Region
The AWS Region of the operation.

AzureVmResourceId
The ARM resource ID of the VM.

AzureLocation
The Azure location of the VM.

AzureVmSize
The size of the VM.

DetectedPlatform
The operating system platform detected on the VM.

DetectedPlatformVersion
The operating system version detected on the VM.

DetectedPlatformFamily
The operating system family detected on the VM.

DetectedArchitecture
The architecture detected on the VM.

ExecutionLog
The output log of the operation.

The step signs in to Azure with the Cloud Connector. When the automation has an `AutomationAssumeRole`, Automation assumes that role, and the role assumes the connector's federation role to get Azure credentials. For the permissions that the role and the connector need, see [Permissions for automations that use a Cloud Connector](automation-cloud-connector-permissions.md).

**Example**
The following step installs a Distributor package on an Azure VM.

------
#### [ YAML ]

```yaml
name: installPackage
action: aws:installDistributorPackageOnAzure
inputs:
  CloudConnector: a1b2c3d4-5678-90ab-cdef-EXAMPLE11111
  AzureVmResourceId: /subscriptions/11111111-2222-3333-4444-555555555555/resourceGroups/my-resource-group/providers/Microsoft.Compute/virtualMachines/my-vm
  PackageName: AmazonCloudWatchAgent
  Action: Install
```

------
#### [ JSON ]

```json
{
  "name": "installPackage",
  "action": "aws:installDistributorPackageOnAzure",
  "inputs": {
    "CloudConnector": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "AzureVmResourceId": "/subscriptions/11111111-2222-3333-4444-555555555555/resourceGroups/my-resource-group/providers/Microsoft.Compute/virtualMachines/my-vm",
    "PackageName": "AmazonCloudWatchAgent",
    "Action": "Install"
  }
}
```

------
