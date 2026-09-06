---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_INDTaxDocuments.html
---

# INDTaxDocuments
<a name="API_INDTaxDocuments"></a>

**Note**
 AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

The tax documents required in AWS Region in India.

## Contents
<a name="API_INDTaxDocuments_Contents"></a>

 ** GSTIN **   <a name="Snowball-Type-INDTaxDocuments-GSTIN"></a>
The Goods and Services Tax (GST) documents required in AWS Region in India.
Type: String
Length Constraints: Fixed length of 15.
Pattern: `\d{2}[A-Z]{5}\d{4}[A-Z]{1}[A-Z\d]{1}[Z]{1}[A-Z\d]{1}`
Required: No

## See Also
<a name="API_INDTaxDocuments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snowball-2016-06-30/INDTaxDocuments)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snowball-2016-06-30/INDTaxDocuments)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snowball-2016-06-30/INDTaxDocuments)
