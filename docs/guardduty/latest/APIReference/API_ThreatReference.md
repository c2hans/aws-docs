---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ThreatReference.html
---

# ThreatReference
<a name="API_ThreatReference"></a>

Contains a reference to a MITRE ATT&CK tactic or technique.

## Contents
<a name="API_ThreatReference_Contents"></a>

 ** name **   <a name="guardduty-Type-ThreatReference-name"></a>
The name of the tactic or technique.
Type: String
Required: No

 ** uid **   <a name="guardduty-Type-ThreatReference-uid"></a>
The MITRE ATT&CK identifier of the tactic or technique, such as `TA0002` or `T1059.004`.
Type: String
Pattern: `(TA|T)\d{4}(\.\d{3})?`
Required: No

## See Also
<a name="API_ThreatReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/ThreatReference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/ThreatReference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/ThreatReference)
