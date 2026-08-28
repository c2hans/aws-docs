---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Edge.html
---

# Edge
<a name="API_Edge"></a>

A directed edge connecting two lineage entities.

## Contents
<a name="API_Edge_Contents"></a>

 ** AssociationType **   <a name="sagemaker-Type-Edge-AssociationType"></a>
The type of the Association(Edge) between the source and destination. For example `ContributedTo`, `Produced`, or `DerivedFrom`.
Type: String
Valid Values: `ContributedTo | AssociatedWith | DerivedFrom | Produced | SameAs`
Required: No

 ** DestinationArn **   <a name="sagemaker-Type-Edge-DestinationArn"></a>
The Amazon Resource Name (ARN) of the destination lineage entity of the directed edge.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:(experiment|experiment-trial-component|artifact|action|context)/.*`
Required: No

 ** SourceArn **   <a name="sagemaker-Type-Edge-SourceArn"></a>
The Amazon Resource Name (ARN) of the source lineage entity of the directed edge.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:(experiment|experiment-trial-component|artifact|action|context)/.*`
Required: No

## See Also
<a name="API_Edge_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/Edge)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/Edge)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/Edge)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
