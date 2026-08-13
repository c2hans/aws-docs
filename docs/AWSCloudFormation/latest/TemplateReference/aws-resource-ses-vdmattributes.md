---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ses-vdmattributes.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::VdmAttributes
<a name="aws-resource-ses-vdmattributes"></a>

The Virtual Deliverability Manager (VDM) attributes that apply to your Amazon SES account.

## Syntax
<a name="aws-resource-ses-vdmattributes-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ses-vdmattributes-syntax.json"></a>

```
{
  "Type" : "AWS::SES::VdmAttributes",
  "Properties" : {
      "[DashboardAttributes](#cfn-ses-vdmattributes-dashboardattributes)" : {{DashboardAttributes}},
      "[GuardianAttributes](#cfn-ses-vdmattributes-guardianattributes)" : {{GuardianAttributes}}
    }
}
```

### YAML
<a name="aws-resource-ses-vdmattributes-syntax.yaml"></a>

```
Type: AWS::SES::VdmAttributes
Properties:
  [DashboardAttributes](#cfn-ses-vdmattributes-dashboardattributes): {{
    DashboardAttributes}}
  [GuardianAttributes](#cfn-ses-vdmattributes-guardianattributes): {{
    GuardianAttributes}}
```

## Properties
<a name="aws-resource-ses-vdmattributes-properties"></a>

`DashboardAttributes`  <a name="cfn-ses-vdmattributes-dashboardattributes"></a>
Specifies additional settings for your VDM configuration as applicable to the Dashboard.
*Required*: No
*Type*: [DashboardAttributes](aws-properties-ses-vdmattributes-dashboardattributes.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GuardianAttributes`  <a name="cfn-ses-vdmattributes-guardianattributes"></a>
Specifies additional settings for your VDM configuration as applicable to the Guardian.
*Required*: No
*Type*: [GuardianAttributes](aws-properties-ses-vdmattributes-guardianattributes.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ses-vdmattributes-return-values"></a>

### Ref
<a name="aws-resource-ses-vdmattributes-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource name.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ses-vdmattributes-return-values-fn--getatt"></a>

####
<a name="aws-resource-ses-vdmattributes-return-values-fn--getatt-fn--getatt"></a>

`VdmAttributesResourceId`  <a name="VdmAttributesResourceId-fn::getatt"></a>
Property description not available.
