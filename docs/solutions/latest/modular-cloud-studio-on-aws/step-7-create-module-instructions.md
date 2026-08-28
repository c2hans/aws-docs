---
source_url: https://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/step-7-create-module-instructions.html
---

# Step 7: Create module instructions (optional)
<a name="step-7-create-module-instructions"></a>

This step allows you to provide custom, user-friendly instructions within the MCS interface, enhancing the user experience by offering clear guidance on module usage after enablement.

To implement module instructions, you’ll need to create an AWS Lambda function that returns instruction content. The Lambda function must be named with the prefix `MCSInstructionGenerationLambda-` and be referenced in your CloudFormation outputs with the key `InstructionGenerationLambdaArn`. Append your stack id (without hyphens) to the Lambda function name is recommended to ensure unique naming across multiple deployment in the same region.

The function can return either a plain string or a JSON object formatted as `{"content": "your instruction string"}`. A basic example implementation for reference:

```
TEMPLATE_FILE_NAME = "template.html"
def handler(event, context):
 with open(
 TEMPLATE_FILE_NAME,
 "r",
 encoding="utf-8") as f:
 instructions = f.read()
 return {"content": instructions}
```

When formatting your instructions, note that inline CSS is supported, but external CSS is not. HTML tags will inherit Cloudscape default styling. The maximum size for the instruction string is **250 KB**.

You can verify successful implementation when a "View" link appears in the module’s row on the UI after deployment. This feature enhances usability by providing context-specific documentation directly within the MCS interface, helping users better understand and use the module’s feature.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Solutions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
