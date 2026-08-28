---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_CreateConfig.html
---

# CreateConfig
<a name="API_CreateConfig"></a>

Creates a `Config` with the specified `configData` parameters.

Only one type of `configData` can be specified.

## Request Syntax
<a name="API_CreateConfig_RequestSyntax"></a>

```
POST /config HTTP/1.1
Content-type: application/json

{
   "configData": { ... },
   "name": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateConfig_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateConfig_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [configData](#API_CreateConfig_RequestSyntax) **   <a name="groundstation-CreateConfig-request-configData"></a>
Parameters of a `Config`.
Type: [ConfigTypeData](API_ConfigTypeData.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [name](#API_CreateConfig_RequestSyntax) **   <a name="groundstation-CreateConfig-request-name"></a>
Name of a `Config`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[ a-zA-Z0-9_:-]{1,256}`
Required: Yes

 ** [tags](#API_CreateConfig_RequestSyntax) **   <a name="groundstation-CreateConfig-request-tags"></a>
Tags assigned to a `Config`.
Type: String to string map
Required: No

## Response Syntax
<a name="API_CreateConfig_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "configArn": "string",
   "configId": "string",
   "configType": "string"
}
```

## Response Elements
<a name="API_CreateConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [configArn](#API_CreateConfig_ResponseSyntax) **   <a name="groundstation-CreateConfig-response-configArn"></a>
ARN of a `Config`.
Type: String
Length Constraints: Minimum length of 82. Maximum length of 424.
Pattern: `arn:aws:groundstation:[-a-z0-9]{1,50}:[0-9]{12}:config/[a-z0-9]+(-[a-z0-9]+){0,4}/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(/.{1,256})?`

 ** [configId](#API_CreateConfig_ResponseSyntax) **   <a name="groundstation-CreateConfig-response-configId"></a>
UUID of a `Config`.
Type: String

 ** [configType](#API_CreateConfig_ResponseSyntax) **   <a name="groundstation-CreateConfig-response-configType"></a>
Type of a `Config`.
Type: String
Valid Values: `antenna-downlink | antenna-downlink-demod-decode | tracking | dataflow-endpoint | antenna-uplink | uplink-echo | s3-recording | telemetry-sink`

## Errors
<a name="API_CreateConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DependencyException **
Dependency encountered an error.
 ** parameterName **
Name of the parameter that caused the exception.
HTTP Status Code: 531

 ** InvalidParameterException **
One or more parameters are not valid.
 ** parameterName **
Name of the invalid parameter.
HTTP Status Code: 431

 ** ResourceLimitExceededException **
Account limits for this resource have been exceeded.
 ** parameterName **
Name of the parameter that exceeded the resource limit.
HTTP Status Code: 429

 ** ResourceNotFoundException **
Resource was not found.
HTTP Status Code: 434

## See Also
<a name="API_CreateConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/groundstation-2019-05-23/CreateConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/groundstation-2019-05-23/CreateConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/CreateConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/groundstation-2019-05-23/CreateConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/CreateConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/groundstation-2019-05-23/CreateConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/groundstation-2019-05-23/CreateConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/groundstation-2019-05-23/CreateConfig)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/groundstation-2019-05-23/CreateConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/CreateConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Ground Station. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ground-station` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
