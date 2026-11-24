---
source_url: https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-action-executeGcpApi.html
---

# `aws:executeGcpApi` – Call and run Google Cloud API operations

The `aws:executeGcpApi` action calls a Google Cloud API method in the Google Cloud projects that a Cloud Connector allows. Automation calls the operation with the Google Cloud client libraries for Python and returns the response as a JSON object, so you can select values from it the same way as for [`aws:executeAwsApi` – Call and run AWS API operations](automation-action-executeAwsApi.md).

**Note**
The `aws:executeGcpApi` action is available in the AWS Regions where Cloud Connector is available.

**Input**
You provide `Service`, `Api`, `Package`, and `CloudConnector`. Each other input is a field of the method's request. You can give the request body in `Body` instead of the request field that holds it.

------
#### [ YAML ]

```yaml
action: aws:executeGcpApi
inputs:
  Service: {{The client library name}}
  Api: {{The method, as Service.Method from the RPC reference}}
  Package: {{The Google Cloud package name}}
  CloudConnector: {{The Cloud Connector ID}}
  {{Request field}}: {{A value}}
  Body: {{The request body, as a JSON object}}
outputs: # {{These are user-specified outputs}}
- Name: {{The name for a user-specified output key}}
  Selector: {{A response attribute specified by using JSONPath format}}
  Type: {{The data type}}
```

------
#### [ JSON ]

```json
{
   "action":"aws:executeGcpApi",
   "inputs":{
      "Service":"{{The client library name}}",
      "Api":"{{The method, as Service.Method from the RPC reference}}",
      "Package":"{{The Google Cloud package name}}",
      "CloudConnector":"{{The Cloud Connector ID}}",
      "{{Request field}}":"{{A value}}",
      "Body":{ {{The request body, as a JSON object}} }
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
The client library name, as in `google.cloud.{{service}}` without the version, for example `secretmanager`, `kms` or `resourcemanager`. It is not the API's host name (`cloudkms`).
Type: String
Required: Yes

Api
`{{Service}}.{{Method}}` from the API's RPC reference, for example `SecretManagerService.ListSecrets`.
Type: String
Required: Yes

Package
The name of the published Google Cloud package that provides the operation. For more information about the available packages and the libraries in each, see [Azure and Google Cloud SDK packages](automation-multicloud-packages.md).
Type: String
Required: Yes

CloudConnector
The ID of the Cloud Connector for the Google Cloud projects that the step acts on. For example, `a1b2c3d4-5678-90ab-cdef-111122223333`.
Type: String
Required: Yes

Request fields
One input per field, named as in either the RPC or the REST reference (`pageSize` or `page_size`). The project goes in `project`, `name`, `parent` or `resource`, and it must be one of the Cloud Connector's projects.
Type: Determined by the chosen API operation
Required: Determined by the chosen API operation

Body
The request body, as a JSON object in the shape that the method's REST reference shows.
Type: StringMap (a JSON object; values can be nested objects and lists)
Required: No

**Outputs**
You specify outputs based on the response from the chosen API operation.

Name
A name for the output.
Type: String
Required: Yes

Selector
Selectors over the response JSON from the REST reference.
+ Field names are camelCase (`createTime`).
+ Enums come back as names, and 64-bit integers as strings.
+ A list method returns one page with `nextPageToken`. Pass that back as `pageToken` to get the next page.
Use output type `String` for 64-bit integers, such as `id` and `diskSizeGb`. Except in Compute Engine, a field that has its default value (`false`, `0`, or an empty string) is left out of the response, as in the REST API.
For more information about the JSONPath that you can use, see [Select values from the response](automation-multicloud-runbooks.md#automation-multicloud-runbooks-selectors).
Type: String
Required: Yes

Type
The data type for the response element. Valid values: `String`, `Integer`, `Boolean`, `StringList`, `StringMap`, `MapList`.
Type: String
Required: Yes

**Credentials and permissions**
Before the step runs, Automation gets a short-lived Google Cloud access token for the connector's service account. If the automation has an `AutomationAssumeRole`, that role assumes the connector's federation role. Otherwise, the identity that started the automation does. For more information about the permissions that each role needs, see [Permissions for automations that use a Cloud Connector](automation-cloud-connector-permissions.md).

**Find a method**
To find a method and its request fields, see [Google Cloud APIs](https://cloud.google.com/apis) on the Google Cloud website, and open the RPC reference for the service. Compute Engine has no RPC reference; use its REST reference.
<a name="automation-action-executeGcpApi-limitations"></a>
**Limitations**
The following limitations apply to `aws:executeGcpApi`, `aws:assertGcpResourceProperty`, and `aws:waitForGcpResourceProperty`.
+ Each call returns one page and doesn't wait for a long-running operation to finish. Compute Engine returns the `Operation` resource, with a `status` of `PENDING`, `RUNNING`, or `DONE`. Other services return a long-running operation with a `name`, and `"done": true` when it finishes.
+ Each call can run for up to 30 seconds. If Google Cloud doesn't respond in that time, the step fails with `Provider API dispatch timed out`.
+ Automation rejects a request that names no project in `project`, `name`, `parent`, or `resource`, with `The request does not name a GCP project, so it cannot be authorized against the Cloud Connector's scope.` This includes organization, folder, and billing-account resources, methods that take the project in another field, such as Pub/Sub `Publisher.GetTopic` (`topic`) and Dataproc (`projectId`), and update methods whose resource name is inside a request field, such as `AlertPolicyService.UpdateAlertPolicy`.
+ Give a project ID, not a project number. Automation rejects a project number, `projects/-`, and a project outside the connector, including public image projects such as `debian-cloud`, with `The GCP project '{{project}}' is not in the list of allowed projects for this Cloud Connector.` If the connector covers a whole organization, any project ID is accepted.
+ The IAM policy methods (`GetIamPolicy`, `SetIamPolicy`, and `TestIamPermissions`) are supported only for Compute Engine.
+ A 32-bit integer field, such as `maxResults` or `pageSize`, must be a number. A value from a runbook parameter of type `String` is rejected; use type `Integer`. 64-bit integers can be numbers or strings.
+ Give a nested field as an object, not as a dotted name. For example, use `interval: {startTime: '2026-01-01T00:00:00Z'}`, not `interval.startTime`.
+ A bytes field must be base64-encoded, as in the REST API. Automation doesn't reject plain text, so plain text is sent as different bytes.
+ The package sets each library's API version. A field that the reference shows but the package's library doesn't have, such as `returnPartialSuccess`, or a REST system parameter such as `fields`, is rejected as an unknown parameter.

To call a service or operation that isn't supported, use a Python script in `aws:executeScript` with the same package. For more information, see [`aws:executeScript` – Run a script](automation-action-executeScript.md).

**Example – Get a virtual machine instance**
The following step gets a virtual machine instance and returns its state. Replace the Cloud Connector ID with your own.

------
#### [ YAML ]

```yaml
name: getInstance
action: aws:executeGcpApi
inputs:
  Service: compute
  Api: Instances.Get
  Package: gcp_202610
  CloudConnector: a1b2c3d4-5678-90ab-cdef-111122223333
  project: my-project
  zone: us-central1-a
  instance: my-vm
outputs:
- Name: InstanceState
  Selector: $.status
  Type: String
```

------
#### [ JSON ]

```json
{
  "name": "getInstance",
  "action": "aws:executeGcpApi",
  "inputs": {
    "Service": "compute",
    "Api": "Instances.Get",
    "Package": "gcp_202610",
    "CloudConnector": "a1b2c3d4-5678-90ab-cdef-111122223333",
    "project": "my-project",
    "zone": "us-central1-a",
    "instance": "my-vm"
  },
  "outputs": [
    {
      "Name": "InstanceState",
      "Selector": "$.status",
      "Type": "String"
    }
  ]
}
```

------

The following YAML and JSON examples show a step that resizes a persistent disk to 200 GB. `Disks.Resize` returns the `Operation` resource as soon as Google Cloud accepts the request, so `OperationStatus` is usually `RUNNING` or `PENDING`. To wait until the resize finishes, pass `OperationName` as the `operation` field of a `ZoneOperations.Get` step in `aws:waitForGcpResourceProperty`, with the `PropertySelector` `$.status` and the `DesiredValues` `DONE`. An operation that failed also reaches `DONE`, and has an `error` property.

------
#### [ YAML ]

```yaml
name: resizeDisk
action: aws:executeGcpApi
inputs:
  Service: compute
  Api: Disks.Resize
  Package: gcp_202610
  CloudConnector: a1b2c3d4-5678-90ab-cdef-111122223333
  project: my-project
  zone: us-central1-a
  disk: my-disk
  Body:
    sizeGb: 200
outputs:
- Name: OperationStatus
  Selector: $.status
  Type: String
- Name: OperationName
  Selector: $.name
  Type: String
```

------
#### [ JSON ]

```json
{
  "name": "resizeDisk",
  "action": "aws:executeGcpApi",
  "inputs": {
    "Service": "compute",
    "Api": "Disks.Resize",
    "Package": "gcp_202610",
    "CloudConnector": "a1b2c3d4-5678-90ab-cdef-111122223333",
    "project": "my-project",
    "zone": "us-central1-a",
    "disk": "my-disk",
    "Body": {
      "sizeGb": 200
    }
  },
  "outputs": [
    {
      "Name": "OperationStatus",
      "Selector": "$.status",
      "Type": "String"
    },
    {
      "Name": "OperationName",
      "Selector": "$.name",
      "Type": "String"
    }
  ]
}
```

------

If Google Cloud rejects the call, the step fails with `GCP client error ({{status}}):` followed by Google Cloud's message, for example `GCP client error (403)` when the connector's service account lacks a permission. Automation also fails the step before it calls Google Cloud when the service, method, a request field, or the project isn't valid. The message names the problem. To let the automation continue after a failure, set `onFailure` on the step. For common errors, see [Troubleshooting automations that use a Cloud Connector](automation-cloud-connector-troubleshooting.md).
