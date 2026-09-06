---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-emailidentity-dkimattributes.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::EmailIdentity DkimAttributes
<a name="aws-properties-ses-emailidentity-dkimattributes"></a>

Used to enable or disable DKIM authentication for an email identity.

## Syntax
<a name="aws-properties-ses-emailidentity-dkimattributes-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-emailidentity-dkimattributes-syntax.json"></a>

```
{
  "[SigningEnabled](#cfn-ses-emailidentity-dkimattributes-signingenabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-ses-emailidentity-dkimattributes-syntax.yaml"></a>

```
  [SigningEnabled](#cfn-ses-emailidentity-dkimattributes-signingenabled): {{Boolean}}
```

## Properties
<a name="aws-properties-ses-emailidentity-dkimattributes-properties"></a>

`SigningEnabled`  <a name="cfn-ses-emailidentity-dkimattributes-signingenabled"></a>
Sets the DKIM signing configuration for the identity.
 When you set this value `true`, then the messages that are sent from the identity are signed using DKIM. If you set this value to `false`, your messages are sent without DKIM signing.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
