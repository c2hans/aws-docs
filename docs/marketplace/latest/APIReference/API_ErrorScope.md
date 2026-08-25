---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_ErrorScope.html
---

# ErrorScope
<a name="API_ErrorScope"></a>

A name-value pair that identifies the resource or attribute that a `ControlError` applies to.

## Contents
<a name="API_ErrorScope_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Name **   <a name="AWSMarketplaceService-Type-ErrorScope-Name"></a>
The name of the resource field the error applies to (for example, `AMI_ID`, `FILE_PATH`, or `PACKAGE_NAME`).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: No

 ** Value **   <a name="AWSMarketplaceService-Type-ErrorScope-Value"></a>
The value of the resource field the error applies to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_ErrorScope_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/ErrorScope)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/ErrorScope)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/ErrorScope)
