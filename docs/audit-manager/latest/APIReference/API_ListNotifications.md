---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ListNotifications.html
---

# ListNotifications
<a name="API_ListNotifications"></a>

**Important**
 AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html).

 Returns a list of all AWS Audit Manager notifications.

## Request Syntax
<a name="API_ListNotifications_RequestSyntax"></a>

```
GET /notifications?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListNotifications_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListNotifications_RequestSyntax) **   <a name="auditmanager-ListNotifications-request-uri-maxResults"></a>
 Represents the maximum number of results on a page or for an API request call.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [nextToken](#API_ListNotifications_RequestSyntax) **   <a name="auditmanager-ListNotifications-request-uri-nextToken"></a>
 The pagination token that's used to fetch the next set of results.
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^[A-Za-z0-9+\/=]*$`

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
         "assessmentId": "string",
         "assessmentName": "string",
         "controlSetId": "string",
         "controlSetName": "string",
         "description": "string",
         "eventTime": number,
         "id": "string",
         "source": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListNotifications_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListNotifications_ResponseSyntax) **   <a name="auditmanager-ListNotifications-response-nextToken"></a>
 The pagination token that's used to fetch the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^[A-Za-z0-9+\/=]*$`

 ** [notifications](#API_ListNotifications_ResponseSyntax) **   <a name="auditmanager-ListNotifications-response-notifications"></a>
 The returned list of notifications.
Type: Array of [Notification](API_Notification.md) objects

## Errors
<a name="API_ListNotifications_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 Your account isn't registered with AWS Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again.
HTTP Status Code: 403

 ** InternalServerException **
 An internal service error occurred during the processing of your request. Try again later.
HTTP Status Code: 500

 ** ValidationException **
 The request has invalid or missing parameters.
 ** fields **
 The fields that caused the error, if applicable.
 ** reason **
 The reason the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_ListNotifications_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/auditmanager-2017-07-25/ListNotifications)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/auditmanager-2017-07-25/ListNotifications)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/ListNotifications)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/auditmanager-2017-07-25/ListNotifications)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/ListNotifications)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/auditmanager-2017-07-25/ListNotifications)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/auditmanager-2017-07-25/ListNotifications)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/auditmanager-2017-07-25/ListNotifications)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/auditmanager-2017-07-25/ListNotifications)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/ListNotifications)
