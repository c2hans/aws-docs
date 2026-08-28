---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_UnusedPermissionDetails.html
---

# UnusedPermissionDetails
<a name="API_UnusedPermissionDetails"></a>

Contains information about an unused access finding for a permission. IAM Access Analyzer charges for unused access analysis based on the number of IAM roles and users analyzed per month. For more details on pricing, see [IAM Access Analyzer pricing](https://aws.amazon.com/iam/access-analyzer/pricing).

## Contents
<a name="API_UnusedPermissionDetails_Contents"></a>

 ** serviceNamespace **   <a name="accessanalyzer-Type-UnusedPermissionDetails-serviceNamespace"></a>
The namespace of the AWS service that contains the unused actions.
Type: String
Required: Yes

 ** actions **   <a name="accessanalyzer-Type-UnusedPermissionDetails-actions"></a>
A list of unused actions for which the unused access finding was generated.
Type: Array of [UnusedAction](API_UnusedAction.md) objects
Required: No

 ** lastAccessed **   <a name="accessanalyzer-Type-UnusedPermissionDetails-lastAccessed"></a>
The time at which the permission was last accessed.
Type: Timestamp
Required: No

## See Also
<a name="API_UnusedPermissionDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/UnusedPermissionDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/UnusedPermissionDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/UnusedPermissionDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Access Analyzer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query access-analyzer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
