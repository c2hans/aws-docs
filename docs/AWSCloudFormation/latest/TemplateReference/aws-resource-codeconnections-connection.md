---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-codeconnections-connection.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeConnections::Connection
<a name="aws-resource-codeconnections-connection"></a>

A resource that is used to connect third-party source providers with services like CodePipeline.

Note: A connection created through CloudFormation, the CLI, or the SDK is in `PENDING` status by default. You can make its status `AVAILABLE` by updating the connection in the console.

## Syntax
<a name="aws-resource-codeconnections-connection-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-codeconnections-connection-syntax.json"></a>

```
{
  "Type" : "AWS::CodeConnections::Connection",
  "Properties" : {
      "[ConnectionName](#cfn-codeconnections-connection-connectionname)" : {{String}},
      "[HostArn](#cfn-codeconnections-connection-hostarn)" : {{String}},
      "[ProviderType](#cfn-codeconnections-connection-providertype)" : {{String}},
      "[Tags](#cfn-codeconnections-connection-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-codeconnections-connection-syntax.yaml"></a>

```
Type: AWS::CodeConnections::Connection
Properties:
  [ConnectionName](#cfn-codeconnections-connection-connectionname): {{String}}
  [HostArn](#cfn-codeconnections-connection-hostarn): {{String}}
  [ProviderType](#cfn-codeconnections-connection-providertype): {{String}}
  [Tags](#cfn-codeconnections-connection-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-codeconnections-connection-properties"></a>

`ConnectionName`  <a name="cfn-codeconnections-connection-connectionname"></a>
The name of the connection. Connection names must be unique in an AWS account.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `32`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`HostArn`  <a name="cfn-codeconnections-connection-hostarn"></a>
The Amazon Resource Name (ARN) of the host associated with the connection.
*Required*: No
*Type*: String
*Pattern*: `arn:aws(-[\w]+)*:.+:.+:[0-9]{12}:.+`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ProviderType`  <a name="cfn-codeconnections-connection-providertype"></a>
The name of the external provider where your third-party code repository is configured.
*Required*: No
*Type*: String
*Allowed values*: `Bitbucket | GitHub | GitHubEnterpriseServer | GitLab | GitLabSelfManaged`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-codeconnections-connection-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-codeconnections-connection-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-codeconnections-connection-return-values"></a>

### Ref
<a name="aws-resource-codeconnections-connection-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-codeconnections-connection-return-values-fn--getatt"></a>

####
<a name="aws-resource-codeconnections-connection-return-values-fn--getatt-fn--getatt"></a>

`ConnectionArn`  <a name="ConnectionArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the connection. The ARN is used as the connection reference when the connection is shared between AWS services.
The ARN is never reused if the connection is deleted.

`ConnectionStatus`  <a name="ConnectionStatus-fn::getatt"></a>
The current status of the connection.

`OwnerAccountId`  <a name="OwnerAccountId-fn::getatt"></a>
The identifier of the external provider where your third-party code repository is configured. For Bitbucket, this is the account ID of the owner of the Bitbucket repository.
