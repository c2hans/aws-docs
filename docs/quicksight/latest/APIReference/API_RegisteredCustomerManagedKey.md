---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_RegisteredCustomerManagedKey.html
---

# RegisteredCustomerManagedKey
<a name="API_RegisteredCustomerManagedKey"></a>

A customer managed key structure that contains the information listed below:
+  `KeyArn` - The ARN of a AWS KMS key that is registered to a Quick Sight account for encryption and decryption use.
+  `DefaultKey` - Indicates whether the current key is set as the default key for encryption and decryption use.

## Contents
<a name="API_RegisteredCustomerManagedKey_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DefaultKey **   <a name="QS-Type-RegisteredCustomerManagedKey-DefaultKey"></a>
Indicates whether a `RegisteredCustomerManagedKey` is set as the default key for encryption and decryption use.
Type: Boolean
Required: No

 ** KeyArn **   <a name="QS-Type-RegisteredCustomerManagedKey-KeyArn"></a>
The ARN of the AWS KMS key that is registered to a Quick Sight account for encryption and decryption use.
Type: String
Required: No

## See Also
<a name="API_RegisteredCustomerManagedKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/RegisteredCustomerManagedKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/RegisteredCustomerManagedKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/RegisteredCustomerManagedKey)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
