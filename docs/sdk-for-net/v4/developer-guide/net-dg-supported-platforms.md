---
source_url: https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-supported-platforms.html
---

Version 4 (V4) of the AWS SDK for .NET has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html).

 [![Orange button with text "Click here for details".](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/images/BannerButton_less-round.png)](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html)

# Platforms supported by the AWS SDK for .NET
<a name="net-dg-supported-platforms"></a>

With the AWS SDK for .NET, you can target different platforms using distinct groups of assemblies. However, not all SDK functionality is the same on each of these platforms. This topic describes the differences in support for each platform.

Version 4.1 of the AWS SDK for .NET includes builds for .NET 11, .NET 10, and .NET 8, and for .NET Standard 2.0 and .NET Framework 4.7.2.

The SDK updates this list once a year in a minor version release. For information about the schedule and about the changes in version 4.1, see [Annual .NET target updates](net-dg-target-updates.md).

## .NET 8 and later
<a name="net-core"></a>

The AWS SDK for .NET includes builds for .NET 8, .NET 10, and .NET 11. These builds include target-specific features such as Native AOT support, bidirectional event stream APIs, and HTTP/2 support. For information about how long each target remains in the SDK, see [Announcing AWS SDK for .NET 4.1](https://aws.amazon.com/blogs/developer/announcing-aws-sdk-for-net-4-1/) on the AWS Developer Blog.

AWS service clients support only asynchronous calling patterns in these builds. This also affects many of the high-level abstractions built on top of service clients, like the Amazon S3 `TransferUtility`, which supports only asynchronous calls.

If your project targets a version of .NET earlier than .NET 8, such as .NET Core 3.1 or .NET 5, 6, or 7, the project falls back to the .NET Standard 2.0 build and you get a compile-time warning. Projects that target .NET 9 use the .NET 8 build. Move projects that target an out-of-support version of .NET to a version that Microsoft supports.

## .NET Standard 2.0
<a name="net-standard-2"></a>

Non-Framework variations of the AWS SDK for .NET comply with [.NET Standard 2.0](https://learn.microsoft.com/en-us/dotnet/standard/net-standard). The AWS SDK for .NET provides only asynchronous methods for applications written against .NET Standard. The .NET Standard 2.0 build doesn't include the target-specific features and optimizations that are available in the .NET 8 and later builds.

## .NET Framework 4.7.2
<a name="net-dg-platform-diff-netfx45"></a>

This version of the AWS SDK for .NET compiles against .NET Framework 4.7.2 and runs in the .NET 4.0 runtime. AWS service clients support synchronous and asynchronous calling patterns and use the [async and await](https://learn.microsoft.com/en-us/previous-versions/hh191443(v=vs.140)) keywords introduced in [C\# 5.0](https://en.wikipedia.org/wiki/C_Sharp_%28programming_language%29#Versions).

## .NET Framework 3.5
<a name="net-dg-platform-diff-winrt"></a>

Version 4 of the AWS SDK for .NET doesn't support .NET Framework 3.5.

## Using Xamarin and .NET MAUI
<a name="portable-class-library"></a>

Mobile and cross-platform UI applications built with Xamarin or .NET MAUI use the .NET Standard 2.0 or .NET 8 and later builds of the AWS SDK for .NET, depending on the target framework of the project. AWS service clients support only asynchronous calling patterns in these applications. For more information, see [Special considerations for Xamarin support](xamarin-special.md).

## Unity support
<a name="unity-support"></a>

For information about Unity support, see [Special considerations for Unity support](unity-special.md).
