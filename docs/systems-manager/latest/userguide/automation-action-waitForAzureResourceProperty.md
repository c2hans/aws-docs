---
source_url: https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-action-waitForAzureResourceProperty.html
---

# `aws:waitForAzureResourceProperty` – Wait on an Azure resource property

The `aws:waitForAzureResourceProperty` action waits until a property of a Microsoft Azure resource has one of a set of values. The action calls an Azure API operation, reads the property named by `PropertySelector` from the response, and compares it to `DesiredValues`. If the value isn't in the list, the action checks again after 3, 9, 27, and 81 seconds, and then at intervals that start at 81 seconds and grow by 0.5% each time. It repeats until the value matches or the step reaches its timeout. If you set `timeoutSeconds`, no interval is longer than 30% of the timeout. Each check is a full call to the Azure API operation.

**Note**
This action has no default timeout. If you don't set `timeoutSeconds` on the step, the step keeps polling until the property matches or the automation ends. For more information, see [Handling timeouts in runbooks](automation-handling-timeouts.md).

**Note**
The `aws:waitForAzureResourceProperty` action is available in the AWS Regions where Cloud Connector is available.

**Input**
You provide the same inputs as [`aws:executeAzureApi` – Call and run Azure API operations](automation-action-executeAzureApi.md), plus `PropertySelector` and `DesiredValues`.

------
#### [ YAML ]

```yaml
action: aws:waitForAzureResourceProperty
inputs:
  Service: {{The Azure SDK service module}}
  Api: {{The operation, as OperationGroup.Method}}
  Package: {{The Azure package name}}
  CloudConnector: {{The Cloud Connector ID}}
  SubscriptionId: {{The Azure subscription ID}}
  {{API operation parameters}}: {{A value}}
  Body: {{The request body, as a JSON object}}
  PropertySelector: {{Response attribute}}
  DesiredValues:
  - {{Desired property value}}
```

------
#### [ JSON ]

```json
{
  "action": "aws:waitForAzureResourceProperty",
  "inputs": {
    "Service":"{{The Azure SDK service module}}",
    "Api":"{{The operation, as OperationGroup.Method}}",
    "Package":"{{The Azure package name}}",
    "CloudConnector":"{{The Cloud Connector ID}}",
    "SubscriptionId":"{{The Azure subscription ID}}",
    "{{API operation parameters}}":"{{A value}}",
    "Body": { {{The request body, as a JSON object}} },
    "PropertySelector": "{{Response attribute}}",
    "DesiredValues": [
      "{{Desired property value}}"
    ]
  }
}
```

------

Service
The module name that follows `azure.mgmt.` in the Azure SDK for Python. For example, specify `compute` for virtual machines (`azure.mgmt.compute`). For a library that has its client in a submodule, include the submodule, for example `resource.resources` for resource groups. For more information about the services that the action doesn't support, see [Limitations](automation-action-executeAzureApi.md#automation-action-executeAzureApi-limitations).
Type: String
Required: Yes

Api
The name of the API operation that you want to run, in the form `OperationGroup.Method`, for example `VirtualMachines.Get`. You can also use the snake\_case form, for example `virtual_machines.get`.
Type: String
Required: Yes

Package
The name of the published Azure SDK package that provides the operation. For more information about the available packages and the libraries in each, see [Azure and Google Cloud SDK packages](automation-multicloud-packages.md).
Type: String
Required: Yes

CloudConnector
The ID of the Cloud Connector that reaches your Azure resources. For example, `a1b2c3d4-5678-90ab-cdef-111122223333`.
Type: String
Required: Yes

SubscriptionId
The ID of the Azure subscription that contains the resource. This input is required, and the subscription must be one that the Cloud Connector allows.
Type: String
Required: Yes

API operation parameters
Any other inputs that you add to the step are passed to the Azure API operation as its parameters, using the parameter names from the Azure REST API reference. For example, `VirtualMachines.Get` takes `resourceGroupName`, `vmName`, and the optional `expand`. For more information, see [Pass parameters and a request body](automation-multicloud-runbooks.md#automation-multicloud-runbooks-inputs).
Type: Determined by the chosen API operation
Required: Determined by the chosen API operation

Body
The request body of the API operation, if it takes one, as a JSON object in the shape that the Azure REST API reference shows. Most operations that read a property don't take a request body. Pass request-body properties in `Body` rather than as separate step inputs.
Type: StringMap
Required: Determined by the chosen API operation

PropertySelector
The JSONPath to a specific attribute in the response object. Automation returns the Azure response as a JSON object. For more information about the JSONPath that you can use, see [Select values from the response](automation-multicloud-runbooks.md#automation-multicloud-runbooks-selectors).
Type: String
Required: Yes

DesiredValues
The values on which to continue the automation. The action polls until the property has one of these values or the step times out. Automation compares each value as a string, and the comparison is case-sensitive. If `PropertySelector` matches more than one value, every value must be in this list. If the selector matches nothing, the action keeps polling.
If the API operation returns an error, the step fails without polling again. For example, a `Get` operation on a resource that doesn't exist yet, or that was deleted, fails the step with `Azure error (ResourceNotFound)`.
Type: StringList
Required: Yes

Automation signs in to Azure with the Cloud Connector. If the automation has an `AutomationAssumeRole`, Automation uses that role to assume the connector's federation role. Otherwise, it uses the credentials of the user who started the automation. For more information about the permissions that each role needs, see [Permissions for automations that use a Cloud Connector](automation-cloud-connector-permissions.md).

For more information about the operation names and services that the action supports, see [Naming rules](automation-action-executeAzureApi.md#automation-action-executeAzureApi-naming) and [Limitations](automation-action-executeAzureApi.md#automation-action-executeAzureApi-limitations).

**Example – Wait until a virtual machine is running**
The following step waits until a virtual machine's power state is running, for example after a step that starts the VM. The power state is usually the second entry in the instance view's `statuses` list, so the example selects `$.properties.instanceView.statuses[1].code`.

------
#### [ YAML ]

```yaml
name: waitForVmRunning
action: aws:waitForAzureResourceProperty
timeoutSeconds: 600
inputs:
  Service: compute
  Api: VirtualMachines.Get
  Package: azure_202610
  CloudConnector: a1b2c3d4-5678-90ab-cdef-111122223333
  SubscriptionId: "11111111-2222-3333-4444-555555555555"
  resourceGroupName: my-resource-group
  vmName: my-vm
  expand: instanceView
  PropertySelector: $.properties.instanceView.statuses[1].code
  DesiredValues:
  - PowerState/running
```

------
#### [ JSON ]

```json
{
  "name": "waitForVmRunning",
  "action": "aws:waitForAzureResourceProperty",
  "timeoutSeconds": 600,
  "inputs": {
    "Service": "compute",
    "Api": "VirtualMachines.Get",
    "Package": "azure_202610",
    "CloudConnector": "a1b2c3d4-5678-90ab-cdef-111122223333",
    "SubscriptionId": "11111111-2222-3333-4444-555555555555",
    "resourceGroupName": "my-resource-group",
    "vmName": "my-vm",
    "expand": "instanceView",
    "PropertySelector": "$.properties.instanceView.statuses[1].code",
    "DesiredValues": [
      "PowerState/running"
    ]
  }
}
```

------
