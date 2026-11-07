---
source_url: https://docs.aws.amazon.com/account-access-runtime/latest/APIReference/API_AccessDetails.html
---

# AccessDetails
<a name="API_AccessDetails"></a>

Describes a role that you can access, including the AWS account that contains the role and the role's ARN.

## Contents
<a name="API_AccessDetails_Contents"></a>

 ** accountId **   <a name="accountaccessruntime-Type-AccessDetails-accountId"></a>
The 12-digit identifier of the AWS account that contains the role.
Type: String
Pattern: `[0-9]{12}`
Required: Yes

 ** roleArn **   <a name="accountaccessruntime-Type-AccessDetails-roleArn"></a>
The Amazon Resource Name (ARN) of the role that you can access.
Type: String
Required: Yes

 ** accountName **   <a name="accountaccessruntime-Type-AccessDetails-accountName"></a>
The display name of the AWS account, if available. This value can be absent when the account name can't be resolved.
Type: String
Required: No

## See Also
<a name="API_AccessDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/account-access-runtime-2018-05-10/AccessDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/account-access-runtime-2018-05-10/AccessDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/account-access-runtime-2018-05-10/AccessDetails)
