---
source_url: https://docs.aws.amazon.com/batch/latest/APIReference/API_ImagePullSecret.html
---

# ImagePullSecret
<a name="API_ImagePullSecret"></a>

References a Kubernetes secret resource. This name of the secret must start and end with an alphanumeric character, is required to be lowercase, can include periods (.) and hyphens (-), and can't contain more than 253 characters.

## Contents
<a name="API_ImagePullSecret_Contents"></a>

 ** name **   <a name="Batch-Type-ImagePullSecret-name"></a>
Provides a unique identifier for the `ImagePullSecret`. This object is required when `EksPodProperties$imagePullSecrets` is used.
Type: String
Required: Yes

## See Also
<a name="API_ImagePullSecret_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/ImagePullSecret)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/ImagePullSecret)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/ImagePullSecret)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Batch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query batch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
