---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_Authentication.html
---

# Authentication
<a name="API_Authentication"></a>

Denotes the user's authentication properties, such as whether it requires a password to authenticate. Used in output responses.

## Contents
<a name="API_Authentication_Contents"></a>

 ** PasswordCount **   <a name="MemoryDB-Type-Authentication-PasswordCount"></a>
The number of passwords belonging to the user. The maximum is two.
Type: Integer
Required: No

 ** Type **   <a name="MemoryDB-Type-Authentication-Type"></a>
Indicates whether the user requires a password to authenticate.
Type: String
Valid Values: `password | no-password | iam`
Required: No

## See Also
<a name="API_Authentication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/Authentication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/Authentication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/Authentication)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MemoryDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query memorydb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
