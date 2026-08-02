---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ActionLocalPortDetails.html
---

# ActionLocalPortDetails
<a name="API_ActionLocalPortDetails"></a>

For `NetworkConnectionAction` and `PortProbeDetails`, `LocalPortDetails` provides information about the local port that was involved in the action.

## Contents
<a name="API_ActionLocalPortDetails_Contents"></a>

 ** Port **   <a name="securityhub-Type-ActionLocalPortDetails-Port"></a>
The number of the port.
Type: Integer
Required: No

 ** PortName **   <a name="securityhub-Type-ActionLocalPortDetails-PortName"></a>
The port name of the local connection.
Length Constraints: 128.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_ActionLocalPortDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ActionLocalPortDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ActionLocalPortDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ActionLocalPortDetails)
