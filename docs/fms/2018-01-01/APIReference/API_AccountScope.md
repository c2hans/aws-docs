---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_AccountScope.html
---

# AccountScope
<a name="API_AccountScope"></a>

Configures the accounts within the administrator's AWS Organizations organization that the specified Firewall Manager administrator can apply policies to.

## Contents
<a name="API_AccountScope_Contents"></a>

 ** Accounts **   <a name="fms-Type-AccountScope-Accounts"></a>
The list of accounts within the organization that the specified Firewall Manager administrator either can or cannot apply policies to, based on the value of `ExcludeSpecifiedAccounts`. If `ExcludeSpecifiedAccounts` is set to `true`, then the Firewall Manager administrator can apply policies to all members of the organization except for the accounts in this list. If `ExcludeSpecifiedAccounts` is set to `false`, then the Firewall Manager administrator can only apply policies to the accounts in this list.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^[0-9]+$`
Required: No

 ** AllAccountsEnabled **   <a name="fms-Type-AccountScope-AllAccountsEnabled"></a>
A boolean value that indicates if the administrator can apply policies to all accounts within an organization. If true, the administrator can apply policies to all accounts within the organization. You can either enable management of all accounts through this operation, or you can specify a list of accounts to manage in `AccountScope$Accounts`. You cannot specify both.
Type: Boolean
Required: No

 ** ExcludeSpecifiedAccounts **   <a name="fms-Type-AccountScope-ExcludeSpecifiedAccounts"></a>
A boolean value that excludes the accounts in `AccountScope$Accounts` from the administrator's scope. If true, the Firewall Manager administrator can apply policies to all members of the organization except for the accounts listed in `AccountScope$Accounts`. You can either specify a list of accounts to exclude by `AccountScope$Accounts`, or you can enable management of all accounts by `AccountScope$AllAccountsEnabled`. You cannot specify both.
Type: Boolean
Required: No

## See Also
<a name="API_AccountScope_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/AccountScope)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/AccountScope)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/AccountScope)
