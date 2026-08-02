---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_TemplateSSMDocumentDetails.html
---

# TemplateSSMDocumentDetails
<a name="API_TemplateSSMDocumentDetails"></a>

This API allows you to create a conformance pack template with an AWS Systems Manager document (SSM document). To deploy a conformance pack using an SSM document, first create an SSM document with conformance pack content, and then provide the `DocumentName` in the [PutConformancePack API](https://docs.aws.amazon.com/config/latest/APIReference/API_PutConformancePack.html). You can also provide the `DocumentVersion`.

The `TemplateSSMDocumentDetails` object contains the name of the SSM document and the version of the SSM document.

## Contents
<a name="API_TemplateSSMDocumentDetails_Contents"></a>

 ** DocumentName **   <a name="config-Type-TemplateSSMDocumentDetails-DocumentName"></a>
The name or Amazon Resource Name (ARN) of the SSM document to use to create a conformance pack. If you use the document name, AWS Config checks only your account and AWS Region for the SSM document.
Type: String
Pattern: `^[a-zA-Z0-9_\-.:/]{3,200}$`
Required: Yes

 ** DocumentVersion **   <a name="config-Type-TemplateSSMDocumentDetails-DocumentVersion"></a>
The version of the SSM document to use to create a conformance pack. By default, AWS Config uses the latest version.
This field is optional.
Type: String
Pattern: `([$]LATEST|[$]DEFAULT|^[1-9][0-9]*$)`
Required: No

## See Also
<a name="API_TemplateSSMDocumentDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/TemplateSSMDocumentDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/TemplateSSMDocumentDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/TemplateSSMDocumentDetails)
