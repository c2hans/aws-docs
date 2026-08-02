---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_AccountEnrollmentStatus.html
---

# AccountEnrollmentStatus
<a name="API_AccountEnrollmentStatus"></a>

Describes the enrollment status of an organization's member accounts in AWS Compute Optimizer.

## Contents
<a name="API_AccountEnrollmentStatus_Contents"></a>

 ** accountId **   <a name="computeoptimizer-Type-AccountEnrollmentStatus-accountId"></a>
The AWS account ID.
Type: String
Required: No

 ** lastUpdatedTimestamp **   <a name="computeoptimizer-Type-AccountEnrollmentStatus-lastUpdatedTimestamp"></a>
The Unix epoch timestamp, in seconds, of when the account enrollment status was last updated.
Type: Timestamp
Required: No

 ** status **   <a name="computeoptimizer-Type-AccountEnrollmentStatus-status"></a>
The account enrollment status.
Type: String
Valid Values: `Active | Inactive | Pending | Failed`
Required: No

 ** statusReason **   <a name="computeoptimizer-Type-AccountEnrollmentStatus-statusReason"></a>
The reason for the account enrollment status.
For example, an account might show a status of `Pending` because member accounts of an organization require more time to be enrolled in the service.
Type: String
Required: No

## See Also
<a name="API_AccountEnrollmentStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/AccountEnrollmentStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/AccountEnrollmentStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/AccountEnrollmentStatus)
