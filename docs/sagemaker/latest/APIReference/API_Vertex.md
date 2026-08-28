---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Vertex.html
---

# Vertex
<a name="API_Vertex"></a>

A lineage entity connected to the starting entity(ies).

## Contents
<a name="API_Vertex_Contents"></a>

 ** Arn **   <a name="sagemaker-Type-Vertex-Arn"></a>
The Amazon Resource Name (ARN) of the lineage entity resource.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:(experiment|experiment-trial-component|artifact|action|context)/.*`
Required: No

 ** LineageType **   <a name="sagemaker-Type-Vertex-LineageType"></a>
The type of resource of the lineage entity.
Type: String
Valid Values: `TrialComponent | Artifact | Context | Action`
Required: No

 ** Type **   <a name="sagemaker-Type-Vertex-Type"></a>
The type of the lineage entity resource. For example: `DataSet`, `Model`, `Endpoint`, etc...
Type: String
Length Constraints: Minimum length of 0. Maximum length of 40.
Required: No

## See Also
<a name="API_Vertex_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/Vertex)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/Vertex)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/Vertex)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
