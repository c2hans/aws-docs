---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_RecommendationRelatedEvent.html
---

# RecommendationRelatedEvent
<a name="API_RecommendationRelatedEvent"></a>

 Information about an event that is related to a recommendation.

## Contents
<a name="API_RecommendationRelatedEvent_Contents"></a>

 ** Name **   <a name="DevOpsGuru-Type-RecommendationRelatedEvent-Name"></a>
 The name of the event. This corresponds to the `Name` field in an `Event` object.
Type: String
Required: No

 ** Resources **   <a name="DevOpsGuru-Type-RecommendationRelatedEvent-Resources"></a>
 A `ResourceCollection` object that contains arrays of the names of AWS CloudFormation stacks. You can specify up to 1000 AWS CloudFormation stacks.
Type: Array of [RecommendationRelatedEventResource](API_RecommendationRelatedEventResource.md) objects
Required: No

## See Also
<a name="API_RecommendationRelatedEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/RecommendationRelatedEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/RecommendationRelatedEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/RecommendationRelatedEvent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DevOps Guru. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devops-guru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
