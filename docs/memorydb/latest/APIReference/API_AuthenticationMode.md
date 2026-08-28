---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_AuthenticationMode.html
---

# AuthenticationMode
<a name="API_AuthenticationMode"></a>

Denotes the user's authentication properties, such as whether it requires a password to authenticate. Used in output responses.

## Contents
<a name="API_AuthenticationMode_Contents"></a>

 ** Passwords **   <a name="MemoryDB-Type-AuthenticationMode-Passwords"></a>
The password(s) used for authentication
Type: Array of strings
Array Members: Minimum number of 1 item.
Required: No

 ** Type **   <a name="MemoryDB-Type-AuthenticationMode-Type"></a>
Indicates whether the user requires a password to authenticate. All newly-created users require a password.
Type: String
Valid Values: `password | iam`
Required: No

## See Also
<a name="API_AuthenticationMode_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/AuthenticationMode)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/AuthenticationMode)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/AuthenticationMode)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MemoryDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query memorydb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
