---
source_url: https://docs.aws.amazon.com/emulator/index.html
---

---
title: 'AWS Emulator Documentation'
canonical_url: https://docs.aws.amazon.com/emulator/
source: aws-documentation
generated_on: 2026-11-12
---

# AWS Emulator Documentation

Test your software against the AWS APIs locally, on your own machine or in CI, with no AWS account.

AWS Emulator is a local emulator of the AWS APIs. Test your software on your own machine or in CI, with no AWS account and without deploying on AWS.

## What is AWS Emulator?

AWS Emulator is a local emulator of the AWS APIs that helps you test your application code before you deploy on AWS. Use it for local testing, continuous integration and delivery (CI/CD), and prototyping with AI coding agents. You don't need an AWS account, and your requests go to the emulator, not to AWS. The emulator is for building and testing your software. AWS Emulator has no additional service fee. You pay only for AWS resources when you deploy on AWS.

## Key benefits

- **Test locally and in CI, with no AWS account**: Run your tests on your own machine, on a development server, or in your CI/CD pipeline. You don't need an AWS account, and you work with emulated resources instead of AWS resources.
- **Closest to AWS for control plane operations**: The emulator matches AWS most closely for the calls that create, describe, update, and delete resources. Where an operation is implemented, it rejects invalid calls with the same errors as AWS. It keeps the state of the resources that you create, so later calls see earlier changes.
- **Works with the AWS CLI and AWS SDKs**: Set environment variables to point the AWS CLI or your AWS SDK at the emulator, and then run your code as usual. For tests written in Rust with the AWS SDK for Rust, you can also run the emulator inside your test process.
- **Built for AI coding agents**: Install the aws-emulator skill, and your AI coding agent installs, starts, and connects the emulator for you. It can also check whether your project is expected to work on the emulator.
- **Measured fidelity, published on GitHub**: How closely the emulator matches AWS is called fidelity. We check the emulator's responses against real AWS. We publish the fidelity checks in the aws-emulator-evaluation-suite repository, and the fidelity scores with each release on the releases page.

## Get started with AWS Emulator

- [Getting started with an AI coding agent](/emulator/latest/userguide/getting-started-agent.html): Install the aws-emulator skill, and let your AI coding agent install, start, and connect AWS Emulator for you.
- [Getting started with AWS Emulator](/emulator/latest/userguide/getting-started.html): Choose how you run the emulator: with an AI coding agent, from a Linux package, in Docker, or in embedded mode for Rust tests. Then point the AWS CLI or your AWS SDK at it.
- [AWS Emulator User Guide](/emulator/latest/userguide/what-is-service.html): Learn what AWS Emulator does, where it matches AWS most closely, and its limitations.
- [Fidelity in AWS Emulator](/emulator/latest/userguide/fidelity.html): Learn how we measure fidelity, how to read the scores for each release, and how to report a difference as an issue on GitHub.

---

## Related resources for AWS Emulator

- [AWS Emulator on GitHub](https://github.com/aws/aws-emulator)
- [aws-emulator-evaluation-suite on GitHub](https://github.com/aws/aws-emulator-evaluation-suite)
- [AWS Emulator User Guide](/emulator/latest/userguide/what-is-service.html)
- [AWS Emulator product page on the AWS website](https://aws.amazon.com/products/developer-tools/emulator/)
