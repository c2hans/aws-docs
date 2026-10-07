---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-applicationsignals-instrumentationconfig-capturelimitsconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApplicationSignals::InstrumentationConfig CaptureLimitsConfig
<a name="aws-properties-applicationsignals-instrumentationconfig-capturelimitsconfig"></a>

Guardrails that prevent instrumentation from impacting application performance by limiting how much data is captured.

## Syntax
<a name="aws-properties-applicationsignals-instrumentationconfig-capturelimitsconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-applicationsignals-instrumentationconfig-capturelimitsconfig-syntax.json"></a>

```
{
  "[MaxCollectionDepth](#cfn-applicationsignals-instrumentationconfig-capturelimitsconfig-maxcollectiondepth)" : {{Integer}},
  "[MaxCollectionWidth](#cfn-applicationsignals-instrumentationconfig-capturelimitsconfig-maxcollectionwidth)" : {{Integer}},
  "[MaxFieldsPerObject](#cfn-applicationsignals-instrumentationconfig-capturelimitsconfig-maxfieldsperobject)" : {{Integer}},
  "[MaxHits](#cfn-applicationsignals-instrumentationconfig-capturelimitsconfig-maxhits)" : {{Integer}},
  "[MaxObjectDepth](#cfn-applicationsignals-instrumentationconfig-capturelimitsconfig-maxobjectdepth)" : {{Integer}},
  "[MaxStackFrames](#cfn-applicationsignals-instrumentationconfig-capturelimitsconfig-maxstackframes)" : {{Integer}},
  "[MaxStackTraceSize](#cfn-applicationsignals-instrumentationconfig-capturelimitsconfig-maxstacktracesize)" : {{Integer}},
  "[MaxStringLength](#cfn-applicationsignals-instrumentationconfig-capturelimitsconfig-maxstringlength)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-applicationsignals-instrumentationconfig-capturelimitsconfig-syntax.yaml"></a>

```
  [MaxCollectionDepth](#cfn-applicationsignals-instrumentationconfig-capturelimitsconfig-maxcollectiondepth): {{Integer}}
  [MaxCollectionWidth](#cfn-applicationsignals-instrumentationconfig-capturelimitsconfig-maxcollectionwidth): {{Integer}}
  [MaxFieldsPerObject](#cfn-applicationsignals-instrumentationconfig-capturelimitsconfig-maxfieldsperobject): {{Integer}}
  [MaxHits](#cfn-applicationsignals-instrumentationconfig-capturelimitsconfig-maxhits): {{Integer}}
  [MaxObjectDepth](#cfn-applicationsignals-instrumentationconfig-capturelimitsconfig-maxobjectdepth): {{Integer}}
  [MaxStackFrames](#cfn-applicationsignals-instrumentationconfig-capturelimitsconfig-maxstackframes): {{Integer}}
  [MaxStackTraceSize](#cfn-applicationsignals-instrumentationconfig-capturelimitsconfig-maxstacktracesize): {{Integer}}
  [MaxStringLength](#cfn-applicationsignals-instrumentationconfig-capturelimitsconfig-maxstringlength): {{Integer}}
```

## Properties
<a name="aws-properties-applicationsignals-instrumentationconfig-capturelimitsconfig-properties"></a>

`MaxCollectionDepth`  <a name="cfn-applicationsignals-instrumentationconfig-capturelimitsconfig-maxcollectiondepth"></a>
The maximum nesting depth to traverse inside collections. Defaults to 3.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MaxCollectionWidth`  <a name="cfn-applicationsignals-instrumentationconfig-capturelimitsconfig-maxcollectionwidth"></a>
The maximum number of items to capture from any collection to prevent large payloads. Defaults to 10.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `20`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MaxFieldsPerObject`  <a name="cfn-applicationsignals-instrumentationconfig-capturelimitsconfig-maxfieldsperobject"></a>
The maximum number of fields to capture for any object. Defaults to 10.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `20`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MaxHits`  <a name="cfn-applicationsignals-instrumentationconfig-capturelimitsconfig-maxhits"></a>
The maximum number of times the instrumentation point can be hit before it is automatically disabled. Defaults to 100.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MaxObjectDepth`  <a name="cfn-applicationsignals-instrumentationconfig-capturelimitsconfig-maxobjectdepth"></a>
The maximum depth for nested object traversal when capturing structured data. Defaults to 3.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MaxStackFrames`  <a name="cfn-applicationsignals-instrumentationconfig-capturelimitsconfig-maxstackframes"></a>
The maximum number of stack frames to capture in stack traces. Defaults to 2.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `20`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MaxStackTraceSize`  <a name="cfn-applicationsignals-instrumentationconfig-capturelimitsconfig-maxstacktracesize"></a>
The maximum total size, in bytes, of a captured stack trace. Defaults to 1000.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MaxStringLength`  <a name="cfn-applicationsignals-instrumentationconfig-capturelimitsconfig-maxstringlength"></a>
The maximum length of captured string values in characters. Strings longer than this are truncated. Defaults to 128.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
