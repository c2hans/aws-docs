---
source_url: https://docs.aws.amazon.com/finspace/latest/data-api/API_AwsCredentials.html
---

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/data-api/amazon-finspace-end-of-support.html).

# AwsCredentials
<a name="API_AwsCredentials"></a>

 The credentials required to access the external Dataview from the S3 location.

## Contents
<a name="API_AwsCredentials_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** accessKeyId **   <a name="finspace-Type-AwsCredentials-accessKeyId"></a>
 The unique identifier for the security credentials.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\s\S]*\S[\s\S]*`
Required: No

 ** expiration **   <a name="finspace-Type-AwsCredentials-expiration"></a>
 The Epoch time when the current credentials expire.
Type: Long
Required: No

 ** secretAccessKey **   <a name="finspace-Type-AwsCredentials-secretAccessKey"></a>
 The secret access key that can be used to sign requests.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `[\s\S]*\S[\s\S]*`
Required: No

 ** sessionToken **   <a name="finspace-Type-AwsCredentials-sessionToken"></a>
 The token that users must pass to use the credentials.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `[\s\S]*\S[\s\S]*`
Required: No

## See Also
<a name="API_AwsCredentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2020-07-13/AwsCredentials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2020-07-13/AwsCredentials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2020-07-13/AwsCredentials)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FinSpace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query finspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
