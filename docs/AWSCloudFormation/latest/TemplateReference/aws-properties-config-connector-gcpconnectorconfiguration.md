---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-config-connector-gcpconnectorconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Config::Connector GcpConnectorConfiguration
<a name="aws-properties-config-connector-gcpconnectorconfiguration"></a>

Configuration for connecting to Google Cloud.

## Syntax
<a name="aws-properties-config-connector-gcpconnectorconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-config-connector-gcpconnectorconfiguration-syntax.json"></a>

```
{
  "[GcpOrganizationId](#cfn-config-connector-gcpconnectorconfiguration-gcporganizationid)" : {{String}},
  "[ServiceAccountEmail](#cfn-config-connector-gcpconnectorconfiguration-serviceaccountemail)" : {{String}},
  "[WorkloadIdentityPoolProvider](#cfn-config-connector-gcpconnectorconfiguration-workloadidentitypoolprovider)" : {{String}}
}
```

### YAML
<a name="aws-properties-config-connector-gcpconnectorconfiguration-syntax.yaml"></a>

```
  [GcpOrganizationId](#cfn-config-connector-gcpconnectorconfiguration-gcporganizationid): {{String}}
  [ServiceAccountEmail](#cfn-config-connector-gcpconnectorconfiguration-serviceaccountemail): {{String}}
  [WorkloadIdentityPoolProvider](#cfn-config-connector-gcpconnectorconfiguration-workloadidentitypoolprovider): {{String}}
```

## Properties
<a name="aws-properties-config-connector-gcpconnectorconfiguration-properties"></a>

`GcpOrganizationId`  <a name="cfn-config-connector-gcpconnectorconfiguration-gcporganizationid"></a>
The Google Cloud organization ID. Specify it to connect all projects in the organization. If the project that the service account belongs to is in an organization, you must specify that organization's ID. Omit it only when that project isn't in an organization. The connector then covers only that project.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `20`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ServiceAccountEmail`  <a name="cfn-config-connector-gcpconnectorconfiguration-serviceaccountemail"></a>
The email address of the Google Cloud service account that AWS Config uses.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z][a-z0-9\-]*@[a-z][a-z0-9\-]*[a-z0-9]\.iam\.gserviceaccount\.com$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`WorkloadIdentityPoolProvider`  <a name="cfn-config-connector-gcpconnectorconfiguration-workloadidentitypoolprovider"></a>
The full resource name of the workload identity pool provider that AWS Config uses to federate into Google Cloud, in the format `projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/PROVIDER_ID`.
*Required*: Yes
*Type*: String
*Pattern*: `^projects/[0-9]+/locations/global/workloadIdentityPools/[^/]+/providers/[^/]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
