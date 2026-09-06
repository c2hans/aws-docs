---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-codeconnections-host.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeConnections::Host
<a name="aws-resource-codeconnections-host"></a>

A resource that represents the infrastructure where a third-party provider is installed. The host is used when you create connections to an installed third-party provider type, such as GitHub Enterprise Server. You create one host for all connections to that provider.

**Note**
A host created through the CLI or the SDK is in `PENDING` status by default. You can make its status `AVAILABLE` by setting up the host in the console.

## Syntax
<a name="aws-resource-codeconnections-host-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-codeconnections-host-syntax.json"></a>

```
{
  "Type" : "AWS::CodeConnections::Host",
  "Properties" : {
      "[Name](#cfn-codeconnections-host-name)" : {{String}},
      "[ProviderEndpoint](#cfn-codeconnections-host-providerendpoint)" : {{String}},
      "[ProviderType](#cfn-codeconnections-host-providertype)" : {{String}},
      "[Tags](#cfn-codeconnections-host-tags)" : {{[ Tag, ... ]}},
      "[VpcConfiguration](#cfn-codeconnections-host-vpcconfiguration)" : {{VpcConfiguration}}
    }
}
```

### YAML
<a name="aws-resource-codeconnections-host-syntax.yaml"></a>

```
Type: AWS::CodeConnections::Host
Properties:
  [Name](#cfn-codeconnections-host-name): {{String}}
  [ProviderEndpoint](#cfn-codeconnections-host-providerendpoint): {{String}}
  [ProviderType](#cfn-codeconnections-host-providertype): {{String}}
  [Tags](#cfn-codeconnections-host-tags): {{
    - Tag}}
  [VpcConfiguration](#cfn-codeconnections-host-vpcconfiguration): {{
    VpcConfiguration}}
```

## Properties
<a name="aws-resource-codeconnections-host-properties"></a>

`Name`  <a name="cfn-codeconnections-host-name"></a>
The name of the host.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ProviderEndpoint`  <a name="cfn-codeconnections-host-providerendpoint"></a>
The endpoint of the infrastructure where your provider type is installed.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProviderType`  <a name="cfn-codeconnections-host-providertype"></a>
The name of the installed provider to be associated with your connection. The host resource represents the infrastructure where your provider type is installed. The valid provider type is GitHub Enterprise Server.
*Required*: Yes
*Type*: String
*Allowed values*: `Bitbucket | GitHub | GitHubEnterpriseServer | GitLab | GitLabSelfManaged | AzureDevOps`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-codeconnections-host-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-codeconnections-host-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcConfiguration`  <a name="cfn-codeconnections-host-vpcconfiguration"></a>
The VPC configuration provisioned for the host.
*Required*: No
*Type*: [VpcConfiguration](aws-properties-codeconnections-host-vpcconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-codeconnections-host-return-values"></a>

### Ref
<a name="aws-resource-codeconnections-host-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-codeconnections-host-return-values-fn--getatt"></a>

####
<a name="aws-resource-codeconnections-host-return-values-fn--getatt-fn--getatt"></a>

`HostArn`  <a name="HostArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the host.

`HostId`  <a name="HostId-fn::getatt"></a>
Property description not available.

`Status`  <a name="Status-fn::getatt"></a>
The status of the host, such as PENDING, AVAILABLE, VPC\_CONFIG\_DELETING, VPC\_CONFIG\_INITIALIZING, and VPC\_CONFIG\_FAILED\_INITIALIZATION.
