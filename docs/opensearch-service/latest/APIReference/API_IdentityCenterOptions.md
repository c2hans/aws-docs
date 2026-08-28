---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_IdentityCenterOptions.html
---

# IdentityCenterOptions
<a name="API_IdentityCenterOptions"></a>

Settings container for integrating IAM Identity Center with OpenSearch UI applications, which enables enabling secure user authentication and access control across multiple data sources. This setup supports single sign-on (SSO) through IAM Identity Center, allowing centralized user management.

## Contents
<a name="API_IdentityCenterOptions_Contents"></a>

 ** EnabledAPIAccess **   <a name="opensearchservice-Type-IdentityCenterOptions-EnabledAPIAccess"></a>
Indicates whether IAM Identity Center is enabled for the application.
Type: Boolean
Required: No

 ** IdentityCenterApplicationARN **   <a name="opensearchservice-Type-IdentityCenterOptions-IdentityCenterApplicationARN"></a>
The ARN of the IAM Identity Center application that integrates with Amazon OpenSearch Service.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:aws[a-z\\-]*:[a-z]+:[a-z0-9\\-]*:[0-9]*:[a-z0-9\\-]+\/[a-z0-9\\-]+\/[a-z0-9\\-]+`
Required: No

 ** IdentityCenterInstanceARN **   <a name="opensearchservice-Type-IdentityCenterOptions-IdentityCenterInstanceARN"></a>
The Amazon Resource Name (ARN) of the IAM Identity Center instance.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:aws[a-z\\-]*:[a-z]+:[a-z0-9\\-]*:[0-9]*:[a-z0-9\\-]+\/[a-z0-9\\-]+`
Required: No

 ** IdentityCenterInstanceRegion **   <a name="opensearchservice-Type-IdentityCenterOptions-IdentityCenterInstanceRegion"></a>
The Region of the IAM Identity Center instance.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 30.
Pattern: `[a-z][a-z0-9\-]+`
Required: No

 ** IdentityStoreId **   <a name="opensearchservice-Type-IdentityCenterOptions-IdentityStoreId"></a>
The identifier of the IAM Identity Store.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^d-[0-9a-f]{10}$|^[0-9a-f]{8}\\b-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-\\b[0-9a-f]{12}$`
Required: No

 ** RolesKey **   <a name="opensearchservice-Type-IdentityCenterOptions-RolesKey"></a>
Specifies the attribute that contains the backend role identifier (such as group name or group ID) in IAM Identity Center.
Type: String
Valid Values: `GroupName | GroupId`
Required: No

 ** SubjectKey **   <a name="opensearchservice-Type-IdentityCenterOptions-SubjectKey"></a>
Specifies the attribute that contains the subject identifier (such as username, user ID, or email) in IAM Identity Center.
Type: String
Valid Values: `UserName | UserId | Email`
Required: No

## See Also
<a name="API_IdentityCenterOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/IdentityCenterOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/IdentityCenterOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/IdentityCenterOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
