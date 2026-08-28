---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-connect-phonenumber.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::PhoneNumber
<a name="aws-resource-connect-phonenumber"></a>

Claims a phone number to the specified Connect Customer instance or traffic distribution group.

## Syntax
<a name="aws-resource-connect-phonenumber-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-connect-phonenumber-syntax.json"></a>

```
{
  "Type" : "AWS::Connect::PhoneNumber",
  "Properties" : {
      "[CountryCode](#cfn-connect-phonenumber-countrycode)" : {{String}},
      "[Description](#cfn-connect-phonenumber-description)" : {{String}},
      "[Prefix](#cfn-connect-phonenumber-prefix)" : {{String}},
      "[SourcePhoneNumberArn](#cfn-connect-phonenumber-sourcephonenumberarn)" : {{String}},
      "[Tags](#cfn-connect-phonenumber-tags)" : {{[ Tag, ... ]}},
      "[TargetArn](#cfn-connect-phonenumber-targetarn)" : {{String}},
      "[Type](#cfn-connect-phonenumber-type)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-connect-phonenumber-syntax.yaml"></a>

```
Type: AWS::Connect::PhoneNumber
Properties:
  [CountryCode](#cfn-connect-phonenumber-countrycode): {{String}}
  [Description](#cfn-connect-phonenumber-description): {{String}}
  [Prefix](#cfn-connect-phonenumber-prefix): {{String}}
  [SourcePhoneNumberArn](#cfn-connect-phonenumber-sourcephonenumberarn): {{String}}
  [Tags](#cfn-connect-phonenumber-tags): {{
    - Tag}}
  [TargetArn](#cfn-connect-phonenumber-targetarn): {{String}}
  [Type](#cfn-connect-phonenumber-type): {{String}}
```

## Properties
<a name="aws-resource-connect-phonenumber-properties"></a>

`CountryCode`  <a name="cfn-connect-phonenumber-countrycode"></a>
The ISO country code.
*Required*: No
*Type*: String
*Pattern*: `^[A-Z]{2}`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-connect-phonenumber-description"></a>
The description of the phone number.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Prefix`  <a name="cfn-connect-phonenumber-prefix"></a>
The prefix of the phone number. If provided, it must contain `+` as part of the country code.
*Pattern*: `^\\+[0-9]{1,15}`
*Required*: No
*Type*: String
*Pattern*: `^\+[0-9]{1,15}`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SourcePhoneNumberArn`  <a name="cfn-connect-phonenumber-sourcephonenumberarn"></a>
The claimed phone number ARN that was previously imported from the external service, such as AWS End User Messaging. If it is from AWS End User Messaging, it looks like the ARN of the phone number that was imported from AWS End User Messaging.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-connect-phonenumber-tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.
*Required*: No
*Type*: Array of [Tag](aws-properties-connect-phonenumber-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetArn`  <a name="cfn-connect-phonenumber-targetarn"></a>
The Amazon Resource Name (ARN) for Connect Customer instances or traffic distribution group that phone numbers are claimed to.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:(instance|traffic-distribution-group)/[-a-zA-Z0-9]*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-connect-phonenumber-type"></a>
The type of phone number.
*Required*: No
*Type*: String
*Pattern*: `TOLL_FREE|DID|UIFN|SHARED|THIRD_PARTY_DID|THIRD_PARTY_TF|SHORT_CODE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-connect-phonenumber-return-values"></a>

### Ref
<a name="aws-resource-connect-phonenumber-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the phone number. For example:

 `{ "Ref": "myPhoneNumber" }`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-connect-phonenumber-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-connect-phonenumber-return-values-fn--getatt-fn--getatt"></a>

`Address`  <a name="Address-fn::getatt"></a>
The phone number, in E.164 format.

`PhoneNumberArn`  <a name="PhoneNumberArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the phone number.

## Examples
<a name="aws-resource-connect-phonenumber--examples"></a>

### Specify a phone number resource
<a name="aws-resource-connect-phonenumber--examples--Specify_a_phone_number_resource"></a>

The following example specifies a phone number resource for an Connect Customer instance.

#### YAML
<a name="aws-resource-connect-phonenumber--examples--Specify_a_phone_number_resource--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
 Description: Specifies a phone number for Connect Customer instance
 Resources:
   PhoneNumber:
     Type: 'AWS::Connect::PhoneNumber'
     Properties:
       TargetArn: arn:aws:connect:region-name:aws-account-id:instance/instance-arn
       Description: phone number created using cfn
       Type: DID
       CountryCode: US
       Tags:
         - Key: testkey
           Value: testValue
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
