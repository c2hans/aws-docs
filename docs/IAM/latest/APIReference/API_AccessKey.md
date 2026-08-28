---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_AccessKey.html
---

# AccessKey
<a name="API_AccessKey"></a>

Contains information about an AWS access key.

 This data type is used as a response element in the [CreateAccessKey](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateAccessKey.html) and [ListAccessKeys](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListAccessKeys.html) operations.

**Note**
The `SecretAccessKey` value is returned only in response to [CreateAccessKey](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateAccessKey.html). You can get a secret access key only when you first create an access key; you cannot recover the secret access key later. If you lose a secret access key, you must create a new access key.

## Contents
<a name="API_AccessKey_Contents"></a>

 ** AccessKeyId **
The ID for this access key.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 128.
Pattern: `[\w]+`
Required: Yes

 ** SecretAccessKey **
The secret key used to sign requests.
Type: String
Required: Yes

 ** Status **
The status of the access key. `Active` means that the key is valid for API calls, while `Inactive` means it is not.
Type: String
Valid Values: `Active | Inactive | Expired`
Required: Yes

 ** UserName **
The name of the IAM user that the access key is associated with.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w+=,.@-]+`
Required: Yes

 ** CreateDate **
The date when the access key was created.
Type: Timestamp
Required: No

## See Also
<a name="API_AccessKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/AccessKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/AccessKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/AccessKey)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Identity and Access Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query IAM` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
