---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ServiceMetadata.html
---

# ServiceMetadata
<a name="API_ServiceMetadata"></a>

 The metadata that's associated with the AWS service.

## Contents
<a name="API_ServiceMetadata_Contents"></a>

 ** category **   <a name="auditmanager-Type-ServiceMetadata-category"></a>
 The category that the AWS service belongs to, such as compute, storage, or database.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `.*\S.*`
Required: No

 ** description **   <a name="auditmanager-Type-ServiceMetadata-description"></a>
 The description of the AWS service.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `.*\S.*`
Required: No

 ** displayName **   <a name="auditmanager-Type-ServiceMetadata-displayName"></a>
 The display name of the AWS service.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `.*\S.*`
Required: No

 ** name **   <a name="auditmanager-Type-ServiceMetadata-name"></a>
 The name of the AWS service.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 40.
Pattern: `^[a-zA-Z0-9-\s().]+$`
Required: No

## See Also
<a name="API_ServiceMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/ServiceMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/ServiceMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/ServiceMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Audit Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query audit-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
