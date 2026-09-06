---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_CreateEphemeris.html
---

# CreateEphemeris
<a name="API_CreateEphemeris"></a>

Create an ephemeris with your specified [EphemerisData](API_EphemerisData.md).

## Request Syntax
<a name="API_CreateEphemeris_RequestSyntax"></a>

```
POST /ephemeris HTTP/1.1
Content-type: application/json

{
   "enabled": {{boolean}},
   "ephemeris": { ... },
   "expirationTime": {{number}},
   "kmsKeyArn": "{{string}}",
   "name": "{{string}}",
   "priority": {{number}},
   "satelliteId": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateEphemeris_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateEphemeris_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [enabled](#API_CreateEphemeris_RequestSyntax) **   <a name="groundstation-CreateEphemeris-request-enabled"></a>
Set to `true` to enable the ephemeris after validation. Set to `false` to keep it disabled.
Type: Boolean
Required: No

 ** [ephemeris](#API_CreateEphemeris_RequestSyntax) **   <a name="groundstation-CreateEphemeris-request-ephemeris"></a>
Ephemeris data.
Type: [EphemerisData](API_EphemerisData.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [expirationTime](#API_CreateEphemeris_RequestSyntax) **   <a name="groundstation-CreateEphemeris-request-expirationTime"></a>
An overall expiration time for the ephemeris in UTC, after which it will become `EXPIRED`.
Type: Timestamp
Required: No

 ** [kmsKeyArn](#API_CreateEphemeris_RequestSyntax) **   <a name="groundstation-CreateEphemeris-request-kmsKeyArn"></a>
The ARN of the KMS key to use for encrypting the ephemeris.
Type: String
Required: No

 ** [name](#API_CreateEphemeris_RequestSyntax) **   <a name="groundstation-CreateEphemeris-request-name"></a>
A name that you can use to identify the ephemeris.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[ a-zA-Z0-9_:-]{1,256}`
Required: Yes

 ** [priority](#API_CreateEphemeris_RequestSyntax) **   <a name="groundstation-CreateEphemeris-request-priority"></a>
A priority score that determines which ephemeris to use when multiple ephemerides overlap.
Higher numbers take precedence. The default is 1. Must be 1 or greater.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 99999.
Required: No

 ** [satelliteId](#API_CreateEphemeris_RequestSyntax) **   <a name="groundstation-CreateEphemeris-request-satelliteId"></a>
The satellite ID that associates this ephemeris with a satellite in AWS Ground Station.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** [tags](#API_CreateEphemeris_RequestSyntax) **   <a name="groundstation-CreateEphemeris-request-tags"></a>
Tags assigned to an ephemeris.
Type: String to string map
Required: No

## Response Syntax
<a name="API_CreateEphemeris_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ephemerisId": "string"
}
```

## Response Elements
<a name="API_CreateEphemeris_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ephemerisId](#API_CreateEphemeris_ResponseSyntax) **   <a name="groundstation-CreateEphemeris-response-ephemerisId"></a>
The AWS Ground Station ephemeris ID.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

## Errors
<a name="API_CreateEphemeris_Errors"></a>

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
<a name="API_CreateEphemeris_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/groundstation-2019-05-23/CreateEphemeris)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/groundstation-2019-05-23/CreateEphemeris)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/CreateEphemeris)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/groundstation-2019-05-23/CreateEphemeris)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/CreateEphemeris)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/groundstation-2019-05-23/CreateEphemeris)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/groundstation-2019-05-23/CreateEphemeris)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/groundstation-2019-05-23/CreateEphemeris)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/groundstation-2019-05-23/CreateEphemeris)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/CreateEphemeris)
