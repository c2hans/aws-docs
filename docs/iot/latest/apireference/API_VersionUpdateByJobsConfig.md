---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_VersionUpdateByJobsConfig.html
---

# VersionUpdateByJobsConfig
<a name="API_VersionUpdateByJobsConfig"></a>

Configuration to manage IoT Job's package version reporting. If configured, Jobs updates the thing's reserved named shadow with the package version information up on successful job completion.

 **Note:** For each job, the destinationPackageVersions attribute has to be set with the correct data for Jobs to report to the thing shadow.

## Contents
<a name="API_VersionUpdateByJobsConfig_Contents"></a>

 ** enabled **   <a name="iot-Type-VersionUpdateByJobsConfig-enabled"></a>
Indicates whether the Job is enabled or not.
Type: Boolean
Required: No

 ** roleArn **   <a name="iot-Type-VersionUpdateByJobsConfig-roleArn"></a>
The Amazon Resource Name (ARN) of the role that grants permission to the AWS IoT jobs service to update the reserved named shadow when the job successfully completes.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

## See Also
<a name="API_VersionUpdateByJobsConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/VersionUpdateByJobsConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/VersionUpdateByJobsConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/VersionUpdateByJobsConfig)
