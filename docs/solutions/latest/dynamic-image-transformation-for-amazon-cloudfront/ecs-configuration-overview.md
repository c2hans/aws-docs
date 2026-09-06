---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/ecs-configuration-overview.html
---

# Configuration overview and setup order
<a name="ecs-configuration-overview"></a>

The ECS architecture has three configuration entities. Create them in the following order, because each step builds on the previous one:

1.  **Origin**: where your source images live (an S3 bucket or an external HTTP server).

1.  **Transformation policy**: how images are processed (resize, format, quality, smart crop, and so on). This step is optional; a mapping can route requests to an origin without applying a policy.

1.  **Mapping**: which incoming requests use which origin and (optionally) which policy.

A mapping references an origin by name and optionally references a transformation policy, so the origin (and any policy you want to attach) must exist before you create the mapping that uses them. The remaining subsections walk through each entity with a complete worked example and the Admin UI navigation path, followed by an [end-to-end walkthrough](ecs-end-to-end-example.md) that ties all three together.

**Tip**
To experiment with transformations before committing to a full configuration, open the [Playground](ecs-playground.md), which applies transformations against your deployment interactively.
