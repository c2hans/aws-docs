---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-m2-environment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::M2::Environment
<a name="aws-resource-m2-environment"></a>

Specifies a runtime environment for a given runtime engine.

## Syntax
<a name="aws-resource-m2-environment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-m2-environment-syntax.json"></a>

```
{
  "Type" : "AWS::M2::Environment",
  "Properties" : {
      "[Description](#cfn-m2-environment-description)" : {{String}},
      "[EngineType](#cfn-m2-environment-enginetype)" : {{String}},
      "[EngineVersion](#cfn-m2-environment-engineversion)" : {{String}},
      "[HighAvailabilityConfig](#cfn-m2-environment-highavailabilityconfig)" : {{HighAvailabilityConfig}},
      "[InstanceType](#cfn-m2-environment-instancetype)" : {{String}},
      "[KmsKeyId](#cfn-m2-environment-kmskeyid)" : {{String}},
      "[Name](#cfn-m2-environment-name)" : {{String}},
      "[NetworkType](#cfn-m2-environment-networktype)" : {{String}},
      "[PreferredMaintenanceWindow](#cfn-m2-environment-preferredmaintenancewindow)" : {{String}},
      "[PubliclyAccessible](#cfn-m2-environment-publiclyaccessible)" : {{Boolean}},
      "[SecurityGroupIds](#cfn-m2-environment-securitygroupids)" : {{[ String, ... ]}},
      "[StorageConfigurations](#cfn-m2-environment-storageconfigurations)" : {{[ StorageConfiguration, ... ]}},
      "[SubnetIds](#cfn-m2-environment-subnetids)" : {{[ String, ... ]}},
      "[Tags](#cfn-m2-environment-tags)" : {{{{{Key}}: {{Value}}, ...}}}
    }
}
```

### YAML
<a name="aws-resource-m2-environment-syntax.yaml"></a>

```
Type: AWS::M2::Environment
Properties:
  [Description](#cfn-m2-environment-description): {{String}}
  [EngineType](#cfn-m2-environment-enginetype): {{String}}
  [EngineVersion](#cfn-m2-environment-engineversion): {{String}}
  [HighAvailabilityConfig](#cfn-m2-environment-highavailabilityconfig): {{
    HighAvailabilityConfig}}
  [InstanceType](#cfn-m2-environment-instancetype): {{String}}
  [KmsKeyId](#cfn-m2-environment-kmskeyid): {{String}}
  [Name](#cfn-m2-environment-name): {{String}}
  [NetworkType](#cfn-m2-environment-networktype): {{String}}
  [PreferredMaintenanceWindow](#cfn-m2-environment-preferredmaintenancewindow): {{String}}
  [PubliclyAccessible](#cfn-m2-environment-publiclyaccessible): {{Boolean}}
  [SecurityGroupIds](#cfn-m2-environment-securitygroupids): {{
    - String}}
  [StorageConfigurations](#cfn-m2-environment-storageconfigurations): {{
    - StorageConfiguration}}
  [SubnetIds](#cfn-m2-environment-subnetids): {{
    - String}}
  [Tags](#cfn-m2-environment-tags): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-resource-m2-environment-properties"></a>

`Description`  <a name="cfn-m2-environment-description"></a>
The description of the runtime environment.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `500`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EngineType`  <a name="cfn-m2-environment-enginetype"></a>
The target platform for the runtime environment.
*Required*: Yes
*Type*: String
*Allowed values*: `microfocus | bluage`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EngineVersion`  <a name="cfn-m2-environment-engineversion"></a>
The version of the runtime engine.
*Required*: No
*Type*: String
*Pattern*: `^\S{1,10}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HighAvailabilityConfig`  <a name="cfn-m2-environment-highavailabilityconfig"></a>
AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).
Defines the details of a high availability configuration.
*Required*: No
*Type*: [HighAvailabilityConfig](aws-properties-m2-environment-highavailabilityconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceType`  <a name="cfn-m2-environment-instancetype"></a>
The instance type of the runtime environment.
*Required*: Yes
*Type*: String
*Pattern*: `^\S{1,20}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyId`  <a name="cfn-m2-environment-kmskeyid"></a>
The identifier of a customer managed key.
*Required*: No
*Type*: String
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-m2-environment-name"></a>
The name of the runtime environment.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9][A-Za-z0-9_\-]{1,59}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NetworkType`  <a name="cfn-m2-environment-networktype"></a>
The network type supported by the runtime environment.
*Required*: No
*Type*: String
*Allowed values*: `ipv4 | dual`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PreferredMaintenanceWindow`  <a name="cfn-m2-environment-preferredmaintenancewindow"></a>
Configures the maintenance window that you want for the runtime environment. The maintenance window must have the format `ddd:hh24:mi-ddd:hh24:mi` and must be less than 24 hours. The following two examples are valid maintenance windows: `sun:23:45-mon:00:15` or `sat:01:00-sat:03:00`.
If you do not provide a value, a random system-generated value will be assigned.
*Required*: No
*Type*: String
*Pattern*: `^\S{1,50}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PubliclyAccessible`  <a name="cfn-m2-environment-publiclyaccessible"></a>
Specifies whether the runtime environment is publicly accessible.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SecurityGroupIds`  <a name="cfn-m2-environment-securitygroupids"></a>
The list of security groups for the VPC associated with this runtime environment.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StorageConfigurations`  <a name="cfn-m2-environment-storageconfigurations"></a>
AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).
Defines the storage configuration for a runtime environment.
*Required*: No
*Type*: Array of [StorageConfiguration](aws-properties-m2-environment-storageconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SubnetIds`  <a name="cfn-m2-environment-subnetids"></a>
The list of subnets associated with the VPC for this runtime environment.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-m2-environment-tags"></a>
An array of key-value pairs to apply to this resource.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
*Required*: No
*Type*: Object of String
*Pattern*: `^(?!aws:).+$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-m2-environment-return-values"></a>

### Ref
<a name="aws-resource-m2-environment-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the environment Amazon Resource Name (ARN), such as the following:

 `{ "Ref": “SampleEnv” }`

Returns a value similar to the following:

 `arn:aws:m2:us-west-2:1234567890:env/y3ca6bhaife2bcvxar3lpivfou`

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-m2-environment-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-m2-environment-return-values-fn--getatt-fn--getatt"></a>

`EnvironmentArn`  <a name="EnvironmentArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the runtime environment.

`EnvironmentId`  <a name="EnvironmentId-fn::getatt"></a>
The unique identifier of the runtime environment.
