---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_AWSAccount.html
---

# AWSAccount
<a name="API_AWSAccount"></a>

 The wrapper of AWS account details, such as account ID or email address.

## Contents
<a name="API_AWSAccount_Contents"></a>

 ** emailAddress **   <a name="auditmanager-Type-AWSAccount-emailAddress"></a>
 The email address that's associated with the AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 320.
Pattern: `^.*@.*$`
Required: No

 ** id **   <a name="auditmanager-Type-AWSAccount-id"></a>
 The identifier for the AWS account.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: No

 ** name **   <a name="auditmanager-Type-AWSAccount-name"></a>
 The name of the AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `^[\u0020-\u007E]+$`
Required: No

## See Also
<a name="API_AWSAccount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/AWSAccount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/AWSAccount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/AWSAccount)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Audit Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query audit-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
