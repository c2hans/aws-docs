---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_RegistryId.html
---

# RegistryId
<a name="API_RegistryId"></a>

A wrapper structure that may contain the registry name and Amazon Resource Name (ARN).

## Contents
<a name="API_RegistryId_Contents"></a>

 ** RegistryArn **   <a name="Glue-Type-RegistryId-RegistryArn"></a>
Arn of the registry to be updated. One of `RegistryArn` or `RegistryName` has to be provided.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10240.
Pattern: `arn:aws(-(cn|us-gov|iso(-[bef])?))?:glue:.*`
Required: No

 ** RegistryName **   <a name="Glue-Type-RegistryId-RegistryName"></a>
Name of the registry. Used only for lookup. One of `RegistryArn` or `RegistryName` has to be provided.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9-_$#.]+`
Required: No

## See Also
<a name="API_RegistryId_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/RegistryId)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/RegistryId)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/RegistryId)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
