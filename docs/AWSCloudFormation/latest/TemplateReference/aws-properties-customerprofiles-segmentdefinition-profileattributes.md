---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-segmentdefinition-profileattributes.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::SegmentDefinition ProfileAttributes
<a name="aws-properties-customerprofiles-segmentdefinition-profileattributes"></a>

The object used to segment on attributes within the customer profile.

## Syntax
<a name="aws-properties-customerprofiles-segmentdefinition-profileattributes-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-segmentdefinition-profileattributes-syntax.json"></a>

```
{
  "[AccountNumber](#cfn-customerprofiles-segmentdefinition-profileattributes-accountnumber)" : {{ProfileDimension}},
  "[AdditionalInformation](#cfn-customerprofiles-segmentdefinition-profileattributes-additionalinformation)" : {{ExtraLengthValueProfileDimension}},
  "[Address](#cfn-customerprofiles-segmentdefinition-profileattributes-address)" : {{AddressDimension}},
  "[Attributes](#cfn-customerprofiles-segmentdefinition-profileattributes-attributes)" : {{{{{Key}}: {{Value}}, ...}}},
  "[BillingAddress](#cfn-customerprofiles-segmentdefinition-profileattributes-billingaddress)" : {{AddressDimension}},
  "[BirthDate](#cfn-customerprofiles-segmentdefinition-profileattributes-birthdate)" : {{DateDimension}},
  "[BusinessEmailAddress](#cfn-customerprofiles-segmentdefinition-profileattributes-businessemailaddress)" : {{ProfileDimension}},
  "[BusinessName](#cfn-customerprofiles-segmentdefinition-profileattributes-businessname)" : {{ProfileDimension}},
  "[BusinessPhoneNumber](#cfn-customerprofiles-segmentdefinition-profileattributes-businessphonenumber)" : {{ProfileDimension}},
  "[EmailAddress](#cfn-customerprofiles-segmentdefinition-profileattributes-emailaddress)" : {{ProfileDimension}},
  "[FirstName](#cfn-customerprofiles-segmentdefinition-profileattributes-firstname)" : {{ProfileDimension}},
  "[GenderString](#cfn-customerprofiles-segmentdefinition-profileattributes-genderstring)" : {{ProfileDimension}},
  "[HomePhoneNumber](#cfn-customerprofiles-segmentdefinition-profileattributes-homephonenumber)" : {{ProfileDimension}},
  "[LastName](#cfn-customerprofiles-segmentdefinition-profileattributes-lastname)" : {{ProfileDimension}},
  "[MailingAddress](#cfn-customerprofiles-segmentdefinition-profileattributes-mailingaddress)" : {{AddressDimension}},
  "[MiddleName](#cfn-customerprofiles-segmentdefinition-profileattributes-middlename)" : {{ProfileDimension}},
  "[MobilePhoneNumber](#cfn-customerprofiles-segmentdefinition-profileattributes-mobilephonenumber)" : {{ProfileDimension}},
  "[PartyTypeString](#cfn-customerprofiles-segmentdefinition-profileattributes-partytypestring)" : {{ProfileDimension}},
  "[PersonalEmailAddress](#cfn-customerprofiles-segmentdefinition-profileattributes-personalemailaddress)" : {{ProfileDimension}},
  "[PhoneNumber](#cfn-customerprofiles-segmentdefinition-profileattributes-phonenumber)" : {{ProfileDimension}},
  "[ProfileType](#cfn-customerprofiles-segmentdefinition-profileattributes-profiletype)" : {{ProfileTypeDimension}},
  "[ShippingAddress](#cfn-customerprofiles-segmentdefinition-profileattributes-shippingaddress)" : {{AddressDimension}}
}
```

### YAML
<a name="aws-properties-customerprofiles-segmentdefinition-profileattributes-syntax.yaml"></a>

```
  [AccountNumber](#cfn-customerprofiles-segmentdefinition-profileattributes-accountnumber): {{
    ProfileDimension}}
  [AdditionalInformation](#cfn-customerprofiles-segmentdefinition-profileattributes-additionalinformation): {{
    ExtraLengthValueProfileDimension}}
  [Address](#cfn-customerprofiles-segmentdefinition-profileattributes-address): {{
    AddressDimension}}
  [Attributes](#cfn-customerprofiles-segmentdefinition-profileattributes-attributes): {{
    {{Key}}: {{Value}}}}
  [BillingAddress](#cfn-customerprofiles-segmentdefinition-profileattributes-billingaddress): {{
    AddressDimension}}
  [BirthDate](#cfn-customerprofiles-segmentdefinition-profileattributes-birthdate): {{
    DateDimension}}
  [BusinessEmailAddress](#cfn-customerprofiles-segmentdefinition-profileattributes-businessemailaddress): {{
    ProfileDimension}}
  [BusinessName](#cfn-customerprofiles-segmentdefinition-profileattributes-businessname): {{
    ProfileDimension}}
  [BusinessPhoneNumber](#cfn-customerprofiles-segmentdefinition-profileattributes-businessphonenumber): {{
    ProfileDimension}}
  [EmailAddress](#cfn-customerprofiles-segmentdefinition-profileattributes-emailaddress): {{
    ProfileDimension}}
  [FirstName](#cfn-customerprofiles-segmentdefinition-profileattributes-firstname): {{
    ProfileDimension}}
  [GenderString](#cfn-customerprofiles-segmentdefinition-profileattributes-genderstring): {{
    ProfileDimension}}
  [HomePhoneNumber](#cfn-customerprofiles-segmentdefinition-profileattributes-homephonenumber): {{
    ProfileDimension}}
  [LastName](#cfn-customerprofiles-segmentdefinition-profileattributes-lastname): {{
    ProfileDimension}}
  [MailingAddress](#cfn-customerprofiles-segmentdefinition-profileattributes-mailingaddress): {{
    AddressDimension}}
  [MiddleName](#cfn-customerprofiles-segmentdefinition-profileattributes-middlename): {{
    ProfileDimension}}
  [MobilePhoneNumber](#cfn-customerprofiles-segmentdefinition-profileattributes-mobilephonenumber): {{
    ProfileDimension}}
  [PartyTypeString](#cfn-customerprofiles-segmentdefinition-profileattributes-partytypestring): {{
    ProfileDimension}}
  [PersonalEmailAddress](#cfn-customerprofiles-segmentdefinition-profileattributes-personalemailaddress): {{
    ProfileDimension}}
  [PhoneNumber](#cfn-customerprofiles-segmentdefinition-profileattributes-phonenumber): {{
    ProfileDimension}}
  [ProfileType](#cfn-customerprofiles-segmentdefinition-profileattributes-profiletype): {{
    ProfileTypeDimension}}
  [ShippingAddress](#cfn-customerprofiles-segmentdefinition-profileattributes-shippingaddress): {{
    AddressDimension}}
```

## Properties
<a name="aws-properties-customerprofiles-segmentdefinition-profileattributes-properties"></a>

`AccountNumber`  <a name="cfn-customerprofiles-segmentdefinition-profileattributes-accountnumber"></a>
A field to describe values to segment on within account number.
*Required*: No
*Type*: [ProfileDimension](aws-properties-customerprofiles-segmentdefinition-profiledimension.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AdditionalInformation`  <a name="cfn-customerprofiles-segmentdefinition-profileattributes-additionalinformation"></a>
A field to describe values to segment on within additional information.
*Required*: No
*Type*: [ExtraLengthValueProfileDimension](aws-properties-customerprofiles-segmentdefinition-extralengthvalueprofiledimension.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Address`  <a name="cfn-customerprofiles-segmentdefinition-profileattributes-address"></a>
A field to describe values to segment on within address.
*Required*: No
*Type*: [AddressDimension](aws-properties-customerprofiles-segmentdefinition-addressdimension.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Attributes`  <a name="cfn-customerprofiles-segmentdefinition-profileattributes-attributes"></a>
A field to describe values to segment on within attributes.
*Required*: No
*Type*: Object of [AttributeDimension](aws-properties-customerprofiles-segmentdefinition-attributedimension.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`BillingAddress`  <a name="cfn-customerprofiles-segmentdefinition-profileattributes-billingaddress"></a>
A field to describe values to segment on within billing address.
*Required*: No
*Type*: [AddressDimension](aws-properties-customerprofiles-segmentdefinition-addressdimension.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`BirthDate`  <a name="cfn-customerprofiles-segmentdefinition-profileattributes-birthdate"></a>
A field to describe values to segment on within birthDate.
*Required*: No
*Type*: [DateDimension](aws-properties-customerprofiles-segmentdefinition-datedimension.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`BusinessEmailAddress`  <a name="cfn-customerprofiles-segmentdefinition-profileattributes-businessemailaddress"></a>
A field to describe values to segment on within business email address.
*Required*: No
*Type*: [ProfileDimension](aws-properties-customerprofiles-segmentdefinition-profiledimension.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`BusinessName`  <a name="cfn-customerprofiles-segmentdefinition-profileattributes-businessname"></a>
A field to describe values to segment on within business name.
*Required*: No
*Type*: [ProfileDimension](aws-properties-customerprofiles-segmentdefinition-profiledimension.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`BusinessPhoneNumber`  <a name="cfn-customerprofiles-segmentdefinition-profileattributes-businessphonenumber"></a>
A field to describe values to segment on within business phone number.
*Required*: No
*Type*: [ProfileDimension](aws-properties-customerprofiles-segmentdefinition-profiledimension.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EmailAddress`  <a name="cfn-customerprofiles-segmentdefinition-profileattributes-emailaddress"></a>
A field to describe values to segment on within email address.
*Required*: No
*Type*: [ProfileDimension](aws-properties-customerprofiles-segmentdefinition-profiledimension.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FirstName`  <a name="cfn-customerprofiles-segmentdefinition-profileattributes-firstname"></a>
A field to describe values to segment on within first name.
*Required*: No
*Type*: [ProfileDimension](aws-properties-customerprofiles-segmentdefinition-profiledimension.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`GenderString`  <a name="cfn-customerprofiles-segmentdefinition-profileattributes-genderstring"></a>
A field to describe values to segment on within genderString.
*Required*: No
*Type*: [ProfileDimension](aws-properties-customerprofiles-segmentdefinition-profiledimension.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`HomePhoneNumber`  <a name="cfn-customerprofiles-segmentdefinition-profileattributes-homephonenumber"></a>
A field to describe values to segment on within home phone number.
*Required*: No
*Type*: [ProfileDimension](aws-properties-customerprofiles-segmentdefinition-profiledimension.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LastName`  <a name="cfn-customerprofiles-segmentdefinition-profileattributes-lastname"></a>
A field to describe values to segment on within last name.
*Required*: No
*Type*: [ProfileDimension](aws-properties-customerprofiles-segmentdefinition-profiledimension.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MailingAddress`  <a name="cfn-customerprofiles-segmentdefinition-profileattributes-mailingaddress"></a>
A field to describe values to segment on within mailing address.
*Required*: No
*Type*: [AddressDimension](aws-properties-customerprofiles-segmentdefinition-addressdimension.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MiddleName`  <a name="cfn-customerprofiles-segmentdefinition-profileattributes-middlename"></a>
A field to describe values to segment on within middle name.
*Required*: No
*Type*: [ProfileDimension](aws-properties-customerprofiles-segmentdefinition-profiledimension.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MobilePhoneNumber`  <a name="cfn-customerprofiles-segmentdefinition-profileattributes-mobilephonenumber"></a>
A field to describe values to segment on within mobile phone number.
*Required*: No
*Type*: [ProfileDimension](aws-properties-customerprofiles-segmentdefinition-profiledimension.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PartyTypeString`  <a name="cfn-customerprofiles-segmentdefinition-profileattributes-partytypestring"></a>
A field to describe values to segment on within partyTypeString.
*Required*: No
*Type*: [ProfileDimension](aws-properties-customerprofiles-segmentdefinition-profiledimension.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PersonalEmailAddress`  <a name="cfn-customerprofiles-segmentdefinition-profileattributes-personalemailaddress"></a>
A field to describe values to segment on within personal email address.
*Required*: No
*Type*: [ProfileDimension](aws-properties-customerprofiles-segmentdefinition-profiledimension.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PhoneNumber`  <a name="cfn-customerprofiles-segmentdefinition-profileattributes-phonenumber"></a>
A field to describe values to segment on within phone number.
*Required*: No
*Type*: [ProfileDimension](aws-properties-customerprofiles-segmentdefinition-profiledimension.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ProfileType`  <a name="cfn-customerprofiles-segmentdefinition-profileattributes-profiletype"></a>
The type of profile.
*Required*: No
*Type*: [ProfileTypeDimension](aws-properties-customerprofiles-segmentdefinition-profiletypedimension.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ShippingAddress`  <a name="cfn-customerprofiles-segmentdefinition-profileattributes-shippingaddress"></a>
A field to describe values to segment on within shipping address.
*Required*: No
*Type*: [AddressDimension](aws-properties-customerprofiles-segmentdefinition-addressdimension.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
