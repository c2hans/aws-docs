---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_AdminPasswordSourceConfigurationInput.html
---

# AdminPasswordSourceConfigurationInput
<a name="API_AdminPasswordSourceConfigurationInput"></a>

The input configuration for the admin password source. This is a union, so only one of the following members can be specified.

## Contents
<a name="API_AdminPasswordSourceConfigurationInput_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** customerManagedAwsSecret **   <a name="odb-Type-AdminPasswordSourceConfigurationInput-customerManagedAwsSecret"></a>
The configuration for using a customer-managed AWS Secrets Manager secret as the admin password source.
Type: [CustomerManagedAwsSecretConfigurationInput](API_CustomerManagedAwsSecretConfigurationInput.md) object
Required: No

## See Also
<a name="API_AdminPasswordSourceConfigurationInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/AdminPasswordSourceConfigurationInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/AdminPasswordSourceConfigurationInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/AdminPasswordSourceConfigurationInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Oracle Database@AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query odb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
