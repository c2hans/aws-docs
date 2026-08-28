---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_RuntimeLogConfigurations.html
---

# RuntimeLogConfigurations
<a name="API_RuntimeLogConfigurations"></a>

The different configurations for runtime logs.

## Contents
<a name="API_RuntimeLogConfigurations_Contents"></a>

 ** DeleteLocalStoreAfterUpload **   <a name="managedintegrations-Type-RuntimeLogConfigurations-DeleteLocalStoreAfterUpload"></a>
Configuration to enable or disable deleting of runtime logs in the device once uploaded to the cloud.
Type: Boolean
Required: No

 ** LocalStoreFileRotationMaxBytes **   <a name="managedintegrations-Type-RuntimeLogConfigurations-LocalStoreFileRotationMaxBytes"></a>
Configuration to set the maximum bytes of runtime logs that can be stored on the device before the oldest logs are deleted or overwritten.
Type: Integer
Required: No

 ** LocalStoreFileRotationMaxFiles **   <a name="managedintegrations-Type-RuntimeLogConfigurations-LocalStoreFileRotationMaxFiles"></a>
Configuration to set the maximum number of runtime log files that can be stored on the device before the oldest files are deleted or overwritten.
Type: Integer
Required: No

 ** LocalStoreLocation **   <a name="managedintegrations-Type-RuntimeLogConfigurations-LocalStoreLocation"></a>
Configuration of where to store runtime logs in the device.
Type: String
Required: No

 ** LogFlushLevel **   <a name="managedintegrations-Type-RuntimeLogConfigurations-LogFlushLevel"></a>
The different log levels available for configuration.
Type: String
Valid Values: `DEBUG | ERROR | INFO | WARN`
Required: No

 ** LogLevel **   <a name="managedintegrations-Type-RuntimeLogConfigurations-LogLevel"></a>
The different log levels available for configuration.
Type: String
Valid Values: `DEBUG | ERROR | INFO | WARN`
Required: No

 ** UploadLog **   <a name="managedintegrations-Type-RuntimeLogConfigurations-UploadLog"></a>
Configuration to enable or disable uploading of runtime logs to the cloud.
Type: Boolean
Required: No

 ** UploadPeriodMinutes **   <a name="managedintegrations-Type-RuntimeLogConfigurations-UploadPeriodMinutes"></a>
Configuration to set the time interval in minutes between each batch of runtime logs that the device uploads to the cloud.
Type: Integer
Required: No

## See Also
<a name="API_RuntimeLogConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/RuntimeLogConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/RuntimeLogConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/RuntimeLogConfigurations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
