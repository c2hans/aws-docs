---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/advanced-prompt-optimization-troubleshooting.html
---

# Troubleshooting
<a name="advanced-prompt-optimization-troubleshooting"></a>

| Error | Cause | Fix |
| --- | --- | --- |
| No inference API is accessible for model | Model access not enabled or IAM permission missing | Enable model access in Bedrock console; verify IAM policy includes bedrock:InvokeModelWithResponseStream |
| Input file is empty | S3 object has 0 bytes | Verify the input JSONL file has content |
| File is not valid JSONL | Malformed JSON in input file | Validate each line is valid JSON |
| AccessDenied on S3 | IAM role lacks S3 permissions | Add s3:GetObject for input path and s3:PutObject for output path |
| ValidationException: multiple evaluation methods | Provided both steeringCriteria AND customLLMJConfig or Lambda | Use only ONE evaluation method per template |
| ValidationException: missing label | Missing customEvaluationMetricLabel when using LLMJ or Lambda | Add the customEvaluationMetricLabel field |
| Silent failure: inputVariables | Multiple keys in one inputVariables object | Use one key per object in the array |
| ValidationException: placeholder mismatch | inputVariables keys don't match {{placeholders}} in template | Ensure keys exactly match placeholder names |
| ValidationException: wrong bracket syntax | Used {variable} instead of {{variable}} | Use double curly brackets |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
