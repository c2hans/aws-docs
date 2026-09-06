---
source_url: https://docs.aws.amazon.com/m2/latest/APIReference/API_ListEnvironments.html
---

# ListEnvironments
<a name="API_ListEnvironments"></a>

**Important**
 AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

Lists the runtime environments.

## Request Syntax
<a name="API_ListEnvironments_RequestSyntax"></a>

```
GET /environments?engineType={{engineType}}&maxResults={{maxResults}}&names={{names}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListEnvironments_RequestParameters"></a>

The request uses the following URI parameters.

 ** [engineType](#API_ListEnvironments_RequestSyntax) **   <a name="m2-ListEnvironments-request-uri-engineType"></a>
The engine type for the runtime environment.
Valid Values: `microfocus | bluage`

 ** [maxResults](#API_ListEnvironments_RequestSyntax) **   <a name="m2-ListEnvironments-request-uri-maxResults"></a>
The maximum number of runtime environments to return.
Valid Range: Minimum value of 1. Maximum value of 2000.

 ** [names](#API_ListEnvironments_RequestSyntax) **   <a name="m2-ListEnvironments-request-uri-names"></a>
The names of the runtime environments. Must be unique within the account.
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Pattern: `[A-Za-z0-9][A-Za-z0-9_\-]{1,59}`

 ** [nextToken](#API_ListEnvironments_RequestSyntax) **   <a name="m2-ListEnvironments-request-uri-nextToken"></a>
A pagination token to control the number of runtime environments displayed in the list.
Pattern: `\S{1,2000}`

## Request Body
<a name="API_ListEnvironments_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListEnvironments_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "environments": [
      {
         "creationTime": number,
         "engineType": "string",
         "engineVersion": "string",
         "environmentArn": "string",
         "environmentId": "string",
         "instanceType": "string",
         "name": "string",
         "networkType": "string",
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListEnvironments_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [environments](#API_ListEnvironments_ResponseSyntax) **   <a name="m2-ListEnvironments-response-environments"></a>
Returns a list of summary details for all the runtime environments in your account.
Type: Array of [EnvironmentSummary](API_EnvironmentSummary.md) objects

 ** [nextToken](#API_ListEnvironments_ResponseSyntax) **   <a name="m2-ListEnvironments-response-nextToken"></a>
A pagination token that's returned when the response doesn't contain all the runtime environments.
Type: String
Pattern: `\S{1,2000}`

## Errors
<a name="API_ListEnvironments_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The account or role doesn't have the right permissions to make the request.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred during the processing of the request.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 ** ThrottlingException **
The number of requests made exceeds the limit.
 ** quotaCode **
The identifier of the throttled request.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
 ** serviceCode **
The identifier of the service that the throttled request was made to.
HTTP Status Code: 429

 ** ValidationException **
One or more parameters provided in the request is not valid.
 ** fieldList **
The list of fields that failed service validation.
 ** reason **
The reason why it failed service validation.
HTTP Status Code: 400

## See Also
<a name="API_ListEnvironments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/m2-2021-04-28/ListEnvironments)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/m2-2021-04-28/ListEnvironments)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/m2-2021-04-28/ListEnvironments)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/m2-2021-04-28/ListEnvironments)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/m2-2021-04-28/ListEnvironments)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/m2-2021-04-28/ListEnvironments)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/m2-2021-04-28/ListEnvironments)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/m2-2021-04-28/ListEnvironments)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/m2-2021-04-28/ListEnvironments)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/m2-2021-04-28/ListEnvironments)
