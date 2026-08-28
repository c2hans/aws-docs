---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_OTAUpdateInfo.html
---

# OTAUpdateInfo
<a name="API_OTAUpdateInfo"></a>

Information about an OTA update.

## Contents
<a name="API_OTAUpdateInfo_Contents"></a>

 ** additionalParameters **   <a name="iot-Type-OTAUpdateInfo-additionalParameters"></a>
A collection of name/value pairs
Type: String to string map
Value Length Constraints: Minimum length of 0. Maximum length of 4096.
Value Pattern: `[\s\S]*`
Required: No

 ** awsIotJobArn **   <a name="iot-Type-OTAUpdateInfo-awsIotJobArn"></a>
The AWS IoT job ARN associated with the OTA update.
Type: String
Required: No

 ** awsIotJobId **   <a name="iot-Type-OTAUpdateInfo-awsIotJobId"></a>
The AWS IoT job ID associated with the OTA update.
Type: String
Required: No

 ** awsJobExecutionsRolloutConfig **   <a name="iot-Type-OTAUpdateInfo-awsJobExecutionsRolloutConfig"></a>
Configuration for the rollout of OTA updates.
Type: [AwsJobExecutionsRolloutConfig](API_AwsJobExecutionsRolloutConfig.md) object
Required: No

 ** awsJobPresignedUrlConfig **   <a name="iot-Type-OTAUpdateInfo-awsJobPresignedUrlConfig"></a>
Configuration information for pre-signed URLs. Valid when `protocols` contains HTTP.
Type: [AwsJobPresignedUrlConfig](API_AwsJobPresignedUrlConfig.md) object
Required: No

 ** creationDate **   <a name="iot-Type-OTAUpdateInfo-creationDate"></a>
The date when the OTA update was created.
Type: Timestamp
Required: No

 ** description **   <a name="iot-Type-OTAUpdateInfo-description"></a>
A description of the OTA update.
Type: String
Length Constraints: Maximum length of 2028.
Pattern: `[^\p{C}]+`
Required: No

 ** errorInfo **   <a name="iot-Type-OTAUpdateInfo-errorInfo"></a>
Error information associated with the OTA update.
Type: [ErrorInfo](API_ErrorInfo.md) object
Required: No

 ** lastModifiedDate **   <a name="iot-Type-OTAUpdateInfo-lastModifiedDate"></a>
The date when the OTA update was last updated.
Type: Timestamp
Required: No

 ** otaUpdateArn **   <a name="iot-Type-OTAUpdateInfo-otaUpdateArn"></a>
The OTA update ARN.
Type: String
Required: No

 ** otaUpdateFiles **   <a name="iot-Type-OTAUpdateInfo-otaUpdateFiles"></a>
A list of files associated with the OTA update.
Type: Array of [OTAUpdateFile](API_OTAUpdateFile.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** otaUpdateId **   <a name="iot-Type-OTAUpdateInfo-otaUpdateId"></a>
The OTA update ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

 ** otaUpdateStatus **   <a name="iot-Type-OTAUpdateInfo-otaUpdateStatus"></a>
The status of the OTA update.
Type: String
Valid Values: `CREATE_PENDING | CREATE_IN_PROGRESS | CREATE_COMPLETE | CREATE_FAILED | DELETE_IN_PROGRESS | DELETE_FAILED`
Required: No

 ** protocols **   <a name="iot-Type-OTAUpdateInfo-protocols"></a>
The protocol used to transfer the OTA update image. Valid values are [HTTP], [MQTT], [HTTP, MQTT]. When both HTTP and MQTT are specified, the target device can choose the protocol.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Valid Values: `MQTT | HTTP`
Required: No

 ** targets **   <a name="iot-Type-OTAUpdateInfo-targets"></a>
The targets of the OTA update.
Type: Array of strings
Array Members: Minimum number of 1 item.
Required: No

 ** targetSelection **   <a name="iot-Type-OTAUpdateInfo-targetSelection"></a>
Specifies whether the OTA update will continue to run (CONTINUOUS), or will be complete after all those things specified as targets have completed the OTA update (SNAPSHOT). If continuous, the OTA update may also be run on a thing when a change is detected in a target. For example, an OTA update will run on a thing when the thing is added to a target group, even after the OTA update was completed by all things originally in the group.
Type: String
Valid Values: `CONTINUOUS | SNAPSHOT`
Required: No

## See Also
<a name="API_OTAUpdateInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/OTAUpdateInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/OTAUpdateInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/OTAUpdateInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
