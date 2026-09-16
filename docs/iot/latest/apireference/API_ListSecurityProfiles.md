---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ListSecurityProfiles.html
---

# ListSecurityProfiles
<a name="API_ListSecurityProfiles"></a>

**Note**
The AWS IoT Device Defender detect feature will no longer be available to new customers starting August 31, 2026. If you would like to use the detect feature, sign up prior to August 31, 2026. To learn about alternatives to AWS IoT Device Defender detect, see [AWS IoT Device Defender detect feature availability change](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/dd-detect-availability-change.html). There is no change to AWS IoT Device Defender audit availability.

Lists the Device Defender security profiles you've created. You can filter security profiles by dimension or custom metric.

Requires permission to access the [ListSecurityProfiles](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

**Note**
 `dimensionName` and `metricName` cannot be used in the same request.

## Request Syntax
<a name="API_ListSecurityProfiles_RequestSyntax"></a>

```
GET /security-profiles?dimensionName={{dimensionName}}&maxResults={{maxResults}}&metricName={{metricName}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListSecurityProfiles_RequestParameters"></a>

The request uses the following URI parameters.

 ** [dimensionName](#API_ListSecurityProfiles_RequestSyntax) **   <a name="iot-ListSecurityProfiles-request-uri-dimensionName"></a>
A filter to limit results to the security profiles that use the defined dimension. Cannot be used with `metricName`
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`

 ** [maxResults](#API_ListSecurityProfiles_RequestSyntax) **   <a name="iot-ListSecurityProfiles-request-uri-maxResults"></a>
The maximum number of results to return at one time.
Valid Range: Minimum value of 1. Maximum value of 250.

 ** [metricName](#API_ListSecurityProfiles_RequestSyntax) **   <a name="iot-ListSecurityProfiles-request-uri-metricName"></a>
 The name of the custom metric. Cannot be used with `dimensionName`.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`

 ** [nextToken](#API_ListSecurityProfiles_RequestSyntax) **   <a name="iot-ListSecurityProfiles-request-uri-nextToken"></a>
The token for the next set of results.

## Request Body
<a name="API_ListSecurityProfiles_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListSecurityProfiles_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "securityProfileIdentifiers": [
      {
         "arn": "string",
         "name": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListSecurityProfiles_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListSecurityProfiles_ResponseSyntax) **   <a name="iot-ListSecurityProfiles-response-nextToken"></a>
A token that can be used to retrieve the next set of results, or `null` if there are no additional results.
Type: String

 ** [securityProfileIdentifiers](#API_ListSecurityProfiles_ResponseSyntax) **   <a name="iot-ListSecurityProfiles-response-securityProfileIdentifiers"></a>
A list of security profile identifiers (names and ARNs).
Type: Array of [SecurityProfileIdentifier](API_SecurityProfileIdentifier.md) objects

## Errors
<a name="API_ListSecurityProfiles_Errors"></a>

 ** InternalFailureException **
An unexpected error has occurred.
 ** message **
The message for the exception.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** message **
The message for the exception.
HTTP Status Code: 404

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

## See Also
<a name="API_ListSecurityProfiles_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/ListSecurityProfiles)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/ListSecurityProfiles)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ListSecurityProfiles)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/ListSecurityProfiles)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ListSecurityProfiles)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/ListSecurityProfiles)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/ListSecurityProfiles)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/ListSecurityProfiles)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/ListSecurityProfiles)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ListSecurityProfiles)
