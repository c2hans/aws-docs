---
source_url: https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_ListApplications.html
---

# ListApplications
<a name="API_ListApplications"></a>

Lists applications based on a set of parameters.

## Request Syntax
<a name="API_ListApplications_RequestSyntax"></a>

```
GET /applications?maxResults={{maxResults}}&nextToken={{nextToken}}&states={{states}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListApplications_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListApplications_RequestSyntax) **   <a name="emrserverless-ListApplications-request-uri-maxResults"></a>
The maximum number of applications that can be listed.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [nextToken](#API_ListApplications_RequestSyntax) **   <a name="emrserverless-ListApplications-request-uri-nextToken"></a>
The token for the next set of application results.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[A-Za-z0-9_=-]+`

 ** [states](#API_ListApplications_RequestSyntax) **   <a name="emrserverless-ListApplications-request-uri-states"></a>
An optional filter for application states. Note that if this filter contains multiple states, the resulting list will be grouped by the state.
Array Members: Minimum number of 1 item. Maximum number of 7 items.
Valid Values: `CREATING | CREATED | STARTING | STARTED | STOPPING | STOPPED | TERMINATED`

## Request Body
<a name="API_ListApplications_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListApplications_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "applications": [
      {
         "architecture": "string",
         "arn": "string",
         "createdAt": number,
         "id": "string",
         "name": "string",
         "releaseLabel": "string",
         "state": "string",
         "stateDetails": "string",
         "type": "string",
         "updatedAt": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListApplications_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [applications](#API_ListApplications_ResponseSyntax) **   <a name="emrserverless-ListApplications-response-applications"></a>
The output lists the specified applications.
Type: Array of [ApplicationSummary](API_ApplicationSummary.md) objects

 ** [nextToken](#API_ListApplications_ResponseSyntax) **   <a name="emrserverless-ListApplications-response-nextToken"></a>
The output displays the token for the next set of application results. This is required for pagination and is available as a response of the previous request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[A-Za-z0-9_=-]+`

## Errors
<a name="API_ListApplications_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
Request processing failed because of an error or failure with the service.
HTTP Status Code: 500

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListApplications_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/emr-serverless-2021-07-13/ListApplications)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/emr-serverless-2021-07-13/ListApplications)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-serverless-2021-07-13/ListApplications)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/emr-serverless-2021-07-13/ListApplications)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-serverless-2021-07-13/ListApplications)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/emr-serverless-2021-07-13/ListApplications)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/emr-serverless-2021-07-13/ListApplications)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/emr-serverless-2021-07-13/ListApplications)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/emr-serverless-2021-07-13/ListApplications)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-serverless-2021-07-13/ListApplications)
