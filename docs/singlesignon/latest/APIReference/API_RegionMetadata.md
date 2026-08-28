---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_RegionMetadata.html
---

# RegionMetadata
<a name="API_RegionMetadata"></a>

Contains information about an enabled Region of an IAM Identity Center instance, including the Region name, status, date added, and whether it is the primary Region.

## Contents
<a name="API_RegionMetadata_Contents"></a>

 ** AddedDate **   <a name="singlesignon-Type-RegionMetadata-AddedDate"></a>
The timestamp when the Region was added to the IAM Identity Center instance. For the primary Region, this is the instance creation time.
Type: Timestamp
Required: No

 ** IsPrimaryRegion **   <a name="singlesignon-Type-RegionMetadata-IsPrimaryRegion"></a>
Indicates whether this is the primary Region where the IAM Identity Center instance was originally enabled. The primary Region cannot be removed.
Type: Boolean
Required: No

 ** RegionName **   <a name="singlesignon-Type-RegionMetadata-RegionName"></a>
The AWS Region name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `([a-z]+-){2,3}\d`
Required: No

 ** Status **   <a name="singlesignon-Type-RegionMetadata-Status"></a>
The current status of the Region. Valid values are ACTIVE (Region is operational), ADDING (Region extension workflow is in progress), or REMOVING (Region removal workflow is in progress).
Type: String
Valid Values: `ACTIVE | ADDING | REMOVING`
Required: No

## See Also
<a name="API_RegionMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/RegionMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/RegionMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/RegionMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IAM Identity Center API Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
