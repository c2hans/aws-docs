---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_InternalAccessDetails.html
---

# InternalAccessDetails
<a name="API_InternalAccessDetails"></a>

Contains information about an internal access finding. This includes details about the access that was identified within your AWS organization or account.

## Contents
<a name="API_InternalAccessDetails_Contents"></a>

 ** accessType **   <a name="accessanalyzer-Type-InternalAccessDetails-accessType"></a>
The type of internal access identified in the finding. This indicates how the access is granted within your AWS environment.
Type: String
Valid Values: `INTRA_ACCOUNT | INTRA_ORG`
Required: No

 ** action **   <a name="accessanalyzer-Type-InternalAccessDetails-action"></a>
The action in the analyzed policy statement that has internal access permission to use.
Type: Array of strings
Required: No

 ** condition **   <a name="accessanalyzer-Type-InternalAccessDetails-condition"></a>
The condition in the analyzed policy statement that resulted in an internal access finding.
Type: String to string map
Required: No

 ** principal **   <a name="accessanalyzer-Type-InternalAccessDetails-principal"></a>
The principal that has access to a resource within the internal environment.
Type: String to string map
Required: No

 ** principalOwnerAccount **   <a name="accessanalyzer-Type-InternalAccessDetails-principalOwnerAccount"></a>
The AWS account ID that owns the principal identified in the internal access finding.
Type: String
Required: No

 ** principalType **   <a name="accessanalyzer-Type-InternalAccessDetails-principalType"></a>
The type of principal identified in the internal access finding, such as IAM role or IAM user.
Type: String
Valid Values: `IAM_ROLE | IAM_USER`
Required: No

 ** resourceControlPolicyRestriction **   <a name="accessanalyzer-Type-InternalAccessDetails-resourceControlPolicyRestriction"></a>
The type of restriction applied to the finding by the resource owner with an AWS Organizations resource control policy (RCP).
+  `APPLICABLE`: There is an RCP present in the organization but IAM Access Analyzer does not include it in the evaluation of effective permissions. For example, if `s3:DeleteObject` is blocked by the RCP and the restriction is `APPLICABLE`, then `s3:DeleteObject` would still be included in the list of actions for the finding. Only applicable to internal access findings with the account as the zone of trust.
+  `FAILED_TO_EVALUATE_RCP`: There was an error evaluating the RCP.
+  `NOT_APPLICABLE`: There was no RCP present in the organization. For internal access findings with the account as the zone of trust, `NOT_APPLICABLE` could also indicate that there was no RCP applicable to the resource.
+  `APPLIED`: An RCP is present in the organization and IAM Access Analyzer included it in the evaluation of effective permissions. For example, if `s3:DeleteObject` is blocked by the RCP and the restriction is `APPLIED`, then `s3:DeleteObject` would not be included in the list of actions for the finding. Only applicable to internal access findings with the organization as the zone of trust.
Type: String
Valid Values: `APPLICABLE | FAILED_TO_EVALUATE_RCP | NOT_APPLICABLE | APPLIED`
Required: No

 ** serviceControlPolicyRestriction **   <a name="accessanalyzer-Type-InternalAccessDetails-serviceControlPolicyRestriction"></a>
The type of restriction applied to the finding by an AWS Organizations service control policy (SCP).
+  `APPLICABLE`: There is an SCP present in the organization but IAM Access Analyzer does not include it in the evaluation of effective permissions. Only applicable to internal access findings with the account as the zone of trust.
+  `FAILED_TO_EVALUATE_SCP`: There was an error evaluating the SCP.
+  `NOT_APPLICABLE`: There was no SCP present in the organization. For internal access findings with the account as the zone of trust, `NOT_APPLICABLE` could also indicate that there was no SCP applicable to the principal.
+  `APPLIED`: An SCP is present in the organization and IAM Access Analyzer included it in the evaluation of effective permissions. Only applicable to internal access findings with the organization as the zone of trust.
Type: String
Valid Values: `APPLICABLE | FAILED_TO_EVALUATE_SCP | NOT_APPLICABLE | APPLIED`
Required: No

 ** sources **   <a name="accessanalyzer-Type-InternalAccessDetails-sources"></a>
The sources of the internal access finding. This indicates how the access that generated the finding is granted within your AWS environment.
Type: Array of [FindingSource](API_FindingSource.md) objects
Required: No

## See Also
<a name="API_InternalAccessDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/InternalAccessDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/InternalAccessDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/InternalAccessDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Access Analyzer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query access-analyzer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
