---
source_url: https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-action-executeAzureApi.html
---

# `aws:executeAzureApi` – Call and run Azure API operations

The `aws:executeAzureApi` action calls and runs a Microsoft Azure API operation on the resources that a Cloud Connector reaches. Automation calls the operation with the Azure SDK for Python and returns the response as a JSON object, so you can select values from it the same way as for [`aws:executeAwsApi` – Call and run AWS API operations](automation-action-executeAwsApi.md).

**Note**
The `aws:executeAzureApi` action is available in the AWS Regions where Cloud Connector is available.

**Input**
You provide `Service`, `Api`, `Package`, `CloudConnector`, and `SubscriptionId`. You pass the request body, if the operation has one, in `Body`. Any other inputs are passed to the Azure API operation as its parameters.

------
#### [ YAML ]

```yaml
action: aws:executeAzureApi
inputs:
  Service: {{The Azure SDK service module}}
  Api: {{The operation, as OperationGroup.Method}}
  Package: {{The Azure package name}}
  CloudConnector: {{The Cloud Connector ID}}
  SubscriptionId: {{The Azure subscription ID}}
  {{API operation parameters}}: {{A value}}
  Body: {{The request body, as a JSON object}}
  NextLink: {{The nextLink value from the previous response, to get the next page}}
outputs: # {{These are user-specified outputs}}
- Name: {{The name for a user-specified output key}}
  Selector: {{A response attribute specified by using JSONPath format}}
  Type: {{The data type}}
```

------
#### [ JSON ]

```json
{
   "action":"aws:executeAzureApi",
   "inputs":{
      "Service":"{{The Azure SDK service module}}",
      "Api":"{{The operation, as OperationGroup.Method}}",
      "Package":"{{The Azure package name}}",
      "CloudConnector":"{{The Cloud Connector ID}}",
      "SubscriptionId":"{{The Azure subscription ID}}",
      "{{API operation parameters}}":"{{A value}}",
      "Body":{ {{The request body, as a JSON object}} },
      "NextLink":"{{The nextLink value from the previous response, to get the next page}}"
   },
   "outputs":[ {{These are user-specified outputs}}
      {
         "Name":"{{The name for a user-specified output key}}",
         "Selector":"{{A response attribute specified by using JSONPath format}}",
         "Type":"{{The data type}}"
      }
   ]
}
```

------

Service
The module name that follows `azure.mgmt.` in the Azure SDK for Python. For example, specify `compute` for virtual machines (`azure.mgmt.compute`). For a library that has its client in a submodule, include the submodule, for example `resource.resources` for resource groups. For more information about the services that the action doesn't support, see [Limitations](#automation-action-executeAzureApi-limitations).
Type: String
Required: Yes

Api
The name of the API operation that you want to run, in the form `OperationGroup.Method`. Use the operation group and operation name from the Azure REST API reference. For example, to get a virtual machine, specify `VirtualMachines.Get`. You can also use the SDK's snake\_case form, for example `virtual_machines.get`. For how to build the name from the REST reference, see [Naming rules](#automation-action-executeAzureApi-naming). A long-running operation returns as soon as Azure accepts the request, without waiting for it to finish. For more information, see [Lists and long-running operations](automation-multicloud-runbooks.md#automation-multicloud-runbooks-paging).
Type: String
Required: Yes

Package
The name of the published Azure SDK package that provides the operation. For more information about the available packages and the libraries in each, see [Azure and Google Cloud SDK packages](automation-multicloud-packages.md).
Type: String
Required: Yes

CloudConnector
The ID of the Cloud Connector that reaches your Azure resources. Automation uses the connector to sign in to Azure. For example, `a1b2c3d4-5678-90ab-cdef-111122223333`.
Type: String
Required: Yes

SubscriptionId
The ID of the Azure subscription that contains the resource. Automation checks this input when the step runs. If the input is missing, the step fails with `Missing required parameter 'SubscriptionId' for Azure API action.` If the Cloud Connector targets specific subscriptions and this subscription isn't one of them, the step fails with `The Azure subscription '{{subscription-id}}' is not in the list of allowed subscriptions for this Cloud Connector.`
Type: String
Required: Yes

API operation parameters
Any other inputs that you add to the step are passed to the Azure API operation as its path and query parameters. Use the parameter names from the Azure REST API reference. For example, `VirtualMachines.Get` takes `resourceGroupName` and `vmName`. Names aren't case-sensitive, and underscores are ignored. The following exceptions apply:
+ Omit the leading `$` from OData query parameters. For example, specify `filter`, `top`, and `expand` instead of `$filter`, `$top`, and `$expand`.
+ Don't specify `api-version`. The package sets the API version.
+ Header parameters, such as `If-Match`, `If-None-Match`, and `x-ms-*` headers, aren't supported.
For more information, see [Pass parameters and a request body](automation-multicloud-runbooks.md#automation-multicloud-runbooks-inputs).
Type: Determined by the chosen API operation
Required: Determined by the chosen API operation

Body
The request body of the API operation, as a JSON object in the shape that the Azure REST API reference shows. For example, for `AvailabilitySets.CreateOrUpdate`, `{"location": "eastus", "tags": {"environment": "test"}}`. Use this input only for an operation that takes a request body. Pass request-body properties in `Body` rather than as separate step inputs.
Type: StringMap (a JSON object; values can be nested objects and lists)
Required: Determined by the chosen API operation

NextLink
Use this input to get the next page of a list operation. Give it the `nextLink` value from the previous response. The step returns the next page. The URL must start with `https://management.azure.com/subscriptions/` followed by the step's `SubscriptionId`. You can't get further pages of a list that isn't scoped to a subscription.
Type: String
Required: No

**Outputs**
You specify outputs based on the response from the chosen API operation.

Name
A name for the output.
Type: String
Required: Yes

Selector
The JSONPath to a specific attribute in the response object. Automation returns the Azure response as a JSON object. For example, for `VirtualMachines.Get`, the selector `$.location` returns the resource's region, and `$.properties.provisioningState` returns its provisioning state. The response uses the property names from the Azure REST API reference. A list operation returns one page. For more information about the JSONPath that you can use, see [Select values from the response](automation-multicloud-runbooks.md#automation-multicloud-runbooks-selectors).
Type: String
Required: Yes

Type
The data type for the response element. Valid values: `String`, `Integer`, `Boolean`, `StringList`, `StringMap`, `MapList`.
Type: String
Required: Yes

**Response size limit**
The Azure response can be at most 358,400 characters, before Automation applies selectors. A larger response fails the step with `Step output size of {{size}} exceeds size limit of 358400 characters`. To stay under the limit with a list operation, request a smaller page or a narrower scope.

**Credentials and permissions**
Automation signs in to Azure with the Cloud Connector. If the automation has an `AutomationAssumeRole`, Automation uses that role to assume the connector's federation role. Otherwise, it uses the credentials of the user who started the automation. For more information about the permissions that each role needs, see [Permissions for automations that use a Cloud Connector](automation-cloud-connector-permissions.md).

**Find an operation**
To find the operations and parameters of a service, see the [Azure REST API reference](https://learn.microsoft.com/rest/api/azure/) on the Microsoft Learn website.
<a name="automation-action-executeAzureApi-naming"></a>
**Naming rules**
To build the `Api` value from a page in the Azure REST API reference, take the operation group and the operation from the page title and remove the spaces. For example, *Virtual Machines - Instance View* becomes `VirtualMachines.InstanceView`. You can also use the SDK's snake\_case names, such as `virtual_machines.instance_view`. The following exceptions apply:
+ In an operation group name, write an acronym that follows other words with only its first letter capitalized. For example, specify `VirtualMachineScaleSetVms.Get`, not `VirtualMachineScaleSetVMs.Get`. Or use the snake\_case form, such as `virtual_machine_scale_set_vms.get`.
+ If the Azure SDK for Python renames an operation, use the SDK name. For example, for the REST operation *Databases - Import*, specify `Databases.ImportMethod`.
+ Don't write the operation group in lowercase without underscores. `virtualmachines.get` isn't accepted. Use `VirtualMachines.Get` or `virtual_machines.get`.
<a name="automation-action-executeAzureApi-limitations"></a>
**Limitations**
The following limitations apply to `aws:executeAzureApi`, `aws:assertAzureResourceProperty`, and `aws:waitForAzureResourceProperty`.
+ Operations that aren't in an operation group, such as `CheckDnsNameAvailability` in `network` and `CheckNameAvailability` in `web`, aren't supported.
+ The package sets the API version of each service. The Azure REST API reference can show a newer version, with parameters or properties that the package's version doesn't have.
+ Each call to Azure must finish within 30 seconds. Otherwise, the step fails with `Provider API dispatch timed out`.

To call a service or operation that isn't supported, use a Python script in `aws:executeScript` with the same package. For more information, see [`aws:executeScript` – Run a script](automation-action-executeScript.md).

**Example – Get a virtual machine**
The following step gets a virtual machine and returns its name and region.

------
#### [ YAML ]

```yaml
name: getVirtualMachine
action: aws:executeAzureApi
inputs:
  Service: compute
  Api: VirtualMachines.Get
  Package: azure_202610
  CloudConnector: a1b2c3d4-5678-90ab-cdef-111122223333
  SubscriptionId: "11111111-2222-3333-4444-555555555555"
  resourceGroupName: my-resource-group
  vmName: my-vm
outputs:
- Name: VmName
  Selector: $.name
  Type: String
- Name: Region
  Selector: $.location
  Type: String
```

------
#### [ JSON ]

```json
{
  "name": "getVirtualMachine",
  "action": "aws:executeAzureApi",
  "inputs": {
    "Service": "compute",
    "Api": "VirtualMachines.Get",
    "Package": "azure_202610",
    "CloudConnector": "a1b2c3d4-5678-90ab-cdef-111122223333",
    "SubscriptionId": "11111111-2222-3333-4444-555555555555",
    "resourceGroupName": "my-resource-group",
    "vmName": "my-vm"
  },
  "outputs": [
    {
      "Name": "VmName",
      "Selector": "$.name",
      "Type": "String"
    },
    {
      "Name": "Region",
      "Selector": "$.location",
      "Type": "String"
    }
  ]
}
```

------

The following YAML and JSON examples show a step that creates an availability set with a tag, and returns its name.

------
#### [ YAML ]

```yaml
name: createAvailabilitySet
action: aws:executeAzureApi
inputs:
  Service: compute
  Api: AvailabilitySets.CreateOrUpdate
  Package: azure_202610
  CloudConnector: a1b2c3d4-5678-90ab-cdef-111122223333
  SubscriptionId: "11111111-2222-3333-4444-555555555555"
  resourceGroupName: my-resource-group
  availabilitySetName: my-availability-set
  Body:
    location: eastus
    tags:
      environment: test
outputs:
- Name: AvailabilitySetName
  Selector: $.name
  Type: String
```

------
#### [ JSON ]

```json
{
  "name": "createAvailabilitySet",
  "action": "aws:executeAzureApi",
  "inputs": {
    "Service": "compute",
    "Api": "AvailabilitySets.CreateOrUpdate",
    "Package": "azure_202610",
    "CloudConnector": "a1b2c3d4-5678-90ab-cdef-111122223333",
    "SubscriptionId": "11111111-2222-3333-4444-555555555555",
    "resourceGroupName": "my-resource-group",
    "availabilitySetName": "my-availability-set",
    "Body": {
      "location": "eastus",
      "tags": {
        "environment": "test"
      }
    }
  },
  "outputs": [
    {
      "Name": "AvailabilitySetName",
      "Selector": "$.name",
      "Type": "String"
    }
  ]
}
```

------

If Azure returns an error, for example because the connector's Azure application doesn't have permission or the resource doesn't exist, the step fails with an error that starts with `Azure error ({{code}})` or `Azure client error ({{status}})` and includes Azure's message. For an Azure server error, the message starts with `Unexpected Azure error`. To let the automation continue after a failure, set `onFailure` on the step. For common errors, see [Troubleshooting automations that use a Cloud Connector](automation-cloud-connector-troubleshooting.md).
