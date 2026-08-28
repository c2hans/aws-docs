---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_StorageConnector.html
---

# StorageConnector
<a name="API_StorageConnector"></a>

Describes a connector that enables persistent storage for users.

## Contents
<a name="API_StorageConnector_Contents"></a>

 ** ConnectorType **   <a name="WorkSpacesApplications-Type-StorageConnector-ConnectorType"></a>
The type of storage connector.
Type: String
Valid Values: `HOMEFOLDERS | GOOGLE_DRIVE | ONE_DRIVE`
Required: Yes

 ** Domains **   <a name="WorkSpacesApplications-Type-StorageConnector-Domains"></a>
The names of the domains for the account.
Type: Array of strings
Array Members: Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** DomainsRequireAdminConsent **   <a name="WorkSpacesApplications-Type-StorageConnector-DomainsRequireAdminConsent"></a>
The OneDrive for Business domains where you require admin consent when users try to link their OneDrive account to WorkSpaces Applications. The attribute can only be specified when ConnectorType=ONE\_DRIVE.
Type: Array of strings
Array Members: Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** ResourceIdentifier **   <a name="WorkSpacesApplications-Type-StorageConnector-ResourceIdentifier"></a>
The ARN of the storage connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## See Also
<a name="API_StorageConnector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/StorageConnector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/StorageConnector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/StorageConnector)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
