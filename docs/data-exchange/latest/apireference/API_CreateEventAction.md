---
source_url: https://docs.aws.amazon.com/data-exchange/latest/apireference/API_CreateEventAction.html
---

# CreateEventAction
<a name="API_CreateEventAction"></a>

This operation creates an event action.

## Request Syntax
<a name="API_CreateEventAction_RequestSyntax"></a>

```
POST /v1/event-actions HTTP/1.1
Content-type: application/json

{
   "Action": {
      "ExportRevisionToS3": {
         "Encryption": {
            "KmsKeyArn": "{{string}}",
            "Type": "{{string}}"
         },
         "RevisionDestination": {
            "Bucket": "{{string}}",
            "KeyPattern": "{{string}}"
         }
      }
   },
   "Event": {
      "RevisionPublished": {
         "DataSetId": "{{string}}"
      }
   },
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateEventAction_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateEventAction_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Action](#API_CreateEventAction_RequestSyntax) **   <a name="dataexchange-CreateEventAction-request-Action"></a>
What occurs after a certain event.
Type: [Action](API_Action.md) object
Required: Yes

 ** [Event](#API_CreateEventAction_RequestSyntax) **   <a name="dataexchange-CreateEventAction-request-Event"></a>
What occurs to start an action.
Type: [Event](API_Event.md) object
Required: Yes

 ** [Tags](#API_CreateEventAction_RequestSyntax) **   <a name="dataexchange-CreateEventAction-request-Tags"></a>
Key-value pairs that you can associate with the event action.
Type: String to string map
Required: No

## Response Syntax
<a name="API_CreateEventAction_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "Action": {
      "ExportRevisionToS3": {
         "Encryption": {
            "KmsKeyArn": "string",
            "Type": "string"
         },
         "RevisionDestination": {
            "Bucket": "string",
            "KeyPattern": "string"
         }
      }
   },
   "Arn": "string",
   "CreatedAt": "string",
   "Event": {
      "RevisionPublished": {
         "DataSetId": "string"
      }
   },
   "Id": "string",
   "Tags": {
      "string" : "string"
   },
   "UpdatedAt": "string"
}
```

## Response Elements
<a name="API_CreateEventAction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [Action](#API_CreateEventAction_ResponseSyntax) **   <a name="dataexchange-CreateEventAction-response-Action"></a>
What occurs after a certain event.
Type: [Action](API_Action.md) object

 ** [Arn](#API_CreateEventAction_ResponseSyntax) **   <a name="dataexchange-CreateEventAction-response-Arn"></a>
The ARN for the event action.
Type: String

 ** [CreatedAt](#API_CreateEventAction_ResponseSyntax) **   <a name="dataexchange-CreateEventAction-response-CreatedAt"></a>
The date and time that the event action was created, in ISO 8601 format.
Type: Timestamp

 ** [Event](#API_CreateEventAction_ResponseSyntax) **   <a name="dataexchange-CreateEventAction-response-Event"></a>
What occurs to start an action.
Type: [Event](API_Event.md) object

 ** [Id](#API_CreateEventAction_ResponseSyntax) **   <a name="dataexchange-CreateEventAction-response-Id"></a>
The unique identifier for the event action.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`

 ** [Tags](#API_CreateEventAction_ResponseSyntax) **   <a name="dataexchange-CreateEventAction-response-Tags"></a>
The tags for the event action.
Type: String to string map

 ** [UpdatedAt](#API_CreateEventAction_ResponseSyntax) **   <a name="dataexchange-CreateEventAction-response-UpdatedAt"></a>
The date and time that the event action was last updated, in ISO 8601 format.
Type: Timestamp

## Errors
<a name="API_CreateEventAction_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to the resource is denied.
 ** Message **
Access to the resource is denied.
HTTP Status Code: 403

 ** InternalServerException **
An exception occurred with the service.
 ** Message **
The message identifying the service exception that occurred.
HTTP Status Code: 500

 ** ServiceLimitExceededException **
The request has exceeded the quotas imposed by the service.
 ** LimitName **
The name of the limit that was reached.
 ** LimitValue **
The value of the exceeded limit.
 ** Message **
The request has exceeded the quotas imposed by the service.
HTTP Status Code: 402

 ** ThrottlingException **
The limit on the number of requests per second was exceeded.
 ** Message **
The limit on the number of requests per second was exceeded.
HTTP Status Code: 429

 ** ValidationException **
The request was invalid.
 ** ExceptionCause **
The unique identifier for the resource that couldn't be found.
 ** Message **
The message that informs you about what was invalid about the request.
HTTP Status Code: 400

## See Also
<a name="API_CreateEventAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dataexchange-2017-07-25/CreateEventAction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dataexchange-2017-07-25/CreateEventAction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dataexchange-2017-07-25/CreateEventAction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dataexchange-2017-07-25/CreateEventAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dataexchange-2017-07-25/CreateEventAction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dataexchange-2017-07-25/CreateEventAction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dataexchange-2017-07-25/CreateEventAction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dataexchange-2017-07-25/CreateEventAction)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dataexchange-2017-07-25/CreateEventAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dataexchange-2017-07-25/CreateEventAction)
