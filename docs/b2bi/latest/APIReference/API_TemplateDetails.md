---
source_url: https://docs.aws.amazon.com/b2bi/latest/APIReference/API_TemplateDetails.html
---

# TemplateDetails
<a name="API_TemplateDetails"></a>

A data structure that contains the information to use when generating a mapping template.

## Contents
<a name="API_TemplateDetails_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** x12 **   <a name="b2bi-Type-TemplateDetails-x12"></a>
A structure that contains the X12 transaction set and version. The X12 structure is used when the system transforms an EDI (electronic data interchange) file.
If an EDI input file contains more than one transaction, each transaction must have the same transaction set and version, for example 214/4010. If not, the transformer cannot parse the file.
Type: [X12Details](API_X12Details.md) object
Required: No

## See Also
<a name="API_TemplateDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/b2bi-2022-06-23/TemplateDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/b2bi-2022-06-23/TemplateDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/b2bi-2022-06-23/TemplateDetails)
