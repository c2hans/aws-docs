---
source_url: https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-supported-platforms.html
---

Version 4 (V4) of the AWS SDK for .NET has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html).

 [![Orange button with text "Click here for details".](http://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/images/BannerButton_less-round.png)](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html)

# Platforms supported by the AWS SDK for .NET
<a name="net-dg-supported-platforms"></a>

The AWS SDK for .NET provides distinct groups of assemblies for developers to target different platforms. However, not all SDK functionality is the same on each of these platforms. This topic describes the differences in support for each platform.

## .NET Core
<a name="net-core"></a>

The AWS SDK for .NET supports applications written for .NET Core (.NET Core 3.1, .NET 5, .NET 6, and so on). AWS service clients only support asynchronous calling patterns in .NET core. This also affects many of the high level abstractions built on top of service clients, like the Amazon S3 `TransferUtility`, which will only support asynchronous calls in the .NET Core environment.

## .NET Standard 2.0
<a name="net-standard-2"></a>

Non-Framework variations of the AWS SDK for .NET comply with [.NET Standard 2.0](https://learn.microsoft.com/en-us/dotnet/standard/net-standard). The AWS SDK for .NET provides only asynchronous methods for applications written against .NET Standard.

## .NET Framework 4.5
<a name="net-dg-platform-diff-netfx45"></a>

This version of the AWS SDK for .NET is compiled against .NET Framework 4.7.2 and runs in the .NET 4.0 runtime. AWS service clients support synchronous and asynchronous calling patterns and use the [async and await](https://learn.microsoft.com/en-us/previous-versions/hh191443(v=vs.140)) keywords introduced in [C\# 5.0](https://en.wikipedia.org/wiki/C_Sharp_%28programming_language%29#Versions).

## .NET Framework 3.5
<a name="net-dg-platform-diff-winrt"></a>

Version 4 of the AWS SDK for .NET doesn't support .NET Framework 3.5.

## Portable Class Library and Xamarin
<a name="portable-class-library"></a>

The AWS SDK for .NET also contains a Portable Class Library implementation. The Portable Class Library implementation can target multiple platforms, including Universal Windows Platform (UWP) and Xamarin on iOS and Android. See the [Mobile SDK for .NET and Xamarin](https://docs.aws.amazon.com/mobile/sdkforxamarin/developerguide/Welcome.html) for more details. AWS service clients only support asynchronous calling patterns.

## Unity support
<a name="unity-support"></a>

For information about Unity support, see [Special considerations for Unity support](unity-special.md).
