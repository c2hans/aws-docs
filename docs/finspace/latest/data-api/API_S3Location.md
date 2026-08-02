---
source_url: https://docs.aws.amazon.com/finspace/latest/data-api/API_S3Location.html
---

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/data-api/amazon-finspace-end-of-support.html).

# S3Location
<a name="API_S3Location"></a>

The location of an external Dataview in an S3 bucket.

## Contents
<a name="API_S3Location_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** bucket **   <a name="finspace-Type-S3Location-bucket"></a>
 The name of the S3 bucket.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `^.*\S.*$`
Required: Yes

 ** key **   <a name="finspace-Type-S3Location-key"></a>
 The path of the folder, within the S3 bucket that contains the Dataset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^.*\S.*$`
Required: Yes

## See Also
<a name="API_S3Location_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2020-07-13/S3Location)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2020-07-13/S3Location)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2020-07-13/S3Location)
