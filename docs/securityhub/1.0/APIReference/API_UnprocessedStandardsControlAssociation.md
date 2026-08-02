---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_UnprocessedStandardsControlAssociation.html
---

# UnprocessedStandardsControlAssociation
<a name="API_UnprocessedStandardsControlAssociation"></a>

 Provides details about which control's enablement status couldn't be retrieved in a specified standard when calling [BatchUpdateStandardsControlAssociations](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchUpdateStandardsControlAssociations.html). This parameter also provides details about why the request was unprocessed.

## Contents
<a name="API_UnprocessedStandardsControlAssociation_Contents"></a>

 ** ErrorCode **   <a name="securityhub-Type-UnprocessedStandardsControlAssociation-ErrorCode"></a>
The error code for the unprocessed standard and control association. The `NOT_FOUND` value has been deprecated and replaced by the `RESOURCE_NOT_FOUND` value.
Type: String
Valid Values: `INVALID_INPUT | ACCESS_DENIED | NOT_FOUND | RESOURCE_NOT_FOUND | LIMIT_EXCEEDED`
Required: Yes

 ** StandardsControlAssociationId **   <a name="securityhub-Type-UnprocessedStandardsControlAssociation-StandardsControlAssociationId"></a>
 An array with one or more objects that includes a security control (identified with `SecurityControlId`, `SecurityControlArn`, or a mix of both parameters) and the Amazon Resource Name (ARN) of a standard. This parameter shows the specific controls for which the enablement status couldn't be retrieved in specified standards when calling [BatchUpdateStandardsControlAssociations](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchUpdateStandardsControlAssociations.html).
Type: [StandardsControlAssociationId](API_StandardsControlAssociationId.md) object
Required: Yes

 ** ErrorReason **   <a name="securityhub-Type-UnprocessedStandardsControlAssociation-ErrorReason"></a>
The reason why the standard and control association was unprocessed.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_UnprocessedStandardsControlAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/UnprocessedStandardsControlAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/UnprocessedStandardsControlAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/UnprocessedStandardsControlAssociation)
