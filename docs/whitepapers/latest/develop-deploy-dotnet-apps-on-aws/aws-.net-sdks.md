---
source_url: https://docs.aws.amazon.com/whitepapers/latest/develop-deploy-dotnet-apps-on-aws/aws-.net-sdks.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# AWS .NET SDKs
<a name="aws-.net-sdks"></a>

One of the great advantages AWS offers over traditional, on-premises resources is that its services can be accessed through REST APIs, enabling integration from any programming or scripting environment capable of stringing together HTTPS requests and sending them over the internet.

Although REST APIs are flexible, it’s easier for developers to work in their native language than to work with REST APIs, and the [AWS SDK for .NET](https://aws.amazon.com/sdk-for-net/) helps developers get started quickly by providing native .NET APIs to the AWS Services. Calling an AWS Service is as easy as calling a method on an object using the SDK.

The AWS SDK for .NET is distributed as multiple [NuGet](https://www.nuget.org/) packages, and contains assemblies for .NET Standard 2.0, .NET Framework 3.5, and .NET Framework 4.x.

As the standard for .NET package management, NuGet is the preferred option for installing the SDK, and provides a number of service-specific packages, such as AWSSDK.EC2 or AWSSDK.S3, each of which depends on the AWSSDK.Core package, which is automatically installed when you reference a service package in the NuGet Package Manager.

If you’re working with older versions of .NET that don’t support .NET Standard 2.0, then the versions of the SDK prior to v3.5 also contain Portable Class Library assemblies, and the [AWS Mobile SDK for Unity](https://docs.aws.amazon.com/mobile/sdkforunity/developerguide/what-is-unity-plugin.html) and [AWS Mobile SDK for .NET and Xamarin](https://docs.aws.amazon.com/mobile/sdkforxamarin/developerguide/Welcome.html) are available for older versions of Unity and Xamarin.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
