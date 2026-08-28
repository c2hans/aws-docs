---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/decision-matrix.html
---

# Decision matrix and when to choose each
<a name="decision-matrix"></a>

| Requirement | Lambda Architecture | ECS Architecture |
| --- | --- | --- |
|  **Image size**  | ≤ 6 MB | ≤ 100 MB |
|  **Cost optimization**  | Yes - Lowest cost | Higher cost |
|  **Transformation policies**  | No | Yes |
|  **Non-S3 origins**  | No | Yes |
|  **Administrative UI**  | No | Yes |
|  **Auto-scaling**  | Yes - Built-in | Yes - Configurable |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
