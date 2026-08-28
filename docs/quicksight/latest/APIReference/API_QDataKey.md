---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_QDataKey.html
---

# QDataKey
<a name="API_QDataKey"></a>

A structure that contains information about the `QDataKey`.

## Contents
<a name="API_QDataKey_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** QDataKeyArn **   <a name="QS-Type-QDataKey-QDataKeyArn"></a>
The ARN of the AWS KMS key that is registered to a Quick Sight account for encryption and decryption use as a `QDataKey`.
Type: String
Required: No

 ** QDataKeyType **   <a name="QS-Type-QDataKey-QDataKeyType"></a>
The type of `QDataKey`.
Type: String
Valid Values: `AWS_OWNED | CMK`
Required: No

## See Also
<a name="API_QDataKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/QDataKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/QDataKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/QDataKey)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
