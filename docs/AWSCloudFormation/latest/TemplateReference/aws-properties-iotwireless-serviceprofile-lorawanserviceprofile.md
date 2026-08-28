---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTWireless::ServiceProfile LoRaWANServiceProfile
<a name="aws-properties-iotwireless-serviceprofile-lorawanserviceprofile"></a>

LoRaWANServiceProfile object.

## Syntax
<a name="aws-properties-iotwireless-serviceprofile-lorawanserviceprofile-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotwireless-serviceprofile-lorawanserviceprofile-syntax.json"></a>

```
{
  "[AddGwMetadata](#cfn-iotwireless-serviceprofile-lorawanserviceprofile-addgwmetadata)" : {{Boolean}},
  "[ChannelMask](#cfn-iotwireless-serviceprofile-lorawanserviceprofile-channelmask)" : {{String}},
  "[DevStatusReqFreq](#cfn-iotwireless-serviceprofile-lorawanserviceprofile-devstatusreqfreq)" : {{Integer}},
  "[DlBucketSize](#cfn-iotwireless-serviceprofile-lorawanserviceprofile-dlbucketsize)" : {{Integer}},
  "[DlRate](#cfn-iotwireless-serviceprofile-lorawanserviceprofile-dlrate)" : {{Integer}},
  "[DlRatePolicy](#cfn-iotwireless-serviceprofile-lorawanserviceprofile-dlratepolicy)" : {{String}},
  "[DrMax](#cfn-iotwireless-serviceprofile-lorawanserviceprofile-drmax)" : {{Integer}},
  "[DrMin](#cfn-iotwireless-serviceprofile-lorawanserviceprofile-drmin)" : {{Integer}},
  "[HrAllowed](#cfn-iotwireless-serviceprofile-lorawanserviceprofile-hrallowed)" : {{Boolean}},
  "[MinGwDiversity](#cfn-iotwireless-serviceprofile-lorawanserviceprofile-mingwdiversity)" : {{Integer}},
  "[NwkGeoLoc](#cfn-iotwireless-serviceprofile-lorawanserviceprofile-nwkgeoloc)" : {{Boolean}},
  "[PrAllowed](#cfn-iotwireless-serviceprofile-lorawanserviceprofile-prallowed)" : {{Boolean}},
  "[RaAllowed](#cfn-iotwireless-serviceprofile-lorawanserviceprofile-raallowed)" : {{Boolean}},
  "[ReportDevStatusBattery](#cfn-iotwireless-serviceprofile-lorawanserviceprofile-reportdevstatusbattery)" : {{Boolean}},
  "[ReportDevStatusMargin](#cfn-iotwireless-serviceprofile-lorawanserviceprofile-reportdevstatusmargin)" : {{Boolean}},
  "[TargetPer](#cfn-iotwireless-serviceprofile-lorawanserviceprofile-targetper)" : {{Integer}},
  "[UlBucketSize](#cfn-iotwireless-serviceprofile-lorawanserviceprofile-ulbucketsize)" : {{Integer}},
  "[UlRate](#cfn-iotwireless-serviceprofile-lorawanserviceprofile-ulrate)" : {{Integer}},
  "[UlRatePolicy](#cfn-iotwireless-serviceprofile-lorawanserviceprofile-ulratepolicy)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotwireless-serviceprofile-lorawanserviceprofile-syntax.yaml"></a>

```
  [AddGwMetadata](#cfn-iotwireless-serviceprofile-lorawanserviceprofile-addgwmetadata): {{Boolean}}
  [ChannelMask](#cfn-iotwireless-serviceprofile-lorawanserviceprofile-channelmask): {{String}}
  [DevStatusReqFreq](#cfn-iotwireless-serviceprofile-lorawanserviceprofile-devstatusreqfreq): {{Integer}}
  [DlBucketSize](#cfn-iotwireless-serviceprofile-lorawanserviceprofile-dlbucketsize): {{Integer}}
  [DlRate](#cfn-iotwireless-serviceprofile-lorawanserviceprofile-dlrate): {{Integer}}
  [DlRatePolicy](#cfn-iotwireless-serviceprofile-lorawanserviceprofile-dlratepolicy): {{String}}
  [DrMax](#cfn-iotwireless-serviceprofile-lorawanserviceprofile-drmax): {{Integer}}
  [DrMin](#cfn-iotwireless-serviceprofile-lorawanserviceprofile-drmin): {{Integer}}
  [HrAllowed](#cfn-iotwireless-serviceprofile-lorawanserviceprofile-hrallowed): {{Boolean}}
  [MinGwDiversity](#cfn-iotwireless-serviceprofile-lorawanserviceprofile-mingwdiversity): {{Integer}}
  [NwkGeoLoc](#cfn-iotwireless-serviceprofile-lorawanserviceprofile-nwkgeoloc): {{Boolean}}
  [PrAllowed](#cfn-iotwireless-serviceprofile-lorawanserviceprofile-prallowed): {{Boolean}}
  [RaAllowed](#cfn-iotwireless-serviceprofile-lorawanserviceprofile-raallowed): {{Boolean}}
  [ReportDevStatusBattery](#cfn-iotwireless-serviceprofile-lorawanserviceprofile-reportdevstatusbattery): {{Boolean}}
  [ReportDevStatusMargin](#cfn-iotwireless-serviceprofile-lorawanserviceprofile-reportdevstatusmargin): {{Boolean}}
  [TargetPer](#cfn-iotwireless-serviceprofile-lorawanserviceprofile-targetper): {{Integer}}
  [UlBucketSize](#cfn-iotwireless-serviceprofile-lorawanserviceprofile-ulbucketsize): {{Integer}}
  [UlRate](#cfn-iotwireless-serviceprofile-lorawanserviceprofile-ulrate): {{Integer}}
  [UlRatePolicy](#cfn-iotwireless-serviceprofile-lorawanserviceprofile-ulratepolicy): {{String}}
```

## Properties
<a name="aws-properties-iotwireless-serviceprofile-lorawanserviceprofile-properties"></a>

`AddGwMetadata`  <a name="cfn-iotwireless-serviceprofile-lorawanserviceprofile-addgwmetadata"></a>
The AddGWMetaData value.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ChannelMask`  <a name="cfn-iotwireless-serviceprofile-lorawanserviceprofile-channelmask"></a>
The ChannelMask value.
This property is `ReadOnly` and can't be inputted for create. It's returned with `Fn::GetAtt`
*Required*: No
*Type*: String
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DevStatusReqFreq`  <a name="cfn-iotwireless-serviceprofile-lorawanserviceprofile-devstatusreqfreq"></a>
The DevStatusReqFreq value.
This property is `ReadOnly` and can't be inputted for create. It's returned with `Fn::GetAtt`
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `2147483647`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DlBucketSize`  <a name="cfn-iotwireless-serviceprofile-lorawanserviceprofile-dlbucketsize"></a>
The DLBucketSize value.
This property is `ReadOnly` and can't be inputted for create. It's returned with `Fn::GetAtt`
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `2147483647`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DlRate`  <a name="cfn-iotwireless-serviceprofile-lorawanserviceprofile-dlrate"></a>
The DLRate value.
This property is `ReadOnly` and can't be inputted for create. It's returned with `Fn::GetAtt`
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `2147483647`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DlRatePolicy`  <a name="cfn-iotwireless-serviceprofile-lorawanserviceprofile-dlratepolicy"></a>
The DLRatePolicy value.
This property is `ReadOnly` and can't be inputted for create. It's returned with `Fn::GetAtt`
*Required*: No
*Type*: String
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DrMax`  <a name="cfn-iotwireless-serviceprofile-lorawanserviceprofile-drmax"></a>
The DRMax value.
This property is `ReadOnly` and can't be inputted for create. It's returned with `Fn::GetAtt`
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `15`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DrMin`  <a name="cfn-iotwireless-serviceprofile-lorawanserviceprofile-drmin"></a>
The DRMin value.
This property is `ReadOnly` and can't be inputted for create. It's returned with `Fn::GetAtt`
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `15`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`HrAllowed`  <a name="cfn-iotwireless-serviceprofile-lorawanserviceprofile-hrallowed"></a>
The HRAllowed value that describes whether handover roaming is allowed.
This property is `ReadOnly` and can't be inputted for create. It's returned with `Fn::GetAtt`
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MinGwDiversity`  <a name="cfn-iotwireless-serviceprofile-lorawanserviceprofile-mingwdiversity"></a>
The MinGwDiversity value.
This property is `ReadOnly` and can't be inputted for create. It's returned with `Fn::GetAtt`
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NwkGeoLoc`  <a name="cfn-iotwireless-serviceprofile-lorawanserviceprofile-nwkgeoloc"></a>
The NwkGeoLoc value.
This property is `ReadOnly` and can't be inputted for create. It's returned with `Fn::GetAtt`
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PrAllowed`  <a name="cfn-iotwireless-serviceprofile-lorawanserviceprofile-prallowed"></a>
The PRAllowed value that describes whether passive roaming is allowed.
This property is `ReadOnly` and can't be inputted for create. It's returned with `Fn::GetAtt`
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RaAllowed`  <a name="cfn-iotwireless-serviceprofile-lorawanserviceprofile-raallowed"></a>
The RAAllowed value that describes whether roaming activation is allowed.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ReportDevStatusBattery`  <a name="cfn-iotwireless-serviceprofile-lorawanserviceprofile-reportdevstatusbattery"></a>
The ReportDevStatusBattery value.
This property is `ReadOnly` and can't be inputted for create. It's returned with `Fn::GetAtt`
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ReportDevStatusMargin`  <a name="cfn-iotwireless-serviceprofile-lorawanserviceprofile-reportdevstatusmargin"></a>
The ReportDevStatusMargin value.
This property is `ReadOnly` and can't be inputted for create. It's returned with `Fn::GetAtt`
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TargetPer`  <a name="cfn-iotwireless-serviceprofile-lorawanserviceprofile-targetper"></a>
The TargetPer value.
This property is `ReadOnly` and can't be inputted for create. It's returned with `Fn::GetAtt`
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`UlBucketSize`  <a name="cfn-iotwireless-serviceprofile-lorawanserviceprofile-ulbucketsize"></a>
The UlBucketSize value.
This property is `ReadOnly` and can't be inputted for create. It's returned with `Fn::GetAtt`
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `2147483647`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`UlRate`  <a name="cfn-iotwireless-serviceprofile-lorawanserviceprofile-ulrate"></a>
The ULRate value.
This property is `ReadOnly` and can't be inputted for create. It's returned with `Fn::GetAtt`
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `2147483647`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`UlRatePolicy`  <a name="cfn-iotwireless-serviceprofile-lorawanserviceprofile-ulratepolicy"></a>
The ULRatePolicy value.
This property is `ReadOnly` and can't be inputted for create. It's returned with `Fn::GetAtt`
*Required*: No
*Type*: String
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
