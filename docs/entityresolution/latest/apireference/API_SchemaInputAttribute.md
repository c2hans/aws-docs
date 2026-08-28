---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_SchemaInputAttribute.html
---

# SchemaInputAttribute
<a name="API_SchemaInputAttribute"></a>

A configuration object for defining input data fields in AWS Entity Resolution. The `SchemaInputAttribute` specifies how individual fields in your input data should be processed and matched.

## Contents
<a name="API_SchemaInputAttribute_Contents"></a>

 ** fieldName **   <a name="API-Type-SchemaInputAttribute-fieldName"></a>
A string containing the field name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[a-zA-Z_0-9- ]*`
Required: Yes

 ** type **   <a name="API-Type-SchemaInputAttribute-type"></a>
The type of the attribute, selected from a list of values.
LiveRamp supports: `NAME` \| `NAME_FIRST` \| `NAME_MIDDLE` \| `NAME_LAST` \| `ADDRESS` \| `ADDRESS_STREET1` \| `ADDRESS_STREET2` \| `ADDRESS_STREET3` \| `ADDRESS_CITY` \| `ADDRESS_STATE` \| `ADDRESS_COUNTRY` \| `ADDRESS_POSTALCODE` \| `PHONE` \| `PHONE_NUMBER` \| `EMAIL_ADDRESS` \| `UNIQUE_ID` \| `PROVIDER_ID`
TransUnion supports: `NAME` \| `NAME_FIRST` \| `NAME_LAST` \| `ADDRESS` \| `ADDRESS_CITY` \| `ADDRESS_STATE` \| `ADDRESS_COUNTRY` \| `ADDRESS_POSTALCODE` \| `PHONE_NUMBER` \| `EMAIL_ADDRESS` \| `UNIQUE_ID` \| `IPV4` \| `IPV6` \| `MAID`
Unified ID 2.0 supports: `PHONE_NUMBER` \| `EMAIL_ADDRESS` \| `UNIQUE_ID`
Normalization is only supported for `NAME`, `ADDRESS`, `PHONE`, and `EMAIL_ADDRESS`.
If you want to normalize `NAME_FIRST`, `NAME_MIDDLE`, and `NAME_LAST`, you must group them by assigning them to the `NAME` `groupName`.
If you want to normalize `ADDRESS_STREET1`, `ADDRESS_STREET2`, `ADDRESS_STREET3`, `ADDRESS_CITY`, `ADDRESS_STATE`, `ADDRESS_COUNTRY`, and `ADDRESS_POSTALCODE`, you must group them by assigning them to the `ADDRESS` `groupName`.
If you want to normalize `PHONE_NUMBER` and `PHONE_COUNTRYCODE`, you must group them by assigning them to the `PHONE` `groupName`.
Type: String
Valid Values: `NAME | NAME_FIRST | NAME_MIDDLE | NAME_LAST | ADDRESS | ADDRESS_STREET1 | ADDRESS_STREET2 | ADDRESS_STREET3 | ADDRESS_CITY | ADDRESS_STATE | ADDRESS_COUNTRY | ADDRESS_POSTALCODE | PHONE | PHONE_NUMBER | PHONE_COUNTRYCODE | EMAIL_ADDRESS | UNIQUE_ID | DATE | STRING | PROVIDER_ID | IPV4 | IPV6 | MAID`
Required: Yes

 ** groupName **   <a name="API-Type-SchemaInputAttribute-groupName"></a>
A string that instructs AWS Entity Resolution to combine several columns into a unified column with the identical attribute type.
For example, when working with columns such as `NAME_FIRST`, `NAME_MIDDLE`, and `NAME_LAST`, assigning them a common `groupName` will prompt AWS Entity Resolution to concatenate them into a single value.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[a-zA-Z_0-9- ]*`
Required: No

 ** hashed **   <a name="API-Type-SchemaInputAttribute-hashed"></a>
 Indicates if the column values are hashed in the schema input.
If the value is set to `TRUE`, the column values are hashed.
If the value is set to `FALSE`, the column values are cleartext.
Type: Boolean
Required: No

 ** matchKey **   <a name="API-Type-SchemaInputAttribute-matchKey"></a>
A key that allows grouping of multiple input attributes into a unified matching group.
For example, consider a scenario where the source table contains various addresses, such as `business_address` and `shipping_address`. By assigning a `matchKey` called `address` to both attributes, AWS Entity Resolution will match records across these fields to create a consolidated matching group.
If no `matchKey` is specified for a column, it won't be utilized for matching purposes but will still be included in the output table.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[a-zA-Z_0-9- ]*`
Required: No

 ** subType **   <a name="API-Type-SchemaInputAttribute-subType"></a>
The subtype of the attribute, selected from a list of values.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[a-zA-Z_0-9- ]*`
Required: No

## See Also
<a name="API_SchemaInputAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/SchemaInputAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/SchemaInputAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/SchemaInputAttribute)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Entity Resolution. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query entityresolution` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
