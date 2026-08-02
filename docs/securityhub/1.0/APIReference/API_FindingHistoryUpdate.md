---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_FindingHistoryUpdate.html
---

# FindingHistoryUpdate
<a name="API_FindingHistoryUpdate"></a>

 An array of objects that provides details about a change to a finding, including the AWS Security Finding Format (ASFF) field that changed, the value of the field before the change, and the value of the field after the change.

## Contents
<a name="API_FindingHistoryUpdate_Contents"></a>

 ** NewValue **   <a name="securityhub-Type-FindingHistoryUpdate-NewValue"></a>
 The value of the ASFF field after the finding change event. To preserve storage and readability, Security Hub CSPM omits this value if [https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_FindingHistoryRecord.html](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_FindingHistoryRecord.html) exceeds database limits.
Type: String
Pattern: `.*\S.*`
Required: No

 ** OldValue **   <a name="securityhub-Type-FindingHistoryUpdate-OldValue"></a>
 The value of the ASFF field before the finding change event.
Type: String
Pattern: `.*\S.*`
Required: No

 ** UpdatedField **   <a name="securityhub-Type-FindingHistoryUpdate-UpdatedField"></a>
 The ASFF field that changed during the finding change event.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_FindingHistoryUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/FindingHistoryUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/FindingHistoryUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/FindingHistoryUpdate)
