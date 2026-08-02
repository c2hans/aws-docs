---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_FindingHistoryRecord.html
---

# FindingHistoryRecord
<a name="API_FindingHistoryRecord"></a>

 A list of events that changed the specified finding during the specified time period. Each record represents a single finding change event.

## Contents
<a name="API_FindingHistoryRecord_Contents"></a>

 ** FindingCreated **   <a name="securityhub-Type-FindingHistoryRecord-FindingCreated"></a>
 Identifies whether the event marks the creation of a new finding. A value of `True` means that the finding is newly created. A value of `False` means that the finding isn’t newly created.
Type: Boolean
Required: No

 ** FindingIdentifier **   <a name="securityhub-Type-FindingHistoryRecord-FindingIdentifier"></a>
Identifies which finding to get the finding history for.
Type: [AwsSecurityFindingIdentifier](API_AwsSecurityFindingIdentifier.md) object
Required: No

 ** NextToken **   <a name="securityhub-Type-FindingHistoryRecord-NextToken"></a>
 A token for pagination purposes. Provide this token in the subsequent request to [https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetFindingsHistory.html](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetFindingsHistory.html) to get up to an additional 100 results of history for the same finding that you specified in your initial request.
Type: String
Required: No

 ** Updates **   <a name="securityhub-Type-FindingHistoryRecord-Updates"></a>
 An array of objects that provides details about the finding change event, including the AWS Security Finding Format (ASFF) field that changed, the value of the field before the change, and the value of the field after the change.
Type: Array of [FindingHistoryUpdate](API_FindingHistoryUpdate.md) objects
Required: No

 ** UpdateSource **   <a name="securityhub-Type-FindingHistoryRecord-UpdateSource"></a>
 Identifies the source of the event that changed the finding. For example, an integrated AWS service or third-party partner integration may call [https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchImportFindings.html](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchImportFindings.html), or an AWS Security Hub CSPM customer may call [https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchUpdateFindings.html](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchUpdateFindings.html).
Type: [FindingHistoryUpdateSource](API_FindingHistoryUpdateSource.md) object
Required: No

 ** UpdateTime **   <a name="securityhub-Type-FindingHistoryRecord-UpdateTime"></a>
 A timestamp that indicates when Security Hub CSPM processed the updated finding record.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: Timestamp
Required: No

## See Also
<a name="API_FindingHistoryRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/FindingHistoryRecord)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/FindingHistoryRecord)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/FindingHistoryRecord)
