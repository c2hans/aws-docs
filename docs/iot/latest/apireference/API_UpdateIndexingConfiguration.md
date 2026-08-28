---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateIndexingConfiguration.html
---

# UpdateIndexingConfiguration
<a name="API_UpdateIndexingConfiguration"></a>

Updates the search configuration.

Requires permission to access the [UpdateIndexingConfiguration](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_UpdateIndexingConfiguration_RequestSyntax"></a>

```
POST /indexing/config HTTP/1.1
Content-type: application/json

{
   "thingGroupIndexingConfiguration": {
      "customFields": [
         {
            "name": "{{string}}",
            "type": "{{string}}"
         }
      ],
      "managedFields": [
         {
            "name": "{{string}}",
            "type": "{{string}}"
         }
      ],
      "thingGroupIndexingMode": "{{string}}"
   },
   "thingIndexingConfiguration": {
      "customFields": [
         {
            "name": "{{string}}",
            "type": "{{string}}"
         }
      ],
      "deviceDefenderIndexingMode": "{{string}}",
      "filter": {
         "connectivity": {
            "includeSocketInformation": [ "{{string}}" ]
         },
         "geoLocations": [
            {
               "name": "{{string}}",
               "order": "{{string}}"
            }
         ],
         "namedShadowNames": [ "{{string}}" ]
      },
      "managedFields": [
         {
            "name": "{{string}}",
            "type": "{{string}}"
         }
      ],
      "namedShadowIndexingMode": "{{string}}",
      "thingConnectivityIndexingMode": "{{string}}",
      "thingIndexingMode": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdateIndexingConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateIndexingConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [thingGroupIndexingConfiguration](#API_UpdateIndexingConfiguration_RequestSyntax) **   <a name="iot-UpdateIndexingConfiguration-request-thingGroupIndexingConfiguration"></a>
Thing group indexing configuration.
Type: [ThingGroupIndexingConfiguration](API_ThingGroupIndexingConfiguration.md) object
Required: No

 ** [thingIndexingConfiguration](#API_UpdateIndexingConfiguration_RequestSyntax) **   <a name="iot-UpdateIndexingConfiguration-request-thingIndexingConfiguration"></a>
Thing indexing configuration.
Type: [ThingIndexingConfiguration](API_ThingIndexingConfiguration.md) object
Required: No

## Response Syntax
<a name="API_UpdateIndexingConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateIndexingConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateIndexingConfiguration_Errors"></a>

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
<a name="API_UpdateIndexingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/UpdateIndexingConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/UpdateIndexingConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/UpdateIndexingConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/UpdateIndexingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/UpdateIndexingConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/UpdateIndexingConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/UpdateIndexingConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/UpdateIndexingConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/UpdateIndexingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/UpdateIndexingConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
