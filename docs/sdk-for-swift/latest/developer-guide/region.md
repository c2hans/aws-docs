---
source_url: https://docs.aws.amazon.com/sdk-for-swift/latest/developer-guide/region.html
---

# Setting the AWS Region for the AWS SDK for Swift
<a name="region"></a>

You can access AWS services that operate in a specific geographic area by using AWS Regions. This can be useful both for redundancy and to keep your data and applications running close to where you and your users access them.

**Important**
Most resources reside in a specific AWS Region and you must supply the correct Region for the resource when using the SDK.

You must set a default AWS Region for the SDK for Swift to use for AWS requests. This default is used for any SDK service method calls that aren't specified with a Region.

For examples on how to set the default region through the shared AWS `config` file or environment variables, see [AWS Region](https://docs.aws.amazon.com/sdkref/latest/guide/feature-region.html) in the *AWS SDKs and Tools Reference Guide*.

## Specifying the Region programmatically
<a name="instantiating-a-client-with-only-a-custom-region"></a>

Most services let you directly specify the Region when you call their constructors. For example, to create an Amazon S3 client configured for the Region `af-south-1`, specify the `region` parameter when creating the client, as shown.

```
do {
    let s3 = try S3Client(region: "af-south-1")

    // Use the client.
} catch {
    // Handle the error.
    dump(error, name: "Error accessing S3 service")
}
```

This lets you handle a common client configuration scenario (specifying a Region while using the default values for all other options) without going through the full configuration process. That process is covered in [Creating and using a custom configuration](config-code.md#creating-and-using-a-custom-configuration).
