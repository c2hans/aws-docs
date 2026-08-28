---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_Node.html
---

# Node
<a name="API_Node"></a>

A structure that represents a node in a dependency graph, containing information about a service, resource, or other entity and its characteristics.

## Contents
<a name="API_Node_Contents"></a>

 ** KeyAttributes **   <a name="applicationsignals-Type-Node-KeyAttributes"></a>
The key attributes that identify this node, including Type, Name, and Environment information.
Type: String to string map
Map Entries: Maximum number of 4 items.
Key Pattern: `[a-zA-Z]{1,50}`
Value Length Constraints: Minimum length of 1. Maximum length of 1024.
Value Pattern: `[ -~]*[!-~]+[ -~]*`
Required: Yes

 ** Name **   <a name="applicationsignals-Type-Node-Name"></a>
The name of the entity represented by this node.
Type: String
Required: Yes

 ** NodeId **   <a name="applicationsignals-Type-Node-NodeId"></a>
A unique identifier for this node within the dependency graph.
Type: String
Required: Yes

 ** Duration **   <a name="applicationsignals-Type-Node-Duration"></a>
The duration or processing time associated with this node, if applicable.
Type: Double
Required: No

 ** Operation **   <a name="applicationsignals-Type-Node-Operation"></a>
The operation associated with this node, if applicable.
Type: String
Required: No

 ** Status **   <a name="applicationsignals-Type-Node-Status"></a>
The status of the entity represented by this node.
Type: String
Required: No

 ** Type **   <a name="applicationsignals-Type-Node-Type"></a>
The type of entity represented by this node, such as `Service` or `Resource`.
Type: String
Required: No

## See Also
<a name="API_Node_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/Node)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/Node)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/Node)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Application Signals. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query applicationsignals` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
