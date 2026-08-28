---
source_url: https://docs.aws.amazon.com/security-lake/latest/APIReference/API_AwsIdentity.html
---

# AwsIdentity
<a name="API_AwsIdentity"></a>

The AWS identity.

## Contents
<a name="API_AwsIdentity_Contents"></a>

 ** externalId **   <a name="securitylake-Type-AwsIdentity-externalId"></a>
The external ID used to establish trust relationship with the AWS identity.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 1224.
Pattern: `[\w+=,.@:\/-]*`
Required: Yes

 ** principal **   <a name="securitylake-Type-AwsIdentity-principal"></a>
The AWS identity principal.
Type: String
Pattern: `([0-9]{12}|[a-z0-9\.\-]*\.(amazonaws|amazon)\.com)`
Required: Yes

## See Also
<a name="API_AwsIdentity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securitylake-2018-05-10/AwsIdentity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securitylake-2018-05-10/AwsIdentity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securitylake-2018-05-10/AwsIdentity)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Security Lake. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query security-lake` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
