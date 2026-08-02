---
source_url: https://docs.aws.amazon.com/data-exchange/latest/apireference/API_LFTagPolicyDetails.html
---

# LFTagPolicyDetails
<a name="API_LFTagPolicyDetails"></a>

Details about the LF-tag policy.

## Contents
<a name="API_LFTagPolicyDetails_Contents"></a>

 ** CatalogId **   <a name="dataexchange-Type-LFTagPolicyDetails-CatalogId"></a>
The identifier for the AWS Glue Data Catalog.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `.*/^[\d]{12}$/.*`
Required: Yes

 ** ResourceDetails **   <a name="dataexchange-Type-LFTagPolicyDetails-ResourceDetails"></a>
Details for the Lake Formation Resources included in the LF-tag policy.
Type: [LFResourceDetails](API_LFResourceDetails.md) object
Required: Yes

 ** ResourceType **   <a name="dataexchange-Type-LFTagPolicyDetails-ResourceType"></a>
The resource type for which the LF-tag policy applies.
Type: String
Valid Values: `TABLE | DATABASE`
Required: Yes

## See Also
<a name="API_LFTagPolicyDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dataexchange-2017-07-25/LFTagPolicyDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dataexchange-2017-07-25/LFTagPolicyDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dataexchange-2017-07-25/LFTagPolicyDetails)
