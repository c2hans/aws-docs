---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_AccountEnrollmentStatus.html
---

# AccountEnrollmentStatus
<a name="API_CostOptimizationHub_AccountEnrollmentStatus"></a>

Describes the enrollment status of an organization's member accounts in Cost Optimization Hub.

## Contents
<a name="API_CostOptimizationHub_AccountEnrollmentStatus_Contents"></a>

 ** accountId **   <a name="awscostmanagement-Type-CostOptimizationHub_AccountEnrollmentStatus-accountId"></a>
The AWS account ID.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** createdTimestamp **   <a name="awscostmanagement-Type-CostOptimizationHub_AccountEnrollmentStatus-createdTimestamp"></a>
The time when the account enrollment status was created.
Type: Timestamp
Required: No

 ** lastUpdatedTimestamp **   <a name="awscostmanagement-Type-CostOptimizationHub_AccountEnrollmentStatus-lastUpdatedTimestamp"></a>
The time when the account enrollment status was last updated.
Type: Timestamp
Required: No

 ** status **   <a name="awscostmanagement-Type-CostOptimizationHub_AccountEnrollmentStatus-status"></a>
The account enrollment status.
Type: String
Valid Values: `Active | Inactive`
Required: No

## See Also
<a name="API_CostOptimizationHub_AccountEnrollmentStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cost-optimization-hub-2022-07-26/AccountEnrollmentStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cost-optimization-hub-2022-07-26/AccountEnrollmentStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cost-optimization-hub-2022-07-26/AccountEnrollmentStatus)
