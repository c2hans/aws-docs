---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-evs-environment-check.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EVS::Environment Check
<a name="aws-properties-evs-environment-check"></a>

A check on the environment to identify environment health and validate VMware VCF licensing compliance.

## Syntax
<a name="aws-properties-evs-environment-check-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-evs-environment-check-syntax.json"></a>

```
{
  "[ImpairedSince](#cfn-evs-environment-check-impairedsince)" : {{String}},
  "[Result](#cfn-evs-environment-check-result)" : {{String}},
  "[Type](#cfn-evs-environment-check-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-evs-environment-check-syntax.yaml"></a>

```
  [ImpairedSince](#cfn-evs-environment-check-impairedsince): {{String}}
  [Result](#cfn-evs-environment-check-result): {{String}}
  [Type](#cfn-evs-environment-check-type): {{String}}
```

## Properties
<a name="aws-properties-evs-environment-check-properties"></a>

`ImpairedSince`  <a name="cfn-evs-environment-check-impairedsince"></a>
The time when environment health began to be impaired.
*Required*: No
*Type*: String
*Update requires*: Updates are not supported.

`Result`  <a name="cfn-evs-environment-check-result"></a>
 The check result.
*Required*: Yes
*Type*: String
*Allowed values*: `PASSED | FAILED | UNKNOWN`
*Update requires*: Updates are not supported.

`Type`  <a name="cfn-evs-environment-check-type"></a>
The check type. Amazon EVS performs the following checks:
+ `KEY_REUSE`: Verifies that the VCF license key is not used by another Amazon EVS environment.
+ `KEY_COVERAGE`: Verifies that the VCF license key allocates sufficient vCPU cores for all deployed hosts.
+ `REACHABILITY`: Verifies that the Amazon EVS control plane has a persistent connection to SDDC Manager.
+ `HOST_COUNT`: Verifies that the environment meets the minimum host count.
+ `VCENTER_REACHABILITY`: Verifies vCenter Server reachability through the vCenter connector.
+ `VCENTER_VM_SYNC`: Verifies that the vCenter connector can synchronize VM inventory from vCenter Server.
+ `VCENTER_VM_EVENT`: Verifies that the vCenter connector can receive VM lifecycle events from vCenter Server.
+ `OPERATIONS_MANAGER_REACHABILITY`: Verifies Operations Manager reachability through the Operations Manager connector.
+ `SDDC_MANAGER_REACHABILITY`: Verifies SDDC Manager reachability through the SDDC Manager connector.
+ `SDDC_MANAGER_HOST_COUNT`: Verifies that the host count reported by SDDC Manager meets Amazon EVS minimum requirements.
+ `SDDC_MANAGER_KEY_COVERAGE`: Verifies that the VCF license key configured in SDDC Manager covers all deployed hosts.
+ `SDDC_MANAGER_KEY_REUSE`: Verifies that the VCF license key configured in SDDC Manager is not used by another Amazon EVS environment.
+ `CONNECTOR_HEALTH`: Aggregate health across all connectors in the environment.
*Required*: Yes
*Type*: String
*Allowed values*: `KEY_REUSE | KEY_COVERAGE | REACHABILITY | VCF_VERSION | HOST_COUNT`
*Update requires*: Updates are not supported.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
