---
source_url: https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_MobileDeviceManagement.html
---

# MobileDeviceManagement
<a name="API_MobileDeviceManagement"></a>

If you don't supply a value, by default Connector for SCEP creates a connector for general-purpose use. A general-purpose connector is designed to work with clients or endpoints that support the SCEP protocol, except Connector for SCEP for Microsoft Intune. For information about considerations and limitations with using Connector for SCEP, see [Considerations and Limitations](https://docs.aws.amazon.com/privateca/latest/userguide/scep-connector.htmlc4scep-considerations-limitations.html).

If you provide an `IntuneConfiguration`, Connector for SCEP creates a connector for use with Microsoft Intune, and you manage the challenge passwords using Microsoft Intune. For more information, see [Using Connector for SCEP for Microsoft Intune](https://docs.aws.amazon.com/privateca/latest/userguide/scep-connector.htmlconnector-for-scep-intune.html).

## Contents
<a name="API_MobileDeviceManagement_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** Intune **   <a name="pcaconnectorscep-Type-MobileDeviceManagement-Intune"></a>
Configuration settings for use with Microsoft Intune. For information about using Connector for SCEP for Microsoft Intune, see [Using Connector for SCEP for Microsoft Intune](https://docs.aws.amazon.com/privateca/latest/userguide/scep-connector.htmlconnector-for-scep-intune.html).
Type: [IntuneConfiguration](API_IntuneConfiguration.md) object
Required: No

## See Also
<a name="API_MobileDeviceManagement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pca-connector-scep-2018-05-10/MobileDeviceManagement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pca-connector-scep-2018-05-10/MobileDeviceManagement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pca-connector-scep-2018-05-10/MobileDeviceManagement)
