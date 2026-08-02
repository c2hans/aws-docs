---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_ReplicationTaskAssessmentRunResultStatistic.html
---

# ReplicationTaskAssessmentRunResultStatistic
<a name="API_ReplicationTaskAssessmentRunResultStatistic"></a>

The object containing the result statistics for a completed assessment run.

## Contents
<a name="API_ReplicationTaskAssessmentRunResultStatistic_Contents"></a>

 ** Cancelled **   <a name="DMS-Type-ReplicationTaskAssessmentRunResultStatistic-Cancelled"></a>
 The number of individual assessments that were cancelled during the assessment run.
Type: Integer
Required: No

 ** Error **   <a name="DMS-Type-ReplicationTaskAssessmentRunResultStatistic-Error"></a>
The number of individual assessments that encountered a critical error and could not complete properly.
Type: Integer
Required: No

 ** Failed **   <a name="DMS-Type-ReplicationTaskAssessmentRunResultStatistic-Failed"></a>
The number of individual assessments that failed to meet the criteria defined in the assessment run.
Type: Integer
Required: No

 ** Passed **   <a name="DMS-Type-ReplicationTaskAssessmentRunResultStatistic-Passed"></a>
The number of individual assessments that successfully passed all checks in the assessment run.
Type: Integer
Required: No

 ** Skipped **   <a name="DMS-Type-ReplicationTaskAssessmentRunResultStatistic-Skipped"></a>
The number of individual assessments that were skipped during the assessment run.
Type: Integer
Required: No

 ** Warning **   <a name="DMS-Type-ReplicationTaskAssessmentRunResultStatistic-Warning"></a>
Indicates that the recent completed AssessmentRun triggered a warning.
Type: Integer
Required: No

## See Also
<a name="API_ReplicationTaskAssessmentRunResultStatistic_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/ReplicationTaskAssessmentRunResultStatistic)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/ReplicationTaskAssessmentRunResultStatistic)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/ReplicationTaskAssessmentRunResultStatistic)
