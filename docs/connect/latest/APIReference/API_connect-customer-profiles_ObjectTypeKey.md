---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_ObjectTypeKey.html
---

# ObjectTypeKey
<a name="API_connect-customer-profiles_ObjectTypeKey"></a>

An object that defines the Key element of a ProfileObject. A Key is a special element that can be used to search for a customer profile.

## Contents
<a name="API_connect-customer-profiles_ObjectTypeKey_Contents"></a>

 ** FieldNames **   <a name="connect-Type-connect-customer-profiles_ObjectTypeKey-FieldNames"></a>
The reference for the key name of the fields map.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: No

 ** StandardIdentifiers **   <a name="connect-Type-connect-customer-profiles_ObjectTypeKey-StandardIdentifiers"></a>
The types of keys that a ProfileObject can have. Each ProfileObject can have only 1 UNIQUE key but multiple PROFILE keys. PROFILE, ASSET, CASE, or ORDER means that this key can be used to tie an object to a PROFILE, ASSET, CASE, or ORDER respectively. UNIQUE means that it can be used to uniquely identify an object. If a key a is marked as SECONDARY, it will be used to search for profiles after all other PROFILE keys have been searched. A LOOKUP\_ONLY key is only used to match a profile but is not persisted to be used for searching of the profile. A NEW\_ONLY key is only used if the profile does not already exist before the object is ingested, otherwise it is only used for matching objects to profiles.
Type: Array of strings
Valid Values: `PROFILE | ASSET | CASE | DEVICE | WEB_ANALYTICS | ORDER | COMMUNICATION_RECORD | AIR_PREFERENCE | HOTEL_PREFERENCE | AIR_BOOKING | AIR_SEGMENT | HOTEL_RESERVATION | HOTEL_STAY_REVENUE | LOYALTY | LOYALTY_TRANSACTION | LOYALTY_PROMOTION | UNIQUE | SECONDARY | LOOKUP_ONLY | NEW_ONLY`
Required: No

## See Also
<a name="API_connect-customer-profiles_ObjectTypeKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/ObjectTypeKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/ObjectTypeKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/ObjectTypeKey)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
