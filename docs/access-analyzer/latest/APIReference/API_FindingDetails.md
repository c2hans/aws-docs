---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_FindingDetails.html
---

# FindingDetails
<a name="API_FindingDetails"></a>

Contains information about an external access or unused access finding. Only one parameter can be used in a `FindingDetails` object.

## Contents
<a name="API_FindingDetails_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** externalAccessDetails **   <a name="accessanalyzer-Type-FindingDetails-externalAccessDetails"></a>
The details for an external access analyzer finding.
Type: [ExternalAccessDetails](API_ExternalAccessDetails.md) object
Required: No

 ** internalAccessDetails **   <a name="accessanalyzer-Type-FindingDetails-internalAccessDetails"></a>
The details for an internal access analyzer finding. This contains information about access patterns identified within your AWS organization or account.
Type: [InternalAccessDetails](API_InternalAccessDetails.md) object
Required: No

 ** unusedIamRoleDetails **   <a name="accessanalyzer-Type-FindingDetails-unusedIamRoleDetails"></a>
The details for an unused access analyzer finding with an unused IAM role finding type.
Type: [UnusedIamRoleDetails](API_UnusedIamRoleDetails.md) object
Required: No

 ** unusedIamUserAccessKeyDetails **   <a name="accessanalyzer-Type-FindingDetails-unusedIamUserAccessKeyDetails"></a>
The details for an unused access analyzer finding with an unused IAM user access key finding type.
Type: [UnusedIamUserAccessKeyDetails](API_UnusedIamUserAccessKeyDetails.md) object
Required: No

 ** unusedIamUserPasswordDetails **   <a name="accessanalyzer-Type-FindingDetails-unusedIamUserPasswordDetails"></a>
The details for an unused access analyzer finding with an unused IAM user password finding type.
Type: [UnusedIamUserPasswordDetails](API_UnusedIamUserPasswordDetails.md) object
Required: No

 ** unusedPermissionDetails **   <a name="accessanalyzer-Type-FindingDetails-unusedPermissionDetails"></a>
The details for an unused access analyzer finding with an unused permission finding type.
Type: [UnusedPermissionDetails](API_UnusedPermissionDetails.md) object
Required: No

## See Also
<a name="API_FindingDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/FindingDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/FindingDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/FindingDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Access Analyzer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query access-analyzer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
