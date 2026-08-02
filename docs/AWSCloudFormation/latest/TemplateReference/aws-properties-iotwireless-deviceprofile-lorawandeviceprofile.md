---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTWireless::DeviceProfile LoRaWANDeviceProfile
<a name="aws-properties-iotwireless-deviceprofile-lorawandeviceprofile"></a>

LoRaWAN device profile object.

## Syntax
<a name="aws-properties-iotwireless-deviceprofile-lorawandeviceprofile-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotwireless-deviceprofile-lorawandeviceprofile-syntax.json"></a>

```
{
  "[ClassBTimeout](#cfn-iotwireless-deviceprofile-lorawandeviceprofile-classbtimeout)" : {{Integer}},
  "[ClassCTimeout](#cfn-iotwireless-deviceprofile-lorawandeviceprofile-classctimeout)" : {{Integer}},
  "[FactoryPresetFreqsList](#cfn-iotwireless-deviceprofile-lorawandeviceprofile-factorypresetfreqslist)" : {{[ Integer, ... ]}},
  "[MacVersion](#cfn-iotwireless-deviceprofile-lorawandeviceprofile-macversion)" : {{String}},
  "[MaxDutyCycle](#cfn-iotwireless-deviceprofile-lorawandeviceprofile-maxdutycycle)" : {{Integer}},
  "[MaxEirp](#cfn-iotwireless-deviceprofile-lorawandeviceprofile-maxeirp)" : {{Integer}},
  "[PingSlotDr](#cfn-iotwireless-deviceprofile-lorawandeviceprofile-pingslotdr)" : {{Integer}},
  "[PingSlotFreq](#cfn-iotwireless-deviceprofile-lorawandeviceprofile-pingslotfreq)" : {{Integer}},
  "[PingSlotPeriod](#cfn-iotwireless-deviceprofile-lorawandeviceprofile-pingslotperiod)" : {{Integer}},
  "[RegParamsRevision](#cfn-iotwireless-deviceprofile-lorawandeviceprofile-regparamsrevision)" : {{String}},
  "[RfRegion](#cfn-iotwireless-deviceprofile-lorawandeviceprofile-rfregion)" : {{String}},
  "[RxDataRate2](#cfn-iotwireless-deviceprofile-lorawandeviceprofile-rxdatarate2)" : {{Integer}},
  "[RxDelay1](#cfn-iotwireless-deviceprofile-lorawandeviceprofile-rxdelay1)" : {{Integer}},
  "[RxDrOffset1](#cfn-iotwireless-deviceprofile-lorawandeviceprofile-rxdroffset1)" : {{Integer}},
  "[RxFreq2](#cfn-iotwireless-deviceprofile-lorawandeviceprofile-rxfreq2)" : {{Integer}},
  "[Supports32BitFCnt](#cfn-iotwireless-deviceprofile-lorawandeviceprofile-supports32bitfcnt)" : {{Boolean}},
  "[SupportsClassB](#cfn-iotwireless-deviceprofile-lorawandeviceprofile-supportsclassb)" : {{Boolean}},
  "[SupportsClassC](#cfn-iotwireless-deviceprofile-lorawandeviceprofile-supportsclassc)" : {{Boolean}},
  "[SupportsJoin](#cfn-iotwireless-deviceprofile-lorawandeviceprofile-supportsjoin)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-iotwireless-deviceprofile-lorawandeviceprofile-syntax.yaml"></a>

```
  [ClassBTimeout](#cfn-iotwireless-deviceprofile-lorawandeviceprofile-classbtimeout): {{Integer}}
  [ClassCTimeout](#cfn-iotwireless-deviceprofile-lorawandeviceprofile-classctimeout): {{Integer}}
  [FactoryPresetFreqsList](#cfn-iotwireless-deviceprofile-lorawandeviceprofile-factorypresetfreqslist): {{
    - Integer}}
  [MacVersion](#cfn-iotwireless-deviceprofile-lorawandeviceprofile-macversion): {{String}}
  [MaxDutyCycle](#cfn-iotwireless-deviceprofile-lorawandeviceprofile-maxdutycycle): {{Integer}}
  [MaxEirp](#cfn-iotwireless-deviceprofile-lorawandeviceprofile-maxeirp): {{Integer}}
  [PingSlotDr](#cfn-iotwireless-deviceprofile-lorawandeviceprofile-pingslotdr): {{Integer}}
  [PingSlotFreq](#cfn-iotwireless-deviceprofile-lorawandeviceprofile-pingslotfreq): {{Integer}}
  [PingSlotPeriod](#cfn-iotwireless-deviceprofile-lorawandeviceprofile-pingslotperiod): {{Integer}}
  [RegParamsRevision](#cfn-iotwireless-deviceprofile-lorawandeviceprofile-regparamsrevision): {{String}}
  [RfRegion](#cfn-iotwireless-deviceprofile-lorawandeviceprofile-rfregion): {{String}}
  [RxDataRate2](#cfn-iotwireless-deviceprofile-lorawandeviceprofile-rxdatarate2): {{Integer}}
  [RxDelay1](#cfn-iotwireless-deviceprofile-lorawandeviceprofile-rxdelay1): {{Integer}}
  [RxDrOffset1](#cfn-iotwireless-deviceprofile-lorawandeviceprofile-rxdroffset1): {{Integer}}
  [RxFreq2](#cfn-iotwireless-deviceprofile-lorawandeviceprofile-rxfreq2): {{Integer}}
  [Supports32BitFCnt](#cfn-iotwireless-deviceprofile-lorawandeviceprofile-supports32bitfcnt): {{Boolean}}
  [SupportsClassB](#cfn-iotwireless-deviceprofile-lorawandeviceprofile-supportsclassb): {{Boolean}}
  [SupportsClassC](#cfn-iotwireless-deviceprofile-lorawandeviceprofile-supportsclassc): {{Boolean}}
  [SupportsJoin](#cfn-iotwireless-deviceprofile-lorawandeviceprofile-supportsjoin): {{Boolean}}
```

## Properties
<a name="aws-properties-iotwireless-deviceprofile-lorawandeviceprofile-properties"></a>

`ClassBTimeout`  <a name="cfn-iotwireless-deviceprofile-lorawandeviceprofile-classbtimeout"></a>
The ClassBTimeout value.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `1000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ClassCTimeout`  <a name="cfn-iotwireless-deviceprofile-lorawandeviceprofile-classctimeout"></a>
The ClassCTimeout value.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `1000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FactoryPresetFreqsList`  <a name="cfn-iotwireless-deviceprofile-lorawandeviceprofile-factorypresetfreqslist"></a>
The list of values that make up the FactoryPresetFreqs value. Valid range of values include a minimum value of 1000000 and a maximum value of 16700000.
*Required*: No
*Type*: Array of Integer
*Maximum*: `20`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MacVersion`  <a name="cfn-iotwireless-deviceprofile-lorawandeviceprofile-macversion"></a>
The MAC version (such as OTAA 1.1 or OTAA 1.0.3) to use with this device profile.
*Required*: No
*Type*: String
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MaxDutyCycle`  <a name="cfn-iotwireless-deviceprofile-lorawandeviceprofile-maxdutycycle"></a>
The MaxDutyCycle value.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MaxEirp`  <a name="cfn-iotwireless-deviceprofile-lorawandeviceprofile-maxeirp"></a>
The MaxEIRP value.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `15`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PingSlotDr`  <a name="cfn-iotwireless-deviceprofile-lorawandeviceprofile-pingslotdr"></a>
The PingSlotDR value.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `15`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PingSlotFreq`  <a name="cfn-iotwireless-deviceprofile-lorawandeviceprofile-pingslotfreq"></a>
The PingSlotFreq value.
*Required*: No
*Type*: Integer
*Minimum*: `1000000`
*Maximum*: `16700000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PingSlotPeriod`  <a name="cfn-iotwireless-deviceprofile-lorawandeviceprofile-pingslotperiod"></a>
The PingSlotPeriod value.
*Required*: No
*Type*: Integer
*Minimum*: `128`
*Maximum*: `4096`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RegParamsRevision`  <a name="cfn-iotwireless-deviceprofile-lorawandeviceprofile-regparamsrevision"></a>
The version of regional parameters.
*Required*: No
*Type*: String
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RfRegion`  <a name="cfn-iotwireless-deviceprofile-lorawandeviceprofile-rfregion"></a>
The frequency band (RFRegion) value.
*Required*: No
*Type*: String
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RxDataRate2`  <a name="cfn-iotwireless-deviceprofile-lorawandeviceprofile-rxdatarate2"></a>
The RXDataRate2 value.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `15`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RxDelay1`  <a name="cfn-iotwireless-deviceprofile-lorawandeviceprofile-rxdelay1"></a>
The RXDelay1 value.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `15`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RxDrOffset1`  <a name="cfn-iotwireless-deviceprofile-lorawandeviceprofile-rxdroffset1"></a>
The RXDROffset1 value.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `7`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RxFreq2`  <a name="cfn-iotwireless-deviceprofile-lorawandeviceprofile-rxfreq2"></a>
The RXFreq2 value.
*Required*: No
*Type*: Integer
*Minimum*: `1000000`
*Maximum*: `16700000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Supports32BitFCnt`  <a name="cfn-iotwireless-deviceprofile-lorawandeviceprofile-supports32bitfcnt"></a>
The Supports32BitFCnt value.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SupportsClassB`  <a name="cfn-iotwireless-deviceprofile-lorawandeviceprofile-supportsclassb"></a>
The SupportsClassB value.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SupportsClassC`  <a name="cfn-iotwireless-deviceprofile-lorawandeviceprofile-supportsclassc"></a>
The SupportsClassC value.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SupportsJoin`  <a name="cfn-iotwireless-deviceprofile-lorawandeviceprofile-supportsjoin"></a>
The SupportsJoin value.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
