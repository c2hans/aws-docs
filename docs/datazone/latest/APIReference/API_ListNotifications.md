---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_ListNotifications.html
---

# ListNotifications
<a name="API_ListNotifications"></a>

Lists all Amazon DataZone notifications.

## Request Syntax
<a name="API_ListNotifications_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/notifications?afterTimestamp={{afterTimestamp}}&beforeTimestamp={{beforeTimestamp}}&maxResults={{maxResults}}&nextToken={{nextToken}}&subjects={{subjects}}&taskStatus={{taskStatus}}&type={{type}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListNotifications_RequestParameters"></a>

The request uses the following URI parameters.

 ** [afterTimestamp](#API_ListNotifications_RequestSyntax) **   <a name="datazone-ListNotifications-request-uri-afterTimestamp"></a>
The time after which you want to list notifications.

 ** [beforeTimestamp](#API_ListNotifications_RequestSyntax) **   <a name="datazone-ListNotifications-request-uri-beforeTimestamp"></a>
The time before which you want to list notifications.

 ** [domainIdentifier](#API_ListNotifications_RequestSyntax) **   <a name="datazone-ListNotifications-request-uri-domainIdentifier"></a>
The identifier of the Amazon DataZone domain.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [maxResults](#API_ListNotifications_RequestSyntax) **   <a name="datazone-ListNotifications-request-uri-maxResults"></a>
The maximum number of notifications to return in a single call to `ListNotifications`. When the number of notifications to be listed is greater than the value of `MaxResults`, the response contains a `NextToken` value that you can use in a subsequent call to `ListNotifications` to list the next set of notifications.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [nextToken](#API_ListNotifications_RequestSyntax) **   <a name="datazone-ListNotifications-request-uri-nextToken"></a>
When the number of notifications is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of notifications, the response includes a pagination token named `NextToken`. You can specify this `NextToken` value in a subsequent call to `ListNotifications` to list the next set of notifications.
Length Constraints: Minimum length of 1. Maximum length of 8192.

 ** [subjects](#API_ListNotifications_RequestSyntax) **   <a name="datazone-ListNotifications-request-uri-subjects"></a>
The subjects of notifications.

 ** [taskStatus](#API_ListNotifications_RequestSyntax) **   <a name="datazone-ListNotifications-request-uri-taskStatus"></a>
The task status of notifications.
Valid Values: `ACTIVE | INACTIVE`

 ** [type](#API_ListNotifications_RequestSyntax) **   <a name="datazone-ListNotifications-request-uri-type"></a>
The type of notifications.
Valid Values: `TASK | EVENT`
Required: Yes

## Request Body
<a name="API_ListNotifications_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListNotifications_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "notifications": [
      {
         "actionLink": "string",
         "creationTimestamp": number,
         "domainIdentifier": "string",
         "identifier": "string",
         "lastUpdatedTimestamp": number,
         "message": "string",
         "metadata": {
            "string" : "string"
         },
         "status": "string",
         "title": "string",
         "topic": {
            "resource": {
               "id": "string",
               "name": "string",
               "type": "string"
            },
            "role": "string",
            "subject": "string"
         },
         "type": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListNotifications_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListNotifications_ResponseSyntax) **   <a name="datazone-ListNotifications-response-nextToken"></a>
When the number of notifications is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of notifications, the response includes a pagination token named `NextToken`. You can specify this `NextToken` value in a subsequent call to `ListNotifications` to list the next set of notifications.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.

 ** [notifications](#API_ListNotifications_ResponseSyntax) **   <a name="datazone-ListNotifications-response-notifications"></a>
The results of the `ListNotifications` action.
Type: Array of [NotificationOutput](API_NotificationOutput.md) objects

## Errors
<a name="API_ListNotifications_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource cannot be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** UnauthorizedException **
You do not have permission to perform this action.
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by the AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListNotifications_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/ListNotifications)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/ListNotifications)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/ListNotifications)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/ListNotifications)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/ListNotifications)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/ListNotifications)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/ListNotifications)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/ListNotifications)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/ListNotifications)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/ListNotifications)
