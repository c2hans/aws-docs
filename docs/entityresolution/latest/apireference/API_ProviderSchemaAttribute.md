---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_ProviderSchemaAttribute.html
---

# ProviderSchemaAttribute
<a name="API_ProviderSchemaAttribute"></a>

The provider schema attribute.

## Contents
<a name="API_ProviderSchemaAttribute_Contents"></a>

 ** fieldName **   <a name="API-Type-ProviderSchemaAttribute-fieldName"></a>
The field name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[a-zA-Z_0-9- ]*`
Required: Yes

 ** type **   <a name="API-Type-ProviderSchemaAttribute-type"></a>
The type of the provider schema attribute.
LiveRamp supports: `NAME` \| `NAME_FIRST` \| `NAME_MIDDLE` \| `NAME_LAST` \| `ADDRESS` \| `ADDRESS_STREET1` \| `ADDRESS_STREET2` \| `ADDRESS_STREET3` \| `ADDRESS_CITY` \| `ADDRESS_STATE` \| `ADDRESS_COUNTRY` \| `ADDRESS_POSTALCODE` \| `PHONE` \| `PHONE_NUMBER` \| `EMAIL_ADDRESS` \| `UNIQUE_ID` \| `PROVIDER_ID`
TransUnion supports: `NAME` \| `NAME_FIRST` \| `NAME_LAST` \| `ADDRESS` \| `ADDRESS_CITY` \| `ADDRESS_STATE` \| `ADDRESS_COUNTRY` \| `ADDRESS_POSTALCODE` \| `PHONE_NUMBER` \| `EMAIL_ADDRESS` \| `UNIQUE_ID` \| `DATE` \| `IPV4` \| `IPV6` \| `MAID`
Unified ID 2.0 supports: `PHONE_NUMBER` \| `EMAIL_ADDRESS` \| `UNIQUE_ID`
Type: String
Valid Values: `NAME | NAME_FIRST | NAME_MIDDLE | NAME_LAST | ADDRESS | ADDRESS_STREET1 | ADDRESS_STREET2 | ADDRESS_STREET3 | ADDRESS_CITY | ADDRESS_STATE | ADDRESS_COUNTRY | ADDRESS_POSTALCODE | PHONE | PHONE_NUMBER | PHONE_COUNTRYCODE | EMAIL_ADDRESS | UNIQUE_ID | DATE | STRING | PROVIDER_ID | IPV4 | IPV6 | MAID`
Required: Yes

 ** hashing **   <a name="API-Type-ProviderSchemaAttribute-hashing"></a>
The hashing attribute of the provider schema.
Type: Boolean
Required: No

 ** subType **   <a name="API-Type-ProviderSchemaAttribute-subType"></a>
The sub type of the provider schema attribute.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[a-zA-Z_0-9- ]*`
Required: No

## See Also
<a name="API_ProviderSchemaAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/ProviderSchemaAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/ProviderSchemaAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/ProviderSchemaAttribute)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Entity Resolution. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query entityresolution` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
