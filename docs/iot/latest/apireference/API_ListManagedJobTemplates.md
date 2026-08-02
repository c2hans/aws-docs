---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ListManagedJobTemplates.html
---

# ListManagedJobTemplates
<a name="API_ListManagedJobTemplates"></a>

Returns a list of managed job templates.

## Request Syntax
<a name="API_ListManagedJobTemplates_RequestSyntax"></a>

```
GET /managed-job-templates?maxResults={{maxResults}}&nextToken={{nextToken}}&templateName={{templateName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListManagedJobTemplates_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListManagedJobTemplates_RequestSyntax) **   <a name="iot-ListManagedJobTemplates-request-uri-maxResults"></a>
Maximum number of entries that can be returned.
Valid Range: Minimum value of 1. Maximum value of 250.

 ** [nextToken](#API_ListManagedJobTemplates_RequestSyntax) **   <a name="iot-ListManagedJobTemplates-request-uri-nextToken"></a>
The token to retrieve the next set of results.

 ** [templateName](#API_ListManagedJobTemplates_RequestSyntax) **   <a name="iot-ListManagedJobTemplates-request-uri-templateName"></a>
An optional parameter for template name. If specified, only the versions of the managed job templates that have the specified template name will be returned.
Length Constraints: Minimum length of 1. Maximum length of 64.

## Request Body
<a name="API_ListManagedJobTemplates_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListManagedJobTemplates_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "managedJobTemplates": [
      {
         "description": "string",
         "environments": [ "string" ],
         "templateArn": "string",
         "templateName": "string",
         "templateVersion": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListManagedJobTemplates_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [managedJobTemplates](#API_ListManagedJobTemplates_ResponseSyntax) **   <a name="iot-ListManagedJobTemplates-response-managedJobTemplates"></a>
A list of managed job templates that are returned.
Type: Array of [ManagedJobTemplateSummary](API_ManagedJobTemplateSummary.md) objects

 ** [nextToken](#API_ListManagedJobTemplates_ResponseSyntax) **   <a name="iot-ListManagedJobTemplates-response-nextToken"></a>
The token to retrieve the next set of results.
Type: String

## Errors
<a name="API_ListManagedJobTemplates_Errors"></a>

 ** InternalServerException **
Internal error from the service that indicates an unexpected error or that the service is unavailable.
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
<a name="API_ListManagedJobTemplates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/ListManagedJobTemplates)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/ListManagedJobTemplates)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ListManagedJobTemplates)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/ListManagedJobTemplates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ListManagedJobTemplates)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/ListManagedJobTemplates)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/ListManagedJobTemplates)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/ListManagedJobTemplates)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/ListManagedJobTemplates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ListManagedJobTemplates)
