---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_AccountLink.html
---

# AccountLink
<a name="API_AccountLink"></a>

Information about about the account link.

## Contents
<a name="API_AccountLink_Contents"></a>

 ** AccountLinkId **   <a name="WorkSpaces-Type-AccountLink-AccountLinkId"></a>
The identifier of the account link.
Type: String
Pattern: `^link-.{8,24}$`
Required: No

 ** AccountLinkStatus **   <a name="WorkSpaces-Type-AccountLink-AccountLinkStatus"></a>
The status of the account link.
Type: String
Valid Values: `LINKED | LINKING_FAILED | LINK_NOT_FOUND | PENDING_ACCEPTANCE_BY_TARGET_ACCOUNT | REJECTED`
Required: No

 ** SourceAccountId **   <a name="WorkSpaces-Type-AccountLink-SourceAccountId"></a>
The identifier of the source account.
Type: String
Pattern: `^\d{12}$`
Required: No

 ** TargetAccountId **   <a name="WorkSpaces-Type-AccountLink-TargetAccountId"></a>
The identifier of the target account.
Type: String
Pattern: `^\d{12}$`
Required: No

## See Also
<a name="API_AccountLink_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/AccountLink)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/AccountLink)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/AccountLink)
