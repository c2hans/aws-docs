---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_SecurityProfile.html
---

# SecurityProfile
<a name="API_SecurityProfile"></a>

Contains information about a security profile.

## Contents
<a name="API_SecurityProfile_Contents"></a>

 ** AllowedAccessControlHierarchyGroupId **   <a name="connect-Type-SecurityProfile-AllowedAccessControlHierarchyGroupId"></a>
The identifier of the hierarchy group that a security profile uses to restrict access to resources in Connect Customer.
Type: String
Required: No

 ** AllowedAccessControlTags **   <a name="connect-Type-SecurityProfile-AllowedAccessControlTags"></a>
The list of tags that a security profile uses to restrict access to resources in Connect Customer.
Type: String to string map
Map Entries: Maximum number of 4 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Maximum length of 256.
Required: No

 ** Arn **   <a name="connect-Type-SecurityProfile-Arn"></a>
The Amazon Resource Name (ARN) for the security profile.
Type: String
Required: No

 ** Description **   <a name="connect-Type-SecurityProfile-Description"></a>
The description of the security profile.
Type: String
Length Constraints: Maximum length of 250.
Required: No

 ** GranularAccessControlConfiguration **   <a name="connect-Type-SecurityProfile-GranularAccessControlConfiguration"></a>
The granular access control configuration for the security profile, including data table permissions.
Type: [GranularAccessControlConfiguration](API_GranularAccessControlConfiguration.md) object
Required: No

 ** HierarchyRestrictedResources **   <a name="connect-Type-SecurityProfile-HierarchyRestrictedResources"></a>
The list of resources that a security profile applies hierarchy restrictions to in Connect Customer. Following are acceptable ResourceNames: `User`.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** Id **   <a name="connect-Type-SecurityProfile-Id"></a>
The identifier for the security profile.
Type: String
Required: No

 ** LastModifiedRegion **   <a name="connect-Type-SecurityProfile-LastModifiedRegion"></a>
The AWS Region where this resource was last modified.
Type: String
Pattern: `[a-z]{2}(-[a-z]+){1,2}(-[0-9])?`
Required: No

 ** LastModifiedTime **   <a name="connect-Type-SecurityProfile-LastModifiedTime"></a>
The timestamp when this resource was last modified.
Type: Timestamp
Required: No

 ** OrganizationResourceId **   <a name="connect-Type-SecurityProfile-OrganizationResourceId"></a>
The organization resource identifier for the security profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** SecurityProfileName **   <a name="connect-Type-SecurityProfile-SecurityProfileName"></a>
The name for the security profile.
Type: String
Required: No

 ** TagRestrictedResources **   <a name="connect-Type-SecurityProfile-TagRestrictedResources"></a>
The list of resources that a security profile applies tag restrictions to in Connect Customer.
Type: Array of strings
Array Members: Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** Tags **   <a name="connect-Type-SecurityProfile-Tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_SecurityProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/SecurityProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/SecurityProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/SecurityProfile)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
