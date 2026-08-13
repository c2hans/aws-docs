---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-config-organizationconformancepack.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Config::OrganizationConformancePack
<a name="aws-resource-config-organizationconformancepack"></a>

OrganizationConformancePack deploys conformance packs across member accounts in an AWS Organizations. OrganizationConformancePack enables organization service access for `config-multiaccountsetup.amazonaws.com` through the `EnableAWSServiceAccess` action and creates a service linked role in the master account of your organization. The service linked role is created only when the role does not exist in the master account.

## Syntax
<a name="aws-resource-config-organizationconformancepack-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-config-organizationconformancepack-syntax.json"></a>

```
{
  "Type" : "AWS::Config::OrganizationConformancePack",
  "Properties" : {
      "[ConformancePackInputParameters](#cfn-config-organizationconformancepack-conformancepackinputparameters)" : {{[ ConformancePackInputParameter, ... ]}},
      "[DeliveryS3Bucket](#cfn-config-organizationconformancepack-deliverys3bucket)" : {{String}},
      "[DeliveryS3KeyPrefix](#cfn-config-organizationconformancepack-deliverys3keyprefix)" : {{String}},
      "[ExcludedAccounts](#cfn-config-organizationconformancepack-excludedaccounts)" : {{[ String, ... ]}},
      "[OrganizationConformancePackName](#cfn-config-organizationconformancepack-organizationconformancepackname)" : {{String}},
      "[Tags](#cfn-config-organizationconformancepack-tags)" : {{[ Tag, ... ]}},
      "[TemplateBody](#cfn-config-organizationconformancepack-templatebody)" : {{String}},
      "[TemplateS3Uri](#cfn-config-organizationconformancepack-templates3uri)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-config-organizationconformancepack-syntax.yaml"></a>

```
Type: AWS::Config::OrganizationConformancePack
Properties:
  [ConformancePackInputParameters](#cfn-config-organizationconformancepack-conformancepackinputparameters): {{
    - ConformancePackInputParameter}}
  [DeliveryS3Bucket](#cfn-config-organizationconformancepack-deliverys3bucket): {{String}}
  [DeliveryS3KeyPrefix](#cfn-config-organizationconformancepack-deliverys3keyprefix): {{String}}
  [ExcludedAccounts](#cfn-config-organizationconformancepack-excludedaccounts): {{
    - String}}
  [OrganizationConformancePackName](#cfn-config-organizationconformancepack-organizationconformancepackname): {{String}}
  [Tags](#cfn-config-organizationconformancepack-tags): {{
    - Tag}}
  [TemplateBody](#cfn-config-organizationconformancepack-templatebody): {{String}}
  [TemplateS3Uri](#cfn-config-organizationconformancepack-templates3uri): {{String}}
```

## Properties
<a name="aws-resource-config-organizationconformancepack-properties"></a>

`ConformancePackInputParameters`  <a name="cfn-config-organizationconformancepack-conformancepackinputparameters"></a>
A list of `ConformancePackInputParameter` objects.
*Required*: No
*Type*: Array of [ConformancePackInputParameter](aws-properties-config-organizationconformancepack-conformancepackinputparameter.md)
*Minimum*: `0`
*Maximum*: `60`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeliveryS3Bucket`  <a name="cfn-config-organizationconformancepack-deliverys3bucket"></a>
The name of the Amazon S3 bucket where AWS Config stores conformance pack templates.
This field is optional.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeliveryS3KeyPrefix`  <a name="cfn-config-organizationconformancepack-deliverys3keyprefix"></a>
Any folder structure you want to add to an Amazon S3 bucket.
This field is optional.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExcludedAccounts`  <a name="cfn-config-organizationconformancepack-excludedaccounts"></a>
A comma-separated list of accounts excluded from organization conformance pack.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OrganizationConformancePackName`  <a name="cfn-config-organizationconformancepack-organizationconformancepackname"></a>
The name you assign to an organization conformance pack.
*Required*: Yes
*Type*: String
*Pattern*: `[a-zA-Z][-a-zA-Z0-9]*`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-config-organizationconformancepack-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-config-organizationconformancepack-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TemplateBody`  <a name="cfn-config-organizationconformancepack-templatebody"></a>
A string containing full conformance pack template body. Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `51200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TemplateS3Uri`  <a name="cfn-config-organizationconformancepack-templates3uri"></a>
Location of file containing the template body. The uri must point to the conformance pack template (max size: 300 KB).
*Required*: No
*Type*: String
*Pattern*: `s3://.*`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-config-organizationconformancepack-return-values"></a>

### Ref
<a name="aws-resource-config-organizationconformancepack-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the name of organization conformance pack.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-config-organizationconformancepack-return-values-fn--getatt"></a>

####
<a name="aws-resource-config-organizationconformancepack-return-values-fn--getatt-fn--getatt"></a>

`OrganizationConformancePackArn`  <a name="OrganizationConformancePackArn-fn::getatt"></a>
Amazon Resource Name (ARN) of organization conformance pack.

## Examples
<a name="aws-resource-config-organizationconformancepack--examples"></a>

### Organization Conformance Pack
<a name="aws-resource-config-organizationconformancepack--examples--Organization_Conformance_Pack"></a>

The following example creates an organization conformance pack.

#### JSON
<a name="aws-resource-config-organizationconformancepack--examples--Organization_Conformance_Pack--json"></a>

```
{
    "Resources": {
        "OrganizationConformancePack": {
            "Type": "AWS::Config::OrganizationConformancePack",
            "Properties": {
                "OrganizationConformancePackName": "OrganizationConformancePackName",
                "DeliveryS3Bucket": "DeliveryS3Bucket",
                "TemplateS3Uri": "s3://bucketname/prefix"
             }
         }
     }
}
```

#### YAML
<a name="aws-resource-config-organizationconformancepack--examples--Organization_Conformance_Pack--yaml"></a>

```
---
Resources:
    OrganizationConformancePack:
        Type: AWS::Config::OrganizationConformancePack
        Properties:
            OrganizationConformancePackName: OrganizationConformancePackName
            DeliveryS3Bucket: DeliveryS3Bucket
            TemplateS3Uri: s3://bucketname/prefix
```
