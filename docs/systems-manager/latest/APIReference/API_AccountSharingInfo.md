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
