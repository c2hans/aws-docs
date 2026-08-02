---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geoapikeys_ListKeysResponseEntry.html
---

# ListKeysResponseEntry
<a name="API_geoapikeys_ListKeysResponseEntry"></a>

An API key resource listed in your AWS account.

## Contents
<a name="API_geoapikeys_ListKeysResponseEntry_Contents"></a>

 ** CreateTime **   <a name="location-Type-geoapikeys_ListKeysResponseEntry-CreateTime"></a>
The timestamp of when the API key was created, in [ ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sss`.
Type: Timestamp
Required: Yes

 ** ExpireTime **   <a name="location-Type-geoapikeys_ListKeysResponseEntry-ExpireTime"></a>
The timestamp for when the API key resource will expire, in [ ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sss`.
Type: Timestamp
Required: Yes

 ** KeyName **   <a name="location-Type-geoapikeys_ListKeysResponseEntry-KeyName"></a>
The name of the API key resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`
Required: Yes

 ** Restrictions **   <a name="location-Type-geoapikeys_ListKeysResponseEntry-Restrictions"></a>
API Restrictions on the allowed actions, resources, referers, Android apps, and Apple apps for an API key resource.
Type: [ApiKeyRestrictions](API_geoapikeys_ApiKeyRestrictions.md) object
Required: Yes

 ** UpdateTime **   <a name="location-Type-geoapikeys_ListKeysResponseEntry-UpdateTime"></a>
The timestamp of when the API key was last updated, in [ ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sss`.
Type: Timestamp
Required: Yes

 ** Description **   <a name="location-Type-geoapikeys_ListKeysResponseEntry-Description"></a>
The optional description for the API key resource.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

## See Also
<a name="API_geoapikeys_ListKeysResponseEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geoapikeys-2020-11-19/ListKeysResponseEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geoapikeys-2020-11-19/ListKeysResponseEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geoapikeys-2020-11-19/ListKeysResponseEntry)
