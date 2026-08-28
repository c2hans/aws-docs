---
source_url: https://docs.aws.amazon.com/data-exchange/latest/apireference/API_SendDataSetNotification.html
---

# SendDataSetNotification
<a name="API_SendDataSetNotification"></a>

The type of event associated with the data set.

## Request Syntax
<a name="API_SendDataSetNotification_RequestSyntax"></a>

```
POST /v1/data-sets/{{DataSetId}}/notification HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "Comment": "{{string}}",
   "Details": {
      "DataUpdate": {
         "DataUpdatedAt": "{{string}}"
      },
      "Deprecation": {
         "DeprecationAt": "{{string}}"
      },
      "SchemaChange": {
         "Changes": [
            {
               "Description": "{{string}}",
               "Name": "{{string}}",
               "Type": "{{string}}"
            }
         ],
         "SchemaChangeAt": "{{string}}"
      }
   },
   "Scope": {
      "LakeFormationTagPolicies": [
         {
            "Database": "{{string}}",
            "Table": "{{string}}"
         }
      ],
      "RedshiftDataShares": [
         {
            "Arn": "{{string}}",
            "Database": "{{string}}",
            "Function": "{{string}}",
            "Schema": "{{string}}",
            "Table": "{{string}}",
            "View": "{{string}}"
         }
      ],
      "S3DataAccesses": [
         {
            "KeyPrefixes": [ "{{string}}" ],
            "Keys": [ "{{string}}" ]
         }
      ]
   },
   "Type": "{{string}}"
}
```

## URI Request Parameters
<a name="API_SendDataSetNotification_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DataSetId](#API_SendDataSetNotification_RequestSyntax) **   <a name="dataexchange-SendDataSetNotification-request-uri-DataSetId"></a>
Affected data set of the notification.
Pattern: `[a-zA-Z0-9]{30,40}`
Required: Yes

## Request Body
<a name="API_SendDataSetNotification_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_SendDataSetNotification_RequestSyntax) **   <a name="dataexchange-SendDataSetNotification-request-ClientToken"></a>
Idempotency key for the notification, this key allows us to deduplicate notifications that are sent in quick succession erroneously.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\x21-\x7E]{1,64}`
Required: No

 ** [Comment](#API_SendDataSetNotification_RequestSyntax) **   <a name="dataexchange-SendDataSetNotification-request-Comment"></a>
Free-form text field for providers to add information about their notifications.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** [Details](#API_SendDataSetNotification_RequestSyntax) **   <a name="dataexchange-SendDataSetNotification-request-Details"></a>
Extra details specific to this notification type.
Type: [NotificationDetails](API_NotificationDetails.md) object
Required: No

 ** [Scope](#API_SendDataSetNotification_RequestSyntax) **   <a name="dataexchange-SendDataSetNotification-request-Scope"></a>
Affected scope of this notification such as the underlying resources affected by the notification event.
Type: [ScopeDetails](API_ScopeDetails.md) object
Required: No

 ** [Type](#API_SendDataSetNotification_RequestSyntax) **   <a name="dataexchange-SendDataSetNotification-request-Type"></a>
The type of the notification. Describing the kind of event the notification is alerting you to.
Type: String
Valid Values: `DATA_DELAY | DATA_UPDATE | DEPRECATION | SCHEMA_CHANGE`
Required: Yes

## Response Syntax
<a name="API_SendDataSetNotification_ResponseSyntax"></a>

```
HTTP/1.1 202
```

## Response Elements
<a name="API_SendDataSetNotification_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response with an empty HTTP body.

## Errors
<a name="API_SendDataSetNotification_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to the resource is denied.
 ** Message **
Access to the resource is denied.
HTTP Status Code: 403

 ** ConflictException **
The request couldn't be completed because it conflicted with the current state of the resource.
 ** Message **
The request couldn't be completed because it conflicted with the current state of the resource.
 ** ResourceId **
The unique identifier for the resource with the conflict.
 ** ResourceType **
The type of the resource with the conflict.
HTTP Status Code: 409

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
<a name="API_SendDataSetNotification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dataexchange-2017-07-25/SendDataSetNotification)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dataexchange-2017-07-25/SendDataSetNotification)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dataexchange-2017-07-25/SendDataSetNotification)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dataexchange-2017-07-25/SendDataSetNotification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dataexchange-2017-07-25/SendDataSetNotification)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dataexchange-2017-07-25/SendDataSetNotification)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dataexchange-2017-07-25/SendDataSetNotification)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dataexchange-2017-07-25/SendDataSetNotification)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dataexchange-2017-07-25/SendDataSetNotification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dataexchange-2017-07-25/SendDataSetNotification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Data Exchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query data-exchange` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
