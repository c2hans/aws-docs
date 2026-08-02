---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-datazone-connection.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::Connection
<a name="aws-resource-datazone-connection"></a>

In Amazon DataZone, a connection enables you to connect your resources (domains, projects, and environments) to external resources and services.

## Syntax
<a name="aws-resource-datazone-connection-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-datazone-connection-syntax.json"></a>

```
{
  "Type" : "AWS::DataZone::Connection",
  "Properties" : {
      "[AwsLocation](#cfn-datazone-connection-awslocation)" : {{AwsLocation}},
      "[Configurations](#cfn-datazone-connection-configurations)" : {{[ ConnectionConfiguration, ... ]}},
      "[Description](#cfn-datazone-connection-description)" : {{String}},
      "[DomainIdentifier](#cfn-datazone-connection-domainidentifier)" : {{String}},
      "[EnableTrustedIdentityPropagation](#cfn-datazone-connection-enabletrustedidentitypropagation)" : {{Boolean}},
      "[EnvironmentIdentifier](#cfn-datazone-connection-environmentidentifier)" : {{String}},
      "[Name](#cfn-datazone-connection-name)" : {{String}},
      "[ProjectIdentifier](#cfn-datazone-connection-projectidentifier)" : {{String}},
      "[Props](#cfn-datazone-connection-props)" : {{ConnectionPropertiesInput}},
      "[Scope](#cfn-datazone-connection-scope)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-datazone-connection-syntax.yaml"></a>

```
Type: AWS::DataZone::Connection
Properties:
  [AwsLocation](#cfn-datazone-connection-awslocation): {{
    AwsLocation}}
  [Configurations](#cfn-datazone-connection-configurations): {{
    - ConnectionConfiguration}}
  [Description](#cfn-datazone-connection-description): {{String}}
  [DomainIdentifier](#cfn-datazone-connection-domainidentifier): {{String}}
  [EnableTrustedIdentityPropagation](#cfn-datazone-connection-enabletrustedidentitypropagation): {{Boolean}}
  [EnvironmentIdentifier](#cfn-datazone-connection-environmentidentifier): {{String}}
  [Name](#cfn-datazone-connection-name): {{String}}
  [ProjectIdentifier](#cfn-datazone-connection-projectidentifier): {{String}}
  [Props](#cfn-datazone-connection-props): {{
    ConnectionPropertiesInput}}
  [Scope](#cfn-datazone-connection-scope): {{String}}
```

## Properties
<a name="aws-resource-datazone-connection-properties"></a>

`AwsLocation`  <a name="cfn-datazone-connection-awslocation"></a>
The location where the connection is created.
*Required*: No
*Type*: [AwsLocation](aws-properties-datazone-connection-awslocation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Configurations`  <a name="cfn-datazone-connection-configurations"></a>
The configurations of a connection summary.
*Required*: No
*Type*: Array of [ConnectionConfiguration](aws-properties-datazone-connection-connectionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-datazone-connection-description"></a>
Connection description.
*Required*: No
*Type*: String
*Pattern*: `^[\S\s]*$`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DomainIdentifier`  <a name="cfn-datazone-connection-domainidentifier"></a>
The ID of the domain where the connection is created.
*Required*: Yes
*Type*: String
*Pattern*: `^dzd[_-][a-zA-Z0-9_-]{1,36}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EnableTrustedIdentityPropagation`  <a name="cfn-datazone-connection-enabletrustedidentitypropagation"></a>
Specifies whether the trusted identity propagation is enabled.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EnvironmentIdentifier`  <a name="cfn-datazone-connection-environmentidentifier"></a>
The ID of the environment where the connection is created.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-datazone-connection-name"></a>
The name of the connection.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w][\w\.\-\_]*$`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ProjectIdentifier`  <a name="cfn-datazone-connection-projectidentifier"></a>
The ID of the project where you want to list connections.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Props`  <a name="cfn-datazone-connection-props"></a>
Connection props.
*Required*: No
*Type*: [ConnectionPropertiesInput](aws-properties-datazone-connection-connectionpropertiesinput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Scope`  <a name="cfn-datazone-connection-scope"></a>
The scope of the connection.
*Required*: No
*Type*: String
*Allowed values*: `DOMAIN | PROJECT`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-datazone-connection-return-values"></a>

### Ref
<a name="aws-resource-datazone-connection-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns a string containing pipe-separated `DomainId` and `ConnectionId`, which uniquely identifies a connection. For example: `{ "Ref": "MyConnection" }` for the resource with the logical ID `MyConnection`, `Ref` returns `DomainId|ConnectionId`.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-datazone-connection-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-datazone-connection-return-values-fn--getatt-fn--getatt"></a>

`ConnectionId`  <a name="ConnectionId-fn::getatt"></a>
The ID of the connection.

`DomainId`  <a name="DomainId-fn::getatt"></a>
The domain ID of the connection.

`DomainUnitId`  <a name="DomainUnitId-fn::getatt"></a>
The domain unit ID of the connection.

`EnvironmentId`  <a name="EnvironmentId-fn::getatt"></a>
The ID of the environment.

`EnvironmentUserRole`  <a name="EnvironmentUserRole-fn::getatt"></a>
The environment user role.

`ProjectId`  <a name="ProjectId-fn::getatt"></a>
The ID of the project.

`Type`  <a name="Type-fn::getatt"></a>
The type of the connection.
