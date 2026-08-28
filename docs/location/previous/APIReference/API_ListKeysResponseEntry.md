---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_ListKeysResponseEntry.html
---

# ListKeysResponseEntry
<a name="API_ListKeysResponseEntry"></a>

An API key resource listed in your AWS account.

## Contents
<a name="API_ListKeysResponseEntry_Contents"></a>

 ** CreateTime **   <a name="location-Type-ListKeysResponseEntry-CreateTime"></a>
The timestamp of when the API key was created, in [ ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ`.
Type: Timestamp
Required: Yes

 ** ExpireTime **   <a name="location-Type-ListKeysResponseEntry-ExpireTime"></a>
The timestamp for when the API key resource will expire, in [ ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ`.
Type: Timestamp
Required: Yes

 ** KeyName **   <a name="location-Type-ListKeysResponseEntry-KeyName"></a>
The name of the API key resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`
Required: Yes

 ** Restrictions **   <a name="location-Type-ListKeysResponseEntry-Restrictions"></a>
API Restrictions on the allowed actions, resources, and referers for an API key resource.
Type: [ApiKeyRestrictions](API_ApiKeyRestrictions.md) object
Required: Yes

 ** UpdateTime **   <a name="location-Type-ListKeysResponseEntry-UpdateTime"></a>
The timestamp of when the API key was last updated, in [ ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ`.
Type: Timestamp
Required: Yes

 ** Description **   <a name="location-Type-ListKeysResponseEntry-Description"></a>
The optional description for the API key resource.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

## See Also
<a name="API_ListKeysResponseEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/ListKeysResponseEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/ListKeysResponseEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/ListKeysResponseEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
