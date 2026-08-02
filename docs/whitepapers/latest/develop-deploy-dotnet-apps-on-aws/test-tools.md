---
source_url: https://docs.aws.amazon.com/whitepapers/latest/develop-deploy-dotnet-apps-on-aws/test-tools.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Test Tools
<a name="test-tools"></a>

Test automation plays a critical part in DevOps, and is the fundamental development practice that enables continuous integration and continuous delivery.

Many developers opt to run their integration tests in environments hosted in AWS. However, if you prefer to execute some tests locally, [AWS SAM Local](https://github.com/thoeni/aws-sam-local) and the [AWS .NET Mock Lambda Test Tool](https://aws.amazon.com/blogs/developer/debugging-net-core-aws-lambda-functions-using-the-aws-net-mock-lambda-test-tool/) can help when developing Lambda functions. The [Localstack](https://github.com/localstack/localstack) project is an open-source tool that runs AWS APIs locally, and can be called directly from your test suites.

When creating mobile applications using [Xamarin](https://dotnet.microsoft.com/apps/xamarin), the [AWS Device Farm](https://aws.amazon.com/device-farm/) gives access to a wide variety of physical phones and devices, providing an effective environment for testing Android and iOS applications.
