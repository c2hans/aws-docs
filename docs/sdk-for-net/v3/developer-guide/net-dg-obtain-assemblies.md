---
source_url: https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/net-dg-obtain-assemblies.html
---

The AWS SDK for .NET V3 has reached end-of-support.

We recommend that you migrate to [AWS SDK for .NET V4](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/welcome.html). For additional details and information on how to migrate, please refer to our [end-of-support announcement](https://aws.amazon.com/blogs/developer/aws-sdk-for-net-v3-end-of-support-announcement/).

# Obtaining assemblies for the AWS SDK for .NET
<a name="net-dg-obtain-assemblies"></a>

This topic describes how you can obtain the AWSSDK assemblies and store them locally (or on premises) for use in your projects. This is **not** the recommended method for handling SDK references, but is required in some environments.

**Note**
The recommended method for handling SDK references is to download and install just the NuGet packages that each project needs. That method is described in [Install AWSSDK packages with NuGet](net-dg-install-assemblies.md).

If you can't or aren't allowed to download and install NuGet packages on a per-project basis, the following options are available to you.

## Download and extract ZIP files
<a name="download-zip-files"></a>

(Remember that this isn't the [recommended method](net-dg-install-assemblies.md) for handling references to the AWS SDK for .NET.)

1. Download one of the following ZIP files:
   + [aws-sdk-net8.0.zip](https://sdk-for-net.amazonwebservices.com/latest/v3/aws-sdk-net8.0.zip) - Assemblies that support .NET 8 and later.
   + [aws-sdk-netcoreapp3.1.zip](https://sdk-for-net.amazonwebservices.com/latest/v3/aws-sdk-netcoreapp3.1.zip) - Assemblies that support .NET Core 3.1 and later.
   + [aws-sdk-netstandard2.0.zip](https://sdk-for-net.amazonwebservices.com/latest/v3/aws-sdk-netstandard2.0.zip) - Assemblies that support .NET Standard 2.0 and 2.1.
   + [aws-sdk-net45.zip](https://sdk-for-net.amazonwebservices.com/latest/v3/aws-sdk-net45.zip) - Assemblies that support .NET Framework 4.5 and later.
   + [aws-sdk-net35.zip](https://sdk-for-net.amazonwebservices.com/latest/v3/aws-sdk-net35.zip) - Assemblies that support .NET Framework 3.5.
**Warning**
Starting August 15th, 2024, the AWS SDK for .NET will end support for .NET Framework 3.5 and will change the minimum .NET Framework version to 4.7.2. For more information, see the blog post [Important changes coming for .NET Framework 3.5 and 4.5 targets of the AWS SDK for .NET](https://aws.amazon.com/blogs/developer/important-changes-coming-for-net-framework-3-5-and-4-5-targets-of-the-aws-sdk-for-net/).

1. Extract the assemblies to some "download" folder on your file system; it doesn't matter where. Make note of this folder.

1. When you set up your project, you get the required assemblies from this folder, as described in [Install AWSSDK assemblies without NuGet](net-dg-install-without-nuget.md).
