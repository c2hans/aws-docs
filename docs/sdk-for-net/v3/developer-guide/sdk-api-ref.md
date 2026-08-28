---
source_url: https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/sdk-api-ref.html
---

The AWS SDK for .NET V3 has reached end-of-support.

We recommend that you migrate to [AWS SDK for .NET V4](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/welcome.html). For additional details and information on how to migrate, please refer to our [end-of-support announcement](https://aws.amazon.com/blogs/developer/aws-sdk-for-net-v3-end-of-support-announcement/).

# API reference for the AWS SDK for .NET
<a name="sdk-api-ref"></a>

The AWS SDK for .NET provides an API that you can use to access AWS services. To see what classes and methods are available in the API, see the [AWS SDK for .NET API Reference](https://docs.aws.amazon.com/sdkfornet/v3/apidocs/).

In addition to the general reference given above, each of the examples under the [Code examples with guidance](tutorials-examples.md) section contains references to the specific methods and classes that are used in that example.

## About API reference versions
<a name="about-api-versions"></a>

The API reference described earlier is for version 3.0 and later of the AWS SDK for .NET.

For information about migrating from older versions of the SDK, see [Migrate your project](net-dg-migrating.md)

To find deprecated content for earlier versions of the SDK API reference, see the following item(s):
+ [AWS SDK for .NET API Reference V1 (deprecated)](samples/sdkfornet-api-ref_v1_deprecated.zip)
+ [AWS SDK for .NET API Reference V2 (deprecated)](samples/sdkfornet-api-ref_v2_deprecated.zip)

To view a deprecated AWS SDK for .NET API reference, you will need to extract it and configure a web browser. The instructions shown next are examples of how to do this. They are based on using the Google Chrome web browser on a Windows system. Adapt them to your specific web browser and operating system.

### View the deprecated API Reference V1
<a name="view-api-reference-v1"></a>

1. Download the ZIP file for the deprecated AWS SDK for .NET API Reference V1. By default, the name of the ZIP file is `sdkfornet-api-ref_v1_deprecated.zip`. That name will be used throughout these instructions.

1. Place the ZIP file in a folder of your choice. For these instructions, the folder name is assumed to be `C:\work\temp\api-refs\V1`.

1. Right-click on the ZIP file and choose **Extract All**. Accept the default location, which is `C:\work\temp\api-refs\V1\sdkfornet-api-ref_v1` for these instructions.

1. Create a shortcut for Google Chrome in the `C:\work\temp\api-refs\V1` folder. Be careful not to move the original application.

1. In the properties of the new shortcut, set the following fields:
   + **Target**: `"{{<path to the Google Chrome application>}}" --disable-web-security --user-data-dir=C:\work\temp\api-refs\V1\data "C:\work\temp\api-refs\V1\sdkfornet-api-ref_v1\Index.html"`

     For the `--user-data-dir` argument, use a folder name that works for your environment. The folder doesn't have to exist.
   + **Start in**: `C:\work\temp\api-refs\V1`

1. Give the shortcut an appropriate name.

1. Open the shortcut to view the old API reference.

### View the deprecated API Reference V2
<a name="view-api-reference-v2"></a>

1. Download the ZIP file for the deprecated AWS SDK for .NET API Reference V2. By default, the name of the ZIP file is `sdkfornet-api-ref_v2_deprecated.zip`. That name will be used throughout these instructions.

1. Place the ZIP file in a folder of your choice. For these instructions, the folder name is assumed to be `C:\work\temp\api-refs\V2`.

1. Right-click on the ZIP file and choose **Extract All**. Accept the default location, which is `C:\work\temp\api-refs\V2\sdkfornet-api-ref_v2` for these instructions.

1. Create a shortcut for Google Chrome in the `C:\work\temp\api-refs\V2` folder. Be careful not to move the original application.

1. In the properties of the new shortcut, set the following fields:
   + **Target**: `"{{<path to the Google Chrome application>}}" --disable-web-security --user-data-dir=C:\work\temp\api-refs\V2\data "C:\work\temp\api-refs\V2\sdkfornet-api-ref_v2\Index.html"`

     For the `--user-data-dir` argument, use a folder name that works for your environment. The folder doesn't have to exist.
   + **Start in**: `C:\work\temp\api-refs\V2`

1. Give the shortcut an appropriate name.

1. Open the shortcut to view the old API reference.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for .NET. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-net` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
