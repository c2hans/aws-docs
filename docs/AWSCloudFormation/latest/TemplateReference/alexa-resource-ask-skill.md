---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/alexa-resource-ask-skill.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# Alexa::ASK::Skill
<a name="alexa-resource-ask-skill"></a>

The `Alexa::ASK::Skill` resource creates an Alexa skill that enables customers to access new abilities. For more information about developing a skill, see the [Build Skills with the Alexa Skills Kit developer documentation](https://developer.amazon.com/docs/ask-overviews/build-skills-with-the-alexa-skills-kit.html).

## Syntax
<a name="alexa-resource-ask-skill-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="alexa-resource-ask-skill-syntax.json"></a>

```
{
  "Type" : "Alexa::ASK::Skill",
  "Properties" : {
      "[AuthenticationConfiguration](#cfn-ask-skill-authenticationconfiguration)" : {{AuthenticationConfiguration}},
      "[SkillPackage](#cfn-ask-skill-skillpackage)" : {{SkillPackage}},
      "[VendorId](#cfn-ask-skill-vendorid)" : {{String}}
    }
}
```

### YAML
<a name="alexa-resource-ask-skill-syntax.yaml"></a>

```
Type: Alexa::ASK::Skill
Properties:
  [AuthenticationConfiguration](#cfn-ask-skill-authenticationconfiguration): {{
    AuthenticationConfiguration}}
  [SkillPackage](#cfn-ask-skill-skillpackage): {{
    SkillPackage}}
  [VendorId](#cfn-ask-skill-vendorid): {{String}}
```

## Properties
<a name="alexa-resource-ask-skill-properties"></a>

`AuthenticationConfiguration`  <a name="cfn-ask-skill-authenticationconfiguration"></a>
 Login with Amazon (LWA) configuration used to authenticate with the Alexa service. Only Login with Amazon clients created through the [Amazon Developer Console](https://developer.amazon.com/lwa/sp/overview.html) are supported. The client ID, client secret, and refresh token are required.
*Required*: Yes
*Type*: [AuthenticationConfiguration](alexa-properties-ask-skill-authenticationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SkillPackage`  <a name="cfn-ask-skill-skillpackage"></a>
Configuration for the skill package that contains the components of the Alexa skill. Skill packages are retrieved from an Amazon S3 bucket and key and used to create and update the skill. For more information about the skill package format, see the [Skill Package API Reference](https://developer.amazon.com/docs/smapi/skill-package-api-reference.html#skill-package-format).
*Required*: Yes
*Type*: [SkillPackage](alexa-properties-ask-skill-skillpackage.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VendorId`  <a name="cfn-ask-skill-vendorid"></a>
The vendor ID associated with the Amazon developer account that will host the skill. Details for retrieving the vendor ID are in [How to get your vendor ID](https://github.com/alexa/alexa-smarthome/wiki/How-to-get-your-vendor-ID). The provided LWA credentials must be linked to the developer account associated with this vendor ID.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="alexa-resource-ask-skill-return-values"></a>

### Ref
<a name="alexa-resource-ask-skill-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the skill ID, such as amzn1.ask.skill.a3103cee-c48c-40a0-a2c9-251141888863.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="alexa-resource-ask-skill-return-values-fn--getatt"></a>

## Examples
<a name="alexa-resource-ask-skill--examples"></a>

### Alexa Skill Resource Configuration
<a name="alexa-resource-ask-skill--examples--Alexa_Skill_Resource_Configuration"></a>

The following example retrieves the skill package from an S3 bucket and provides credentials for authentication with the Alexa service through Login with Amazon (LWA).

#### JSON
<a name="alexa-resource-ask-skill--examples--Alexa_Skill_Resource_Configuration--json"></a>

```
"MySkill": {
  "Type": "Alexa::ASK::Skill",
  "Properties": {
    "SkillPackage": {
      "S3Bucket": "my-skill-packages",
      "S3Key": "skillpackage.zip",
      "S3BucketRole": { "Fn::GetAtt": [ "S3BucketReadRole", "Arn" ] },
      "Overrides": {
        "Manifest": {
          "apis": {
            "custom": {
              "endpoint": {
                "uri": { "Fn::GetAtt" : [ "SkillFunction", "Arn" ] }
              }
            }
          }
        }
      }
    },
    "AuthenticationConfiguration": {
      "ClientId": "amzn1.application-oa2-client.1234",
      "ClientSecret": "1234",
      "RefreshToken": "Atzr|1234"
    },
    "VendorId": "1234"
  }
}
```

#### YAML
<a name="alexa-resource-ask-skill--examples--Alexa_Skill_Resource_Configuration--yaml"></a>

```
MySkill: Type: "Alexa::ASK::Skill"
  Properties:
    SkillPackage:
      S3Bucket: "my-skill-packages"
      S3Key: "skillpackage.zip"
      S3BucketRole: !GetAtt S3BucketReadRole.Arn
      Overrides:
        Manifest:
          apis:
            custom:
              endpoint:
                uri: !GetAtt SkillFunction.Arn
    AuthenticationConfiguration:
      ClientId: "amzn1.application-oa2-client.1234"
      ClientSecret: "1234"
      RefreshToken: "Atzr|1234"
    VendorId: "1234"
```
