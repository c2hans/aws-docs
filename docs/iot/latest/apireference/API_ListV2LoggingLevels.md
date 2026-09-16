---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ListV2LoggingLevels.html
---

# ListV2LoggingLevels
<a name="API_ListV2LoggingLevels"></a>

Lists logging levels.

Requires permission to access the [ListV2LoggingLevels](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_ListV2LoggingLevels_RequestSyntax"></a>

```
GET /v2LoggingLevel?maxResults={{maxResults}}&nextToken={{nextToken}}&targetType={{targetType}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListV2LoggingLevels_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListV2LoggingLevels_RequestSyntax) **   <a name="iot-ListV2LoggingLevels-request-uri-maxResults"></a>
The maximum number of results to return at one time.
Valid Range: Minimum value of 1. Maximum value of 250.

 ** [nextToken](#API_ListV2LoggingLevels_RequestSyntax) **   <a name="iot-ListV2LoggingLevels-request-uri-nextToken"></a>
To retrieve the next set of results, the `nextToken` value from a previous response; otherwise **null** to receive the first set of results.

 ** [targetType](#API_ListV2LoggingLevels_RequestSyntax) **   <a name="iot-ListV2LoggingLevels-request-uri-targetType"></a>
The type of resource for which you are configuring logging. Must be `THING_Group`.
Valid Values: `DEFAULT | THING_GROUP | CLIENT_ID | SOURCE_IP | PRINCIPAL_ID`

## Request Body
<a name="API_ListV2LoggingLevels_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListV2LoggingLevels_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "logTargetConfigurations": [
      {
         "logLevel": "string",
         "logTarget": {
            "targetName": "string",
            "targetType": "string"
         }
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListV2LoggingLevels_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [logTargetConfigurations](#API_ListV2LoggingLevels_ResponseSyntax) **   <a name="iot-ListV2LoggingLevels-response-logTargetConfigurations"></a>
The logging configuration for a target.
Type: Array of [LogTargetConfiguration](API_LogTargetConfiguration.md) objects

 ** [nextToken](#API_ListV2LoggingLevels_ResponseSyntax) **   <a name="iot-ListV2LoggingLevels-response-nextToken"></a>
The token to use to get the next set of results, or **null** if there are no additional results.
Type: String

## Errors
<a name="API_ListV2LoggingLevels_Errors"></a>

 ** InternalException **
An unexpected error has occurred.
 ** message **
The message for the exception.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** NotConfiguredException **
The resource is not configured.
 ** message **
The message for the exception.
HTTP Status Code: 404

 ** ServiceUnavailableException **
The service is temporarily unavailable.
 ** message **
The message for the exception.
HTTP Status Code: 503

## See Also
<a name="API_ListV2LoggingLevels_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/ListV2LoggingLevels)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/ListV2LoggingLevels)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ListV2LoggingLevels)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/ListV2LoggingLevels)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ListV2LoggingLevels)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/ListV2LoggingLevels)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/ListV2LoggingLevels)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/ListV2LoggingLevels)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/ListV2LoggingLevels)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ListV2LoggingLevels)
