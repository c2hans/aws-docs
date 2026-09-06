---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ActionRemotePortDetails.html
---

# ActionRemotePortDetails
<a name="API_ActionRemotePortDetails"></a>

Provides information about the remote port that was involved in an attempted network connection.

## Contents
<a name="API_ActionRemotePortDetails_Contents"></a>

 ** Port **   <a name="securityhub-Type-ActionRemotePortDetails-Port"></a>
The number of the port.
Type: Integer
Required: No

 ** PortName **   <a name="securityhub-Type-ActionRemotePortDetails-PortName"></a>
The port name of the remote connection.
Length Constraints: 128.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_ActionRemotePortDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ActionRemotePortDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ActionRemotePortDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ActionRemotePortDetails)
