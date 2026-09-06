---
source_url: https://docs.aws.amazon.com/b2bi/latest/APIReference/API_EdiType.html
---

# EdiType
<a name="API_EdiType"></a>

Specifies the details for the EDI standard that is being used for the transformer. Currently, only X12 is supported. X12 is a set of standards and corresponding messages that define specific business documents.

## Contents
<a name="API_EdiType_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** x12Details **   <a name="b2bi-Type-EdiType-x12Details"></a>
Returns the details for the EDI standard that is being used for the transformer. Currently, only X12 is supported. X12 is a set of standards and corresponding messages that define specific business documents.
Type: [X12Details](API_X12Details.md) object
Required: No

## See Also
<a name="API_EdiType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/b2bi-2022-06-23/EdiType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/b2bi-2022-06-23/EdiType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/b2bi-2022-06-23/EdiType)
