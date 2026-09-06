---
source_url: https://docs.aws.amazon.com/awscloudtraildata/latest/APIReference/API_ResultErrorEntry.html
---

# ResultErrorEntry
<a name="API_ResultErrorEntry"></a>

Includes the error code and error message for events that could not be ingested by CloudTrail.

## Contents
<a name="API_ResultErrorEntry_Contents"></a>

 ** errorCode **   <a name="awscloudtraildata-Type-ResultErrorEntry-errorCode"></a>
The error code for events that could not be ingested by CloudTrail. Possible error codes include: `FieldTooLong`, `FieldNotFound`, `InvalidChecksum`, `InvalidData`, `InvalidRecipient`, `InvalidEventSource`, `AccountNotSubscribed`, `Throttling`, and `InternalFailure`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** errorMessage **   <a name="awscloudtraildata-Type-ResultErrorEntry-errorMessage"></a>
The message that describes the error for events that could not be ingested by CloudTrail.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** id **   <a name="awscloudtraildata-Type-ResultErrorEntry-id"></a>
The original event ID from the source event that could not be ingested by CloudTrail.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[-_A-Za-z0-9]+`
Required: Yes

## See Also
<a name="API_ResultErrorEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-data-2021-08-11/ResultErrorEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-data-2021-08-11/ResultErrorEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-data-2021-08-11/ResultErrorEntry)
