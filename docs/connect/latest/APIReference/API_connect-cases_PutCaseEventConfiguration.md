---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_PutCaseEventConfiguration.html
---

# PutCaseEventConfiguration
<a name="API_connect-cases_PutCaseEventConfiguration"></a>

Adds case event publishing configuration. For a complete list of fields you can add to the event message, see [Create case fields](https://docs.aws.amazon.com/connect/latest/adminguide/case-fields.html) in the *Connect Customer Administrator Guide*.

## Request Syntax
<a name="API_connect-cases_PutCaseEventConfiguration_RequestSyntax"></a>

```
PUT /domains/{{domainId}}/case-event-configuration HTTP/1.1
Content-type: application/json

{
   "eventBridge": {
      "enabled": {{boolean}},
      "includedData": {
         "caseData": {
            "fields": [
               {
                  "id": "{{string}}"
               }
            ]
         },
         "relatedItemData": {
            "includeContent": {{boolean}}
         }
      }
   }
}
```

## URI Request Parameters
<a name="API_connect-cases_PutCaseEventConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainId](#API_connect-cases_PutCaseEventConfiguration_RequestSyntax) **   <a name="connect-connect-cases_PutCaseEventConfiguration-request-uri-domainId"></a>
The unique identifier of the Cases domain.
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

## Request Body
<a name="API_connect-cases_PutCaseEventConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [eventBridge](#API_connect-cases_PutCaseEventConfiguration_RequestSyntax) **   <a name="connect-connect-cases_PutCaseEventConfiguration-request-eventBridge"></a>
Configuration to enable EventBridge case event delivery and determine what data is delivered.
Type: [EventBridgeConfiguration](API_connect-cases_EventBridgeConfiguration.md) object
Required: Yes

## Response Syntax
<a name="API_connect-cases_PutCaseEventConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_connect-cases_PutCaseEventConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_connect-cases_PutCaseEventConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.
HTTP Status Code: 409

 ** InternalServerException **
We couldn't process your request because of an issue with the server. Try again later.
 ** retryAfterSeconds **
Advice to clients on when the call can be safely retried.
HTTP Status Code: 500

 ** ResourceNotFoundException **
We couldn't find the requested resource. Check that your resources exists and were created in the same AWS Region as your request, and try your request again.
 ** resourceId **
Unique identifier of the resource affected.
 ** resourceType **
Type of the resource affected.
HTTP Status Code: 404

 ** ThrottlingException **
The rate has been exceeded for this API. Please try again after a few minutes.
HTTP Status Code: 429

 ** ValidationException **
The request isn't valid. Check the syntax and try again.
HTTP Status Code: 400

## Examples
<a name="API_connect-cases_PutCaseEventConfiguration_Examples"></a>

### Request and Response example
<a name="API_connect-cases_PutCaseEventConfiguration_Example_1"></a>

This example illustrates one use of PutCaseEventConfiguration.

```
{
  "enabled":true,
  "includedData":{
    "caseData":{
      "fields":[
        {
        "id":"status"
        },
        {
        "id":"title"
        },
        {
        "id":"customer_id"
        },
        {
        "id":"case_reason"
        }
        ]
    },
   "relatedItemData":{
       "includeContent":true
    }
  }}
```

```
{ }
```

## See Also
<a name="API_connect-cases_PutCaseEventConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectcases-2022-10-03/PutCaseEventConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectcases-2022-10-03/PutCaseEventConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/PutCaseEventConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectcases-2022-10-03/PutCaseEventConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/PutCaseEventConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectcases-2022-10-03/PutCaseEventConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectcases-2022-10-03/PutCaseEventConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectcases-2022-10-03/PutCaseEventConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connectcases-2022-10-03/PutCaseEventConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/PutCaseEventConfiguration)
