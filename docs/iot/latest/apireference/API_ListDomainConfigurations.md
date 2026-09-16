---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ListDomainConfigurations.html
---

# ListDomainConfigurations
<a name="API_ListDomainConfigurations"></a>

Gets a list of domain configurations for the user. This list is sorted alphabetically by domain configuration name.

Requires permission to access the [ListDomainConfigurations](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_ListDomainConfigurations_RequestSyntax"></a>

```
GET /domainConfigurations?marker={{marker}}&pageSize={{pageSize}}&serviceType={{serviceType}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDomainConfigurations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [marker](#API_ListDomainConfigurations_RequestSyntax) **   <a name="iot-ListDomainConfigurations-request-uri-marker"></a>
The marker for the next set of results.
Length Constraints: Maximum length of 1024.
Pattern: `[A-Za-z0-9+/]+={0,2}`

 ** [pageSize](#API_ListDomainConfigurations_RequestSyntax) **   <a name="iot-ListDomainConfigurations-request-uri-pageSize"></a>
The result page size.
Valid Range: Minimum value of 1. Maximum value of 250.

 ** [serviceType](#API_ListDomainConfigurations_RequestSyntax) **   <a name="iot-ListDomainConfigurations-request-uri-serviceType"></a>
The type of service delivered by the endpoint.
Valid Values: `DATA | CREDENTIAL_PROVIDER | JOBS`

## Request Body
<a name="API_ListDomainConfigurations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDomainConfigurations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "domainConfigurations": [
      {
         "domainConfigurationArn": "string",
         "domainConfigurationName": "string",
         "serviceType": "string"
      }
   ],
   "nextMarker": "string"
}
```

## Response Elements
<a name="API_ListDomainConfigurations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [domainConfigurations](#API_ListDomainConfigurations_ResponseSyntax) **   <a name="iot-ListDomainConfigurations-response-domainConfigurations"></a>
A list of objects that contain summary information about the user's domain configurations.
Type: Array of [DomainConfigurationSummary](API_DomainConfigurationSummary.md) objects

 ** [nextMarker](#API_ListDomainConfigurations_ResponseSyntax) **   <a name="iot-ListDomainConfigurations-response-nextMarker"></a>
The marker for the next set of results.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `[A-Za-z0-9+/]+={0,2}`

## Errors
<a name="API_ListDomainConfigurations_Errors"></a>

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

 ** ServiceUnavailableException **
The service is temporarily unavailable.
 ** message **
The message for the exception.
HTTP Status Code: 503

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** UnauthorizedException **
You are not authorized to perform this operation.
 ** message **
The message for the exception.
HTTP Status Code: 401

## See Also
<a name="API_ListDomainConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/ListDomainConfigurations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/ListDomainConfigurations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ListDomainConfigurations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/ListDomainConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ListDomainConfigurations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/ListDomainConfigurations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/ListDomainConfigurations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/ListDomainConfigurations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/ListDomainConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ListDomainConfigurations)
