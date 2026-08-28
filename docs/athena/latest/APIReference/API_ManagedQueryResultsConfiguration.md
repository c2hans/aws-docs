---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_ManagedQueryResultsConfiguration.html
---

# ManagedQueryResultsConfiguration
<a name="API_ManagedQueryResultsConfiguration"></a>

 The configuration for storing results in Athena owned storage, which includes whether this feature is enabled; whether encryption configuration, if any, is used for encrypting query results.

## Contents
<a name="API_ManagedQueryResultsConfiguration_Contents"></a>

 ** Enabled **   <a name="athena-Type-ManagedQueryResultsConfiguration-Enabled"></a>
If set to true, allows you to store query results in Athena owned storage. If set to false, workgroup member stores query results in location specified under `ResultConfiguration$OutputLocation`. The default is false. A workgroup cannot have the `ResultConfiguration$OutputLocation` parameter when you set this field to true.
Type: Boolean
Required: Yes

 ** EncryptionConfiguration **   <a name="athena-Type-ManagedQueryResultsConfiguration-EncryptionConfiguration"></a>
If you encrypt query and calculation results in Athena owned storage, this field indicates the encryption option (for example, SSE\_KMS or CSE\_KMS) and key information.
Type: [ManagedQueryResultsEncryptionConfiguration](API_ManagedQueryResultsEncryptionConfiguration.md) object
Required: No

## See Also
<a name="API_ManagedQueryResultsConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/ManagedQueryResultsConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/ManagedQueryResultsConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/ManagedQueryResultsConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
