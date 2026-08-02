---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ivs-playbackrestrictionpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IVS::PlaybackRestrictionPolicy
<a name="aws-resource-ivs-playbackrestrictionpolicy"></a>

The `AWS::IVS::PlaybackRestrictionPolicy` resource specifies an Amazon IVS playback restriction policy. A playback restriction policy constrains playback by country and/or origin sites. For more information, see [Undesired Content and Viewers](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/undesired-content.html) in the *Amazon IVS Low-Latency Streaming User Guide*.

## Syntax
<a name="aws-resource-ivs-playbackrestrictionpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ivs-playbackrestrictionpolicy-syntax.json"></a>

```
{
  "Type" : "AWS::IVS::PlaybackRestrictionPolicy",
  "Properties" : {
      "[AllowedCountries](#cfn-ivs-playbackrestrictionpolicy-allowedcountries)" : {{[ String, ... ]}},
      "[AllowedOrigins](#cfn-ivs-playbackrestrictionpolicy-allowedorigins)" : {{[ String, ... ]}},
      "[EnableStrictOriginEnforcement](#cfn-ivs-playbackrestrictionpolicy-enablestrictoriginenforcement)" : {{Boolean}},
      "[Name](#cfn-ivs-playbackrestrictionpolicy-name)" : {{String}},
      "[Tags](#cfn-ivs-playbackrestrictionpolicy-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-ivs-playbackrestrictionpolicy-syntax.yaml"></a>

```
Type: AWS::IVS::PlaybackRestrictionPolicy
Properties:
  [AllowedCountries](#cfn-ivs-playbackrestrictionpolicy-allowedcountries): {{
    - String}}
  [AllowedOrigins](#cfn-ivs-playbackrestrictionpolicy-allowedorigins): {{
    - String}}
  [EnableStrictOriginEnforcement](#cfn-ivs-playbackrestrictionpolicy-enablestrictoriginenforcement): {{Boolean}}
  [Name](#cfn-ivs-playbackrestrictionpolicy-name): {{String}}
  [Tags](#cfn-ivs-playbackrestrictionpolicy-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-ivs-playbackrestrictionpolicy-properties"></a>

`AllowedCountries`  <a name="cfn-ivs-playbackrestrictionpolicy-allowedcountries"></a>
A list of country codes that control geoblocking restrictions. Allowed values are the officially assigned ISO 3166-1 alpha-2 codes. Default: All countries (an empty array).
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AllowedOrigins`  <a name="cfn-ivs-playbackrestrictionpolicy-allowedorigins"></a>
A list of origin sites that control CORS restriction. Allowed values are the same as valid values of the Origin header defined at [https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Origin"](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Origin)
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnableStrictOriginEnforcement`  <a name="cfn-ivs-playbackrestrictionpolicy-enablestrictoriginenforcement"></a>
Whether channel playback is constrained by the origin site.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-ivs-playbackrestrictionpolicy-name"></a>
Playback-restriction-policy name.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9-_]*$`
*Minimum*: `0`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-ivs-playbackrestrictionpolicy-tags"></a>
An array of key-value pairs to apply to this resource.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-playbackrestrictionpolicy-tag.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-ivs-playbackrestrictionpolicy-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ivs-playbackrestrictionpolicy-return-values"></a>

### Ref
<a name="aws-resource-ivs-playbackrestrictionpolicy-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the playback-restriction-policy ARN. For example:

 `{ "Ref": "myPlaybackRestrictionPolicy" }`

For the Amazon IVS playback restriction policy `"myPlaybackRestrictionPolicy"`, `Ref` returns the playback-restriction-policy ARN.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ivs-playbackrestrictionpolicy-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ivs-playbackrestrictionpolicy-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The playback-restriction-policy ARN. For example: `arn:aws:ivs:us-west-2:123456789012:playback-restriction-policy/abcdABCDefgh`

## Examples
<a name="aws-resource-ivs-playbackrestrictionpolicy--examples"></a>

### PlaybackRestrictionPolicy Template Examples
<a name="aws-resource-ivs-playbackrestrictionpolicy--examples--PlaybackRestrictionPolicy_Template_Examples"></a>

The following examples specify an Amazon IVS playback restriction policy.

#### JSON
<a name="aws-resource-ivs-playbackrestrictionpolicy--examples--PlaybackRestrictionPolicy_Template_Examples--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
        "PlaybackRestrictionPolicy": {
            "Type": "AWS::IVS::PlaybackRestrictionPolicy",
            "Properties": {
                "AllowedCountries" : [ "US" ],
                "AllowedOrigins" : [ "https://aws.amazon.com" ],
                "EnableStrictOriginEnforcement" : true,
                "Name": "myPlaybackRestrictionPolicy",
                "Tags": [
                    {
                        "Key": "MyKey",
                        "Value": "MyValue"
                    }
                ]
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-ivs-playbackrestrictionpolicy--examples--PlaybackRestrictionPolicy_Template_Examples--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  PlaybackRestrictionPolicy:
    Type: AWS::IVS::PlaybackRestrictionPolicy
    Properties:
      AllowedCountries:
        - US
      AllowedOrigins:
        - https://aws.amazon.com
      EnableStrictOriginEnforcement: true
      Name: myPlaybackRestrictionPolicy
      Tags:
        - Key: myKey
          Value: myValue
```

## See also
<a name="aws-resource-ivs-playbackrestrictionpolicy--seealso"></a>
+  [Getting Started with IVS Low-Latency Streaming](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/getting-started.html)
+  [Undesired Content and Viewers](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/undesired-content.html)
