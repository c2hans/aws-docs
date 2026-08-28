---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations-HypothesisVisualization.html
---

# Understanding hypothesis visualizations
<a name="Investigations-HypothesisVisualization"></a>

When CloudWatch investigations generates hypotheses that include multiple resources, the investigation view provides a visual representation of the causal relationships between those resources. This visual hypothesis view helps you quickly understand complex issues without reading lengthy text explanations.

The hypothesis visualization displays resources as nodes connected by the pathways identified by CloudWatch investigations. For example, if a hypothesis involves Lambda function A affecting DynamoDB table B, you'll see two nodes visualizing the relationship.

**Key features of hypothesis visualizations:**
+ **Resource nodes** - Each AWS resource mentioned in the hypothesis appears as a distinct node, labeled with the resource type and identifier.
+ **Connections** - Connections between nodes indicate the relationships that CloudWatch investigations has identified.
+ **Visual context** - The layout helps you understand the scope and complexity of multi-resource issues at a glance.

This visual representation is particularly valuable for:
+ Understanding distributed system failures that span multiple services
+ Identifying upstream and downstream impact relationships
+ Quickly assessing the scope of an issue before diving into detailed analysis

**Note**
Hypothesis visualizations are automatically generated when CloudWatch investigations identifies causal relationships between multiple resources.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
