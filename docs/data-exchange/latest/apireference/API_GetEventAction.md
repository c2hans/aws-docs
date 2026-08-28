---
source_url: https://docs.aws.amazon.com/data-exchange/latest/apireference/API_GetEventAction.html
---

# GetEventAction
<a name="API_GetEventAction"></a>

This operation retrieves information about an event action.

## Request Syntax
<a name="API_GetEventAction_RequestSyntax"></a>

```
GET /v1/event-actions/{{EventActionId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetEventAction_RequestParameters"></a>

The request uses the following URI parameters.

 ** [EventActionId](#API_GetEventAction_RequestSyntax) **   <a name="dataexchange-GetEventAction-request-uri-EventActionId"></a>
The unique identifier for the event action.
Required: Yes

## Request Body
<a name="API_GetEventAction_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetEventAction_ResponseSyntax"></a>

```
HTTP/1.1 200
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
<a name="API_GetEventAction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Action](#API_GetEventAction_ResponseSyntax) **   <a name="dataexchange-GetEventAction-response-Action"></a>
What occurs after a certain event.
Type: [Action](API_Action.md) object

 ** [Arn](#API_GetEventAction_ResponseSyntax) **   <a name="dataexchange-GetEventAction-response-Arn"></a>
The ARN for the event action.
Type: String

 ** [CreatedAt](#API_GetEventAction_ResponseSyntax) **   <a name="dataexchange-GetEventAction-response-CreatedAt"></a>
The date and time that the event action was created, in ISO 8601 format.
Type: Timestamp

 ** [Event](#API_GetEventAction_ResponseSyntax) **   <a name="dataexchange-GetEventAction-response-Event"></a>
What occurs to start an action.
Type: [Event](API_Event.md) object

 ** [Id](#API_GetEventAction_ResponseSyntax) **   <a name="dataexchange-GetEventAction-response-Id"></a>
The unique identifier for the event action.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`

 ** [Tags](#API_GetEventAction_ResponseSyntax) **   <a name="dataexchange-GetEventAction-response-Tags"></a>
The tags for the event action.
Type: String to string map

 ** [UpdatedAt](#API_GetEventAction_ResponseSyntax) **   <a name="dataexchange-GetEventAction-response-UpdatedAt"></a>
The date and time that the event action was last updated, in ISO 8601 format.
Type: Timestamp

## Errors
<a name="API_GetEventAction_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An exception occurred with the service.
 ** Message **
The message identifying the service exception that occurred.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource couldn't be found.
 ** Message **
The resource couldn't be found.
 ** ResourceId **
The unique identifier for the resource that couldn't be found.
 ** ResourceType **
The type of resource that couldn't be found.
HTTP Status Code: 404

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
<a name="API_GetEventAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dataexchange-2017-07-25/GetEventAction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dataexchange-2017-07-25/GetEventAction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dataexchange-2017-07-25/GetEventAction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dataexchange-2017-07-25/GetEventAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dataexchange-2017-07-25/GetEventAction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dataexchange-2017-07-25/GetEventAction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dataexchange-2017-07-25/GetEventAction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dataexchange-2017-07-25/GetEventAction)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dataexchange-2017-07-25/GetEventAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dataexchange-2017-07-25/GetEventAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Data Exchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query data-exchange` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
