---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_OTAUpdateFile.html
---

# OTAUpdateFile
<a name="API_OTAUpdateFile"></a>

Describes a file to be associated with an OTA update.

## Contents
<a name="API_OTAUpdateFile_Contents"></a>

 ** attributes **   <a name="iot-Type-OTAUpdateFile-attributes"></a>
A list of name-attribute pairs. They won't be sent to devices as a part of the Job document.
Type: String to string map
Value Length Constraints: Minimum length of 0. Maximum length of 4096.
Value Pattern: `[\s\S]*`
Required: No

 ** codeSigning **   <a name="iot-Type-OTAUpdateFile-codeSigning"></a>
The code signing method of the file.
Type: [CodeSigning](API_CodeSigning.md) object
Required: No

 ** fileLocation **   <a name="iot-Type-OTAUpdateFile-fileLocation"></a>
The location of the updated firmware.
Type: [FileLocation](API_FileLocation.md) object
Required: No

 ** fileName **   <a name="iot-Type-OTAUpdateFile-fileName"></a>
The name of the file.
Type: String
Required: No

 ** fileType **   <a name="iot-Type-OTAUpdateFile-fileType"></a>
An integer value you can include in the job document to allow your devices to identify the type of file received from the cloud.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 255.
Required: No

 ** fileVersion **   <a name="iot-Type-OTAUpdateFile-fileVersion"></a>
The file version.
Type: String
Required: No

## See Also
<a name="API_OTAUpdateFile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/OTAUpdateFile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/OTAUpdateFile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/OTAUpdateFile)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
