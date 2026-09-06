---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_UnprocessedStandardsControlAssociationUpdate.html
---

# UnprocessedStandardsControlAssociationUpdate
<a name="API_UnprocessedStandardsControlAssociationUpdate"></a>

Provides details about which control's enablement status could not be updated in a specified standard when calling the [BatchUpdateStandardsControlAssociations](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchUpdateStandardsControlAssociations.html) API. This parameter also provides details about why the request was unprocessed.

## Contents
<a name="API_UnprocessedStandardsControlAssociationUpdate_Contents"></a>

 ** ErrorCode **   <a name="securityhub-Type-UnprocessedStandardsControlAssociationUpdate-ErrorCode"></a>
The error code for the unprocessed update of the control's enablement status in the specified standard. The `NOT_FOUND` value has been deprecated and replaced by the `RESOURCE_NOT_FOUND` value.
Type: String
Valid Values: `INVALID_INPUT | ACCESS_DENIED | NOT_FOUND | RESOURCE_NOT_FOUND | LIMIT_EXCEEDED`
Required: Yes

 ** StandardsControlAssociationUpdate **   <a name="securityhub-Type-UnprocessedStandardsControlAssociationUpdate-StandardsControlAssociationUpdate"></a>
An array of control and standard associations for which an update failed when calling [BatchUpdateStandardsControlAssociations](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchUpdateStandardsControlAssociations.html).
Type: [StandardsControlAssociationUpdate](API_StandardsControlAssociationUpdate.md) object
Required: Yes

 ** ErrorReason **   <a name="securityhub-Type-UnprocessedStandardsControlAssociationUpdate-ErrorReason"></a>
The reason why a control's enablement status in the specified standard couldn't be updated.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_UnprocessedStandardsControlAssociationUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/UnprocessedStandardsControlAssociationUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/UnprocessedStandardsControlAssociationUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/UnprocessedStandardsControlAssociationUpdate)
