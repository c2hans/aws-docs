---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_GetConfig.html
---

# GetConfig
<a name="API_GetConfig"></a>

Returns `Config` information.

Only one `Config` response can be returned.

## Request Syntax
<a name="API_GetConfig_RequestSyntax"></a>

```
GET /config/{{configType}}/{{configId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetConfig_RequestParameters"></a>

The request uses the following URI parameters.

 ** [configId](#API_GetConfig_RequestSyntax) **   <a name="groundstation-GetConfig-request-uri-configId"></a>
UUID of a `Config`.
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** [configType](#API_GetConfig_RequestSyntax) **   <a name="groundstation-GetConfig-request-uri-configType"></a>
Type of a `Config`.
Valid Values: `antenna-downlink | antenna-downlink-demod-decode | tracking | dataflow-endpoint | antenna-uplink | uplink-echo | s3-recording | telemetry-sink`
Required: Yes

## Request Body
<a name="API_GetConfig_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetConfig_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "configArn": "string",
   "configData": { ... },
   "configId": "string",
   "configType": "string",
   "name": "string",
   "tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_GetConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [configArn](#API_GetConfig_ResponseSyntax) **   <a name="groundstation-GetConfig-response-configArn"></a>
ARN of a `Config`
Type: String
Length Constraints: Minimum length of 82. Maximum length of 424.
Pattern: `arn:aws:groundstation:[-a-z0-9]{1,50}:[0-9]{12}:config/[a-z0-9]+(-[a-z0-9]+){0,4}/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(/.{1,256})?`

 ** [configData](#API_GetConfig_ResponseSyntax) **   <a name="groundstation-GetConfig-response-configData"></a>
Data elements in a `Config`.
Type: [ConfigTypeData](API_ConfigTypeData.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [configId](#API_GetConfig_ResponseSyntax) **   <a name="groundstation-GetConfig-response-configId"></a>
UUID of a `Config`.
Type: String

 ** [configType](#API_GetConfig_ResponseSyntax) **   <a name="groundstation-GetConfig-response-configType"></a>
Type of a `Config`.
Type: String
Valid Values: `antenna-downlink | antenna-downlink-demod-decode | tracking | dataflow-endpoint | antenna-uplink | uplink-echo | s3-recording | telemetry-sink`

 ** [name](#API_GetConfig_ResponseSyntax) **   <a name="groundstation-GetConfig-response-name"></a>
Name of a `Config`.
Type: String

 ** [tags](#API_GetConfig_ResponseSyntax) **   <a name="groundstation-GetConfig-response-tags"></a>
Tags assigned to a `Config`.
Type: String to string map

## Errors
<a name="API_GetConfig_Errors"></a>

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

 ** ResourceNotFoundException **
Resource was not found.
HTTP Status Code: 434

## See Also
<a name="API_GetConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/groundstation-2019-05-23/GetConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/groundstation-2019-05-23/GetConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/GetConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/groundstation-2019-05-23/GetConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/GetConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/groundstation-2019-05-23/GetConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/groundstation-2019-05-23/GetConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/groundstation-2019-05-23/GetConfig)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/groundstation-2019-05-23/GetConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/GetConfig)
