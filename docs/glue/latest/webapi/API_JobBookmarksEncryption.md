---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_JobBookmarksEncryption.html
---

# JobBookmarksEncryption
<a name="API_JobBookmarksEncryption"></a>

Specifies how job bookmark data should be encrypted.

## Contents
<a name="API_JobBookmarksEncryption_Contents"></a>

 ** JobBookmarksEncryptionMode **   <a name="Glue-Type-JobBookmarksEncryption-JobBookmarksEncryptionMode"></a>
The encryption mode to use for job bookmarks data.
Type: String
Valid Values: `DISABLED | CSE-KMS`
Required: No

 ** KmsKeyArn **   <a name="Glue-Type-JobBookmarksEncryption-KmsKeyArn"></a>
The Amazon Resource Name (ARN) of the KMS key to be used to encrypt the data.
Type: String
Pattern: `^$|arn:aws[a-z0-9-]*:kms:.*`
Required: No

## See Also
<a name="API_JobBookmarksEncryption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/JobBookmarksEncryption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/JobBookmarksEncryption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/JobBookmarksEncryption)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
