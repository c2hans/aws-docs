---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_SidewalkStartImportInfo.html
---

# SidewalkStartImportInfo
<a name="API_SidewalkStartImportInfo"></a>

Information about an import task created for bulk provisioning.

## Contents
<a name="API_SidewalkStartImportInfo_Contents"></a>

 ** DeviceCreationFile **   <a name="iotwireless-Type-SidewalkStartImportInfo-DeviceCreationFile"></a>
The CSV file contained in an S3 bucket that's used for adding devices to an import task.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

 ** Positioning **   <a name="iotwireless-Type-SidewalkStartImportInfo-Positioning"></a>
The Positioning object of the Sidewalk device.
Type: [SidewalkPositioning](API_SidewalkPositioning.md) object
Required: No

 ** Role **   <a name="iotwireless-Type-SidewalkStartImportInfo-Role"></a>
The IAM role that allows AWS IoT Wireless to access the CSV file in the S3 bucket.
Type: String
Length Constraints: Maximum length of 2048.
Required: No

## See Also
<a name="API_SidewalkStartImportInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/SidewalkStartImportInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/SidewalkStartImportInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/SidewalkStartImportInfo)
