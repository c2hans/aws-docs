---
source_url: https://docs.aws.amazon.com/chime/latest/APIReference/API_Account.html
---

**End of support notice**: On February 20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/). **Note:** This does not impact the availability of the [Amazon Chime SDK service](https://aws.amazon.com/chime/chime-sdk/).

# Account
<a name="API_Account"></a>

The Amazon Chime account details. An AWS account can have multiple Amazon Chime accounts.

## Contents
<a name="API_Account_Contents"></a>

 ** AccountId **   <a name="chime-Type-Account-AccountId"></a>
The Amazon Chime account ID.
Type: String
Required: Yes

 ** AwsAccountId **   <a name="chime-Type-Account-AwsAccountId"></a>
The AWS account ID.
Type: String
Required: Yes

 ** Name **   <a name="chime-Type-Account-Name"></a>
The Amazon Chime account name.
Type: String
Required: Yes

 ** AccountStatus **   <a name="chime-Type-Account-AccountStatus"></a>
The status of the account.
Type: String
Valid Values: `Suspended | Active`
Required: No

 ** AccountType **   <a name="chime-Type-Account-AccountType"></a>
The Amazon Chime account type. For more information about different account types, see [Managing Your Amazon Chime Accounts](https://docs.aws.amazon.com/chime/latest/ag/manage-chime-account.html) in the *Amazon Chime Administration Guide*.
Type: String
Valid Values: `Team | EnterpriseDirectory | EnterpriseLWA | EnterpriseOIDC`
Required: No

 ** CreatedTimestamp **   <a name="chime-Type-Account-CreatedTimestamp"></a>
The Amazon Chime account creation timestamp, in ISO 8601 format.
Type: Timestamp
Required: No

 ** DefaultLicense **   <a name="chime-Type-Account-DefaultLicense"></a>
The default license for the Amazon Chime account.
Type: String
Valid Values: `Basic | Plus | Pro | ProTrial`
Required: No

 ** SigninDelegateGroups **   <a name="chime-Type-Account-SigninDelegateGroups"></a>
The sign-in delegate groups associated with the account.
Type: Array of [SigninDelegateGroup](API_SigninDelegateGroup.md) objects
Required: No

 ** SupportedLicenses **   <a name="chime-Type-Account-SupportedLicenses"></a>
Supported licenses for the Amazon Chime account.
Type: Array of strings
Valid Values: `Basic | Plus | Pro | ProTrial`
Required: No

## See Also
<a name="API_Account_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-2018-05-01/Account)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-2018-05-01/Account)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-2018-05-01/Account)
