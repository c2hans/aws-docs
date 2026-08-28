---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_WebACLHasIncompatibleConfigurationViolation.html
---

# WebACLHasIncompatibleConfigurationViolation
<a name="API_WebACLHasIncompatibleConfigurationViolation"></a>

The violation details for a web ACL whose configuration is incompatible with the Firewall Manager policy.

## Contents
<a name="API_WebACLHasIncompatibleConfigurationViolation_Contents"></a>

 ** Description **   <a name="fms-Type-WebACLHasIncompatibleConfigurationViolation-Description"></a>
Information about the problems that Firewall Manager encountered with the web ACL configuration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** WebACLArn **   <a name="fms-Type-WebACLHasIncompatibleConfigurationViolation-WebACLArn"></a>
The Amazon Resource Name (ARN) of the web ACL.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## See Also
<a name="API_WebACLHasIncompatibleConfigurationViolation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/WebACLHasIncompatibleConfigurationViolation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/WebACLHasIncompatibleConfigurationViolation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/WebACLHasIncompatibleConfigurationViolation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for 1.0. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
