---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/advanced-prompt-optimization-quotas.html
---

# Supported Regions, models, and quotas
<a name="advanced-prompt-optimization-quotas"></a>

## Supported Regions
<a name="advanced-prompt-optimization-quotas-regions"></a>

Advanced Prompt Optimization is available in the following AWS Regions:
+ US East (N. Virginia) (us-east-1)
+ US East (Ohio) (us-east-2)
+ US West (Oregon) (us-west-2)
+ Canada (Central) (ca-central-1)
+ South America (São Paulo) (sa-east-1)
+ Europe (Ireland) (eu-west-1)
+ Europe (London) (eu-west-2)
+ Europe (Frankfurt) (eu-central-1)
+ Europe (Zurich) (eu-central-2)
+ Asia Pacific (Mumbai) (ap-south-1)
+ Asia Pacific (Tokyo) (ap-northeast-1)
+ Asia Pacific (Seoul) (ap-northeast-2)
+ Asia Pacific (Singapore) (ap-southeast-1)
+ Asia Pacific (Sydney) (ap-southeast-2)

## Supported target models
<a name="advanced-prompt-optimization-quotas-models"></a>

Advanced Prompt Optimization supports all Amazon Bedrock models that output text modality.

## Supported judge models
<a name="advanced-prompt-optimization-quotas-judge"></a>

When using the custom LLM-as-a-judge evaluation method, the following models are available as judge models:
+ anthropic.claude-opus-4-6-v1
+ anthropic.claude-sonnet-4-5-20250929-v1:0
+ anthropic.claude-sonnet-4-6

## Quotas
<a name="advanced-prompt-optimization-quotas-limits"></a>

| Quota | Limit |
| --- | --- |
| Concurrent jobs | 20 per account per region |
| Input file size | 50 MB |
| Templates per job | 10 |
| Evaluation samples per template | 100 |
| Text variables per template | 20 |
| Multimodal files per sample | 100 |
| Models per job | 5 |
| Steering criteria per template | 5 |

## Supported multimodal file types
<a name="advanced-prompt-optimization-quotas-filetypes"></a>

| Category | Supported formats | Notes |
| --- | --- | --- |
| Image | JPG (.jpg), JPEG (.jpeg), PNG (.png), GIF (.gif), WebP (.webp) | Support depends on the target model. For animated GIF and WebP files, models typically use only the first frame. To include multiple frames, split them into separate image files and include them as individual multimodal files in the evaluation sample. |
| Document | PDF (.pdf) |  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
