---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-redshift-qev2idcapplication.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Redshift::QEV2IdcApplication
<a name="aws-resource-redshift-qev2idcapplication"></a>

<a name="aws-resource-redshift-qev2idcapplication-description"></a>The `AWS::Redshift::QEV2IdcApplication` resource Property description not available. for Redshift.

## Syntax
<a name="aws-resource-redshift-qev2idcapplication-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-redshift-qev2idcapplication-syntax.json"></a>

```
{
  "Type" : "AWS::Redshift::QEV2IdcApplication",
  "Properties" : {
      "[IdcDisplayName](#cfn-redshift-qev2idcapplication-idcdisplayname)" : {{String}},
      "[IdcInstanceArn](#cfn-redshift-qev2idcapplication-idcinstancearn)" : {{String}},
      "[Qev2IdcApplicationName](#cfn-redshift-qev2idcapplication-qev2idcapplicationname)" : {{String}},
      "[Tags](#cfn-redshift-qev2idcapplication-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-redshift-qev2idcapplication-syntax.yaml"></a>

```
Type: AWS::Redshift::QEV2IdcApplication
Properties:
  [IdcDisplayName](#cfn-redshift-qev2idcapplication-idcdisplayname): {{String}}
  [IdcInstanceArn](#cfn-redshift-qev2idcapplication-idcinstancearn): {{String}}
  [Qev2IdcApplicationName](#cfn-redshift-qev2idcapplication-qev2idcapplicationname): {{String}}
  [Tags](#cfn-redshift-qev2idcapplication-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-redshift-qev2idcapplication-properties"></a>

`IdcDisplayName`  <a name="cfn-redshift-qev2idcapplication-idcdisplayname"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w+=,.@-]+$`
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IdcInstanceArn`  <a name="cfn-redshift-qev2idcapplication-idcinstancearn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Qev2IdcApplicationName`  <a name="cfn-redshift-qev2idcapplication-qev2idcapplicationname"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z][a-z0-9]*(-[a-z0-9]+)*$`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-redshift-qev2idcapplication-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-redshift-qev2idcapplication-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-redshift-qev2idcapplication-return-values"></a>

### Ref
<a name="aws-resource-redshift-qev2idcapplication-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-redshift-qev2idcapplication-return-values-fn--getatt"></a>

####
<a name="aws-resource-redshift-qev2idcapplication-return-values-fn--getatt-fn--getatt"></a>

`IdcManagedApplicationArn`  <a name="IdcManagedApplicationArn-fn::getatt"></a>
Property description not available.

`IdcOnboardStatus`  <a name="IdcOnboardStatus-fn::getatt"></a>
Property description not available.

`Qev2IdcApplicationArn`  <a name="Qev2IdcApplicationArn-fn::getatt"></a>
Property description not available.
