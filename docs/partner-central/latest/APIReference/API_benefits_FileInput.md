---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_benefits_FileInput.html
---

# FileInput
<a name="API_benefits_FileInput"></a>

Represents input information for uploading a file to a benefit application.

## Contents
<a name="API_benefits_FileInput_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** FileURI **   <a name="AWSPartnerCentral-Type-benefits_FileInput-FileURI"></a>
The URI or location where the file should be stored or has been uploaded.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `(s3://|https://).*`
Required: Yes

 ** BusinessUseCase **   <a name="AWSPartnerCentral-Type-benefits_FileInput-BusinessUseCase"></a>
The business purpose or use case that this file supports in the benefit application.
Type: String
Required: No

## See Also
<a name="API_benefits_FileInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-benefits-2018-05-10/FileInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-benefits-2018-05-10/FileInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-benefits-2018-05-10/FileInput)
