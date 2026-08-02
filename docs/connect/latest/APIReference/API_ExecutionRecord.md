---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ExecutionRecord.html
---

# ExecutionRecord
<a name="API_ExecutionRecord"></a>

Contains information about a test case execution record.

## Contents
<a name="API_ExecutionRecord_Contents"></a>

 ** ObservationId **   <a name="connect-Type-ExecutionRecord-ObservationId"></a>
The identifier of the execution record.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** Record **   <a name="connect-Type-ExecutionRecord-Record"></a>
The details of the executed record.
Type: String
Required: No

 ** Status **   <a name="connect-Type-ExecutionRecord-Status"></a>
The status of the action execution.
Type: String
Valid Values: `PASSED | FAILED | IN_PROGRESS | STOPPED`
Required: No

 ** Timestamp **   <a name="connect-Type-ExecutionRecord-Timestamp"></a>
The timestamp when the action was executed.
Type: Timestamp
Required: No

## See Also
<a name="API_ExecutionRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ExecutionRecord)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ExecutionRecord)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ExecutionRecord)
