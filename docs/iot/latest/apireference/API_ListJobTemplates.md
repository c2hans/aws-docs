---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ListJobTemplates.html
---

# ListJobTemplates
<a name="API_ListJobTemplates"></a>

Returns a list of job templates.

Requires permission to access the [ListJobTemplates](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_ListJobTemplates_RequestSyntax"></a>

```
GET /job-templates?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListJobTemplates_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListJobTemplates_RequestSyntax) **   <a name="iot-ListJobTemplates-request-uri-maxResults"></a>
The maximum number of results to return in the list.
Valid Range: Minimum value of 1. Maximum value of 250.

 ** [nextToken](#API_ListJobTemplates_RequestSyntax) **   <a name="iot-ListJobTemplates-request-uri-nextToken"></a>
The token to use to return the next set of results in the list.

## Request Body
<a name="API_ListJobTemplates_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListJobTemplates_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "jobTemplates": [
      {
         "createdAt": number,
         "description": "string",
         "jobTemplateArn": "string",
         "jobTemplateId": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListJobTemplates_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [jobTemplates](#API_ListJobTemplates_ResponseSyntax) **   <a name="iot-ListJobTemplates-response-jobTemplates"></a>
A list of objects that contain information about the job templates.
Type: Array of [JobTemplateSummary](API_JobTemplateSummary.md) objects

 ** [nextToken](#API_ListJobTemplates_ResponseSyntax) **   <a name="iot-ListJobTemplates-response-nextToken"></a>
The token for the next set of results, or **null** if there are no additional results.
Type: String

## Errors
<a name="API_ListJobTemplates_Errors"></a>

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

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

## See Also
<a name="API_ListJobTemplates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/ListJobTemplates)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/ListJobTemplates)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ListJobTemplates)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/ListJobTemplates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ListJobTemplates)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/ListJobTemplates)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/ListJobTemplates)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/ListJobTemplates)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/ListJobTemplates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ListJobTemplates)
