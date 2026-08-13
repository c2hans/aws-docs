---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ivs-publickey.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IVS::PublicKey
<a name="aws-resource-ivs-publickey"></a>

The `AWS::IVS::PublicKey` resource specifies an Amazon IVS public key used to sign stage participant tokens. For more information, see [Distribute Participant Tokens](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/getting-started-distribute-tokens.html) in the *Amazon IVS Real-Time Streaming User Guide*.

## Syntax
<a name="aws-resource-ivs-publickey-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ivs-publickey-syntax.json"></a>

```
{
  "Type" : "AWS::IVS::PublicKey",
  "Properties" : {
      "[Name](#cfn-ivs-publickey-name)" : {{String}},
      "[PublicKeyMaterial](#cfn-ivs-publickey-publickeymaterial)" : {{String}},
      "[Tags](#cfn-ivs-publickey-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-ivs-publickey-syntax.yaml"></a>

```
Type: AWS::IVS::PublicKey
Properties:
  [Name](#cfn-ivs-publickey-name): {{String}}
  [PublicKeyMaterial](#cfn-ivs-publickey-publickeymaterial): {{String}}
  [Tags](#cfn-ivs-publickey-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-ivs-publickey-properties"></a>

`Name`  <a name="cfn-ivs-publickey-name"></a>
Public key name. The value does not need to be unique.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9-_]*$`
*Minimum*: `0`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PublicKeyMaterial`  <a name="cfn-ivs-publickey-publickeymaterial"></a>
The public portion of a customer-generated key pair. Note that this field is required to create the AWS::IVS::PublicKey resource.
*Required*: No
*Type*: String
*Pattern*: `-----BEGIN PUBLIC KEY-----\r?\n([a-zA-Z0-9+/=\r\n]+)\r?\n-----END PUBLIC KEY-----(\r?\n)?`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-ivs-publickey-tags"></a>
An array of key-value pairs to apply to this resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-ivs-publickey-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ivs-publickey-return-values"></a>

### Ref
<a name="aws-resource-ivs-publickey-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the public key ARN. For example:

 `{ "Ref": "myPublicKey" }`

For the Amazon IVS public key `myPublicKey`, `Ref` returns the public key ARN.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ivs-publickey-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ivs-publickey-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The public key ARN. For example: `arn:aws:ivs:us-west-2:123456789012:public-key/abcdABCDefgh`

`Fingerprint`  <a name="Fingerprint-fn::getatt"></a>
The public key identifier. For example: `98:0d:1a:a0:19:96:1e:ea:0a:0a:2c:9a:42:19:2b:e7`

## Examples
<a name="aws-resource-ivs-publickey--examples"></a>

### PublicKey Template Examples
<a name="aws-resource-ivs-publickey--examples--PublicKey_Template_Examples"></a>

The following examples specify an Amazon IVS public key.

#### JSON
<a name="aws-resource-ivs-publickey--examples--PublicKey_Template_Examples--json"></a>

```
{
     "AWSTemplateFormatVersion": "2010-09-09",
     "Resources": {
         "PublicKey": {
             "Type": "AWS::IVS::PublicKey",
             "Properties": {
                 "PublicKeyMaterial": "-----BEGIN PUBLIC KEY-----\nMHYwEAYHKoZIzj0CAQYFK4EEACIDYgAEwOR43ETwEoWif1i14aL8GtDMNkT/kBQm\nh4sas9P//bjCU988rmQQXVBfftKT9xngg+W6hzOEpeUlCRlAtz6b6U79naYYRaSk\nK/UhYGWkXlbJlc9zn13imYWgVGe/BMFp\n-----END PUBLIC KEY-----\n",
                 "Name": "MyPublicKey",
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
<a name="aws-resource-ivs-publickey--examples--PublicKey_Template_Examples--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  PublicKey:
    Type: AWS::IVS::PublicKey
    Properties:
      PublicKeyMaterial: |
        -----BEGIN PUBLIC KEY-----
        MHYwEAYHKoZIzj0CAQYFK4EEACIDYgAEwOR43ETwEoWif1i14aL8GtDMNkT/kBQm
        h4sas9P//bjCU988rmQQXVBfftKT9xngg+W6hzOEpeUlCRlAtz6b6U79naYYRaSk
        K/UhYGWkXlbJlc9zn13imYWgVGe/BMFp
        -----END PUBLIC KEY-----
      Name: MyPublicKey
      Tags:
        - Key: MyKey
          Value: MyValue
```

## See also
<a name="aws-resource-ivs-publickey--seealso"></a>
+  [Distribute Participant Tokens](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/getting-started-distribute-tokens.html)
+ [PublicKey](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_PublicKey.html) data type
+ [ImportPublicKey](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_ImportPublicKey.html) API endpoint
