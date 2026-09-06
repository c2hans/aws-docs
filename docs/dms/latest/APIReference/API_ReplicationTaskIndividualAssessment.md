---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_ReplicationTaskIndividualAssessment.html
---

# ReplicationTaskIndividualAssessment
<a name="API_ReplicationTaskIndividualAssessment"></a>

Provides information that describes an individual assessment from a premigration assessment run.

## Contents
<a name="API_ReplicationTaskIndividualAssessment_Contents"></a>

 ** IndividualAssessmentName **   <a name="DMS-Type-ReplicationTaskIndividualAssessment-IndividualAssessmentName"></a>
Name of this individual assessment.
Type: String
Required: No

 ** ReplicationTaskAssessmentRunArn **   <a name="DMS-Type-ReplicationTaskIndividualAssessment-ReplicationTaskAssessmentRunArn"></a>
ARN of the premigration assessment run that is created to run this individual assessment.
Type: String
Required: No

 ** ReplicationTaskIndividualAssessmentArn **   <a name="DMS-Type-ReplicationTaskIndividualAssessment-ReplicationTaskIndividualAssessmentArn"></a>
Amazon Resource Name (ARN) of this individual assessment.
Type: String
Required: No

 ** ReplicationTaskIndividualAssessmentStartDate **   <a name="DMS-Type-ReplicationTaskIndividualAssessment-ReplicationTaskIndividualAssessmentStartDate"></a>
Date when this individual assessment was started as part of running the `StartReplicationTaskAssessmentRun` operation.
Type: Timestamp
Required: No

 ** Status **   <a name="DMS-Type-ReplicationTaskIndividualAssessment-Status"></a>
Individual assessment status.
This status can have one of the following values:
+  `"cancelled"`
+  `"error"`
+  `"failed"`
+  `"passed"`
+  `"pending"`
+  `"skipped"`
+  `"running"`
Type: String
Required: No

## See Also
<a name="API_ReplicationTaskIndividualAssessment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/ReplicationTaskIndividualAssessment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/ReplicationTaskIndividualAssessment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/ReplicationTaskIndividualAssessment)
