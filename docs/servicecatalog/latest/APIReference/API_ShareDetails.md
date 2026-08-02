---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_ShareDetails.html
---

# ShareDetails
<a name="API_ShareDetails"></a>

Information about the portfolio share operation.

## Contents
<a name="API_ShareDetails_Contents"></a>

 ** ShareErrors **   <a name="servicecatalog-Type-ShareDetails-ShareErrors"></a>
List of errors.
Type: Array of [ShareError](API_ShareError.md) objects
Required: No

 ** SuccessfulShares **   <a name="servicecatalog-Type-ShareDetails-SuccessfulShares"></a>
List of accounts for whom the operation succeeded.
Type: Array of strings
Pattern: `^[0-9]{12}$`
Required: No

## See Also
<a name="API_ShareDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/ShareDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/ShareDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/ShareDetails)
