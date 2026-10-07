---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-workspaces-directory-accessendpoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WorkSpaces::Directory AccessEndpoint
<a name="aws-properties-workspaces-directory-accessendpoint"></a>

Describes the access type and endpoint for a WorkSpace.

## Syntax
<a name="aws-properties-workspaces-directory-accessendpoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-workspaces-directory-accessendpoint-syntax.json"></a>

```
{
  "[AccessEndpointType](#cfn-workspaces-directory-accessendpoint-accessendpointtype)" : {{String}},
  "[VpcEndpointId](#cfn-workspaces-directory-accessendpoint-vpcendpointid)" : {{String}}
}
```

### YAML
<a name="aws-properties-workspaces-directory-accessendpoint-syntax.yaml"></a>

```
  [AccessEndpointType](#cfn-workspaces-directory-accessendpoint-accessendpointtype): {{String}}
  [VpcEndpointId](#cfn-workspaces-directory-accessendpoint-vpcendpointid): {{String}}
```

## Properties
<a name="aws-properties-workspaces-directory-accessendpoint-properties"></a>

`AccessEndpointType`  <a name="cfn-workspaces-directory-accessendpoint-accessendpointtype"></a>
Indicates the type of access endpoint.
*Required*: No
*Type*: String
*Allowed values*: `STREAMING_WSP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcEndpointId`  <a name="cfn-workspaces-directory-accessendpoint-vpcendpointid"></a>
Indicates the VPC endpoint to use for access.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9\_\-]{1,1000}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
