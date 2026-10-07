---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-applicationsignals-instrumentationconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApplicationSignals::InstrumentationConfig
<a name="aws-resource-applicationsignals-instrumentationconfig"></a>

Creates a dynamic instrumentation configuration for a specific code or endpoint location within a service and environment. Configurations are immutable after creation.

For `BREAKPOINT` type configurations, they expire after 24 hours unless a shorter expiration is provided. For `PROBE` type configurations, they persist until explicitly deleted; an expiration cannot be set for `PROBE` configurations.

If a configuration already exists for the same service, environment, signal type, and location, this operation returns a conflict instead of overwriting it. Use attribute filters and capture settings to control where the instrumentation runs and which data is collected.

## Syntax
<a name="aws-resource-applicationsignals-instrumentationconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-applicationsignals-instrumentationconfig-syntax.json"></a>

```
{
  "Type" : "AWS::ApplicationSignals::InstrumentationConfig",
  "Properties" : {
      "[AttributeFilters](#cfn-applicationsignals-instrumentationconfig-attributefilters)" : {{[ {{{Key}}: {{Value}}, ...}, ... ]}},
      "[CaptureConfiguration](#cfn-applicationsignals-instrumentationconfig-captureconfiguration)" : {{CaptureConfiguration}},
      "[Description](#cfn-applicationsignals-instrumentationconfig-description)" : {{String}},
      "[Environment](#cfn-applicationsignals-instrumentationconfig-environment)" : {{String}},
      "[ExpiresAt](#cfn-applicationsignals-instrumentationconfig-expiresat)" : {{String}},
      "[InstrumentationType](#cfn-applicationsignals-instrumentationconfig-instrumentationtype)" : {{String}},
      "[Location](#cfn-applicationsignals-instrumentationconfig-location)" : {{Location}},
      "[Service](#cfn-applicationsignals-instrumentationconfig-service)" : {{String}},
      "[SignalType](#cfn-applicationsignals-instrumentationconfig-signaltype)" : {{String}},
      "[Tags](#cfn-applicationsignals-instrumentationconfig-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-applicationsignals-instrumentationconfig-syntax.yaml"></a>

```
Type: AWS::ApplicationSignals::InstrumentationConfig
Properties:
  [AttributeFilters](#cfn-applicationsignals-instrumentationconfig-attributefilters): {{
    -
    {{Key}}: {{Value}}}}
  [CaptureConfiguration](#cfn-applicationsignals-instrumentationconfig-captureconfiguration): {{
    CaptureConfiguration}}
  [Description](#cfn-applicationsignals-instrumentationconfig-description): {{String}}
  [Environment](#cfn-applicationsignals-instrumentationconfig-environment): {{String}}
  [ExpiresAt](#cfn-applicationsignals-instrumentationconfig-expiresat): {{String}}
  [InstrumentationType](#cfn-applicationsignals-instrumentationconfig-instrumentationtype): {{String}}
  [Location](#cfn-applicationsignals-instrumentationconfig-location): {{
    Location}}
  [Service](#cfn-applicationsignals-instrumentationconfig-service): {{String}}
  [SignalType](#cfn-applicationsignals-instrumentationconfig-signaltype): {{String}}
  [Tags](#cfn-applicationsignals-instrumentationconfig-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-applicationsignals-instrumentationconfig-properties"></a>

`AttributeFilters`  <a name="cfn-applicationsignals-instrumentationconfig-attributefilters"></a>
Client-side filters that determine which instances apply this instrumentation.
*Required*: No
*Type*: Array of Object
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CaptureConfiguration`  <a name="cfn-applicationsignals-instrumentationconfig-captureconfiguration"></a>
The capture settings for this instrumentation configuration.
*Required*: Yes
*Type*: [CaptureConfiguration](aws-properties-applicationsignals-instrumentationconfig-captureconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-applicationsignals-instrumentationconfig-description"></a>
An optional short description of the instrumentation configuration.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Environment`  <a name="cfn-applicationsignals-instrumentationconfig-environment"></a>
The environment where the service is running.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9:/+=,.@_-]+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ExpiresAt`  <a name="cfn-applicationsignals-instrumentationconfig-expiresat"></a>
The timestamp when this configuration expires.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InstrumentationType`  <a name="cfn-applicationsignals-instrumentationconfig-instrumentationtype"></a>
The type of instrumentation for this configuration.
*Required*: Yes
*Type*: String
*Allowed values*: `BREAKPOINT | PROBE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Location`  <a name="cfn-applicationsignals-instrumentationconfig-location"></a>
The location where this instrumentation is applied.
*Required*: Yes
*Type*: [Location](aws-properties-applicationsignals-instrumentationconfig-location.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Service`  <a name="cfn-applicationsignals-instrumentationconfig-service"></a>
The service that this instrumentation configuration targets.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9:/+=,.@_-]+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SignalType`  <a name="cfn-applicationsignals-instrumentationconfig-signaltype"></a>
The telemetry signal type for this instrumentation configuration.
*Required*: Yes
*Type*: String
*Allowed values*: `SNAPSHOT`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-applicationsignals-instrumentationconfig-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-applicationsignals-instrumentationconfig-tag.md)
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-applicationsignals-instrumentationconfig-return-values"></a>

### Ref
<a name="aws-resource-applicationsignals-instrumentationconfig-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-applicationsignals-instrumentationconfig-return-values-fn--getatt"></a>

####
<a name="aws-resource-applicationsignals-instrumentationconfig-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN for the instrumentation configuration.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when this instrumentation configuration was created.

`LocationHash`  <a name="LocationHash-fn::getatt"></a>
The stable hash derived from the location that uniquely identifies this instrumentation point within the service and environment.
