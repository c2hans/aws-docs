---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-networksecuritymanager-scope.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkSecurityManager::Scope

The `AWS::NetworkSecurityManager::Scope` resource specifies an AWS Network Security Manager scope. A scope selects the accounts and the resources that a deployment applies to.

A scope can instead be a *specialized* scope, which is built for one specific purpose. A scope with a `SpecializedScopeType` of `IGW_FIREWALL_SUBNET_CONNECTIVITY_OVERRIDE` selects the subnets that a subnet connectivity override in an AWS Network Firewall automated internet firewall policy applies to. You can't associate a specialized scope with a deployment.

You define reusable rules and templates, combine them into policies, then use a scope to choose where those protections apply. For more information, see the [AWS Network Security Manager Developer Guide](https://docs.aws.amazon.com/network-security-manager/latest/devguide/what-is.html).

## Syntax
<a name="aws-resource-networksecuritymanager-scope-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-networksecuritymanager-scope-syntax.json"></a>

```json
{
  "Type" : "AWS::NetworkSecurityManager::Scope",
  "Properties" : {
      "[ScopeConfiguration](#cfn-networksecuritymanager-scope-scopeconfiguration)" : {{String}},
      "[ScopeDescription](#cfn-networksecuritymanager-scope-scopedescription)" : {{String}},
      "[ScopeName](#cfn-networksecuritymanager-scope-scopename)" : {{String}},
      "[SpecializedScopeType](#cfn-networksecuritymanager-scope-specializedscopetype)" : {{String}},
      "[Tags](#cfn-networksecuritymanager-scope-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-networksecuritymanager-scope-syntax.yaml"></a>

```yaml
Type: AWS::NetworkSecurityManager::Scope
Properties:
  [ScopeConfiguration](#cfn-networksecuritymanager-scope-scopeconfiguration): {{String}}
  [ScopeDescription](#cfn-networksecuritymanager-scope-scopedescription): {{String}}
  [ScopeName](#cfn-networksecuritymanager-scope-scopename): {{String}}
  [SpecializedScopeType](#cfn-networksecuritymanager-scope-specializedscopetype): {{String}}
  [Tags](#cfn-networksecuritymanager-scope-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-networksecuritymanager-scope-properties"></a>

`ScopeConfiguration`  <a name="cfn-networksecuritymanager-scope-scopeconfiguration"></a>
The configuration that defines which accounts and resources are in scope, as a JSON string.
Unlike the AWS Network Security Manager API, which takes this configuration as a structure, the AWS CloudFormation property takes the serialized JSON document. Because the value is an opaque string, AWS CloudFormation does not validate its contents when it validates your template. An invalid configuration is reported when the stack is provisioned.
The JSON document supports the following top-level members:
 `AccountFilter`
The account filter that determines which accounts are in scope. Set exactly one of `IncludeAll`, `Include`, or `Exclude`. Use `IncludeAll` to apply no account filtering, `Include` to select only the specified accounts and organizational units, or `Exclude` to select every account except those specified.
The `Include` and `Exclude` members each take a set of accounts and organizational units, with `AccountIds` for AWS account IDs and `OrganizationalUnits` for AWS Organizations organizational units (OUs).
 `ResourceScopes`
The resource-level scoping configuration, keyed by resource type, that defines which resources within the selected accounts are in scope. For each resource type, set exactly one of `IncludeAll`, `Include`, or `Exclude`.
The supported resource types are `AWS::ApiGateway::Stage`, `AWS::CloudFront::Distribution`, `AWS::EC2::EIP`, `AWS::ElasticLoadBalancingV2::LoadBalancer::application`, `AWS::ElasticLoadBalancing::LoadBalancer`, `AWS::EC2::VPC`, and `AWS::EC2::Subnet`. Select `AWS::EC2::VPC` for a scope that a deployment of an `IGW_FIREWALL` policy protects. A scope whose `SpecializedScopeType` is `IGW_FIREWALL_SUBNET_CONNECTIVITY_OVERRIDE` can select only `AWS::EC2::Subnet`.
The `Include` and `Exclude` members each take a set of resources defined by `ExplicitArns`, by an `Expression`, or by both. An expression combines leaf conditions with the `And`, `Or`, and `Not` operators. A leaf condition matches resources by tag key-value pairs or by resource-type-specific configuration.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScopeDescription`  <a name="cfn-networksecuritymanager-scope-scopedescription"></a>
A description of the scope.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9 _.:/=+\-@]*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScopeName`  <a name="cfn-networksecuritymanager-scope-scopename"></a>
The name of the scope.
 To change the name of a scope, AWS CloudFormation deletes the existing scope and creates a new one, which also changes the values returned for `ScopeId` and `ScopeArn`.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9][a-zA-Z0-9 _.:/=+\-@]*$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SpecializedScopeType`  <a name="cfn-networksecuritymanager-scope-specializedscopetype"></a>
The specialized type of the scope. Omit this property to create a standard scope, which you can associate with a deployment.
Specify `IGW_FIREWALL_SUBNET_CONNECTIVITY_OVERRIDE` to create a scope that selects the subnets a subnet connectivity override applies to in an AWS Network Firewall automated internet firewall policy. Reference the scope from the `Scopes` property of a `SubnetConnectivityOverride` in the policy's `IgwFirewallConfig`. A scope of this type must select only `AWS::EC2::Subnet` resources and must not include an `AccountFilter`, because the deployment that applies the policy determines which accounts are in scope. You can't associate a specialized scope with a deployment.
You can't change the specialized type after you create the scope. Changing this property replaces the scope.
*Required*: No
*Type*: String
*Allowed values*: `IGW_FIREWALL_SUBNET_CONNECTIVITY_OVERRIDE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-networksecuritymanager-scope-tags"></a>
The tags to assign to the scope.
*Required*: No
*Type*: Array of [Tag](aws-properties-networksecuritymanager-scope-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-networksecuritymanager-scope-return-values"></a>

### Ref
<a name="aws-resource-networksecuritymanager-scope-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the scope. For example:

 `{ "Ref": "MyScope" }`

For a scope named `ScopeName`, `Ref` returns a value such as `arn:aws:network-security-manager:us-east-1:123456789012:scope:abcd1234-5678-90ab-cdef-EXAMPLE11111`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-networksecuritymanager-scope-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-networksecuritymanager-scope-return-values-fn--getatt-fn--getatt"></a>

`ScopeArn`  <a name="ScopeArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the scope. For example: `arn:aws:network-security-manager:us-east-1:123456789012:scope:abcd1234-5678-90ab-cdef-EXAMPLE11111`.

`ScopeId`  <a name="ScopeId-fn::getatt"></a>
The service-generated unique identifier of the scope. For example: `abcd1234-5678-90ab-cdef-EXAMPLE11111`.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the scope.
Scopes that you manage with AWS CloudFormation are always published, so this attribute returns `ACTIVE`. The AWS Network Security Manager API also supports an unpublished `DRAFT` status, which AWS CloudFormation does not use.
*Allowed Values*: `ACTIVE`

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The date and time when the scope was last updated, in ISO 8601 format. For example: `2026-11-19T21:42:56Z`.

`Version`  <a name="Version-fn::getatt"></a>
The version of the scope. AWS Network Security Manager increments this value each time it publishes a new version of the scope. For example: `1`.

## Examples
<a name="aws-resource-networksecuritymanager-scope--examples"></a>

**Topics**
+ [Select every CloudFront distribution in the organization](#aws-resource-networksecuritymanager-scope--examples--Select_every_CloudFront_distribution_in_the_organization)
+ [Select subnets for an internet firewall connectivity override](#aws-resource-networksecuritymanager-scope--examples--Select_subnets_for_an_internet_firewall_connectivity_override)

### Select every CloudFront distribution in the organization
<a name="aws-resource-networksecuritymanager-scope--examples--Select_every_CloudFront_distribution_in_the_organization"></a>

#### YAML
<a name="aws-resource-networksecuritymanager-scope--examples--Select_every_CloudFront_distribution_in_the_organization--yaml"></a>

```yaml
                AWSTemplateFormatVersion: "2010-09-09"
                Description: Selects the accounts and resources that a Network Security Manager deployment protects.
                Resources:
                  AllDistributionsScope:
                    Type: AWS::NetworkSecurityManager::Scope
                    Properties:
                      ScopeName: all-cloudfront-distributions
                      ScopeDescription: Every CloudFront distribution in every account in the organization.
                      ScopeConfiguration: '{"AccountFilter":{"IncludeAll":true},"ResourceScopes":{"AWS::CloudFront::Distribution":{"IncludeAll":true}}}'
                Outputs:
                  ScopeArn:
                    Value: !GetAtt AllDistributionsScope.ScopeArn
```

### Select subnets for an internet firewall connectivity override
<a name="aws-resource-networksecuritymanager-scope--examples--Select_subnets_for_an_internet_firewall_connectivity_override"></a>

#### YAML
<a name="aws-resource-networksecuritymanager-scope--examples--Select_subnets_for_an_internet_firewall_connectivity_override--yaml"></a>

```yaml
                AWSTemplateFormatVersion: "2010-09-09"
                Description: Selects the subnets that an internet firewall policy override applies to.
                Resources:
                  IsolatedSubnetsScope:
                    Type: AWS::NetworkSecurityManager::Scope
                    Properties:
                      ScopeName: isolated-subnets
                      ScopeDescription: Subnets tagged as isolated.
                      SpecializedScopeType: IGW_FIREWALL_SUBNET_CONNECTIVITY_OVERRIDE
                      ScopeConfiguration: '{"ResourceScopes":{"AWS::EC2::Subnet":{"Include":{"Expression":{"Criteria":{"Tags":{"network-zone":"isolated"}}}}}}}'
                Outputs:
                  ScopeArn:
                    Value: !GetAtt IsolatedSubnetsScope.ScopeArn
```
