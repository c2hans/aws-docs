---
source_url: https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_DataCollectionDetails.html
---

# DataCollectionDetails
<a name="API_DataCollectionDetails"></a>

 Detailed information about an assessment.

## Contents
<a name="API_DataCollectionDetails_Contents"></a>

 ** completionTime **   <a name="migrationhubstrategy-Type-DataCollectionDetails-completionTime"></a>
 The time the assessment completes.
Type: Timestamp
Required: No

 ** failed **   <a name="migrationhubstrategy-Type-DataCollectionDetails-failed"></a>
 The number of failed servers in the assessment.
Type: Integer
Required: No

 ** inProgress **   <a name="migrationhubstrategy-Type-DataCollectionDetails-inProgress"></a>
 The number of servers with the assessment status `IN_PROGESS`.
Type: Integer
Required: No

 ** servers **   <a name="migrationhubstrategy-Type-DataCollectionDetails-servers"></a>
 The total number of servers in the assessment.
Type: Integer
Required: No

 ** startTime **   <a name="migrationhubstrategy-Type-DataCollectionDetails-startTime"></a>
 The start time of assessment.
Type: Timestamp
Required: No

 ** status **   <a name="migrationhubstrategy-Type-DataCollectionDetails-status"></a>
 The status of the assessment.
Type: String
Valid Values: `IN_PROGRESS | COMPLETE | FAILED | STOPPED`
Required: No

 ** statusMessage **   <a name="migrationhubstrategy-Type-DataCollectionDetails-statusMessage"></a>
The status message of the assessment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Pattern: `.*\S.*`
Required: No

 ** success **   <a name="migrationhubstrategy-Type-DataCollectionDetails-success"></a>
 The number of successful servers in the assessment.
Type: Integer
Required: No

## See Also
<a name="API_DataCollectionDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhubstrategy-2020-02-19/DataCollectionDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhubstrategy-2020-02-19/DataCollectionDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhubstrategy-2020-02-19/DataCollectionDetails)
