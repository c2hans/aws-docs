---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_RecoveryPoint.html
---

# RecoveryPoint
<a name="API_RecoveryPoint"></a>

The automatically created recovery point of a namespace. Recovery points are created every 30 minutes and kept for 24 hours.

## Contents
<a name="API_RecoveryPoint_Contents"></a>

 ** namespaceArn **   <a name="redshiftserverless-Type-RecoveryPoint-namespaceArn"></a>
The Amazon Resource Name (ARN) of the namespace the recovery point is associated with.
Type: String
Required: No

 ** namespaceName **   <a name="redshiftserverless-Type-RecoveryPoint-namespaceName"></a>
The name of the namespace the recovery point is associated with.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-z0-9-]+`
Required: No

 ** recoveryPointCreateTime **   <a name="redshiftserverless-Type-RecoveryPoint-recoveryPointCreateTime"></a>
The time the recovery point is created.
Type: Timestamp
Required: No

 ** recoveryPointId **   <a name="redshiftserverless-Type-RecoveryPoint-recoveryPointId"></a>
The unique identifier of the recovery point.
Type: String
Required: No

 ** totalSizeInMegaBytes **   <a name="redshiftserverless-Type-RecoveryPoint-totalSizeInMegaBytes"></a>
The total size of the data in the recovery point in megabytes.
Type: Double
Required: No

 ** workgroupName **   <a name="redshiftserverless-Type-RecoveryPoint-workgroupName"></a>
The name of the workgroup the recovery point is associated with.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-z0-9-]+`
Required: No

## See Also
<a name="API_RecoveryPoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/RecoveryPoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/RecoveryPoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/RecoveryPoint)
