---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/ecs-architecture-usage.html
---

# ECS architecture
<a name="ecs-architecture-usage"></a>

This section covers how to use the solution when deployed with the ECS architecture. In this architecture, you manage image processing through the Admin UI, a web console where you define where your source images live (origins), how images are transformed (transformation policies), and which requests use which configuration (mappings).

If you are evaluating the solution, the worked examples in this section show both what a valid configuration looks like for each entity and where you create it in the Admin UI, so you can assess fit and estimate trial effort before committing to a deployment. To try transformations interactively without creating any configuration first, use the [Playground](ecs-playground.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
