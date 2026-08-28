---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DescribeEphemeris.html
---

# DescribeEphemeris
<a name="API_DescribeEphemeris"></a>

Retrieve information about an existing ephemeris.

## Request Syntax
<a name="API_DescribeEphemeris_RequestSyntax"></a>

```
GET /ephemeris/{{ephemerisId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeEphemeris_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ephemerisId](#API_DescribeEphemeris_RequestSyntax) **   <a name="groundstation-DescribeEphemeris-request-uri-ephemerisId"></a>
The AWS Ground Station ephemeris ID.
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

## Request Body
<a name="API_DescribeEphemeris_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeEphemeris_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "creationTime": number,
   "enabled": boolean,
   "ephemerisId": "string",
   "errorReasons": [
      {
         "errorCode": "string",
         "errorMessage": "string"
      }
   ],
   "invalidReason": "string",
   "name": "string",
   "priority": number,
   "satelliteId": "string",
   "status": "string",
   "suppliedData": { ... },
   "tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_DescribeEphemeris_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [creationTime](#API_DescribeEphemeris_ResponseSyntax) **   <a name="groundstation-DescribeEphemeris-response-creationTime"></a>
The time the ephemeris was uploaded in UTC.
Type: Timestamp

 ** [enabled](#API_DescribeEphemeris_ResponseSyntax) **   <a name="groundstation-DescribeEphemeris-response-enabled"></a>
Whether or not the ephemeris is enabled.
Type: Boolean

 ** [ephemerisId](#API_DescribeEphemeris_ResponseSyntax) **   <a name="groundstation-DescribeEphemeris-response-ephemerisId"></a>
The AWS Ground Station ephemeris ID.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

 ** [errorReasons](#API_DescribeEphemeris_ResponseSyntax) **   <a name="groundstation-DescribeEphemeris-response-errorReasons"></a>
Detailed error information for ephemerides with `INVALID` status.
Provides specific error codes and messages to help diagnose validation failures.
Type: Array of [EphemerisErrorReason](API_EphemerisErrorReason.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.

 ** [invalidReason](#API_DescribeEphemeris_ResponseSyntax) **   <a name="groundstation-DescribeEphemeris-response-invalidReason"></a>
Reason that an ephemeris failed validation. Appears only when the status is `INVALID`.
Type: String
Valid Values: `METADATA_INVALID | TIME_RANGE_INVALID | TRAJECTORY_INVALID | KMS_KEY_INVALID | VALIDATION_ERROR`

 ** [name](#API_DescribeEphemeris_ResponseSyntax) **   <a name="groundstation-DescribeEphemeris-response-name"></a>
A name that you can use to identify the ephemeris.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[ a-zA-Z0-9_:-]{1,256}`

 ** [priority](#API_DescribeEphemeris_ResponseSyntax) **   <a name="groundstation-DescribeEphemeris-response-priority"></a>
A priority score that determines which ephemeris to use when multiple ephemerides overlap.
Higher numbers take precedence. The default is 1. Must be 1 or greater.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 99999.

 ** [satelliteId](#API_DescribeEphemeris_ResponseSyntax) **   <a name="groundstation-DescribeEphemeris-response-satelliteId"></a>
The AWS Ground Station satellite ID associated with ephemeris.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

 ** [status](#API_DescribeEphemeris_ResponseSyntax) **   <a name="groundstation-DescribeEphemeris-response-status"></a>
The status of the ephemeris.
Type: String
Valid Values: `VALIDATING | INVALID | ERROR | ENABLED | DISABLED | EXPIRED`

 ** [suppliedData](#API_DescribeEphemeris_ResponseSyntax) **   <a name="groundstation-DescribeEphemeris-response-suppliedData"></a>
Supplied ephemeris data.
Type: [EphemerisTypeDescription](API_EphemerisTypeDescription.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [tags](#API_DescribeEphemeris_ResponseSyntax) **   <a name="groundstation-DescribeEphemeris-response-tags"></a>
Tags assigned to an ephemeris.
Type: String to string map

## Errors
<a name="API_DescribeEphemeris_Errors"></a>

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
<a name="API_DescribeEphemeris_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/groundstation-2019-05-23/DescribeEphemeris)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/groundstation-2019-05-23/DescribeEphemeris)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/DescribeEphemeris)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/groundstation-2019-05-23/DescribeEphemeris)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/DescribeEphemeris)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/groundstation-2019-05-23/DescribeEphemeris)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/groundstation-2019-05-23/DescribeEphemeris)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/groundstation-2019-05-23/DescribeEphemeris)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/groundstation-2019-05-23/DescribeEphemeris)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/DescribeEphemeris)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Ground Station. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ground-station` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
