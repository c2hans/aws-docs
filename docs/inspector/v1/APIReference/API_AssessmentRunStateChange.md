---
source_url: https://docs.aws.amazon.com/inspector/v1/APIReference/API_AssessmentRunStateChange.html
---

# AssessmentRunStateChange
<a name="API_AssessmentRunStateChange"></a>

Used as one of the elements of the [AssessmentRun](API_AssessmentRun.md) data type.

## Contents
<a name="API_AssessmentRunStateChange_Contents"></a>

 ** state **   <a name="Inspector-Type-AssessmentRunStateChange-state"></a>
The assessment run state.
Type: String
Valid Values: `CREATED | START_DATA_COLLECTION_PENDING | START_DATA_COLLECTION_IN_PROGRESS | COLLECTING_DATA | STOP_DATA_COLLECTION_PENDING | DATA_COLLECTED | START_EVALUATING_RULES_PENDING | EVALUATING_RULES | FAILED | ERROR | COMPLETED | COMPLETED_WITH_ERRORS | CANCELED`
Required: Yes

 ** stateChangedAt **   <a name="Inspector-Type-AssessmentRunStateChange-stateChangedAt"></a>
The last time the assessment run state changed.
Type: Timestamp
Required: Yes

## See Also
<a name="API_AssessmentRunStateChange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector-2016-02-16/AssessmentRunStateChange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/AssessmentRunStateChange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector-2016-02-16/AssessmentRunStateChange)
