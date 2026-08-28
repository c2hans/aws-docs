---
source_url: https://docs.aws.amazon.com/cdk/v2/guide/testing-locally-build-with-sam-cli.html
---

This is the AWS CDK v2 Developer Guide. The older CDK v1 entered maintenance on June 1, 2022 and ended support on June 1, 2023.

# Building AWS CDK applications with AWS SAM
<a name="testing-locally-build-with-sam-cli"></a>

The AWS SAM CLI provides support for building Lambda functions and layers defined in your AWS CDK application with ` [sam build](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-build.html) `.

For Lambda functions that use zip artifacts, run `cdk synth` before you run `sam local` commands. `sam build` isn’t required.

If your AWS CDK application uses functions with the image type, run `cdk synth` and then run `sam build` before you run `sam local` commands. When you run `sam build`, AWS SAM doesn’t build Lambda functions or layers that use runtime-specific constructs, for example, ` [NodejsFunction](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_lambda_nodejs.NodejsFunction.html) `. `sam build` doesn’t support [bundled assets](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.BundlingOptions.html).

## Example
<a name="testing-locally-build-with-sam-cli-examples"></a>

Running the following command from the AWS CDK project root directory builds the application.

```
$ sam build -t <./cdk.out/CdkSamExampleStack.template.json>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Cloud Development Kit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
