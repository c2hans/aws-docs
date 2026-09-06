---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_AgentStatusSearchCriteria.html
---

# AgentStatusSearchCriteria
<a name="API_AgentStatusSearchCriteria"></a>

The search criteria to be used to return agent statuses.

## Contents
<a name="API_AgentStatusSearchCriteria_Contents"></a>

 ** AndConditions **   <a name="connect-Type-AgentStatusSearchCriteria-AndConditions"></a>
A leaf node condition which can be used to specify a string condition.
The currently supported values for `FieldName` are `name`, `description`, `state`, `type`, `displayOrder`, and `resourceID`.
Type: Array of [AgentStatusSearchCriteria](#API_AgentStatusSearchCriteria) objects
Required: No

 ** OrConditions **   <a name="connect-Type-AgentStatusSearchCriteria-OrConditions"></a>
A list of conditions which would be applied together with an `OR` condition.
Type: Array of [AgentStatusSearchCriteria](#API_AgentStatusSearchCriteria) objects
Required: No

 ** StringCondition **   <a name="connect-Type-AgentStatusSearchCriteria-StringCondition"></a>
A leaf node condition which can be used to specify a string condition.
The currently supported values for `FieldName` are `name`, `description`, `state`, `type`, `displayOrder`, and `resourceID`.
Type: [StringCondition](API_StringCondition.md) object
Required: No

## See Also
<a name="API_AgentStatusSearchCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/AgentStatusSearchCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/AgentStatusSearchCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/AgentStatusSearchCriteria)
