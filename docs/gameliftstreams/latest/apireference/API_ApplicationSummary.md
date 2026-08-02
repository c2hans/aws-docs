---
source_url: https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ApplicationSummary.html
---

# ApplicationSummary
<a name="API_ApplicationSummary"></a>

Describes an application resource that represents a collection of content for streaming with Amazon GameLift Streams. To retrieve additional application details, call [GetApplication](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetApplication.html).

## Contents
<a name="API_ApplicationSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Arn **   <a name="gameliftstreams-Type-ApplicationSummary-Arn"></a>
An Amazon Resource Name (ARN) that's assigned to an application resource and uniquely identifies the application across all AWS Regions. Format is `arn:aws:gameliftstreams:[AWS Region]:[AWS account]:application/[resource ID]`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(^[a-zA-Z0-9-]+$)|(^arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)$)`
Required: Yes

 ** CreatedAt **   <a name="gameliftstreams-Type-ApplicationSummary-CreatedAt"></a>
A timestamp that indicates when this resource was created. Timestamps are expressed using in ISO8601 format, such as: `2022-12-27T22:29:40+00:00` (UTC).
Type: Timestamp
Required: No

 ** Description **   <a name="gameliftstreams-Type-ApplicationSummary-Description"></a>
A human-readable label for the application. You can edit this value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Pattern: `[a-zA-Z0-9-_.!+@/][a-zA-Z0-9-_.!+@/ ]*`
Required: No

 ** Id **   <a name="gameliftstreams-Type-ApplicationSummary-Id"></a>
An ID that uniquely identifies the application resource. Example ID: `a-9ZY8X7Wv6`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[a-zA-Z0-9-]+`
Required: No

 ** LastUpdatedAt **   <a name="gameliftstreams-Type-ApplicationSummary-LastUpdatedAt"></a>
A timestamp that indicates when this resource was last updated. Timestamps are expressed using in ISO8601 format, such as: `2022-12-27T22:29:40+00:00` (UTC).
Type: Timestamp
Required: No

 ** RuntimeEnvironment **   <a name="gameliftstreams-Type-ApplicationSummary-RuntimeEnvironment"></a>
 Configuration settings that identify the operating system for an application resource. This can also include a compatibility layer and other drivers.
A runtime environment can be one of the following:
+  For Linux applications
  +  Ubuntu 22.04 LTS (`Type=UBUNTU, Version=22_04_LTS`)
+  For Windows applications
  + Microsoft Windows Server 2022 Base (`Type=WINDOWS, Version=2022`)
  + Proton 10.0-4 (`Type=PROTON, Version=20260204`)
  + Proton 9.0-2 (`Type=PROTON, Version=20250516`)
  + Proton 8.0-5 (`Type=PROTON, Version=20241007`)
  + Proton 8.0-2c (`Type=PROTON, Version=20230704`)
Type: [RuntimeEnvironment](API_RuntimeEnvironment.md) object
Required: No

 ** Status **   <a name="gameliftstreams-Type-ApplicationSummary-Status"></a>
The current status of the application resource. Possible statuses include the following:
+  `INITIALIZED`: Amazon GameLift Streams has received the request and is initiating the work flow to create an application.
+  `PROCESSING`: The create application work flow is in process. Amazon GameLift Streams is copying the content and caching for future deployment in a stream group.
+  `READY`: The application is ready to deploy in a stream group.
+  `ERROR`: An error occurred when setting up the application. For more information about the error, call `GetApplication` and refer to `StatusReason`.
+  `DELETING`: Amazon GameLift Streams is in the process of deleting the application.
Type: String
Valid Values: `INITIALIZED | PROCESSING | READY | DELETING | ERROR`
Required: No

## See Also
<a name="API_ApplicationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gameliftstreams-2018-05-10/ApplicationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gameliftstreams-2018-05-10/ApplicationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gameliftstreams-2018-05-10/ApplicationSummary)
