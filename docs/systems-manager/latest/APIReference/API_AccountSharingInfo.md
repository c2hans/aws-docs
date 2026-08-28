---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_AccountSharingInfo.html
---

# AccountSharingInfo
<a name="API_AccountSharingInfo"></a>

Information includes the AWS account ID where the current document is shared and the version shared with that account.

## Contents
<a name="API_AccountSharingInfo_Contents"></a>

 ** AccountId **   <a name="systemsmanager-Type-AccountSharingInfo-AccountId"></a>
The AWS account ID where the current document is shared.
Type: String
Pattern: `(?i)all|[0-9]{12}`
Required: No

 ** SharedDocumentVersion **   <a name="systemsmanager-Type-AccountSharingInfo-SharedDocumentVersion"></a>
The version of the current document shared with the account.
Type: String
Length Constraints: Maximum length of 8.
Pattern: `([$]LATEST|[$]DEFAULT|[$]ALL)`
Required: No

## See Also
<a name="API_AccountSharingInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/AccountSharingInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/AccountSharingInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/AccountSharingInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
