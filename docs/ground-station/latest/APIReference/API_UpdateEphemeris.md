---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_UpdateEphemeris.html
---

# UpdateEphemeris
<a name="API_UpdateEphemeris"></a>

Update an existing ephemeris.

## Request Syntax
<a name="API_UpdateEphemeris_RequestSyntax"></a>

```
PUT /ephemeris/{{ephemerisId}} HTTP/1.1
Content-type: application/json

{
   "enabled": {{boolean}},
   "name": "{{string}}",
   "priority": {{number}}
}
```

## URI Request Parameters
<a name="API_UpdateEphemeris_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ephemerisId](#API_UpdateEphemeris_RequestSyntax) **   <a name="groundstation-UpdateEphemeris-request-uri-ephemerisId"></a>
The AWS Ground Station ephemeris ID.
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

## Request Body
<a name="API_UpdateEphemeris_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [enabled](#API_UpdateEphemeris_RequestSyntax) **   <a name="groundstation-UpdateEphemeris-request-enabled"></a>
Enable or disable the ephemeris. Changing this value doesn't require re-validation.
Type: Boolean
Required: Yes

 ** [name](#API_UpdateEphemeris_RequestSyntax) **   <a name="groundstation-UpdateEphemeris-request-name"></a>
A name that you can use to identify the ephemeris.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[ a-zA-Z0-9_:-]{1,256}`
Required: No

 ** [priority](#API_UpdateEphemeris_RequestSyntax) **   <a name="groundstation-UpdateEphemeris-request-priority"></a>
A priority score that determines which ephemeris to use when multiple ephemerides overlap.
Higher numbers take precedence. The default is 1. Must be 1 or greater.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 99999.
Required: No

## Response Syntax
<a name="API_UpdateEphemeris_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ephemerisId": "string"
}
```

## Response Elements
<a name="API_UpdateEphemeris_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ephemerisId](#API_UpdateEphemeris_ResponseSyntax) **   <a name="groundstation-UpdateEphemeris-response-ephemerisId"></a>
The AWS Ground Station ephemeris ID.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

## Errors
<a name="API_UpdateEphemeris_Errors"></a>

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
<a name="API_UpdateEphemeris_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/groundstation-2019-05-23/UpdateEphemeris)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/groundstation-2019-05-23/UpdateEphemeris)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/UpdateEphemeris)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/groundstation-2019-05-23/UpdateEphemeris)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/UpdateEphemeris)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/groundstation-2019-05-23/UpdateEphemeris)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/groundstation-2019-05-23/UpdateEphemeris)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/groundstation-2019-05-23/UpdateEphemeris)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/groundstation-2019-05-23/UpdateEphemeris)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/UpdateEphemeris)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Ground Station. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ground-station` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
