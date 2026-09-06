---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-datazone-domain.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::Domain
<a name="aws-resource-datazone-domain"></a>

The `AWS::DataZone::Domain`resource specifies an Amazon DataZone domain. You can use domains to organize your assets, users, and their projects.

## Syntax
<a name="aws-resource-datazone-domain-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-datazone-domain-syntax.json"></a>

```
{
  "Type" : "AWS::DataZone::Domain",
  "Properties" : {
      "[Description](#cfn-datazone-domain-description)" : {{String}},
      "[DomainExecutionRole](#cfn-datazone-domain-domainexecutionrole)" : {{String}},
      "[DomainVersion](#cfn-datazone-domain-domainversion)" : {{String}},
      "[KmsKeyIdentifier](#cfn-datazone-domain-kmskeyidentifier)" : {{String}},
      "[Name](#cfn-datazone-domain-name)" : {{String}},
      "[ServiceRole](#cfn-datazone-domain-servicerole)" : {{String}},
      "[SingleSignOn](#cfn-datazone-domain-singlesignon)" : {{SingleSignOn}},
      "[Tags](#cfn-datazone-domain-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-datazone-domain-syntax.yaml"></a>

```
Type: AWS::DataZone::Domain
Properties:
  [Description](#cfn-datazone-domain-description): {{String}}
  [DomainExecutionRole](#cfn-datazone-domain-domainexecutionrole): {{String}}
  [DomainVersion](#cfn-datazone-domain-domainversion): {{String}}
  [KmsKeyIdentifier](#cfn-datazone-domain-kmskeyidentifier): {{String}}
  [Name](#cfn-datazone-domain-name): {{String}}
  [ServiceRole](#cfn-datazone-domain-servicerole): {{String}}
  [SingleSignOn](#cfn-datazone-domain-singlesignon): {{
    SingleSignOn}}
  [Tags](#cfn-datazone-domain-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-datazone-domain-properties"></a>

`Description`  <a name="cfn-datazone-domain-description"></a>
The description of the Amazon DataZone domain.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DomainExecutionRole`  <a name="cfn-datazone-domain-domainexecutionrole"></a>
The domain execution role that is created when an Amazon DataZone domain is created. The domain execution role is created in the AWS account that houses the Amazon DataZone domain.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[^:]*:iam::\d{12}:role(/[a-zA-Z0-9+=,.@_-]+)*/[a-zA-Z0-9+=,.@_-]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DomainVersion`  <a name="cfn-datazone-domain-domainversion"></a>
The domain version.
*Required*: No
*Type*: String
*Allowed values*: `V1 | V2`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`KmsKeyIdentifier`  <a name="cfn-datazone-domain-kmskeyidentifier"></a>
The identifier of the AWS Key Management Service (KMS) key that is used to encrypt the Amazon DataZone domain, metadata, and reporting data.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}$`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-datazone-domain-name"></a>
The name of the Amazon DataZone domain.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServiceRole`  <a name="cfn-datazone-domain-servicerole"></a>
The service role of the domain.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[^:]*:iam::\d{12}:role(/[a-zA-Z0-9+=,.@_-]+)*/[a-zA-Z0-9+=,.@_-]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SingleSignOn`  <a name="cfn-datazone-domain-singlesignon"></a>
The single sign-on details in Amazon DataZone.
*Required*: No
*Type*: [SingleSignOn](aws-properties-datazone-domain-singlesignon.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-datazone-domain-tags"></a>
The tags specified for the Amazon DataZone domain.
*Required*: No
*Type*: Array of [Tag](aws-properties-datazone-domain-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-datazone-domain-return-values"></a>

### Ref
<a name="aws-resource-datazone-domain-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ID of the Amazon DataZone domain.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-datazone-domain-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-datazone-domain-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN of the Amazon DataZone domain.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
A timestamp of when a Amazon DataZone domain was created.

`Id`  <a name="Id-fn::getatt"></a>
The ID of the Amazon DataZone domain.

`LastUpdatedAt`  <a name="LastUpdatedAt-fn::getatt"></a>
A timestamp of when a Amazon DataZone domain was last updated.

`ManagedAccountId`  <a name="ManagedAccountId-fn::getatt"></a>
The identifier of the AWS account that manages the domain.

`PortalUrl`  <a name="PortalUrl-fn::getatt"></a>
The data portal URL for the Amazon DataZone domain.

`RootDomainUnitId`  <a name="RootDomainUnitId-fn::getatt"></a>
The ID of the root domain unit.

`Status`  <a name="Status-fn::getatt"></a>
The status of the Amazon DataZone domain.
