---
source_url: https://docs.aws.amazon.com/cdk/blocks/devguide/testing.html
---

# Testing AWS CDK Blocks applications

You can run the tests for a AWS CDK Blocks application in two places: against each CDK Block’s local implementation, or against a sandbox on AWS. This page explains what each place tests and how to choose between them.

## Where to run tests
<a name="testing-layers"></a>

| Where | What runs | What it catches | What it misses |
| --- | --- | --- | --- |
| Local implementations | Every CDK Block runs its local implementation. This is what `npm run dev` and your test runner use by default. | Mistakes in your business logic and in how you use each CDK Block, such as a failed conditional write, an expired item, or a payload that fails schema validation. | How AWS services respond. The AWS SDK is never loaded. |
| Sandbox | Your whole application, deployed to AWS with `npm run sandbox`. | Everything that depends on real AWS: IAM grants, the deployed API and job wiring, quotas, performance, and real model output. | Nothing on AWS, but each run takes a deploy and costs what the resources cost. |

At GA, each CDK Block runs locally on its own built-in implementation, so your app works without an AWS account. [AWS Emulator](https://docs.aws.amazon.com/emulator/latest/userguide/what-is-service.html) support for CDK Blocks is planned.

## Choosing where to run a test
<a name="testing-choose"></a>

Run most tests against local implementations. They run in milliseconds, need no AWS account, and run in CI on every commit. For how to write them, see [Testing with local implementations](local-development.md#local-development-testing). Use a sandbox for what only AWS can show: the IAM grants that CDK Blocks adds, the deployed API and job wiring, quotas, performance, and model output. Also use a sandbox for any behavior that a CDK Block’s `DESIGN.md` lists as different on AWS. Many CDK Blocks ship a `DESIGN.md` in their npm package with a "Mock vs AWS Behavior Differences" table. Run your sandbox tests before you ship. For more information, see [Test against a sandbox](local-development.md#local-development-testing-sandbox).

## Related resources
<a name="testing-related"></a>
+  [Testing with local implementations](local-development.md#local-development-testing)
+  [Deploy to a sandbox](deploy-to-aws.md#deploy-sandbox)
