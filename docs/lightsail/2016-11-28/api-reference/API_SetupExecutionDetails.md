---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_SetupExecutionDetails.html
---

# SetupExecutionDetails
<a name="API_SetupExecutionDetails"></a>

Returns details about the commands that were run.

## Contents
<a name="API_SetupExecutionDetails_Contents"></a>

 ** command **   <a name="Lightsail-Type-SetupExecutionDetails-command"></a>
The command that was executed.
Type: String
Required: No

 ** dateTime **   <a name="Lightsail-Type-SetupExecutionDetails-dateTime"></a>
The timestamp for when the request was run.
Type: Timestamp
Required: No

 ** name **   <a name="Lightsail-Type-SetupExecutionDetails-name"></a>
The name of the target resource.
Type: String
Pattern: `.*\S.*`
Required: No

 ** standardError **   <a name="Lightsail-Type-SetupExecutionDetails-standardError"></a>
The text written by the command to stderr.
Type: String
Required: No

 ** standardOutput **   <a name="Lightsail-Type-SetupExecutionDetails-standardOutput"></a>
The text written by the command to stdout.
Type: String
Required: No

 ** status **   <a name="Lightsail-Type-SetupExecutionDetails-status"></a>
The status of the `SetupInstanceHttps` request.
Type: String
Valid Values: `succeeded | failed | inProgress`
Required: No

 ** version **   <a name="Lightsail-Type-SetupExecutionDetails-version"></a>
The current version of the script..
Type: String
Required: No

## See Also
<a name="API_SetupExecutionDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/SetupExecutionDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/SetupExecutionDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/SetupExecutionDetails)
