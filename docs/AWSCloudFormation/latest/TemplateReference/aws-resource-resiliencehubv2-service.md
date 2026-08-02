---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-resiliencehubv2-service.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ResilienceHubV2::Service
<a name="aws-resource-resiliencehubv2-service"></a>

Represents a service in Resilience Hub. A service is the primary unit of resilience assessment.

## Syntax
<a name="aws-resource-resiliencehubv2-service-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-resiliencehubv2-service-syntax.json"></a>

```
{
  "Type" : "AWS::ResilienceHubV2::Service",
  "Properties" : {
      "[Assertions](#cfn-resiliencehubv2-service-assertions)" : {{[ AssertionDefinition, ... ]}},
      "[AssociatedSystems](#cfn-resiliencehubv2-service-associatedsystems)" : {{[ AssociatedSystem, ... ]}},
      "[DependencyDiscovery](#cfn-resiliencehubv2-service-dependencydiscovery)" : {{String}},
      "[Description](#cfn-resiliencehubv2-service-description)" : {{String}},
      "[InputSources](#cfn-resiliencehubv2-service-inputsources)" : {{[ InputSourceDefinition, ... ]}},
      "[KmsKeyId](#cfn-resiliencehubv2-service-kmskeyid)" : {{String}},
      "[Name](#cfn-resiliencehubv2-service-name)" : {{String}},
      "[PermissionModel](#cfn-resiliencehubv2-service-permissionmodel)" : {{PermissionModel}},
      "[PolicyArn](#cfn-resiliencehubv2-service-policyarn)" : {{String}},
      "[Regions](#cfn-resiliencehubv2-service-regions)" : {{[ String, ... ]}},
      "[ReportConfiguration](#cfn-resiliencehubv2-service-reportconfiguration)" : {{ServiceReportConfiguration}},
      "[Tags](#cfn-resiliencehubv2-service-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-resiliencehubv2-service-syntax.yaml"></a>

```
Type: AWS::ResilienceHubV2::Service
Properties:
  [Assertions](#cfn-resiliencehubv2-service-assertions): {{
    - AssertionDefinition}}
  [AssociatedSystems](#cfn-resiliencehubv2-service-associatedsystems): {{
    - AssociatedSystem}}
  [DependencyDiscovery](#cfn-resiliencehubv2-service-dependencydiscovery): {{String}}
  [Description](#cfn-resiliencehubv2-service-description): {{String}}
  [InputSources](#cfn-resiliencehubv2-service-inputsources): {{
    - InputSourceDefinition}}
  [KmsKeyId](#cfn-resiliencehubv2-service-kmskeyid): {{String}}
  [Name](#cfn-resiliencehubv2-service-name): {{String}}
  [PermissionModel](#cfn-resiliencehubv2-service-permissionmodel): {{
    PermissionModel}}
  [PolicyArn](#cfn-resiliencehubv2-service-policyarn): {{String}}
  [Regions](#cfn-resiliencehubv2-service-regions): {{
    - String}}
  [ReportConfiguration](#cfn-resiliencehubv2-service-reportconfiguration): {{
    ServiceReportConfiguration}}
  [Tags](#cfn-resiliencehubv2-service-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-resiliencehubv2-service-properties"></a>

`Assertions`  <a name="cfn-resiliencehubv2-service-assertions"></a>
Property description not available.
*Required*: No
*Type*: Array of [AssertionDefinition](aws-properties-resiliencehubv2-service-assertiondefinition.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AssociatedSystems`  <a name="cfn-resiliencehubv2-service-associatedsystems"></a>
The systems associated with the service.
*Required*: No
*Type*: Array of [AssociatedSystem](aws-properties-resiliencehubv2-service-associatedsystem.md)
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DependencyDiscovery`  <a name="cfn-resiliencehubv2-service-dependencydiscovery"></a>
The dependency discovery configuration for the service.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED | INITIALIZING`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-resiliencehubv2-service-description"></a>
The description of the event.
*Required*: No
*Type*: String
*Maximum*: `615`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InputSources`  <a name="cfn-resiliencehubv2-service-inputsources"></a>
Property description not available.
*Required*: No
*Type*: Array of [InputSourceDefinition](aws-properties-resiliencehubv2-service-inputsourcedefinition.md)
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyId`  <a name="cfn-resiliencehubv2-service-kmskeyid"></a>
KMS key identifier — accepts key ID, key ARN, alias name, or alias ARN.
*Required*: No
*Type*: String
*Pattern*: `^((arn:aws(-[^:]+)?:kms:[a-zA-Z0-9-]*:[0-9]{12}:((key/[a-zA-Z0-9-]{36})|(alias/[a-zA-Z0-9-_/]+)))|([a-zA-Z0-9-]{36})|(alias/[a-zA-Z0-9-_/]+))$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-resiliencehubv2-service-name"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9][A-Za-z0-9_\-]{1,59}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PermissionModel`  <a name="cfn-resiliencehubv2-service-permissionmodel"></a>
The permission model for the service.
*Required*: No
*Type*: [PermissionModel](aws-properties-resiliencehubv2-service-permissionmodel.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PolicyArn`  <a name="cfn-resiliencehubv2-service-policyarn"></a>
ARN identifier.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Regions`  <a name="cfn-resiliencehubv2-service-regions"></a>
The Regions where the service operates.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ReportConfiguration`  <a name="cfn-resiliencehubv2-service-reportconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [ServiceReportConfiguration](aws-properties-resiliencehubv2-service-servicereportconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-resiliencehubv2-service-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-resiliencehubv2-service-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-resiliencehubv2-service-return-values"></a>

### Ref
<a name="aws-resource-resiliencehubv2-service-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-resiliencehubv2-service-return-values-fn--getatt"></a>

####
<a name="aws-resource-resiliencehubv2-service-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when the service was created.

`ServiceArn`  <a name="ServiceArn-fn::getatt"></a>
ARN identifier.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The timestamp when the service was last updated.
