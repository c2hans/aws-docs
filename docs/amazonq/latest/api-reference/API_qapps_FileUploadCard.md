---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_FileUploadCard.html
---

# FileUploadCard
<a name="API_qapps_FileUploadCard"></a>

A card in an Amazon Q App that allows the user to upload a file.

## Contents
<a name="API_qapps_FileUploadCard_Contents"></a>

 ** dependencies **   <a name="qbusiness-Type-qapps_FileUploadCard-dependencies"></a>
Any dependencies or requirements for the file upload card.
Type: Array of strings
Required: Yes

 ** id **   <a name="qbusiness-Type-qapps_FileUploadCard-id"></a>
The unique identifier of the file upload card.
Type: String
Pattern: `[\da-f]{8}-[\da-f]{4}-[45][\da-f]{3}-[89ABab][\da-f]{3}-[\da-f]{12}`
Required: Yes

 ** title **   <a name="qbusiness-Type-qapps_FileUploadCard-title"></a>
The title of the file upload card.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `[^{}\\"<>]+`
Required: Yes

 ** type **   <a name="qbusiness-Type-qapps_FileUploadCard-type"></a>
The type of the card.
Type: String
Valid Values: `text-input | q-query | file-upload | q-plugin | form-input`
Required: Yes

 ** allowOverride **   <a name="qbusiness-Type-qapps_FileUploadCard-allowOverride"></a>
A flag indicating if the user can override the default file for the upload card.
Type: Boolean
Required: No

 ** fileId **   <a name="qbusiness-Type-qapps_FileUploadCard-fileId"></a>
The unique identifier of the file associated with the card.
Type: String
Required: No

 ** filename **   <a name="qbusiness-Type-qapps_FileUploadCard-filename"></a>
The name of the file being uploaded.
Type: String
Required: No

## See Also
<a name="API_qapps_FileUploadCard_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qapps-2023-11-27/FileUploadCard)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qapps-2023-11-27/FileUploadCard)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qapps-2023-11-27/FileUploadCard)
