---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsIamAccessKeySessionContextAttributes.html
---

# AwsIamAccessKeySessionContextAttributes
<a name="API_AwsIamAccessKeySessionContextAttributes"></a>

Attributes of the session that the key was used for.

## Contents
<a name="API_AwsIamAccessKeySessionContextAttributes_Contents"></a>

 ** CreationDate **   <a name="securityhub-Type-AwsIamAccessKeySessionContextAttributes-CreationDate"></a>
Indicates when the session was created.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** MfaAuthenticated **   <a name="securityhub-Type-AwsIamAccessKeySessionContextAttributes-MfaAuthenticated"></a>
Indicates whether the session used multi-factor authentication (MFA).
Type: Boolean
Required: No

## See Also
<a name="API_AwsIamAccessKeySessionContextAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsIamAccessKeySessionContextAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsIamAccessKeySessionContextAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsIamAccessKeySessionContextAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
