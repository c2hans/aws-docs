---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_Node.html
---

# Node
<a name="API_Node"></a>

A node represents an AWS Glue component (trigger, crawler, or job) on a workflow graph.

## Contents
<a name="API_Node_Contents"></a>

 ** CrawlerDetails **   <a name="Glue-Type-Node-CrawlerDetails"></a>
Details of the crawler when the node represents a crawler.
Type: [CrawlerNodeDetails](API_CrawlerNodeDetails.md) object
Required: No

 ** JobDetails **   <a name="Glue-Type-Node-JobDetails"></a>
Details of the Job when the node represents a Job.
Type: [JobNodeDetails](API_JobNodeDetails.md) object
Required: No

 ** Name **   <a name="Glue-Type-Node-Name"></a>
The name of the AWS Glue component represented by the node.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** TriggerDetails **   <a name="Glue-Type-Node-TriggerDetails"></a>
Details of the Trigger when the node represents a Trigger.
Type: [TriggerNodeDetails](API_TriggerNodeDetails.md) object
Required: No

 ** Type **   <a name="Glue-Type-Node-Type"></a>
The type of AWS Glue component represented by the node.
Type: String
Valid Values: `CRAWLER | JOB | TRIGGER`
Required: No

 ** UniqueId **   <a name="Glue-Type-Node-UniqueId"></a>
The unique Id assigned to the node within the workflow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## See Also
<a name="API_Node_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/Node)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/Node)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/Node)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
