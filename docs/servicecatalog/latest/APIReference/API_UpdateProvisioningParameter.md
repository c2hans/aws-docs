---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_UpdateProvisioningParameter.html
---

# UpdateProvisioningParameter
<a name="API_UpdateProvisioningParameter"></a>

The parameter key-value pair used to update a provisioned product.

## Contents
<a name="API_UpdateProvisioningParameter_Contents"></a>

 ** Key **   <a name="servicecatalog-Type-UpdateProvisioningParameter-Key"></a>
The parameter key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

 ** UsePreviousValue **   <a name="servicecatalog-Type-UpdateProvisioningParameter-UsePreviousValue"></a>
If set to true, `Value` is ignored and the previous parameter value is kept.
Type: Boolean
Required: No

 ** Value **   <a name="servicecatalog-Type-UpdateProvisioningParameter-Value"></a>
The parameter value.
Type: String
Length Constraints: Maximum length of 4096.
Required: No

## See Also
<a name="API_UpdateProvisioningParameter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/UpdateProvisioningParameter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/UpdateProvisioningParameter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/UpdateProvisioningParameter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
