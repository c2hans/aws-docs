---
source_url: https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-multicloud-parameter-types.html
---

# Parameter types for Azure and Google Cloud resources

Automation runbooks can declare parameters that use the following types to identify a Cloud Connector, a Microsoft Azure resource, or a Google Cloud resource. When an execution starts, Automation validates each input value against the type's pattern. A value that doesn't match fails with `Value "{{value}}" not matching "{{pattern}}"`. An empty value isn't checked. When you create or update a runbook, a type string that isn't listed here fails with `Parameter type: {{type}} is invalid`.
+ Systems Manager matches type strings exactly, including their mixed casing. For example, `microsoft.Compute/VirtualMachines` starts with a lowercase `m`, but `Microsoft.Storage/storageAccounts/blobServices/containers` starts with an uppercase `M`. A type string with the wrong casing isn't recognized.
+ Azure resource ID values are matched case-insensitively.
+ In the Automation console, a parameter of type `AWS::SSM::CloudConnector::Id` is a connector list (**Choose or enter a Cloud Connector ID**). An Azure virtual machine (VM) input shows a typed field with a format hint. For Azure types other than blob containers and managed identities, you can choose the resource from a list after you use Azure sign-in. Google Cloud inputs are typed fields. For Azure sign-in, see [Choosing Azure resources with Azure sign-in](automation-azure-sign-in.md).

With a Cloud Connector target, Automation passes each resource ID in the input named in `TargetParameterName`. The VM types work with the default target. For other types, set `AzureResourceType` or `GcpAssetType` on the target to the matching type. A `storage.googleapis.com/Bucket` input doesn't accept the ID that the target passes. See the note after the Google Cloud table.

## Cloud Connector type
<a name="automation-multicloud-parameter-types-connector"></a>

| Type | Base type | Value format | Description |
| --- | --- | --- | --- |
| AWS::SSM::CloudConnector::Id | String | a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 | The ID of a Cloud Connector, as a GUID in lowercase. |

## Azure types
<a name="automation-multicloud-parameter-types-azure"></a>

Azure values are full Azure Resource Manager (ARM) resource IDs. In the examples, replace the placeholders with your subscription ID, resource group, and resource names.

| Type | Base type | Value format | Description |
| --- | --- | --- | --- |
| microsoft.Compute/VirtualMachines | String | /subscriptions/<subscription-id>/resourceGroups/<resource-group>/providers/Microsoft.Compute/virtualMachines/<vm-name> | An Azure virtual machine. |
| List<microsoft.Compute/VirtualMachines> | StringList | /subscriptions/<subscription-id>/resourceGroups/<resource-group>/providers/Microsoft.Compute/virtualMachines/<vm-name> | A list of Azure virtual machines. |
| microsoft.Compute/disks | String | /subscriptions/<subscription-id>/resourceGroups/<resource-group>/providers/Microsoft.Compute/disks/<disk-name> | An Azure managed disk. |
| microsoft.Compute/virtualMachineScaleSets | String | /subscriptions/<subscription-id>/resourceGroups/<resource-group>/providers/Microsoft.Compute/virtualMachineScaleSets/<scale-set-name> | An Azure virtual machine scale set. |
| microsoft.Sql/servers | String | /subscriptions/<subscription-id>/resourceGroups/<resource-group>/providers/Microsoft.Sql/servers/<server-name> | An Azure SQL server. |
| microsoft.Sql/servers/databases | String | /subscriptions/<subscription-id>/resourceGroups/<resource-group>/providers/Microsoft.Sql/servers/<server-name>/databases/<database-name> | An Azure SQL database. |
| microsoft.Storage/StorageAccounts | String | /subscriptions/<subscription-id>/resourceGroups/<resource-group>/providers/Microsoft.Storage/storageAccounts/<account-name> | An Azure storage account. |
| Microsoft.Storage/storageAccounts/blobServices/containers | String | /subscriptions/<subscription-id>/resourceGroups/<resource-group>/providers/Microsoft.Storage/storageAccounts/<account-name>/blobServices/default/containers/<container-name> | An Azure blob container. |
| List<Microsoft.Storage/storageAccounts/blobServices/containers> | StringList | /subscriptions/<subscription-id>/resourceGroups/<resource-group>/providers/Microsoft.Storage/storageAccounts/<account-name>/blobServices/default/containers/<container-name> | A list of Azure blob containers. |
| microsoft.KeyVault/vaults | String | /subscriptions/<subscription-id>/resourceGroups/<resource-group>/providers/Microsoft.KeyVault/vaults/<vault-name> | An Azure key vault. |
| microsoft.Web/sites | String | /subscriptions/<subscription-id>/resourceGroups/<resource-group>/providers/Microsoft.Web/sites/<site-name> | An Azure App Service app. |
| microsoft.ContainerService/managedClusters | String | /subscriptions/<subscription-id>/resourceGroups/<resource-group>/providers/Microsoft.ContainerService/managedClusters/<cluster-name> | An Azure Kubernetes Service (AKS) cluster. |
| microsoft.ContainerInstance/containerGroups | String | /subscriptions/<subscription-id>/resourceGroups/<resource-group>/providers/Microsoft.ContainerInstance/containerGroups/<group-name> | An Azure Container Instances container group. |
| microsoft.ManagedIdentity/userAssignedIdentities | String | /subscriptions/<subscription-id>/resourceGroups/<resource-group>/providers/Microsoft.ManagedIdentity/userAssignedIdentities/<identity-name> | An Azure user-assigned managed identity. |
| List<microsoft.ManagedIdentity/userAssignedIdentities> | StringList | /subscriptions/<subscription-id>/resourceGroups/<resource-group>/providers/Microsoft.ManagedIdentity/userAssignedIdentities/<identity-name> | A list of Azure user-assigned managed identities. |

## Google Cloud types
<a name="automation-multicloud-parameter-types-gcp"></a>

Google Cloud values are resource names in the form shown. Except for buckets, a value can also start with the service prefix that Cloud Asset Inventory uses, such as `//compute.googleapis.com/` (for Cloud SQL, `//cloudsql.googleapis.com/`). In the examples, replace the placeholders with your project, zone or location, and resource names.

| Type | Base type | Value format | Description |
| --- | --- | --- | --- |
| compute.googleapis.com/Instance | String | projects/<project-id>/zones/<zone>/instances/<instance-name> | A Google Cloud VM instance. |
| List<compute.googleapis.com/Instance> | StringList | projects/<project-id>/zones/<zone>/instances/<instance-name> | A list of Google Cloud VM instances. |
| compute.googleapis.com/Disk | String | projects/<project-id>/zones/<zone>/disks/<disk-name> or projects/<project-id>/regions/<region>/disks/<disk-name> | A Google Cloud disk (zonal or regional). |
| compute.googleapis.com/InstanceGroup | String | projects/<project-id>/zones/<zone>/instanceGroups/<group-name> or projects/<project-id>/regions/<region>/instanceGroups/<group-name> | A Google Cloud instance group. |
| container.googleapis.com/Cluster | String | projects/<project-id>/locations/<location>/clusters/<cluster-name> or projects/<project-id>/zones/<zone>/clusters/<cluster-name> | A Google Kubernetes Engine (GKE) cluster. |
| sqladmin.googleapis.com/Instance | String | projects/<project-id>/instances/<instance-name> | A Cloud SQL instance. |
| run.googleapis.com/Service | String | projects/<project-id>/locations/<location>/services/<service-name> | A Cloud Run service. |
| cloudfunctions.googleapis.com/CloudFunction | String | projects/<project-id>/locations/<location>/functions/<function-name> | A Cloud Functions function. |
| bigquery.googleapis.com/Dataset | String | projects/<project-id>/datasets/<dataset-name> | A BigQuery dataset. |
| pubsub.googleapis.com/Topic | String | projects/<project-id>/topics/<topic-name> | A Pub/Sub topic. |
| storage.googleapis.com/Bucket | String | <bucket-name> | A Cloud Storage bucket. |
| List<storage.googleapis.com/Bucket> | StringList | <bucket-name> | A list of Cloud Storage buckets. |
| iam.googleapis.com/ServiceAccount | String | projects/<project-id>/serviceAccounts/<service-account-email> | A Google Cloud service account. |
| List<iam.googleapis.com/ServiceAccount> | StringList | projects/<project-id>/serviceAccounts/<service-account-email> | A list of Google Cloud service accounts. |

**Note**
A Cloud Connector target passes a bucket as `//storage.googleapis.com/{{bucket-name}}`, which the `storage.googleapis.com/Bucket` type doesn't accept. To run a runbook on buckets with a Cloud Connector target, use a `String` input for the bucket with an `allowedPattern` that accepts the `//storage.googleapis.com/` prefix, and remove the prefix in the runbook.

## Example runbook
<a name="automation-multicloud-parameter-types-example"></a>

The following runbook declares a `CloudConnector` parameter of type `AWS::SSM::CloudConnector::Id`, a `VmIds` parameter of type `List<microsoft.Compute/VirtualMachines>`, and an `AutomationAssumeRole` parameter of type `AWS::IAM::Role::Arn`. The step uses the `aws:executeAzureApi` action to call an Azure API operation.

```yaml
schemaVersion: '0.3'
assumeRole: '{{ AutomationAssumeRole }}'
parameters:
  CloudConnector:
    type: AWS::SSM::CloudConnector::Id
    description: The Cloud Connector that reaches your Azure resources.
  VmIds:
    type: List<microsoft.Compute/VirtualMachines>
    description: The Azure virtual machines to act on.
  AutomationAssumeRole:
    type: AWS::IAM::Role::Arn
    description: The role that Automation assumes to run this runbook.
mainSteps:
  - name: getVirtualMachine
    action: aws:executeAzureApi
    inputs:
      Service: compute
      Api: VirtualMachines.Get
      Package: azure_202610
      CloudConnector: '{{ CloudConnector }}'
      SubscriptionId: '11111111-2222-3333-4444-555555555555'
      resourceGroupName: my-resource-group
      vmName: my-vm
```

In this step, `Service`, `Api`, `Package`, `CloudConnector`, and `SubscriptionId` are inputs to the `aws:executeAzureApi` action. The other inputs (`resourceGroupName` and `vmName`) are passed to the Azure API operation as its parameters. To use the IDs in `VmIds`, split each ID into its subscription, resource group, and VM name with `aws:executeScript`, as shown in [Create runbooks that call Azure and Google Cloud APIs](automation-multicloud-runbooks.md).
