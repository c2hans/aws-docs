---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-groundstation-config-demodulationconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GroundStation::Config DemodulationConfig
<a name="aws-properties-groundstation-config-demodulationconfig"></a>

 Defines demodulation settings.

## Syntax
<a name="aws-properties-groundstation-config-demodulationconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-groundstation-config-demodulationconfig-syntax.json"></a>

```
{
  "[UnvalidatedJSON](#cfn-groundstation-config-demodulationconfig-unvalidatedjson)" : {{String}}
}
```

### YAML
<a name="aws-properties-groundstation-config-demodulationconfig-syntax.yaml"></a>

```
  [UnvalidatedJSON](#cfn-groundstation-config-demodulationconfig-unvalidatedjson): {{String}}
```

## Properties
<a name="aws-properties-groundstation-config-demodulationconfig-properties"></a>

`UnvalidatedJSON`  <a name="cfn-groundstation-config-demodulationconfig-unvalidatedjson"></a>
 The demodulation settings are in JSON format and define parameters for demodulation, for example which modulation scheme (e.g. PSK, QPSK, etc.) and matched filter to use.
*Required*: No
*Type*: String
*Pattern*: `^[{}\[\]:.,"0-9A-z\-_\s]{1,8192}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-groundstation-config-demodulationconfig--examples"></a>

### Create a DemodulationConfig
<a name="aws-properties-groundstation-config-demodulationconfig--examples--Create_a_DemodulationConfig"></a>

The following example creates a Ground Station `DemodulationConfig`

#### JSON
<a name="aws-properties-groundstation-config-demodulationconfig--examples--Create_a_DemodulationConfig--json"></a>

```
{
  "DemodulationConfig": {
    "UnvalidatedJSON": "{ \"type\":\"QPSK\", \"qpsk\":{ \"carrierFrequencyRecovery\":{ \"centerFrequency\":{ \"value\":7812, \"units\":\"MHz\" }, \"range\":{ \"value\":250, \"units\":\"kHz\" } }, \"symbolTimingRecovery\":{ \"symbolRate\":{ \"value\":15, \"units\":\"Msps\" }, \"range\":{ \"value\":0.75, \"units\":\"ksps\" }, \"matchedFilter\":{ \"type\":\"ROOT_RAISED_COSINE\", \"rolloffFactor\":0.5 } } } }"
  },
}
```

#### YAML
<a name="aws-properties-groundstation-config-demodulationconfig--examples--Create_a_DemodulationConfig--yaml"></a>

```
DemodulationConfig:
  UnvalidatedJSON: '{
    "type":"QPSK",
    "qpsk":{
      "carrierFrequencyRecovery":{
        "centerFrequency":{
          "value":7812,
          "units":"MHz"
        },
        "range":{
          "value":250,
          "units":"kHz"
        }
      },
      "symbolTimingRecovery":{
        "symbolRate":{
          "value":15,
          "units":"Msps"
      },
      "range":{
        "value":0.75,
        "units":"ksps"
      },
      "matchedFilter":{
        "type":"ROOT_RAISED_COSINE",
        "rolloffFactor":0.5
      }
    }
  }
}'
```
