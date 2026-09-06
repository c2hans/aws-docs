---
source_url: https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/net-dg-supported-platforms.html
---

The AWS SDK for .NET V3 has reached end-of-support.

We recommend that you migrate to [AWS SDK for .NET V4](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/welcome.html). For additional details and information on how to migrate, please refer to our [end-of-support announcement](https://aws.amazon.com/blogs/developer/aws-sdk-for-net-v3-end-of-support-announcement/).

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

**Warning**
Starting August 15th, 2024, the AWS SDK for .NET will end support for .NET Framework 3.5 and will change the minimum .NET Framework version to 4.7.2. For more information, see the blog post [Important changes coming for .NET Framework 3.5 and 4.5 targets of the AWS SDK for .NET](https://aws.amazon.com/blogs/developer/important-changes-coming-for-net-framework-3-5-and-4-5-targets-of-the-aws-sdk-for-net/).

This version of the AWS SDK for .NET is compiled against .NET Framework 4.5 and runs in the .NET 4.0 runtime. AWS service clients support synchronous and asynchronous calling patterns and use the [async and await](https://learn.microsoft.com/en-us/previous-versions/hh191443(v=vs.140)) keywords introduced in [C\# 5.0](https://en.wikipedia.org/wiki/C_Sharp_%28programming_language%29#Versions).

## .NET Framework 3.5
<a name="net-dg-platform-diff-winrt"></a>

**Warning**
Starting August 15th, 2024, the AWS SDK for .NET will end support for .NET Framework 3.5 and will change the minimum .NET Framework version to 4.7.2. For more information, see the blog post [Important changes coming for .NET Framework 3.5 and 4.5 targets of the AWS SDK for .NET](https://aws.amazon.com/blogs/developer/important-changes-coming-for-net-framework-3-5-and-4-5-targets-of-the-aws-sdk-for-net/).

This version of the AWS SDK for .NET is compiled against .NET Framework 3.5, and runs in either the .NET 2.0 or .NET 4.0 runtime. AWS service clients support synchronous and asynchronous calling patterns and use the older Begin and End pattern.

**Note**
The AWS SDK for .NET is not Federal Information Processing Standard (FIPS) compliant when used by applications built against version 2.0 of the CLR. For details on how you can substitute a FIPS compliant implementation in that environment, refer to [CryptoConfig](https://learn.microsoft.com/en-us/archive/blogs/shawnfa/cryptoconfig) on the Microsoft blog and the [CLR Security](https://github.com/MicrosoftArchive/clrsecurity/) team's HMACSHA256 class ( HMACSHA256Cng ) in Security.Cryptography.dll.

## Portable Class Library and Xamarin
<a name="portable-class-library"></a>

The AWS SDK for .NET also contains a Portable Class Library implementation. The Portable Class Library implementation can target multiple platforms, including Universal Windows Platform (UWP) and Xamarin on iOS and Android. See the [Mobile SDK for .NET and Xamarin](https://docs.aws.amazon.com/mobile/sdkforxamarin/developerguide/Welcome.html) for more details. AWS service clients only support asynchronous calling patterns.

## Unity support
<a name="unity-support"></a>

For information about Unity support, see [Special considerations for Unity support](unity-special.md).

## More information
<a name="more-info"></a>

[Migrating to version 3.5 of the AWS SDK for .NET](net-dg-v35.md)
