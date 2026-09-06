---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_StatusReason.html
---

# StatusReason
<a name="API_StatusReason"></a>

Provides additional context for the value of `Compliance.Status`.

## Contents
<a name="API_StatusReason_Contents"></a>

 ** ReasonCode **   <a name="securityhub-Type-StatusReason-ReasonCode"></a>
A code that represents a reason for the control status. For the list of status reason codes and their meanings, see [Compliance details for control findings](https://docs.aws.amazon.com/securityhub/latest/userguide/controls-findings-create-update.html#control-findings-asff-compliance) in the * AWS Security Hub CSPM User Guide*.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** Description **   <a name="securityhub-Type-StatusReason-Description"></a>
The corresponding description for the status reason code.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_StatusReason_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/StatusReason)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/StatusReason)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/StatusReason)
