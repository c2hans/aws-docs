---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_BatchDescribeErrorDetail.html
---

# BatchDescribeErrorDetail
<a name="API_BatchDescribeErrorDetail"></a>

An object that contains an error code and error message.

## Contents
<a name="API_BatchDescribeErrorDetail_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ErrorCode **   <a name="AWSMarketplaceService-Type-BatchDescribeErrorDetail-ErrorCode"></a>
The error code returned.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 72.
Pattern: `^[a-zA-Z_]+$`
Required: No

 ** ErrorMessage **   <a name="AWSMarketplaceService-Type-BatchDescribeErrorDetail-ErrorMessage"></a>
The error message returned.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^(.)+$`
Required: No

## See Also
<a name="API_BatchDescribeErrorDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/BatchDescribeErrorDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/BatchDescribeErrorDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/BatchDescribeErrorDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
