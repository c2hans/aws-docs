---
source_url: https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-multicloud-runbooks.html
---

# Create runbooks that call Azure and Google Cloud APIs

A runbook can call Microsoft Azure and Google Cloud APIs through a Cloud Connector. Automation uses the connector to get short-lived Azure or Google Cloud credentials, so the runbook doesn't store any cloud credentials. You can call the APIs in two ways:

API actions
Each step calls one API operation, and you don't write code. Use these actions when one call, a check, or a wait does what you need.

`aws:executeScript` with a cloud SDK
Use the Azure or Google Cloud package libraries in a Python script. Automation provides the libraries and an access token for the connector's cloud. Use a script when you need several calls, loops, or your own logic in one step.

A runbook that calls Azure or Google Cloud APIs can have the following inputs:
+ An `AutomationAssumeRole` input that the runbook's `assumeRole` names. Automation uses this role to get credentials for the connector's cloud. Without an assume role, Automation uses the identity of the person who starts the automation, and the connector's federation role must trust that identity. For more information about the role to use, see [Permissions for automations that use a Cloud Connector](automation-cloud-connector-permissions.md).
+ An input for the Cloud Connector ID, of type `AWS::SSM::CloudConnector::Id`, that you pass to each step that calls a cloud API or SDK.
+ To execute the runbook in rate-controlled mode with a Cloud Connector target, an input for the resource, of a resource type such as `microsoft.Compute/VirtualMachines` or `compute.googleapis.com/Instance`. Automation passes each target resource's ID in this input. For more information about the types, see [Parameter types for Azure and Google Cloud resources](automation-multicloud-parameter-types.md).

## Choose an API action
<a name="automation-multicloud-runbooks-actions"></a>

The following actions call Azure and Google Cloud APIs. Each one takes a `CloudConnector` input and a `Package` input that names the SDK package to use.

| Azure | Google Cloud | Use it to |
| --- | --- | --- |
| [`aws:executeAzureApi` – Call and run Azure API operations](automation-action-executeAzureApi.md) | [`aws:executeGcpApi` – Call and run Google Cloud API operations](automation-action-executeGcpApi.md) | Call one API operation and select values from the response. |
| [`aws:assertAzureResourceProperty` – Assert an Azure resource state](automation-action-assertAzureResourceProperty.md) | [`aws:assertGcpResourceProperty` – Assert a Google Cloud resource state](automation-action-assertGcpResourceProperty.md) | Continue only when a resource property has one of a set of values. |
| [`aws:waitForAzureResourceProperty` – Wait on an Azure resource property](automation-action-waitForAzureResourceProperty.md) | [`aws:waitForGcpResourceProperty` – Wait on a Google Cloud resource property](automation-action-waitForGcpResourceProperty.md) | Wait until a resource property has one of a set of values. |

Each of the following runbooks acts on one VM. When you execute a runbook on a Cloud Connector target with rate control, Automation executes it once for each resource that the target selects. Each runbook splits the resource ID (here, a VM ID) into its parts with `aws:executeScript`, because each API action takes them as separate inputs.

The Azure runbook checks that the VM is running. The Google Cloud runbook starts the instance, and then waits until it's running:

------
#### [ Azure ]

This runbook splits the VM ID into the subscription, resource group, and VM name.

```yaml
description: Checks that an Azure VM is running.
schemaVersion: '0.3'
assumeRole: '{{ AutomationAssumeRole }}'
parameters:
  AutomationAssumeRole:
    type: AWS::IAM::Role::Arn
    description: The role that Automation assumes to run this runbook.
  CloudConnector:
    type: AWS::SSM::CloudConnector::Id
    description: The Cloud Connector that reaches the VM.
  VmId:
    type: microsoft.Compute/VirtualMachines
    description: The resource ID of the Azure VM.
mainSteps:
  - name: parseVmId
    action: aws:executeScript
    inputs:
      Runtime: python3.11
      Handler: parse_vm_id
      InputPayload:
        VmId: '{{ VmId }}'
      Script: |-
        def parse_vm_id(events, context):
            # Resource IDs can be in any casing (a Cloud Connector target passes them in lowercase), so compare segment names in lowercase.
            segments = events["VmId"].strip("/").split("/")
            parts = {segments[i].lower(): segments[i + 1] for i in range(0, len(segments) - 1, 2)}
            return {
                "subscriptionId": parts["subscriptions"],
                "resourceGroup": parts["resourcegroups"],
                "vmName": parts["virtualmachines"],
            }
    outputs:
      - Name: SubscriptionId
        Selector: $.Payload.subscriptionId
        Type: String
      - Name: ResourceGroup
        Selector: $.Payload.resourceGroup
        Type: String
      - Name: VmName
        Selector: $.Payload.vmName
        Type: String
  - name: assertRunning
    action: aws:assertAzureResourceProperty
    inputs:
      Service: compute
      Api: VirtualMachines.Get
      Package: azure_202610
      CloudConnector: '{{ CloudConnector }}'
      SubscriptionId: '{{ parseVmId.SubscriptionId }}'
      resourceGroupName: '{{ parseVmId.ResourceGroup }}'
      vmName: '{{ parseVmId.VmName }}'
      expand: instanceView
      PropertySelector: $.properties.instanceView.statuses[1].code
      DesiredValues:
        - PowerState/running
```

In the `assertRunning` step, `resourceGroupName`, `vmName`, and `expand` are passed to the API operation as its parameters. `expand: instanceView` adds the VM's power state to the response. The other inputs are inputs of the action. The step continues the automation only if the VM's power state is running. Otherwise, the step fails.

------
#### [ Google Cloud ]

This runbook splits the instance ID into the project, zone, and instance name.

```yaml
description: Starts a Google Cloud VM instance and waits until it's running.
schemaVersion: '0.3'
assumeRole: '{{ AutomationAssumeRole }}'
parameters:
  AutomationAssumeRole:
    type: AWS::IAM::Role::Arn
    description: The role that Automation assumes to run this runbook.
  CloudConnector:
    type: AWS::SSM::CloudConnector::Id
    description: The Cloud Connector that reaches the instance.
  InstanceId:
    type: compute.googleapis.com/Instance
    description: The instance, as projects/PROJECT/zones/ZONE/instances/NAME or //compute.googleapis.com/projects/PROJECT/zones/ZONE/instances/NAME.
mainSteps:
  - name: parseInstanceId
    action: aws:executeScript
    inputs:
      Runtime: python3.11
      Handler: parse_instance_id
      InputPayload:
        InstanceId: '{{ InstanceId }}'
      Script: |-
        def parse_instance_id(events, context):
            name = events["InstanceId"].removeprefix("//compute.googleapis.com/").strip("/")
            segments = name.split("/")
            parts = {segments[i]: segments[i + 1] for i in range(0, len(segments) - 1, 2)}
            return {
                "project": parts["projects"],
                "zone": parts["zones"],
                "instanceName": parts["instances"],
            }
    outputs:
      - Name: Project
        Selector: $.Payload.project
        Type: String
      - Name: Zone
        Selector: $.Payload.zone
        Type: String
      - Name: InstanceName
        Selector: $.Payload.instanceName
        Type: String
  - name: startInstance
    action: aws:executeGcpApi
    inputs:
      Service: compute
      Api: Instances.Start
      Package: gcp_202610
      CloudConnector: '{{ CloudConnector }}'
      project: '{{ parseInstanceId.Project }}'
      zone: '{{ parseInstanceId.Zone }}'
      instance: '{{ parseInstanceId.InstanceName }}'
  - name: waitForRunning
    action: aws:waitForGcpResourceProperty
    timeoutSeconds: 600
    inputs:
      Service: compute
      Api: Instances.Get
      Package: gcp_202610
      CloudConnector: '{{ CloudConnector }}'
      project: '{{ parseInstanceId.Project }}'
      zone: '{{ parseInstanceId.Zone }}'
      instance: '{{ parseInstanceId.InstanceName }}'
      PropertySelector: $.status
      DesiredValues:
        - RUNNING
```

In the `startInstance` and `waitForRunning` steps, `project`, `zone`, and `instance` are passed to the API operation as its parameters. The other inputs are inputs of the action.

The `startInstance` step returns when Google Cloud accepts the request, before the instance is running. The `waitForRunning` step then checks the instance's status until it's `RUNNING`. Set `timeoutSeconds` on that step, as the example does, so that it stops checking if the instance doesn't start.

**Important**
The custom role that connector setup gives the connector's service account can read instances, but it doesn't include `compute.instances.start`. Until you give the service account a role that includes it in the instance's project, the `startInstance` step fails with an error that includes `GCP client error (403)`. For more information, see [Permissions in Azure and Google Cloud](automation-cloud-connector-permissions.md#automation-cloud-connector-permissions-cloud).

------

## Pass parameters and a request body
<a name="automation-multicloud-runbooks-inputs"></a>

Each API action has its own inputs, such as `Service`, `Api`, `Package`, and `CloudConnector`, which the action's page describes. Automation passes every other step input to the API operation as a parameter. Name these parameters as the cloud's REST API reference does. For Google Cloud, only the `Api` input uses the name from the RPC reference. The following exceptions apply:
+ For an Azure OData query parameter, leave out the leading `$` (for example, `expand`, not `$expand`). Azure header parameters, such as `If-Match`, `If-None-Match`, and `x-ms-*` headers, aren't supported.
+ For Google Cloud, give a nested field as an object, not as a dotted name. For example, use `interval: {startTime: '2026-01-01T00:00:00Z'}`, not `interval.startTime`. For the other rules, see [`aws:executeGcpApi` – Call and run Google Cloud API operations](automation-action-executeGcpApi.md).

Path and query parameters
Add each parameter as a step input with its name from the REST API reference. For example, Azure `VirtualMachines.Get` takes `resourceGroupName` and `vmName`, and Google Cloud `Instances.Get` takes `project`, `zone`, and `instance`. Names aren't case-sensitive, and underscores are ignored.

`Body`
For an operation that takes a request body, put the body in the `Body` input. Use an object in the shape that the Azure or Google Cloud REST API reference shows for the request body. In a YAML runbook, write the object as nested keys, as the following example shows.
For example, the following inputs create an Azure availability set with a tag, with `AvailabilitySets.CreateOrUpdate`:

```yaml
  resourceGroupName: my-resource-group
  availabilitySetName: my-availability-set
  Body:
    location: eastus
    tags:
      environment: test
```

**Note**
Although you can also give top-level request-body properties as separate step inputs, beside the path and query parameters, use `Body` instead. A separate input is always used as the path or query parameter of the same name, so a body property that shares a name with a path or query parameter can be set only in `Body`.

Automation checks the request before it calls the cloud. The step fails with a validation error if the request has any of these problems:
+ A property in `Body` isn't in the request body. The error names the property with a `Body.` prefix, for example `Body.locaton`.
+ `Body` isn't a JSON object, or the operation doesn't take a request body.
+ The same body property is in `Body` and in a separate step input.

## Lists and long-running operations
<a name="automation-multicloud-runbooks-paging"></a>

The API actions make one call to the cloud, like one REST API request. They don't read further pages of a list or wait for a long-running operation to finish.

A list operation returns one page of results. Each cloud tells you that more items remain, and how to get them, as follows:
+ Azure returns the items in `value`. When more items remain, the response also has `nextLink`. To get the next page, run the same operation with the `NextLink` input set to that value.
+ Google Cloud includes `nextPageToken` when more items remain. To get the next page, run the same operation with the operation's `pageToken` parameter set to that value. To set the page size, use the operation's `maxResults` (Compute Engine) or `pageSize` parameter. Pass the page size as a number, for example from a parameter of type `Integer`.

A long-running operation returns without waiting for the operation to finish, as follows:
+ An Azure long-running operation, such as starting a virtual machine, returns the first response that Azure sends, as soon as Azure accepts the request. This is often the resource with a `provisioningState` of `Updating`, or an empty object.
+ A Compute Engine operation that changes a resource, such as `Instances.Start`, returns the `Operation` resource without waiting for it to finish. To wait on the operation itself, poll the `Operation` resource with [`aws:waitForGcpResourceProperty` – Wait on a Google Cloud resource property](automation-action-waitForGcpResourceProperty.md), for example with `Api: ZoneOperations.Get` and a `PropertySelector` of `$.status` that waits for `DONE`. `DONE` means that the operation finished, not that it succeeded. A failed operation also reaches `DONE` and reports the failure in its `error` property. To check for a failure, get the operation again in a later step and check `$.error`.

To wait for the result, add an [`aws:waitForAzureResourceProperty` – Wait on an Azure resource property](automation-action-waitForAzureResourceProperty.md) or [`aws:waitForGcpResourceProperty` – Wait on a Google Cloud resource property](automation-action-waitForGcpResourceProperty.md) step after it, as the Google Cloud example in [Choose an API action](#automation-multicloud-runbooks-actions) does.

## Select values from the response
<a name="automation-multicloud-runbooks-selectors"></a>

The API actions return the cloud's response as a JSON object. Output `Selector` values and `PropertySelector` are JSONPath expressions into that object. Keep the following in mind when you write them:
+ Property names are the ones in the cloud's REST API reference, usually in camelCase. An Azure resource has most of its properties under `properties`. For example, use `$.properties.provisioningState` and `$.properties.hardwareProfile.vmSize` for an Azure VM, and `$.machineType` for a Google Cloud instance.
+ A list operation returns one page. Azure returns its items in a `value` list, such as for `VirtualMachines.ListAll`. Select from it with `$.value`, for example `$.value[0].name` or `$.value[?(@.location == 'eastus')].name`. For more pages, see [Lists and long-running operations](#automation-multicloud-runbooks-paging).
+ For more information about the JSONPath operators that you can use, see [Using JSONPath in runbooks](automation-action-outputs-inputs.md#automation-action-json-path).
+ Match `DesiredValues` to the value as the response returns it. Both clouds return enum values as strings, such as `Succeeded` in Azure and `RUNNING` in Google Cloud.
+ An API action's response can be at most 358,400 characters, before Automation applies selectors. A larger response fails the step with `Step output size of {{size}} exceeds size limit of 358400 characters`. For a large list, request a single resource, a narrower scope, or a smaller page.

## Use the Azure and Google Cloud SDKs in a script
<a name="automation-multicloud-runbooks-sdk"></a>

In an `aws:executeScript` step, set these two inputs to call Azure or Google Cloud from a Python script:

`CloudConnector`
The Cloud Connector ID. Automation gets an access token for the connector's cloud and sets it as an environment variable in the script's runtime environment.

`Package`
The SDK package to add to the script's runtime. The script imports the libraries in the package directly, so you don't install them. For the available packages and the runtimes that each supports, see [Azure and Google Cloud SDK packages](automation-multicloud-packages.md).

The Azure package contains Azure SDK for Python libraries such as `azure.mgmt.compute`, and the Google Cloud package contains Google Cloud client libraries for Python such as `google.cloud.compute_v1`. For more information about the full list of libraries and their major versions, see [Azure and Google Cloud SDK packages](automation-multicloud-packages.md).

Automation sets the `AZURE_ACCESS_TOKEN` or `GCP_ACCESS_TOKEN` environment variable in the script's runtime environment to an access token for the connector's cloud. For the other environment variables that Automation sets, see the `CloudConnector` input in [`aws:executeScript` – Run a script](automation-action-executeScript.md).

Keep the following in mind when you write the script:
+ `Package` isn't currently supported with the PowerShell runtime. In a PowerShell script, call the cloud's REST API with `Invoke-RestMethod` and the header `Authorization: Bearer $env:AZURE_ACCESS_TOKEN` or `Authorization: Bearer $env:GCP_ACCESS_TOKEN`.
+ Use a package for the connector's cloud. Automation doesn't check that the connector and the package are for the same cloud.
+ The token can't be refreshed. Build a credential that returns the token as-is, as the following examples do, so that the SDK doesn't try to get a new one. An `aws:executeScript` step runs for at most 600 seconds.
+ Don't print the token or return it in the step's output.
+ Don't use `azure.identity` credentials, such as `DefaultAzureCredential`, or `google.auth.default()`. They can't get a token in the step. Build the credential from `AZURE_ACCESS_TOKEN` or `GCP_ACCESS_TOKEN`, as the following examples do.
+ The Azure token works only with Azure Resource Manager, so use the management libraries (`azure.mgmt.*`). The data-plane libraries in the package, such as `azure.storage.blob`, need a different token.
+ For a Google Cloud API that has no `google.cloud` library, such as Cloud SQL Admin, use `googleapiclient.discovery.build(..., credentials=credentials, static_discovery=True)`.
+ The script's output is limited as described for `Payload` in [`aws:executeScript` – Run a script](automation-action-executeScript.md).
+ Your script can do only what the connector's identity can do in the cloud. To do more, give the connector's identity more roles in that cloud, as described in [Permissions in Azure and Google Cloud](automation-cloud-connector-permissions.md#automation-cloud-connector-permissions-cloud).

### Example – Azure
<a name="automation-multicloud-runbooks-sdk-azure"></a>

The following YAML runbook gets an Azure VM's size and power state with the Azure SDK for Python. The script builds an Azure credential from `AZURE_ACCESS_TOKEN` and passes it to `ComputeManagementClient`.

```yaml
description: Gets an Azure VM's size and power state with the Azure SDK for Python.
schemaVersion: '0.3'
assumeRole: '{{ AutomationAssumeRole }}'
parameters:
  AutomationAssumeRole:
    type: AWS::IAM::Role::Arn
    description: The role that Automation assumes to run this runbook.
  CloudConnector:
    type: AWS::SSM::CloudConnector::Id
    description: The Cloud Connector that reaches the VM.
  VmId:
    type: microsoft.Compute/VirtualMachines
    description: The resource ID of the Azure VM.
mainSteps:
  - name: getPowerState
    action: aws:executeScript
    inputs:
      Runtime: python3.11
      Handler: get_power_state
      CloudConnector: '{{ CloudConnector }}'
      Package: azure_202610
      InputPayload:
        VmId: '{{ VmId }}'
      Script: |-
        import os
        import time
        from types import SimpleNamespace

        from azure.core.credentials import AccessToken
        from azure.mgmt.compute import ComputeManagementClient

        def parse_vm_id(vm_id):
            """Returns the subscription ID, resource group, and VM name from an Azure VM resource ID.

            The ID can be in any casing, so the segment names are compared in lowercase.
            """
            segments = vm_id.strip("/").split("/")
            parts = {segments[i].lower(): segments[i + 1] for i in range(0, len(segments) - 1, 2)}
            return parts["subscriptions"], parts["resourcegroups"], parts["virtualmachines"]

        def get_power_state(events, context):
            subscription_id, resource_group, vm_name = parse_vm_id(events["VmId"])
            # The token can't be refreshed, so get_token returns the same token every time.
            # An aws:executeScript step runs for at most 600 seconds.
            token = AccessToken(os.environ["AZURE_ACCESS_TOKEN"], int(time.time()) + 600)
            credential = SimpleNamespace(get_token=lambda *scopes, **kwargs: token)
            with ComputeManagementClient(credential, subscription_id) as client:
                vm = client.virtual_machines.get(resource_group, vm_name, expand="instanceView")

            power_state = "unknown"
            statuses = vm.instance_view.statuses if vm.instance_view else []
            for status in statuses or []:
                if status.code and status.code.startswith("PowerState/"):
                    power_state = status.code.split("/", 1)[1]

            return {
                "vmName": vm.name,
                "location": vm.location,
                "vmSize": vm.hardware_profile.vm_size,
                "powerState": power_state,
            }
    outputs:
      - Name: VmSize
        Selector: $.Payload.vmSize
        Type: String
      - Name: PowerState
        Selector: $.Payload.powerState
        Type: String
```

To list resources across the connector's subscriptions, read `AZURE_SUBSCRIPTION_IDS`, a comma-separated list. Automation doesn't set it for a connector that covers the whole tenant.

### Example – Google Cloud
<a name="automation-multicloud-runbooks-sdk-gcp"></a>

The following YAML runbook gets a Google Cloud VM instance's status and machine type with the Google Cloud client libraries for Python. The script builds a credential from `GCP_ACCESS_TOKEN` and passes it to `InstancesClient`.

```yaml
description: Gets a Google Cloud VM instance's status with the Google Cloud client libraries for Python.
schemaVersion: '0.3'
assumeRole: '{{ AutomationAssumeRole }}'
parameters:
  AutomationAssumeRole:
    type: AWS::IAM::Role::Arn
    description: The role that Automation assumes to run this runbook.
  CloudConnector:
    type: AWS::SSM::CloudConnector::Id
    description: The Cloud Connector that reaches the instance.
  InstanceId:
    type: compute.googleapis.com/Instance
    description: The instance, as projects/PROJECT/zones/ZONE/instances/NAME or //compute.googleapis.com/projects/PROJECT/zones/ZONE/instances/NAME.
mainSteps:
  - name: getStatus
    action: aws:executeScript
    inputs:
      Runtime: python3.11
      Handler: get_status
      CloudConnector: '{{ CloudConnector }}'
      Package: gcp_202610
      InputPayload:
        InstanceId: '{{ InstanceId }}'
      Script: |-
        import os

        from google.cloud import compute_v1
        from google.oauth2.credentials import Credentials

        def parse_instance_id(instance_id):
            """Returns the project, zone, and instance name from projects/PROJECT/zones/ZONE/instances/NAME."""
            name = instance_id.removeprefix("//compute.googleapis.com/").strip("/")
            segments = name.split("/")
            parts = {segments[i]: segments[i + 1] for i in range(0, len(segments) - 1, 2)}
            return parts["projects"], parts["zones"], parts["instances"]

        def get_status(events, context):
            project, zone, instance_name = parse_instance_id(events["InstanceId"])
            # The token can't be refreshed. Credentials without an expiry time don't try to refresh it.
            credentials = Credentials(token=os.environ["GCP_ACCESS_TOKEN"])
            with compute_v1.InstancesClient(credentials=credentials) as client:
                instance = client.get(project=project, zone=zone, instance=instance_name)

            return {
                "instanceName": instance.name,
                "status": instance.status,
                "machineType": instance.machine_type.rsplit("/", 1)[-1],
            }
    outputs:
      - Name: Status
        Selector: $.Payload.status
        Type: String
      - Name: MachineType
        Selector: $.Payload.machineType
        Type: String
```

To list resources across the connector's projects, read `GCP_PROJECT_IDS`, a comma-separated list. Automation doesn't set it for a connector that covers a whole organization. Use `GCP_ORGANIZATION_ID` instead.

## Execute the runbook
<a name="automation-multicloud-runbooks-next"></a>

After you author a runbook, create it in Systems Manager. Then execute it. To show it in the **Hybrid and multicloud** filters of the Automation console and to offer the Cloud Connector target for it, set the runbook's cloud providers to `Azure` or `GCP`. For more information about cloud providers and running the runbook, see the following topics:
+ [Specifying cloud providers for SSM documents](documents-cloud-providers.md)
+ [Run an automation on Azure or Google Cloud resources (console)](running-automations-cloud-connector-console.md)
+ [Run an automation on Azure or Google Cloud resources (command line)](running-automations-cloud-connector-cli.md)
