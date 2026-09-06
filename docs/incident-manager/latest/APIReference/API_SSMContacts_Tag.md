---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_Tag.html
---

# Tag
<a name="API_SSMContacts_Tag"></a>

A container of a key-value name pair.

## Contents
<a name="API_SSMContacts_Tag_Contents"></a>

 ** Key **   <a name="IncidentManager-Type-SSMContacts_Tag-Key"></a>
Name of the object key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[\\\/a-zA-Z0-9_+=\-]*$`
Required: No

 ** Value **   <a name="IncidentManager-Type-SSMContacts_Tag-Value"></a>
Value of the tag.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[\p{L}\p{Z}\p{N}_.:\/=+\-@]*$`
Required: No

## See Also
<a name="API_SSMContacts_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-contacts-2021-05-03/Tag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-contacts-2021-05-03/Tag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-contacts-2021-05-03/Tag)
