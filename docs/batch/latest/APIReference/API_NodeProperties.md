---
source_url: https://docs.aws.amazon.com/batch/latest/APIReference/API_NodeProperties.html
---

# NodeProperties
<a name="API_NodeProperties"></a>

An object that represents the node properties of a multi-node parallel job.

**Note**
Node properties can't be specified for Amazon EKS based job definitions.

## Contents
<a name="API_NodeProperties_Contents"></a>

 ** mainNode **   <a name="Batch-Type-NodeProperties-mainNode"></a>
Specifies the node index for the main node of a multi-node parallel job. This node index value must be fewer than the number of nodes.
Type: Integer
Required: Yes

 ** nodeRangeProperties **   <a name="Batch-Type-NodeProperties-nodeRangeProperties"></a>
A list of node ranges and their properties that are associated with a multi-node parallel job.
Type: Array of [NodeRangeProperty](API_NodeRangeProperty.md) objects
Required: Yes

 ** numNodes **   <a name="Batch-Type-NodeProperties-numNodes"></a>
The number of nodes that are associated with a multi-node parallel job.
Type: Integer
Required: Yes

## See Also
<a name="API_NodeProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/NodeProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/NodeProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/NodeProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Batch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query batch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
