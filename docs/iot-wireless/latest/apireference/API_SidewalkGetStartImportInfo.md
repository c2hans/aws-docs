---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_SidewalkGetStartImportInfo.html
---

# SidewalkGetStartImportInfo
<a name="API_SidewalkGetStartImportInfo"></a>

Sidewalk-related information for devices in an import task that are being onboarded.

## Contents
<a name="API_SidewalkGetStartImportInfo_Contents"></a>

 ** DeviceCreationFileList **   <a name="iotwireless-Type-SidewalkGetStartImportInfo-DeviceCreationFileList"></a>
List of Sidewalk devices that are added to the import task.
Type: Array of strings
Length Constraints: Maximum length of 1024.
Required: No

 ** Positioning **   <a name="iotwireless-Type-SidewalkGetStartImportInfo-Positioning"></a>
The Positioning object of the Sidewalk device.
Type: [SidewalkPositioning](API_SidewalkPositioning.md) object
Required: No

 ** Role **   <a name="iotwireless-Type-SidewalkGetStartImportInfo-Role"></a>
The IAM role that allows AWS IoT Wireless to access the CSV file in the S3 bucket.
Type: String
Length Constraints: Maximum length of 2048.
Required: No

## See Also
<a name="API_SidewalkGetStartImportInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/SidewalkGetStartImportInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/SidewalkGetStartImportInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/SidewalkGetStartImportInfo)
