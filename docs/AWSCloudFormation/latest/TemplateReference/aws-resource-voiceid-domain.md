---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-voiceid-domain.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::VoiceID::Domain
<a name="aws-resource-voiceid-domain"></a>

**Important**
End of support notice: On May 20, 2026, AWS will end support for Connect Customer Voice ID. After May 20, 2026, you will no longer be able to access Voice ID on the Connect Customer console, access Voice ID features on the Connect Customer admin website or Contact Control Panel, or access Voice ID resources. For more information, visit [ Connect Customer Voice ID end of support](https://docs.aws.amazon.com/connect/latest/adminguide/amazonconnect-voiceid-end-of-support.html).

Creates a domain that contains all Connect Customer Voice ID data, such as speakers, fraudsters, customer audio, and voiceprints. Every domain is created with a default watchlist that fraudsters can be a part of.

## Syntax
<a name="aws-resource-voiceid-domain-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-voiceid-domain-syntax.json"></a>

```
{
  "Type" : "AWS::VoiceID::Domain",
  "Properties" : {
      "[Description](#cfn-voiceid-domain-description)" : {{String}},
      "[Name](#cfn-voiceid-domain-name)" : {{String}},
      "[ServerSideEncryptionConfiguration](#cfn-voiceid-domain-serversideencryptionconfiguration)" : {{ServerSideEncryptionConfiguration}},
      "[Tags](#cfn-voiceid-domain-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-voiceid-domain-syntax.yaml"></a>

```
Type: AWS::VoiceID::Domain
Properties:
  [Description](#cfn-voiceid-domain-description): {{String}}
  [Name](#cfn-voiceid-domain-name): {{String}}
  [ServerSideEncryptionConfiguration](#cfn-voiceid-domain-serversideencryptionconfiguration): {{
    ServerSideEncryptionConfiguration}}
  [Tags](#cfn-voiceid-domain-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-voiceid-domain-properties"></a>

`Description`  <a name="cfn-voiceid-domain-description"></a>
The description of the domain.
*Required*: No
*Type*: String
*Pattern*: `^([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)$`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-voiceid-domain-name"></a>
The name for the domain.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9][a-zA-Z0-9_-]*$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServerSideEncryptionConfiguration`  <a name="cfn-voiceid-domain-serversideencryptionconfiguration"></a>
The server-side encryption configuration containing the KMS key identifier you want Voice ID to use to encrypt your data.
*Required*: Yes
*Type*: [ServerSideEncryptionConfiguration](aws-properties-voiceid-domain-serversideencryptionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-voiceid-domain-tags"></a>
The tags used to organize, track, or control access for this resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-voiceid-domain-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-voiceid-domain-return-values"></a>

### Ref
<a name="aws-resource-voiceid-domain-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the `DomainId` of the domain.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-voiceid-domain-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-voiceid-domain-return-values-fn--getatt-fn--getatt"></a>

`DomainId`  <a name="DomainId-fn::getatt"></a>
The identifier of the domain.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
