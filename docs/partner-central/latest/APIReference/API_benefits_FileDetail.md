---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_benefits_FileDetail.html
---

# FileDetail
<a name="API_benefits_FileDetail"></a>

Represents detailed information about a file attached to a benefit application.

## Contents
<a name="API_benefits_FileDetail_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** FileURI **   <a name="AWSPartnerCentral-Type-benefits_FileDetail-FileURI"></a>
The URI or location where the file is stored.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `(s3://|https://).*`
Required: Yes

 ** BusinessUseCase **   <a name="AWSPartnerCentral-Type-benefits_FileDetail-BusinessUseCase"></a>
The business purpose or use case that this file supports in the benefit application.
Type: String
Required: No

 ** CreatedAt **   <a name="AWSPartnerCentral-Type-benefits_FileDetail-CreatedAt"></a>
The timestamp when the file was uploaded.
Type: Timestamp
Required: No

 ** CreatedBy **   <a name="AWSPartnerCentral-Type-benefits_FileDetail-CreatedBy"></a>
The identifier of the user who uploaded the file.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** FileName **   <a name="AWSPartnerCentral-Type-benefits_FileDetail-FileName"></a>
The original name of the uploaded file.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** FileStatus **   <a name="AWSPartnerCentral-Type-benefits_FileDetail-FileStatus"></a>
The current processing status of the file (e.g., uploaded, processing, approved, rejected).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: No

 ** FileStatusReason **   <a name="AWSPartnerCentral-Type-benefits_FileDetail-FileStatusReason"></a>
The reason for that particulat file status.
Type: String
Required: No

 ** FileType **   <a name="AWSPartnerCentral-Type-benefits_FileDetail-FileType"></a>
The type or category of the file (e.g., document, image, spreadsheet).
Type: String
Valid Values: `application/msword | application/vnd.openxmlformats-officedocument.wordprocessingml.document | application/vnd.openxmlformats-officedocument.spreadsheetml.sheet | application/vnd.openxmlformats-officedocument.presentationml.presentation | application/pdf | image/png | image/jpeg | image/svg+xml | text/csv`
Required: No

## See Also
<a name="API_benefits_FileDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-benefits-2018-05-10/FileDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-benefits-2018-05-10/FileDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-benefits-2018-05-10/FileDetail)
