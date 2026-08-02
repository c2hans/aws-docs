---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-uxc-accountcustomization.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::UXC::AccountCustomization
<a name="aws-resource-uxc-accountcustomization"></a>

The `AWS::UXC::AccountCustomization` resource specifies account-level UX customization settings for the console, including account color, visible services, and visible regions.

## Syntax
<a name="aws-resource-uxc-accountcustomization-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-uxc-accountcustomization-syntax.json"></a>

```
{
  "Type" : "AWS::UXC::AccountCustomization",
  "Properties" : {
      "[AccountColor](#cfn-uxc-accountcustomization-accountcolor)" : {{String}},
      "[VisibleRegions](#cfn-uxc-accountcustomization-visibleregions)" : {{[ String, ... ]}},
      "[VisibleServices](#cfn-uxc-accountcustomization-visibleservices)" : {{[ String, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-uxc-accountcustomization-syntax.yaml"></a>

```
Type: AWS::UXC::AccountCustomization
Properties:
  [AccountColor](#cfn-uxc-accountcustomization-accountcolor): {{String}}
  [VisibleRegions](#cfn-uxc-accountcustomization-visibleregions): {{
    - String}}
  [VisibleServices](#cfn-uxc-accountcustomization-visibleservices): {{
    - String}}
```

## Properties
<a name="aws-resource-uxc-accountcustomization-properties"></a>

`AccountColor`  <a name="cfn-uxc-accountcustomization-accountcolor"></a>
The account color preference to set. Set to `none` to reset to the default (no color).
*Required*: No
*Type*: String
*Allowed values*: `none | pink | purple | darkBlue | lightBlue | teal | green | yellow | orange | red`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VisibleRegions`  <a name="cfn-uxc-accountcustomization-visibleregions"></a>
The list of AWS Region codes to make visible in the AWS Management Console. Omitting this property or setting it to an empty array resets to the default, which makes all Regions visible. For a list of valid Region codes, see [AWS Regions](https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html).
*Required*: No
*Type*: Array of String
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VisibleServices`  <a name="cfn-uxc-accountcustomization-visibleservices"></a>
The list of AWS service identifiers to make visible in the AWS Management Console. Omitting this property or setting it to an empty array resets to the default, which makes all services visible. For valid service identifiers, call [ListServices](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/APIReference/API_ListServices.html).
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `64 | 500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-uxc-accountcustomization-return-values"></a>

### Ref
<a name="aws-resource-uxc-accountcustomization-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the account ID. For example: `123456789012`.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-uxc-accountcustomization-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-uxc-accountcustomization-return-values-fn--getatt-fn--getatt"></a>

`AccountId`  <a name="AccountId-fn::getatt"></a>
The 12-digit account ID that this customization belongs to. For example: `123456789012`.
