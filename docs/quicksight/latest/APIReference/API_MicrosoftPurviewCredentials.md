---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_MicrosoftPurviewCredentials.html
---

# MicrosoftPurviewCredentials
<a name="API_MicrosoftPurviewCredentials"></a>

The credentials for Microsoft Purview DLP integration. The credentials are stored in AWS Secrets Manager and referenced by ARN.

## Contents
<a name="API_MicrosoftPurviewCredentials_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** SecretArn **   <a name="QS-Type-MicrosoftPurviewCredentials-SecretArn"></a>
The ARN of the AWS Secrets Manager secret that contains the Microsoft Purview OAuth credentials. The secret includes the Azure tenant ID, client ID, and client secret or certificate.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws(-[\w]+)*:secretsmanager:[a-z0-9\-]+:\d{12}:secret:.+`
Required: Yes

## See Also
<a name="API_MicrosoftPurviewCredentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/MicrosoftPurviewCredentials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/MicrosoftPurviewCredentials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/MicrosoftPurviewCredentials)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
