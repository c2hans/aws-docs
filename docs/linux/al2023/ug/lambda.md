---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/lambda.html
---

# Using AL2023 in AWS Lambda
<a name="lambda"></a>

 With AWS Lambda, you can run code without provisioning or managing servers. You pay only for the compute time that you consume–there's no charge when your code isn't running. You can run code for virtually any type of application or backend service–all with zero administration. Just upload your code and Lambda takes care of everything required to run and scale your code with high availability.

## AL2023 `provided.al2023` managed runtime and container image
<a name="lambda-provided-al2023"></a>

 The `provided.al2023` base runtime is based on the [AL2023 minimal container image](https://docs.aws.amazon.com/linux/al2023/ug/minimal-container.html), and provides an AL2023 based Lambda managed runtime and [container base image](https://gallery.ecr.aws/lambda/provided). Because the `provided.al2023` runtime is based on the AL2023 minimal container image, it is substantially smaller at less than 40 MB than the `provided.al2` runtime at around 109 MB.

 For more information, see [Lambda runtimes](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html) and [Working with Lambda container images](https://docs.aws.amazon.com/lambda/latest/dg/images-create.html).

## AL2023 based Lambda runtimes
<a name="lambda-al2023-based"></a>

 Future releases of managed language runtimes, such as Node.js 20, Python 3.12, Java 21, and .NET 8, are based on AL2023 and will use `provided.al2023` as the base image as described in the [announcement of AL2023 based runtimes](https://aws.amazon.com/blogs/compute/introducing-the-amazon-linux-2023-runtime-for-aws-lambda/) .

**AL2023 based Lambda functions**
+ [AL2023 Lambda functions written in Go](go.md#lambda-go)
+ [AL2023 Lambda functions written in Rust](rust.md#lambda-rust)

 For more information, see [Lambda runtimes](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html) in the *AWS Lambda Developer Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
