---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_BulkJobResult.html
---

# BulkJobResult

The outcome of processing a single record within a bulk job. It identifies the record and, when the record didn't succeed, carries an error code and message.

## Contents
<a name="API_BulkJobResult_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** RequestId **   <a name="AWSPartnerCentral-Type-BulkJobResult-RequestId"></a>
The identifier of the record in the bulk job file.
Type: String
Required: Yes

 ** Status **   <a name="AWSPartnerCentral-Type-BulkJobResult-Status"></a>
The outcome of processing the record.
Type: String
Valid Values: `SUCCEEDED | FAILED`
Required: Yes

 ** ErrorCode **   <a name="AWSPartnerCentral-Type-BulkJobResult-ErrorCode"></a>
A code that identifies why the record failed. Present only when the record failed.
Type: String
Required: No

 ** ErrorMessage **   <a name="AWSPartnerCentral-Type-BulkJobResult-ErrorMessage"></a>
A description of why the record failed. Present only when the record failed.
Type: String
Required: No

 ** ResourceIdentifier **   <a name="AWSPartnerCentral-Type-BulkJobResult-ResourceIdentifier"></a>
This value is the identifier of the resource that Partner Central created or updated for the record. A failed record includes this value when Partner Central created the resource before the failure.
Type: String
Required: No

## See Also
<a name="API_BulkJobResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/BulkJobResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/BulkJobResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/BulkJobResult)
