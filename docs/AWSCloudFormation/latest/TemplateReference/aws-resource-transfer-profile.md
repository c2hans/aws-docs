---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-transfer-profile.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Transfer::Profile
<a name="aws-resource-transfer-profile"></a>

Creates the local or partner profile to use for AS2 transfers.

## Syntax
<a name="aws-resource-transfer-profile-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-transfer-profile-syntax.json"></a>

```
{
  "Type" : "AWS::Transfer::Profile",
  "Properties" : {
      "[As2Id](#cfn-transfer-profile-as2id)" : {{String}},
      "[CertificateIds](#cfn-transfer-profile-certificateids)" : {{[ String, ... ]}},
      "[ProfileType](#cfn-transfer-profile-profiletype)" : {{String}},
      "[Tags](#cfn-transfer-profile-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-transfer-profile-syntax.yaml"></a>

```
Type: AWS::Transfer::Profile
Properties:
  [As2Id](#cfn-transfer-profile-as2id): {{String}}
  [CertificateIds](#cfn-transfer-profile-certificateids): {{
    - String}}
  [ProfileType](#cfn-transfer-profile-profiletype): {{String}}
  [Tags](#cfn-transfer-profile-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-transfer-profile-properties"></a>

`As2Id`  <a name="cfn-transfer-profile-as2id"></a>
The `As2Id` is the *AS2-name*, as defined in the [RFC 4130](https://datatracker.ietf.org/doc/html/rfc4130). For inbound transfers, this is the `AS2-From` header for the AS2 messages sent from the partner. For outbound connectors, this is the `AS2-To` header for the AS2 messages sent to the partner using the `StartFileTransfer` API operation. This ID cannot include spaces.
*Required*: Yes
*Type*: String
*Pattern*: `^[\u0020-\u007E\s]*$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CertificateIds`  <a name="cfn-transfer-profile-certificateids"></a>
An array of identifiers for the imported certificates. You use this identifier for working with profiles and partner profiles.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProfileType`  <a name="cfn-transfer-profile-profiletype"></a>
Indicates whether to list only `LOCAL` type profiles or only `PARTNER` type profiles. If not supplied in the request, the command lists all types of profiles.
*Required*: Yes
*Type*: String
*Allowed values*: `LOCAL | PARTNER`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-transfer-profile-tags"></a>
Key-value pairs that can be used to group and search for profiles.
*Required*: No
*Type*: Array of [Tag](aws-properties-transfer-profile-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-transfer-profile-return-values"></a>

### Ref
<a name="aws-resource-transfer-profile-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-transfer-profile-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-transfer-profile-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
 The Amazon Resource Name associated with the profile, in the form `arn:aws:transfer:region:account-id:profile/profile-id/` .

`ProfileId`  <a name="ProfileId-fn::getatt"></a>
The unique identifier for the AS2 profile, returned after the API call succeeds.
