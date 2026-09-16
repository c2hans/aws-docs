---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListDataAccessors.html
---

# ListDataAccessors
<a name="API_ListDataAccessors"></a>

**Note**
Amazon Q Business will no longer be open to new customers starting on July 31, 2026. If you would like to use the service, please sign up prior to July 30. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

Lists the data accessors for a Amazon Q Business application. This operation returns a paginated list of data accessor summaries, including the friendly name, unique identifier, ARN, associated IAM role, and creation/update timestamps for each data accessor.

## Request Syntax
<a name="API_ListDataAccessors_RequestSyntax"></a>

```
GET /applications/{{applicationId}}/dataaccessors?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDataAccessors_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_ListDataAccessors_RequestSyntax) **   <a name="qbusiness-ListDataAccessors-request-uri-applicationId"></a>
The unique identifier of the Amazon Q Business application.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: Yes

 ** [maxResults](#API_ListDataAccessors_RequestSyntax) **   <a name="qbusiness-ListDataAccessors-request-uri-maxResults"></a>
The maximum number of results to return in a single call.
Valid Range: Minimum value of 1. Maximum value of 10.

 ** [nextToken](#API_ListDataAccessors_RequestSyntax) **   <a name="qbusiness-ListDataAccessors-request-uri-nextToken"></a>
The token for the next set of results. (You received this token from a previous call.)
Length Constraints: Minimum length of 1. Maximum length of 1500.

## Request Body
<a name="API_ListDataAccessors_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDataAccessors_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "dataAccessors": [
      {
         "authenticationDetail": {
            "authenticationConfiguration": { ... },
            "authenticationType": "string",
            "externalIds": [ "string" ]
         },
         "createdAt": number,
         "dataAccessorArn": "string",
         "dataAccessorId": "string",
         "displayName": "string",
         "idcApplicationArn": "string",
         "principal": "string",
         "updatedAt": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListDataAccessors_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [dataAccessors](#API_ListDataAccessors_ResponseSyntax) **   <a name="qbusiness-ListDataAccessors-response-dataAccessors"></a>
The list of data accessors.
Type: Array of [DataAccessor](API_DataAccessor.md) objects

 ** [nextToken](#API_ListDataAccessors_ResponseSyntax) **   <a name="qbusiness-ListDataAccessors-response-nextToken"></a>
The token to use to retrieve the next set of results, if there are any.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1500.

## Errors
<a name="API_ListDataAccessors_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.
HTTP Status Code: 403

 ** InternalServerException **
An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact [Support](http://aws.amazon.com/contact-us/) for help.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.
 ** message **
The message describing a `ResourceNotFoundException`.
 ** resourceId **
The identifier of the resource affected.
 ** resourceType **
The type of the resource affected.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to throttling. Reduce the number of requests and try again.
HTTP Status Code: 429

 ** ValidationException **
The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.
 ** fields **
The input field(s) that failed validation.
 ** message **
The message describing the `ValidationException`.
 ** reason **
The reason for the `ValidationException`.
HTTP Status Code: 400

## See Also
<a name="API_ListDataAccessors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qbusiness-2023-11-27/ListDataAccessors)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qbusiness-2023-11-27/ListDataAccessors)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/ListDataAccessors)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qbusiness-2023-11-27/ListDataAccessors)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/ListDataAccessors)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qbusiness-2023-11-27/ListDataAccessors)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qbusiness-2023-11-27/ListDataAccessors)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qbusiness-2023-11-27/ListDataAccessors)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/qbusiness-2023-11-27/ListDataAccessors)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/ListDataAccessors)
