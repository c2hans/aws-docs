---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_NetworkMigrationAnalysisResultTarget.html
---

# NetworkMigrationAnalysisResultTarget
<a name="API_NetworkMigrationAnalysisResultTarget"></a>

The target resource information for an analysis result.

## Contents
<a name="API_NetworkMigrationAnalysisResultTarget_Contents"></a>

 ** subnetID **   <a name="mgn-Type-NetworkMigrationAnalysisResultTarget-subnetID"></a>
The subnet ID of the target resource.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `subnet-[0-9a-fA-F]{8,}`
Required: No

 ** vpcID **   <a name="mgn-Type-NetworkMigrationAnalysisResultTarget-vpcID"></a>
The VPC ID of the target resource.
Type: String
Pattern: `vpc-([0-9a-f]){8}(([0-9a-f]){9})?`
Required: No

## See Also
<a name="API_NetworkMigrationAnalysisResultTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/NetworkMigrationAnalysisResultTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/NetworkMigrationAnalysisResultTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/NetworkMigrationAnalysisResultTarget)
