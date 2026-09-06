---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_OpsItemFilter.html
---

# OpsItemFilter
<a name="API_OpsItemFilter"></a>

Describes an OpsItem filter.

## Contents
<a name="API_OpsItemFilter_Contents"></a>

 ** Key **   <a name="systemsmanager-Type-OpsItemFilter-Key"></a>
The name of the filter.
Type: String
Valid Values: `Status | CreatedBy | Source | Priority | Title | OpsItemId | CreatedTime | LastModifiedTime | ActualStartTime | ActualEndTime | PlannedStartTime | PlannedEndTime | OperationalData | OperationalDataKey | OperationalDataValue | ResourceId | AutomationId | Category | Severity | OpsItemType | AccessRequestByRequesterArn | AccessRequestByRequesterId | AccessRequestByApproverArn | AccessRequestByApproverId | AccessRequestBySourceAccountId | AccessRequestBySourceOpsItemId | AccessRequestBySourceRegion | AccessRequestByIsReplica | AccessRequestByTargetResourceId | ChangeRequestByRequesterArn | ChangeRequestByRequesterName | ChangeRequestByApproverArn | ChangeRequestByApproverName | ChangeRequestByTemplate | ChangeRequestByTargetsResourceGroup | InsightByType | AccountId`
Required: Yes

 ** Operator **   <a name="systemsmanager-Type-OpsItemFilter-Operator"></a>
The operator used by the filter call.
Type: String
Valid Values: `Equal | Contains | GreaterThan | LessThan`
Required: Yes

 ** Values **   <a name="systemsmanager-Type-OpsItemFilter-Values"></a>
The filter value.
Type: Array of strings
Required: Yes

## See Also
<a name="API_OpsItemFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/OpsItemFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/OpsItemFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/OpsItemFilter)
