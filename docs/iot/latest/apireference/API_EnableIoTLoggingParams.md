---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_EnableIoTLoggingParams.html
---

# EnableIoTLoggingParams
<a name="API_EnableIoTLoggingParams"></a>

Parameters used when defining a mitigation action that enable AWS IoT Core logging.

## Contents
<a name="API_EnableIoTLoggingParams_Contents"></a>

 ** logLevel **   <a name="iot-Type-EnableIoTLoggingParams-logLevel"></a>
Specifies the type of information to be logged.
Type: String
Valid Values: `DEBUG | INFO | ERROR | WARN | DISABLED`
Required: Yes

 ** roleArnForLogging **   <a name="iot-Type-EnableIoTLoggingParams-roleArnForLogging"></a>
The Amazon Resource Name (ARN) of the IAM role used for logging.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: Yes

## See Also
<a name="API_EnableIoTLoggingParams_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/EnableIoTLoggingParams)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/EnableIoTLoggingParams)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/EnableIoTLoggingParams)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
