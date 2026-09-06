---
source_url: https://docs.aws.amazon.com/panorama/latest/api/API_ListApplicationInstances.html
---

# ListApplicationInstances
<a name="API_ListApplicationInstances"></a>

**Important**
End of support notice: On May 31, 2026, AWS will end support for AWS Panorama. After May 31, 2026, you will no longer be able to access the AWS Panorama console or AWS Panorama resources. For more information, see [AWS Panorama end of support](https://docs.aws.amazon.com/panorama/latest/dev/panorama-end-of-support.html).

Returns a list of application instances.

## Request Syntax
<a name="API_ListApplicationInstances_RequestSyntax"></a>

```
GET /application-instances?deviceId={{DeviceId}}&maxResults={{MaxResults}}&nextToken={{NextToken}}&statusFilter={{StatusFilter}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListApplicationInstances_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DeviceId](#API_ListApplicationInstances_RequestSyntax) **   <a name="panorama-ListApplicationInstances-request-uri-DeviceId"></a>
The application instances' device ID.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\-\_]+`

 ** [MaxResults](#API_ListApplicationInstances_RequestSyntax) **   <a name="panorama-ListApplicationInstances-request-uri-MaxResults"></a>
The maximum number of application instances to return in one page of results.
Valid Range: Minimum value of 0. Maximum value of 25.

 ** [NextToken](#API_ListApplicationInstances_RequestSyntax) **   <a name="panorama-ListApplicationInstances-request-uri-NextToken"></a>
Specify the pagination token from a previous request to retrieve the next page of results.
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `.+`

 ** [StatusFilter](#API_ListApplicationInstances_RequestSyntax) **   <a name="panorama-ListApplicationInstances-request-uri-StatusFilter"></a>
Only include instances with a specific status.
Valid Values: `DEPLOYMENT_SUCCEEDED | DEPLOYMENT_ERROR | REMOVAL_SUCCEEDED | REMOVAL_FAILED | PROCESSING_DEPLOYMENT | PROCESSING_REMOVAL | DEPLOYMENT_FAILED`

## Request Body
<a name="API_ListApplicationInstances_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListApplicationInstances_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ApplicationInstances": [
      {
         "ApplicationInstanceId": "string",
         "Arn": "string",
         "CreatedTime": number,
         "DefaultRuntimeContextDevice": "string",
         "DefaultRuntimeContextDeviceName": "string",
         "Description": "string",
         "HealthStatus": "string",
         "Name": "string",
         "RuntimeContextStates": [
            {
               "DesiredState": "string",
               "DeviceReportedStatus": "string",
               "DeviceReportedTime": number,
               "RuntimeContextName": "string"
            }
         ],
         "Status": "string",
         "StatusDescription": "string",
         "Tags": {
            "string" : "string"
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListApplicationInstances_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApplicationInstances](#API_ListApplicationInstances_ResponseSyntax) **   <a name="panorama-ListApplicationInstances-response-ApplicationInstances"></a>
A list of application instances.
Type: Array of [ApplicationInstance](API_ApplicationInstance.md) objects

 ** [NextToken](#API_ListApplicationInstances_ResponseSyntax) **   <a name="panorama-ListApplicationInstances-response-NextToken"></a>
A pagination token that's included if more results are available.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `.+`

## Errors
<a name="API_ListApplicationInstances_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The requestor does not have permission to access the target action or resource.
HTTP Status Code: 403

 ** InternalServerException **
An internal error occurred.
 ** RetryAfterSeconds **
The number of seconds a client should wait before retrying the call.
HTTP Status Code: 500

## See Also
<a name="API_ListApplicationInstances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/panorama-2019-07-24/ListApplicationInstances)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/panorama-2019-07-24/ListApplicationInstances)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/panorama-2019-07-24/ListApplicationInstances)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/panorama-2019-07-24/ListApplicationInstances)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/panorama-2019-07-24/ListApplicationInstances)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/panorama-2019-07-24/ListApplicationInstances)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/panorama-2019-07-24/ListApplicationInstances)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/panorama-2019-07-24/ListApplicationInstances)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/panorama-2019-07-24/ListApplicationInstances)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/panorama-2019-07-24/ListApplicationInstances)
