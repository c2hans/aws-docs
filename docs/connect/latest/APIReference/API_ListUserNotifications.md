---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ListUserNotifications.html
---

# ListUserNotifications
<a name="API_ListUserNotifications"></a>

Retrieves a paginated list of notifications for a specific user, including the notification status for that user.

## Request Syntax
<a name="API_ListUserNotifications_RequestSyntax"></a>

```
GET /users/{{InstanceId}}/{{UserId}}/notifications?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListUserNotifications_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_ListUserNotifications_RequestSyntax) **   <a name="connect-ListUserNotifications-request-uri-InstanceId"></a>
The identifier of the Amazon Connect instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [MaxResults](#API_ListUserNotifications_RequestSyntax) **   <a name="connect-ListUserNotifications-request-uri-MaxResults"></a>
The maximum number of results to return per page. Valid range is 1-1000.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [NextToken](#API_ListUserNotifications_RequestSyntax) **   <a name="connect-ListUserNotifications-request-uri-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response to retrieve the next page of results.

 ** [UserId](#API_ListUserNotifications_RequestSyntax) **   <a name="connect-ListUserNotifications-request-uri-UserId"></a>
The identifier of the user.
Required: Yes

## Request Body
<a name="API_ListUserNotifications_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListUserNotifications_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "UserNotifications": [
      {
         "Content": {
            "string" : "string"
         },
         "CreatedAt": number,
         "ExpiresAt": number,
         "InstanceId": "string",
         "NotificationId": "string",
         "NotificationStatus": "string",
         "Priority": "string",
         "RecipientId": "string",
         "Source": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListUserNotifications_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListUserNotifications_ResponseSyntax) **   <a name="connect-ListUserNotifications-response-NextToken"></a>
The token for the next set of results. If present, there are more results available.
Type: String

 ** [UserNotifications](#API_ListUserNotifications_ResponseSyntax) **   <a name="connect-ListUserNotifications-response-UserNotifications"></a>
A list of notifications sent to the specified user.
Type: Array of [UserNotificationSummary](API_UserNotificationSummary.md) objects

## Errors
<a name="API_ListUserNotifications_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_ListUserNotifications_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/ListUserNotifications)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/ListUserNotifications)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ListUserNotifications)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/ListUserNotifications)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ListUserNotifications)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/ListUserNotifications)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/ListUserNotifications)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/ListUserNotifications)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/ListUserNotifications)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ListUserNotifications)
