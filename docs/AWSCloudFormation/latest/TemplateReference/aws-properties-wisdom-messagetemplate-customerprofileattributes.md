---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-messagetemplate-customerprofileattributes.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::MessageTemplate CustomerProfileAttributes
<a name="aws-properties-wisdom-messagetemplate-customerprofileattributes"></a>

The customer profile attributes that are used with the message template.

## Syntax
<a name="aws-properties-wisdom-messagetemplate-customerprofileattributes-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-messagetemplate-customerprofileattributes-syntax.json"></a>

```
{
  "[AccountNumber](#cfn-wisdom-messagetemplate-customerprofileattributes-accountnumber)" : {{String}},
  "[AdditionalInformation](#cfn-wisdom-messagetemplate-customerprofileattributes-additionalinformation)" : {{String}},
  "[Address1](#cfn-wisdom-messagetemplate-customerprofileattributes-address1)" : {{String}},
  "[Address2](#cfn-wisdom-messagetemplate-customerprofileattributes-address2)" : {{String}},
  "[Address3](#cfn-wisdom-messagetemplate-customerprofileattributes-address3)" : {{String}},
  "[Address4](#cfn-wisdom-messagetemplate-customerprofileattributes-address4)" : {{String}},
  "[BillingAddress1](#cfn-wisdom-messagetemplate-customerprofileattributes-billingaddress1)" : {{String}},
  "[BillingAddress2](#cfn-wisdom-messagetemplate-customerprofileattributes-billingaddress2)" : {{String}},
  "[BillingAddress3](#cfn-wisdom-messagetemplate-customerprofileattributes-billingaddress3)" : {{String}},
  "[BillingAddress4](#cfn-wisdom-messagetemplate-customerprofileattributes-billingaddress4)" : {{String}},
  "[BillingCity](#cfn-wisdom-messagetemplate-customerprofileattributes-billingcity)" : {{String}},
  "[BillingCountry](#cfn-wisdom-messagetemplate-customerprofileattributes-billingcountry)" : {{String}},
  "[BillingCounty](#cfn-wisdom-messagetemplate-customerprofileattributes-billingcounty)" : {{String}},
  "[BillingPostalCode](#cfn-wisdom-messagetemplate-customerprofileattributes-billingpostalcode)" : {{String}},
  "[BillingProvince](#cfn-wisdom-messagetemplate-customerprofileattributes-billingprovince)" : {{String}},
  "[BillingState](#cfn-wisdom-messagetemplate-customerprofileattributes-billingstate)" : {{String}},
  "[BirthDate](#cfn-wisdom-messagetemplate-customerprofileattributes-birthdate)" : {{String}},
  "[BusinessEmailAddress](#cfn-wisdom-messagetemplate-customerprofileattributes-businessemailaddress)" : {{String}},
  "[BusinessName](#cfn-wisdom-messagetemplate-customerprofileattributes-businessname)" : {{String}},
  "[BusinessPhoneNumber](#cfn-wisdom-messagetemplate-customerprofileattributes-businessphonenumber)" : {{String}},
  "[City](#cfn-wisdom-messagetemplate-customerprofileattributes-city)" : {{String}},
  "[Country](#cfn-wisdom-messagetemplate-customerprofileattributes-country)" : {{String}},
  "[County](#cfn-wisdom-messagetemplate-customerprofileattributes-county)" : {{String}},
  "[Custom](#cfn-wisdom-messagetemplate-customerprofileattributes-custom)" : {{{{{Key}}: {{Value}}, ...}}},
  "[EmailAddress](#cfn-wisdom-messagetemplate-customerprofileattributes-emailaddress)" : {{String}},
  "[FirstName](#cfn-wisdom-messagetemplate-customerprofileattributes-firstname)" : {{String}},
  "[Gender](#cfn-wisdom-messagetemplate-customerprofileattributes-gender)" : {{String}},
  "[HomePhoneNumber](#cfn-wisdom-messagetemplate-customerprofileattributes-homephonenumber)" : {{String}},
  "[LastName](#cfn-wisdom-messagetemplate-customerprofileattributes-lastname)" : {{String}},
  "[MailingAddress1](#cfn-wisdom-messagetemplate-customerprofileattributes-mailingaddress1)" : {{String}},
  "[MailingAddress2](#cfn-wisdom-messagetemplate-customerprofileattributes-mailingaddress2)" : {{String}},
  "[MailingAddress3](#cfn-wisdom-messagetemplate-customerprofileattributes-mailingaddress3)" : {{String}},
  "[MailingAddress4](#cfn-wisdom-messagetemplate-customerprofileattributes-mailingaddress4)" : {{String}},
  "[MailingCity](#cfn-wisdom-messagetemplate-customerprofileattributes-mailingcity)" : {{String}},
  "[MailingCountry](#cfn-wisdom-messagetemplate-customerprofileattributes-mailingcountry)" : {{String}},
  "[MailingCounty](#cfn-wisdom-messagetemplate-customerprofileattributes-mailingcounty)" : {{String}},
  "[MailingPostalCode](#cfn-wisdom-messagetemplate-customerprofileattributes-mailingpostalcode)" : {{String}},
  "[MailingProvince](#cfn-wisdom-messagetemplate-customerprofileattributes-mailingprovince)" : {{String}},
  "[MailingState](#cfn-wisdom-messagetemplate-customerprofileattributes-mailingstate)" : {{String}},
  "[MiddleName](#cfn-wisdom-messagetemplate-customerprofileattributes-middlename)" : {{String}},
  "[MobilePhoneNumber](#cfn-wisdom-messagetemplate-customerprofileattributes-mobilephonenumber)" : {{String}},
  "[PartyType](#cfn-wisdom-messagetemplate-customerprofileattributes-partytype)" : {{String}},
  "[PhoneNumber](#cfn-wisdom-messagetemplate-customerprofileattributes-phonenumber)" : {{String}},
  "[PostalCode](#cfn-wisdom-messagetemplate-customerprofileattributes-postalcode)" : {{String}},
  "[ProfileARN](#cfn-wisdom-messagetemplate-customerprofileattributes-profilearn)" : {{String}},
  "[ProfileId](#cfn-wisdom-messagetemplate-customerprofileattributes-profileid)" : {{String}},
  "[Province](#cfn-wisdom-messagetemplate-customerprofileattributes-province)" : {{String}},
  "[ShippingAddress1](#cfn-wisdom-messagetemplate-customerprofileattributes-shippingaddress1)" : {{String}},
  "[ShippingAddress2](#cfn-wisdom-messagetemplate-customerprofileattributes-shippingaddress2)" : {{String}},
  "[ShippingAddress3](#cfn-wisdom-messagetemplate-customerprofileattributes-shippingaddress3)" : {{String}},
  "[ShippingAddress4](#cfn-wisdom-messagetemplate-customerprofileattributes-shippingaddress4)" : {{String}},
  "[ShippingCity](#cfn-wisdom-messagetemplate-customerprofileattributes-shippingcity)" : {{String}},
  "[ShippingCountry](#cfn-wisdom-messagetemplate-customerprofileattributes-shippingcountry)" : {{String}},
  "[ShippingCounty](#cfn-wisdom-messagetemplate-customerprofileattributes-shippingcounty)" : {{String}},
  "[ShippingPostalCode](#cfn-wisdom-messagetemplate-customerprofileattributes-shippingpostalcode)" : {{String}},
  "[ShippingProvince](#cfn-wisdom-messagetemplate-customerprofileattributes-shippingprovince)" : {{String}},
  "[ShippingState](#cfn-wisdom-messagetemplate-customerprofileattributes-shippingstate)" : {{String}},
  "[State](#cfn-wisdom-messagetemplate-customerprofileattributes-state)" : {{String}}
}
```

### YAML
<a name="aws-properties-wisdom-messagetemplate-customerprofileattributes-syntax.yaml"></a>

```
  [AccountNumber](#cfn-wisdom-messagetemplate-customerprofileattributes-accountnumber): {{String}}
  [AdditionalInformation](#cfn-wisdom-messagetemplate-customerprofileattributes-additionalinformation): {{String}}
  [Address1](#cfn-wisdom-messagetemplate-customerprofileattributes-address1): {{String}}
  [Address2](#cfn-wisdom-messagetemplate-customerprofileattributes-address2): {{String}}
  [Address3](#cfn-wisdom-messagetemplate-customerprofileattributes-address3): {{String}}
  [Address4](#cfn-wisdom-messagetemplate-customerprofileattributes-address4): {{String}}
  [BillingAddress1](#cfn-wisdom-messagetemplate-customerprofileattributes-billingaddress1): {{String}}
  [BillingAddress2](#cfn-wisdom-messagetemplate-customerprofileattributes-billingaddress2): {{String}}
  [BillingAddress3](#cfn-wisdom-messagetemplate-customerprofileattributes-billingaddress3): {{String}}
  [BillingAddress4](#cfn-wisdom-messagetemplate-customerprofileattributes-billingaddress4): {{String}}
  [BillingCity](#cfn-wisdom-messagetemplate-customerprofileattributes-billingcity): {{String}}
  [BillingCountry](#cfn-wisdom-messagetemplate-customerprofileattributes-billingcountry): {{String}}
  [BillingCounty](#cfn-wisdom-messagetemplate-customerprofileattributes-billingcounty): {{String}}
  [BillingPostalCode](#cfn-wisdom-messagetemplate-customerprofileattributes-billingpostalcode): {{String}}
  [BillingProvince](#cfn-wisdom-messagetemplate-customerprofileattributes-billingprovince): {{String}}
  [BillingState](#cfn-wisdom-messagetemplate-customerprofileattributes-billingstate): {{String}}
  [BirthDate](#cfn-wisdom-messagetemplate-customerprofileattributes-birthdate): {{String}}
  [BusinessEmailAddress](#cfn-wisdom-messagetemplate-customerprofileattributes-businessemailaddress): {{String}}
  [BusinessName](#cfn-wisdom-messagetemplate-customerprofileattributes-businessname): {{String}}
  [BusinessPhoneNumber](#cfn-wisdom-messagetemplate-customerprofileattributes-businessphonenumber): {{String}}
  [City](#cfn-wisdom-messagetemplate-customerprofileattributes-city): {{String}}
  [Country](#cfn-wisdom-messagetemplate-customerprofileattributes-country): {{String}}
  [County](#cfn-wisdom-messagetemplate-customerprofileattributes-county): {{String}}
  [Custom](#cfn-wisdom-messagetemplate-customerprofileattributes-custom): {{
    {{Key}}: {{Value}}}}
  [EmailAddress](#cfn-wisdom-messagetemplate-customerprofileattributes-emailaddress): {{String}}
  [FirstName](#cfn-wisdom-messagetemplate-customerprofileattributes-firstname): {{String}}
  [Gender](#cfn-wisdom-messagetemplate-customerprofileattributes-gender): {{String}}
  [HomePhoneNumber](#cfn-wisdom-messagetemplate-customerprofileattributes-homephonenumber): {{String}}
  [LastName](#cfn-wisdom-messagetemplate-customerprofileattributes-lastname): {{String}}
  [MailingAddress1](#cfn-wisdom-messagetemplate-customerprofileattributes-mailingaddress1): {{String}}
  [MailingAddress2](#cfn-wisdom-messagetemplate-customerprofileattributes-mailingaddress2): {{String}}
  [MailingAddress3](#cfn-wisdom-messagetemplate-customerprofileattributes-mailingaddress3): {{String}}
  [MailingAddress4](#cfn-wisdom-messagetemplate-customerprofileattributes-mailingaddress4): {{String}}
  [MailingCity](#cfn-wisdom-messagetemplate-customerprofileattributes-mailingcity): {{String}}
  [MailingCountry](#cfn-wisdom-messagetemplate-customerprofileattributes-mailingcountry): {{String}}
  [MailingCounty](#cfn-wisdom-messagetemplate-customerprofileattributes-mailingcounty): {{String}}
  [MailingPostalCode](#cfn-wisdom-messagetemplate-customerprofileattributes-mailingpostalcode): {{String}}
  [MailingProvince](#cfn-wisdom-messagetemplate-customerprofileattributes-mailingprovince): {{String}}
  [MailingState](#cfn-wisdom-messagetemplate-customerprofileattributes-mailingstate): {{String}}
  [MiddleName](#cfn-wisdom-messagetemplate-customerprofileattributes-middlename): {{String}}
  [MobilePhoneNumber](#cfn-wisdom-messagetemplate-customerprofileattributes-mobilephonenumber): {{String}}
  [PartyType](#cfn-wisdom-messagetemplate-customerprofileattributes-partytype): {{String}}
  [PhoneNumber](#cfn-wisdom-messagetemplate-customerprofileattributes-phonenumber): {{String}}
  [PostalCode](#cfn-wisdom-messagetemplate-customerprofileattributes-postalcode): {{String}}
  [ProfileARN](#cfn-wisdom-messagetemplate-customerprofileattributes-profilearn): {{String}}
  [ProfileId](#cfn-wisdom-messagetemplate-customerprofileattributes-profileid): {{String}}
  [Province](#cfn-wisdom-messagetemplate-customerprofileattributes-province): {{String}}
  [ShippingAddress1](#cfn-wisdom-messagetemplate-customerprofileattributes-shippingaddress1): {{String}}
  [ShippingAddress2](#cfn-wisdom-messagetemplate-customerprofileattributes-shippingaddress2): {{String}}
  [ShippingAddress3](#cfn-wisdom-messagetemplate-customerprofileattributes-shippingaddress3): {{String}}
  [ShippingAddress4](#cfn-wisdom-messagetemplate-customerprofileattributes-shippingaddress4): {{String}}
  [ShippingCity](#cfn-wisdom-messagetemplate-customerprofileattributes-shippingcity): {{String}}
  [ShippingCountry](#cfn-wisdom-messagetemplate-customerprofileattributes-shippingcountry): {{String}}
  [ShippingCounty](#cfn-wisdom-messagetemplate-customerprofileattributes-shippingcounty): {{String}}
  [ShippingPostalCode](#cfn-wisdom-messagetemplate-customerprofileattributes-shippingpostalcode): {{String}}
  [ShippingProvince](#cfn-wisdom-messagetemplate-customerprofileattributes-shippingprovince): {{String}}
  [ShippingState](#cfn-wisdom-messagetemplate-customerprofileattributes-shippingstate): {{String}}
  [State](#cfn-wisdom-messagetemplate-customerprofileattributes-state): {{String}}
```

## Properties
<a name="aws-properties-wisdom-messagetemplate-customerprofileattributes-properties"></a>

`AccountNumber`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-accountnumber"></a>
A unique account number that you have given to the customer.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AdditionalInformation`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-additionalinformation"></a>
Any additional information relevant to the customer's profile.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Address1`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-address1"></a>
The first line of a customer address.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Address2`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-address2"></a>
The second line of a customer address.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Address3`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-address3"></a>
The third line of a customer address.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Address4`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-address4"></a>
The fourth line of a customer address.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BillingAddress1`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-billingaddress1"></a>
The first line of a customer’s billing address.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BillingAddress2`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-billingaddress2"></a>
The second line of a customer’s billing address.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BillingAddress3`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-billingaddress3"></a>
The third line of a customer’s billing address.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BillingAddress4`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-billingaddress4"></a>
The fourth line of a customer’s billing address.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BillingCity`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-billingcity"></a>
The city of a customer’s billing address.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BillingCountry`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-billingcountry"></a>
The country of a customer’s billing address.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BillingCounty`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-billingcounty"></a>
The county of a customer’s billing address.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BillingPostalCode`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-billingpostalcode"></a>
The postal code of a customer’s billing address.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BillingProvince`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-billingprovince"></a>
The province of a customer’s billing address.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BillingState`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-billingstate"></a>
The state of a customer’s billing address.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BirthDate`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-birthdate"></a>
The customer's birth date.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BusinessEmailAddress`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-businessemailaddress"></a>
The customer's business email address.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BusinessName`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-businessname"></a>
The name of the customer's business.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BusinessPhoneNumber`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-businessphonenumber"></a>
The customer's business phone number.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`City`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-city"></a>
The city in which a customer lives.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Country`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-country"></a>
The country in which a customer lives.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`County`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-county"></a>
The county in which a customer lives.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Custom`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-custom"></a>
The custom attributes in customer profile attributes.
*Required*: No
*Type*: Object of String
*Pattern*: `^[a-zA-Z0-9\s._:/=+@-]*$`
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EmailAddress`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-emailaddress"></a>
The customer's email address, which has not been specified as a personal or business address.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FirstName`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-firstname"></a>
The customer's first name.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Gender`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-gender"></a>
The customer's gender.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HomePhoneNumber`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-homephonenumber"></a>
The customer's mobile phone number.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LastName`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-lastname"></a>
The customer's last name.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MailingAddress1`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-mailingaddress1"></a>
The first line of a customer’s mailing address.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MailingAddress2`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-mailingaddress2"></a>
The second line of a customer’s mailing address.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MailingAddress3`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-mailingaddress3"></a>
The third line of a customer’s mailing address.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MailingAddress4`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-mailingaddress4"></a>
The fourth line of a customer’s mailing address.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MailingCity`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-mailingcity"></a>
The city of a customer’s mailing address.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MailingCountry`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-mailingcountry"></a>
The country of a customer’s mailing address.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MailingCounty`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-mailingcounty"></a>
The county of a customer’s mailing address.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MailingPostalCode`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-mailingpostalcode"></a>
The postal code of a customer’s mailing address.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MailingProvince`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-mailingprovince"></a>
The province of a customer’s mailing address.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MailingState`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-mailingstate"></a>
The state of a customer’s mailing address.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MiddleName`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-middlename"></a>
The customer's middle name.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MobilePhoneNumber`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-mobilephonenumber"></a>
The customer's mobile phone number.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PartyType`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-partytype"></a>
The customer's party type.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PhoneNumber`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-phonenumber"></a>
The customer's phone number, which has not been specified as a mobile, home, or business number.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PostalCode`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-postalcode"></a>
The postal code of a customer address.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProfileARN`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-profilearn"></a>
The ARN of a customer profile.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProfileId`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-profileid"></a>
The unique identifier of a customer profile.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Province`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-province"></a>
The province in which a customer lives.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShippingAddress1`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-shippingaddress1"></a>
The first line of a customer’s shipping address.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShippingAddress2`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-shippingaddress2"></a>
The second line of a customer’s shipping address.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShippingAddress3`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-shippingaddress3"></a>
The third line of a customer’s shipping address.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShippingAddress4`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-shippingaddress4"></a>
The fourth line of a customer’s shipping address.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShippingCity`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-shippingcity"></a>
The city of a customer’s shipping address.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShippingCountry`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-shippingcountry"></a>
The country of a customer’s shipping address.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShippingCounty`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-shippingcounty"></a>
The county of a customer’s shipping address.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShippingPostalCode`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-shippingpostalcode"></a>
The postal code of a customer’s shipping address.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShippingProvince`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-shippingprovince"></a>
The province of a customer’s shipping address.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShippingState`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-shippingstate"></a>
The state of a customer’s shipping address.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`State`  <a name="cfn-wisdom-messagetemplate-customerprofileattributes-state"></a>
The state in which a customer lives.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32767`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
