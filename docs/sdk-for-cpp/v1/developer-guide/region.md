---
source_url: https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/region.html
---

# Setting the AWS Region for the AWS SDK for C\+\+
<a name="region"></a>

You can access AWS services that operate in a specific geographic area by using AWS Regions. This can be useful both for redundancy and to keep your data and applications running close to where you and your users access them.

**Important**
Most resources reside in a specific AWS Region and you must supply the correct Region for the resource when using the SDK.

For examples on how to set the default region through the shared AWS `config` file or environment variables, see [AWS Region](https://docs.aws.amazon.com/sdkref/latest/guide/feature-region.html) in the *AWS SDKs and Tools Reference Guide*.

You must set a default AWS Region for the AWS SDK for C\+\+ to use for AWS requests. This default is used for any SDK service method calls that aren't specified with a Region. In the SDK for C\+\+, you can also set the default region using the [Client configuration in code](client-config.md).
