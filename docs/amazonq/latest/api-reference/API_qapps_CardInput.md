---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_CardInput.html
---

# CardInput
<a name="API_qapps_CardInput"></a>

The properties defining an input card in an Amazon Q App.

## Contents
<a name="API_qapps_CardInput_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** fileUpload **   <a name="qbusiness-Type-qapps_CardInput-fileUpload"></a>
A container for the properties of the file upload input card.
Type: [FileUploadCardInput](API_qapps_FileUploadCardInput.md) object
Required: No

 ** formInput **   <a name="qbusiness-Type-qapps_CardInput-formInput"></a>
A container for the properties of the form input card.
Type: [FormInputCardInput](API_qapps_FormInputCardInput.md) object
Required: No

 ** qPlugin **   <a name="qbusiness-Type-qapps_CardInput-qPlugin"></a>
A container for the properties of the plugin input card.
Type: [QPluginCardInput](API_qapps_QPluginCardInput.md) object
Required: No

 ** qQuery **   <a name="qbusiness-Type-qapps_CardInput-qQuery"></a>
A container for the properties of the query input card.
Type: [QQueryCardInput](API_qapps_QQueryCardInput.md) object
Required: No

 ** textInput **   <a name="qbusiness-Type-qapps_CardInput-textInput"></a>
A container for the properties of the text input card.
Type: [TextInputCardInput](API_qapps_TextInputCardInput.md) object
Required: No

## See Also
<a name="API_qapps_CardInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qapps-2023-11-27/CardInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qapps-2023-11-27/CardInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qapps-2023-11-27/CardInput)
