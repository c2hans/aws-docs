---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_AppflowIntegration.html
---

# AppflowIntegration
<a name="API_connect-customer-profiles_AppflowIntegration"></a>

Details for workflow of type `APPFLOW_INTEGRATION`.

## Contents
<a name="API_connect-customer-profiles_AppflowIntegration_Contents"></a>

 ** FlowDefinition **   <a name="connect-Type-connect-customer-profiles_AppflowIntegration-FlowDefinition"></a>
The configurations that control how Customer Profiles retrieves data from the source, Amazon AppFlow. Customer Profiles uses this information to create an AppFlow flow on behalf of customers.
Type: [FlowDefinition](API_connect-customer-profiles_FlowDefinition.md) object
Required: Yes

 ** Batches **   <a name="connect-Type-connect-customer-profiles_AppflowIntegration-Batches"></a>
Batches in workflow of type `APPFLOW_INTEGRATION`.
Type: Array of [Batch](API_connect-customer-profiles_Batch.md) objects
Required: No

## See Also
<a name="API_connect-customer-profiles_AppflowIntegration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/AppflowIntegration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/AppflowIntegration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/AppflowIntegration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
