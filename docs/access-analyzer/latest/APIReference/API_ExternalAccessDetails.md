---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_ExternalAccessDetails.html
---

# ExternalAccessDetails
<a name="API_ExternalAccessDetails"></a>

Contains information about an external access finding.

## Contents
<a name="API_ExternalAccessDetails_Contents"></a>

 ** condition **   <a name="accessanalyzer-Type-ExternalAccessDetails-condition"></a>
The condition in the analyzed policy statement that resulted in an external access finding.
Type: String to string map
Required: Yes

 ** action **   <a name="accessanalyzer-Type-ExternalAccessDetails-action"></a>
The action in the analyzed policy statement that an external principal has permission to use.
Type: Array of strings
Required: No

 ** isPublic **   <a name="accessanalyzer-Type-ExternalAccessDetails-isPublic"></a>
Specifies whether the external access finding is public.
Type: Boolean
Required: No

 ** principal **   <a name="accessanalyzer-Type-ExternalAccessDetails-principal"></a>
The external principal that has access to a resource within the zone of trust.
Type: String to string map
Required: No

 ** resourceControlPolicyRestriction **   <a name="accessanalyzer-Type-ExternalAccessDetails-resourceControlPolicyRestriction"></a>
The type of restriction applied to the finding by the resource owner with an Organizations resource control policy (RCP).
+  `APPLICABLE`: There is an RCP present in the organization but IAM Access Analyzer does not include it in the evaluation of effective permissions. For example, if `s3:DeleteObject` is blocked by the RCP and the restriction is `APPLICABLE`, then `s3:DeleteObject` would still be included in the list of actions for the finding.
+  `FAILED_TO_EVALUATE_RCP`: There was an error evaluating the RCP.
+  `NOT_APPLICABLE`: There was no RCP present in the organization, or there was no RCP applicable to the resource. For example, the resource being analyzed is an Amazon RDS snapshot and there is an RCP in the organization, but the RCP only impacts Amazon S3 buckets.
+  `APPLIED`: This restriction is not currently available for external access findings.
Type: String
Valid Values: `APPLICABLE | FAILED_TO_EVALUATE_RCP | NOT_APPLICABLE | APPLIED`
Required: No

 ** sources **   <a name="accessanalyzer-Type-ExternalAccessDetails-sources"></a>
The sources of the external access finding. This indicates how the access that generated the finding is granted. It is populated for Amazon S3 bucket findings.
Type: Array of [FindingSource](API_FindingSource.md) objects
Required: No

## See Also
<a name="API_ExternalAccessDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/ExternalAccessDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/ExternalAccessDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/ExternalAccessDetails)
