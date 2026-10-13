---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_RecordExpirySpecification.html
---

# RecordExpirySpecification
<a name="API_RecordExpirySpecification"></a>

Specifies the record expiry (long-term memory time-to-live) applied to the records in a batch request. Provide exactly one of `recordExpiryDurationDays` or `action`. Set `recordExpiryDurationDays` to configure or update the expiry, or set `action` to `REMOVE` to remove a previously configured expiry.

## Contents
<a name="API_RecordExpirySpecification_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** action **   <a name="BedrockAgentCore-Type-RecordExpirySpecification-action"></a>
The action to apply to the existing record expiry configuration. Set to `REMOVE` to remove a previously configured expiry so that the records no longer expire. This value does not apply when creating records.
Type: String
Valid Values: `REMOVE`
Required: No

 ** recordExpiryDurationDays **   <a name="BedrockAgentCore-Type-RecordExpirySpecification-recordExpiryDurationDays"></a>
The duration, in days, after which the records in this request expire. The minimum is 31 days.
Type: Integer
Valid Range: Minimum value of 31.
Required: No

## See Also
<a name="API_RecordExpirySpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/RecordExpirySpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/RecordExpirySpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/RecordExpirySpecification)
