---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-domain-domainsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Domain DomainSettings
<a name="aws-properties-sagemaker-domain-domainsettings"></a>

A collection of settings that apply to the `SageMaker Domain`. These settings are specified through the `CreateDomain` API call.

## Syntax
<a name="aws-properties-sagemaker-domain-domainsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-domain-domainsettings-syntax.json"></a>

```
{
  "[DockerSettings](#cfn-sagemaker-domain-domainsettings-dockersettings)" : {{DockerSettings}},
  "[ExecutionRoleIdentityConfig](#cfn-sagemaker-domain-domainsettings-executionroleidentityconfig)" : {{String}},
  "[IpAddressType](#cfn-sagemaker-domain-domainsettings-ipaddresstype)" : {{String}},
  "[RStudioServerProDomainSettings](#cfn-sagemaker-domain-domainsettings-rstudioserverprodomainsettings)" : {{RStudioServerProDomainSettings}},
  "[SecurityGroupIds](#cfn-sagemaker-domain-domainsettings-securitygroupids)" : {{[ String, ... ]}},
  "[UnifiedStudioSettings](#cfn-sagemaker-domain-domainsettings-unifiedstudiosettings)" : {{UnifiedStudioSettings}}
}
```

### YAML
<a name="aws-properties-sagemaker-domain-domainsettings-syntax.yaml"></a>

```
  [DockerSettings](#cfn-sagemaker-domain-domainsettings-dockersettings): {{
    DockerSettings}}
  [ExecutionRoleIdentityConfig](#cfn-sagemaker-domain-domainsettings-executionroleidentityconfig): {{String}}
  [IpAddressType](#cfn-sagemaker-domain-domainsettings-ipaddresstype): {{String}}
  [RStudioServerProDomainSettings](#cfn-sagemaker-domain-domainsettings-rstudioserverprodomainsettings): {{
    RStudioServerProDomainSettings}}
  [SecurityGroupIds](#cfn-sagemaker-domain-domainsettings-securitygroupids): {{
    - String}}
  [UnifiedStudioSettings](#cfn-sagemaker-domain-domainsettings-unifiedstudiosettings): {{
    UnifiedStudioSettings}}
```

## Properties
<a name="aws-properties-sagemaker-domain-domainsettings-properties"></a>

`DockerSettings`  <a name="cfn-sagemaker-domain-domainsettings-dockersettings"></a>
A collection of settings that configure the domain's Docker interaction.
*Required*: No
*Type*: [DockerSettings](aws-properties-sagemaker-domain-dockersettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExecutionRoleIdentityConfig`  <a name="cfn-sagemaker-domain-domainsettings-executionroleidentityconfig"></a>
The configuration for attaching a SageMaker AI user profile name to the execution role as a [sts:SourceIdentity key](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_monitor.html).
*Required*: No
*Type*: String
*Allowed values*: `USER_PROFILE_NAME | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IpAddressType`  <a name="cfn-sagemaker-domain-domainsettings-ipaddresstype"></a>
The IP address type for the domain. Specify `ipv4` for IPv4-only connectivity or `dualstack` for both IPv4 and IPv6 connectivity. When you specify `dualstack`, the subnet must support IPv6 CIDR blocks. If not specified, defaults to `ipv4`.
*Required*: No
*Type*: String
*Allowed values*: `IPV4 | DUALSTACK`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RStudioServerProDomainSettings`  <a name="cfn-sagemaker-domain-domainsettings-rstudioserverprodomainsettings"></a>
A collection of settings that configure the `RStudioServerPro` Domain-level app.
*Required*: No
*Type*: [RStudioServerProDomainSettings](aws-properties-sagemaker-domain-rstudioserverprodomainsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecurityGroupIds`  <a name="cfn-sagemaker-domain-domainsettings-securitygroupids"></a>
The security groups for the Amazon Virtual Private Cloud that the `Domain` uses for communication between Domain-level apps and user apps.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `32 | 3`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UnifiedStudioSettings`  <a name="cfn-sagemaker-domain-domainsettings-unifiedstudiosettings"></a>
The settings that apply to an SageMaker AI domain when you use it in Amazon SageMaker Unified Studio.
*Required*: No
*Type*: [UnifiedStudioSettings](aws-properties-sagemaker-domain-unifiedstudiosettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
