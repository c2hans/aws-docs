---
source_url: https://docs.aws.amazon.com/network-security-manager/latest/APIReference/API_ResourceSynchronizationStatusSummary.html
---

# ResourceSynchronizationStatusSummary
<a name="API_ResourceSynchronizationStatusSummary"></a>

The synchronization status of a resource covered by a deployment.

## Contents
<a name="API_ResourceSynchronizationStatusSummary_Contents"></a>

 ** accountId **   <a name="networksecuritymanager-Type-ResourceSynchronizationStatusSummary-accountId"></a>
The AWS account ID that owns the resource.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `(?:[0-9]{12})`
Required: Yes

 ** resourceArn **   <a name="networksecuritymanager-Type-ResourceSynchronizationStatusSummary-resourceArn"></a>
The ARN of the resource whose synchronization status is reported.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 1010.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:(.+)`
Required: Yes

 ** synchronizationStatus **   <a name="networksecuritymanager-Type-ResourceSynchronizationStatusSummary-synchronizationStatus"></a>
The synchronization status of the resource, such as `IN_SYNC` or `OUT_OF_SYNC`.
Type: String
Valid Values: `IN_SYNC | OUT_OF_SYNC | NOT_APPLICABLE`
Required: Yes

 ** updatedAt **   <a name="networksecuritymanager-Type-ResourceSynchronizationStatusSummary-updatedAt"></a>
The time when the resource was last updated.
Type: Timestamp
Required: Yes

 ** deploymentArn **   <a name="networksecuritymanager-Type-ResourceSynchronizationStatusSummary-deploymentArn"></a>
The ARN of the deployment that the synchronization status is associated with. This is absent for aggregate (cross-deployment) statuses.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 1010.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:(.+)`
Required: No

 ** evaluatedAt **   <a name="networksecuritymanager-Type-ResourceSynchronizationStatusSummary-evaluatedAt"></a>
The time when the synchronization status was last evaluated.
Type: Timestamp
Required: No

 ** outOfSyncReasons **   <a name="networksecuritymanager-Type-ResourceSynchronizationStatusSummary-outOfSyncReasons"></a>
The reasons the resource is out of sync, keyed by firewall type. This is null when the resource is in sync.
Type: [OutOfSyncReasonsView](API_OutOfSyncReasonsView.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** remediationIssues **   <a name="networksecuritymanager-Type-ResourceSynchronizationStatusSummary-remediationIssues"></a>
Details about remediation issues, keyed by firewall type. This is null when there are no remediation issues.
Type: [RemediationIssuesView](API_RemediationIssuesView.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** resourceType **   <a name="networksecuritymanager-Type-ResourceSynchronizationStatusSummary-resourceType"></a>
The type of the resource, in AWS CloudFormation format.
Type: String
Valid Values: `AWS::ApiGateway::Stage | AWS::CloudFront::Distribution | AWS::EC2::EIP | AWS::ElasticLoadBalancingV2::LoadBalancer::application | AWS::ElasticLoadBalancing::LoadBalancer | AWS::WAFv2::WebACL | AWS::Shield::Protection | AWS::ShieldRegional::Protection`
Required: No

## See Also
<a name="API_ResourceSynchronizationStatusSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-security-manager-2025-10-30/ResourceSynchronizationStatusSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-security-manager-2025-10-30/ResourceSynchronizationStatusSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-security-manager-2025-10-30/ResourceSynchronizationStatusSummary)
