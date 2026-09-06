---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_Card.html
---

# Card
<a name="API_qapps_Card"></a>

A card representing a component or step in an Amazon Q App's flow.

## Contents
<a name="API_qapps_Card_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** fileUpload **   <a name="qbusiness-Type-qapps_Card-fileUpload"></a>
A container for the properties of the file upload card.
Type: [FileUploadCard](API_qapps_FileUploadCard.md) object
Required: No

 ** formInput **   <a name="qbusiness-Type-qapps_Card-formInput"></a>
A container for the properties of the form input card.
Type: [FormInputCard](API_qapps_FormInputCard.md) object
Required: No

 ** qPlugin **   <a name="qbusiness-Type-qapps_Card-qPlugin"></a>
A container for the properties of the plugin card.
Type: [QPluginCard](API_qapps_QPluginCard.md) object
Required: No

 ** qQuery **   <a name="qbusiness-Type-qapps_Card-qQuery"></a>
A container for the properties of the query card.
Type: [QQueryCard](API_qapps_QQueryCard.md) object
Required: No

 ** textInput **   <a name="qbusiness-Type-qapps_Card-textInput"></a>
A container for the properties of the text input card.
Type: [TextInputCard](API_qapps_TextInputCard.md) object
Required: No

## See Also
<a name="API_qapps_Card_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qapps-2023-11-27/Card)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qapps-2023-11-27/Card)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qapps-2023-11-27/Card)
