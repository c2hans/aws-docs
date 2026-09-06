---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_TaskConfiguration.html
---

# TaskConfiguration
<a name="API_TaskConfiguration"></a>

The task execution configuration. Specify a [containerTaskConfiguration](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ContainerTaskConfiguration.html) for a custom container workload.

## Contents
<a name="API_TaskConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** containerTaskConfiguration **   <a name="iotsitewise-Type-TaskConfiguration-containerTaskConfiguration"></a>
Configuration for running a custom container image on managed compute.
Type: [ContainerTaskConfiguration](API_ContainerTaskConfiguration.md) object
Required: No

## See Also
<a name="API_TaskConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/TaskConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/TaskConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/TaskConfiguration)
