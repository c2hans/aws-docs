---
source_url: https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-action-assertGcpResourceProperty.html
---

# `aws:assertGcpResourceProperty` – Assert a Google Cloud resource state

The `aws:assertGcpResourceProperty` action checks that a property of a Google Cloud resource has one of a set of values. The action calls a Google Cloud API operation once, reads the property named by `PropertySelector` from the response, and continues the automation only when the value is in `DesiredValues`. Otherwise, the step fails.

**Note**
The `aws:assertGcpResourceProperty` action is available in the AWS Regions where Cloud Connector is available.

**Input**
You provide the same inputs as [`aws:executeGcpApi` – Call and run Google Cloud API operations](automation-action-executeGcpApi.md), plus `PropertySelector` and `DesiredValues`.

------
#### [ YAML ]

```yaml
action: aws:assertGcpResourceProperty
inputs:
  Service: {{The client library name}}
  Api: {{The method, as Service.Method from the RPC reference}}
  Package: {{The Google Cloud package name}}
  CloudConnector: {{The Cloud Connector ID}}
  {{Request field}}: {{A value}}
  Body: {{The request body, as a JSON object}}
  PropertySelector: {{Response attribute}}
  DesiredValues:
  - {{Desired property value}}
```

------
#### [ JSON ]

```json
{
  "action": "aws:assertGcpResourceProperty",
  "inputs": {
    "Service":"{{The client library name}}",
    "Api":"{{The method, as Service.Method from the RPC reference}}",
    "Package":"{{The Google Cloud package name}}",
    "CloudConnector":"{{The Cloud Connector ID}}",
    "{{Request field}}":"{{A value}}",
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
The request body, as a JSON object in the shape that the method's REST reference shows. You can use `Body` instead of the request field that holds the body. It works only for client libraries that support REST, such as Compute Engine and Secret Manager. Other libraries, such as Cloud Monitoring, Pub/Sub, and IAM, reject it with `takes no request body`; give the request fields instead.
Type: StringMap (a JSON object; values can be nested objects and lists)
Required: No

PropertySelector
Selectors over the response JSON from the REST reference.
+ Field names are camelCase (`createTime`).
+ Enums come back as names, and 64-bit integers as strings.
+ A list method returns one page with `nextPageToken`. Pass that back as `pageToken` to get the next page.
For more information about the JSONPath that you can use, see [Select values from the response](automation-multicloud-runbooks.md#automation-multicloud-runbooks-selectors).
Type: String
Required: Yes

DesiredValues
The values on which to continue the automation. Automation compares each value that `PropertySelector` matches, as a string, with this list. Give Boolean values as `True` or `False`. If the selector matches several values, each one must be in the list.
If the selector matches nothing, for example because the response leaves out a field at its default value, the step fails with `Property value from the API output is empty. Desired values: ['RUNNING']`. If a value isn't in the list, the step fails with `Property value 'TERMINATED' from the API output is not in the desired values. Desired values: ['RUNNING']`. If the API call fails, for example with `GCP client error (404)` because the resource doesn't exist, the step fails with that error.
Type: StringList
Required: Yes

Before the step runs, Automation gets a short-lived Google Cloud access token for the connector's service account. If the automation has an `AutomationAssumeRole`, that role assumes the connector's federation role. Otherwise, the identity that started the automation does. For more information about the permissions that each role needs, see [Permissions for automations that use a Cloud Connector](automation-cloud-connector-permissions.md).

For more information about the limitations that apply to all Google Cloud API actions, see [Limitations](automation-action-executeGcpApi.md#automation-action-executeGcpApi-limitations).

**Example – Assert that a virtual machine instance is running**
The following step asserts that a virtual machine instance is running.

------
#### [ YAML ]

```yaml
name: assertInstanceRunning
action: aws:assertGcpResourceProperty
inputs:
  Service: compute
  Api: Instances.Get
  Package: gcp_202610
  CloudConnector: a1b2c3d4-5678-90ab-cdef-111122223333
  project: my-project
  zone: us-central1-a
  instance: my-vm
  PropertySelector: $.status
  DesiredValues:
  - RUNNING
```

------
#### [ JSON ]

```json
{
  "name": "assertInstanceRunning",
  "action": "aws:assertGcpResourceProperty",
  "inputs": {
    "Service": "compute",
    "Api": "Instances.Get",
    "Package": "gcp_202610",
    "CloudConnector": "a1b2c3d4-5678-90ab-cdef-111122223333",
    "project": "my-project",
    "zone": "us-central1-a",
    "instance": "my-vm",
    "PropertySelector": "$.status",
    "DesiredValues": [
      "RUNNING"
    ]
  }
}
```

------
