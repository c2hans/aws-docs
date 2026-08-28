---
source_url: https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_InstanceProperty.html
---

# InstanceProperty
<a name="API_InstanceProperty"></a>

A key-value pair you set that identifies a property of the authenticating instance.

## Contents
<a name="API_InstanceProperty_Contents"></a>

 ** failed **   <a name="rolesanywhere-Type-InstanceProperty-failed"></a>
Indicates whether the temporary credential request was successful.
Type: Boolean
Required: No

 ** properties **   <a name="rolesanywhere-Type-InstanceProperty-properties"></a>
A list of instanceProperty objects.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 200.
Value Length Constraints: Minimum length of 1. Maximum length of 200.
Required: No

 ** seenAt **   <a name="rolesanywhere-Type-InstanceProperty-seenAt"></a>
The ISO-8601 time stamp of when the certificate was last used in a temporary credential request.
Type: Timestamp
Required: No

## See Also
<a name="API_InstanceProperty_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rolesanywhere-2018-05-10/InstanceProperty)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rolesanywhere-2018-05-10/InstanceProperty)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rolesanywhere-2018-05-10/InstanceProperty)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IAM Roles Anywhere. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rolesanywhere` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
