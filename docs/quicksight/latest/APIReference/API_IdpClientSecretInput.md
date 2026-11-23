---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_IdpClientSecretInput.html
---

# IdpClientSecretInput

An IdP-provided client secret that you store in AWS Secrets Manager.

## Contents
<a name="API_IdpClientSecretInput_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** RegionalSecretManagerArns **   <a name="QS-Type-IdpClientSecretInput-RegionalSecretManagerArns"></a>
The ARN of the AWS Secrets Manager secret that holds the client secret, for each Region.
Type: String to string map
Map Entries: Maximum number of 10 items.
Key Length Constraints: Minimum length of 5. Maximum length of 30.
Key Pattern: `[a-z]{2}(-[a-z]+)+-[0-9]+`
Value Length Constraints: Minimum length of 20. Maximum length of 2048.
Value Pattern: `arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):secretsmanager:[a-z0-9-]+:[0-9]{12}:secret:.+`
Required: Yes

## See Also
<a name="API_IdpClientSecretInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/IdpClientSecretInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/IdpClientSecretInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/IdpClientSecretInput)
