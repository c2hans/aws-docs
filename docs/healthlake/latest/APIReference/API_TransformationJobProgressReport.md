---
source_url: https://docs.aws.amazon.com/healthlake/latest/APIReference/API_TransformationJobProgressReport.html
---

# TransformationJobProgressReport
<a name="API_TransformationJobProgressReport"></a>

Contains progress metrics for a data transformation job, including counts of files scanned, converted, and failed.

## Contents
<a name="API_TransformationJobProgressReport_Contents"></a>

 ** TotalFilesConverted **   <a name="HealthLake-Type-TransformationJobProgressReport-TotalFilesConverted"></a>
The total number of source files successfully converted.
Type: Long
Required: Yes

 ** TotalFilesFailed **   <a name="HealthLake-Type-TransformationJobProgressReport-TotalFilesFailed"></a>
The total number of source files that failed conversion.
Type: Long
Required: Yes

 ** TotalFilesScanned **   <a name="HealthLake-Type-TransformationJobProgressReport-TotalFilesScanned"></a>
The total number of source files scanned by the job.
Type: Long
Required: Yes

 ** TotalResourcesGenerated **   <a name="HealthLake-Type-TransformationJobProgressReport-TotalResourcesGenerated"></a>
The total number of FHIR R4 resources generated across all converted files.
Type: Long
Required: Yes

## See Also
<a name="API_TransformationJobProgressReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/healthlake-2017-07-01/TransformationJobProgressReport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/healthlake-2017-07-01/TransformationJobProgressReport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/healthlake-2017-07-01/TransformationJobProgressReport)
