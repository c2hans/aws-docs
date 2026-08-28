---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_NetworkMigrationFailedResourceDetails.html
---

# NetworkMigrationFailedResourceDetails
<a name="API_NetworkMigrationFailedResourceDetails"></a>

Details about a resource that failed to deploy.

## Contents
<a name="API_NetworkMigrationFailedResourceDetails_Contents"></a>

 ** logicalID **   <a name="mgn-Type-NetworkMigrationFailedResourceDetails-logicalID"></a>
The logical ID of the failed resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z][a-zA-Z0-9-]*`
Required: No

 ** status **   <a name="mgn-Type-NetworkMigrationFailedResourceDetails-status"></a>
The status of the failed resource.
Type: String
Valid Values: `CREATE_FAILED | DELETE_FAILED`
Required: No

 ** statusReason **   <a name="mgn-Type-NetworkMigrationFailedResourceDetails-statusReason"></a>
The reason why the resource failed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 65536.
Required: No

## See Also
<a name="API_NetworkMigrationFailedResourceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/NetworkMigrationFailedResourceDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/NetworkMigrationFailedResourceDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/NetworkMigrationFailedResourceDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for ApplicationMigrationService. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
