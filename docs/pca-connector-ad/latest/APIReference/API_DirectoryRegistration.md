---
source_url: https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_DirectoryRegistration.html
---

# DirectoryRegistration
<a name="API_DirectoryRegistration"></a>

The directory registration represents the authorization of the connector service with a directory.

## Contents
<a name="API_DirectoryRegistration_Contents"></a>

 ** Arn **   <a name="PcaConnectorAd-Type-DirectoryRegistration-Arn"></a>
The Amazon Resource Name (ARN) that was returned when you called CreateDirectoryRegistration.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `arn:[\w-]+:pca-connector-ad:[\w-]+:[0-9]+:directory-registration\/d-[0-9a-f]{10}`
Required: No

 ** CreatedAt **   <a name="PcaConnectorAd-Type-DirectoryRegistration-CreatedAt"></a>
The date and time that the directory registration was created.
Type: Timestamp
Required: No

 ** DirectoryId **   <a name="PcaConnectorAd-Type-DirectoryRegistration-DirectoryId"></a>
The identifier of the Active Directory.
Type: String
Pattern: `d-[0-9a-f]{10}`
Required: No

 ** Status **   <a name="PcaConnectorAd-Type-DirectoryRegistration-Status"></a>
Status of the directory registration.
Type: String
Valid Values: `CREATING | ACTIVE | DELETING | FAILED`
Required: No

 ** StatusReason **   <a name="PcaConnectorAd-Type-DirectoryRegistration-StatusReason"></a>
Additional information about the directory registration status if the status is failed.
Type: String
Valid Values: `DIRECTORY_ACCESS_DENIED | DIRECTORY_RESOURCE_NOT_FOUND | DIRECTORY_NOT_ACTIVE | DIRECTORY_NOT_REACHABLE | DIRECTORY_TYPE_NOT_SUPPORTED | INTERNAL_FAILURE`
Required: No

 ** UpdatedAt **   <a name="PcaConnectorAd-Type-DirectoryRegistration-UpdatedAt"></a>
The date and time that the directory registration was updated.
Type: Timestamp
Required: No

## See Also
<a name="API_DirectoryRegistration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pca-connector-ad-2018-05-10/DirectoryRegistration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pca-connector-ad-2018-05-10/DirectoryRegistration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pca-connector-ad-2018-05-10/DirectoryRegistration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Private CA Connector for Active Directory. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pca-connector-ad` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
