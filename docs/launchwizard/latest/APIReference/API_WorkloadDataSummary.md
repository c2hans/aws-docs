---
source_url: https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_WorkloadDataSummary.html
---

# WorkloadDataSummary
<a name="API_WorkloadDataSummary"></a>

Describes workload data.

## Contents
<a name="API_WorkloadDataSummary_Contents"></a>

 ** displayName **   <a name="launchwizard-Type-WorkloadDataSummary-displayName"></a>
The display name of the workload data.
Type: String
Required: No

 ** status **   <a name="launchwizard-Type-WorkloadDataSummary-status"></a>
The status of the workload.
Type: String
Valid Values: `ACTIVE | INACTIVE | DISABLED | DELETED`
Required: No

 ** workloadName **   <a name="launchwizard-Type-WorkloadDataSummary-workloadName"></a>
The name of the workload.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[A-Za-z][a-zA-Z0-9-_]*`
Required: No

## See Also
<a name="API_WorkloadDataSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/launch-wizard-2018-05-10/WorkloadDataSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/launch-wizard-2018-05-10/WorkloadDataSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/launch-wizard-2018-05-10/WorkloadDataSummary)
