---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_Entity.html
---

# Entity
<a name="API_Entity"></a>

An entity supported by a given `ConnectionType`.

## Contents
<a name="API_Entity_Contents"></a>

 ** Category **   <a name="Glue-Type-Entity-Category"></a>
The type of entities that are present in the response. This value depends on the source connection. For example this is `SObjects` for Salesforce and `databases` or `schemas` or `tables` for sources like Amazon Redshift.
Type: String
Required: No

 ** CustomProperties **   <a name="Glue-Type-Entity-CustomProperties"></a>
An optional map of keys which may be returned for an entity by a connector.
Type: String to string map
Required: No

 ** Description **   <a name="Glue-Type-Entity-Description"></a>
A description of the entity.
Type: String
Required: No

 ** EntityName **   <a name="Glue-Type-Entity-EntityName"></a>
The name of the entity.
Type: String
Required: No

 ** IsParentEntity **   <a name="Glue-Type-Entity-IsParentEntity"></a>
A Boolean value which helps to determine whether there are sub objects that can be listed.
Type: Boolean
Required: No

 ** Label **   <a name="Glue-Type-Entity-Label"></a>
Label used for the entity.
Type: String
Required: No

## See Also
<a name="API_Entity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/Entity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/Entity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/Entity)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
