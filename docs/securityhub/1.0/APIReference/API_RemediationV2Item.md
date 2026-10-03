---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_RemediationV2Item.html
---

# RemediationV2Item
<a name="API_RemediationV2Item"></a>

A remediation target.

## Contents
<a name="API_RemediationV2Item_Contents"></a>

 ** Outcome **   <a name="securityhub-Type-RemediationV2Item-Outcome"></a>
The outcome of the remediation target's resolution.
Type: [RemediationOutcome](API_RemediationOutcome.md) object
Required: Yes

 ** Priority **   <a name="securityhub-Type-RemediationV2Item-Priority"></a>
The remediation target's priority. Valid values are `Critical`, `High`, `Medium`, and `Low`.
Type: String
Valid Values: `Critical | High | Medium | Low`
Required: Yes

 ** RemediationSummary **   <a name="securityhub-Type-RemediationV2Item-RemediationSummary"></a>
A summary of the remediation target.
Type: [RemediationSummaryDetail](API_RemediationSummaryDetail.md) object
Required: Yes

 ** Resource **   <a name="securityhub-Type-RemediationV2Item-Resource"></a>
The remediation target's associated resource.
Type: [RemediationResource](API_RemediationResource.md) object
Required: Yes

 ** Status **   <a name="securityhub-Type-RemediationV2Item-Status"></a>
The current status of the remediation target.
+  `New` specifies that the remediation target was newly identified.
+  `Updated` specifies that the remediation target changed after it was identified.
+  `Resolved` specifies that the remediation target is no longer present.
Type: String
Valid Values: `New | Updated | Resolved`
Required: Yes

 ** TargetUid **   <a name="securityhub-Type-RemediationV2Item-TargetUid"></a>
The unique identifier (ID) of the remediation target.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** Trait **   <a name="securityhub-Type-RemediationV2Item-Trait"></a>
The trait associated with the remediation target.
Type: [RemediationTrait](API_RemediationTrait.md) object
Required: Yes

 ** Guidance **   <a name="securityhub-Type-RemediationV2Item-Guidance"></a>
The remediation target's guidance. Returned only when `ShowGuidance` is `true` in the request.
Type: [RemediationGuidance](API_RemediationGuidance.md) object
Required: No

 ** UpdatedAt **   <a name="securityhub-Type-RemediationV2Item-UpdatedAt"></a>
The remediation target's last updated timestamp.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: Timestamp
Required: No

## See Also
<a name="API_RemediationV2Item_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/RemediationV2Item)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/RemediationV2Item)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/RemediationV2Item)
