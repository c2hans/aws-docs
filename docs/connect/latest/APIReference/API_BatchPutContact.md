---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_BatchPutContact.html
---

# BatchPutContact
<a name="API_BatchPutContact"></a>

**Note**
Only the Connect Customer outbound campaigns service principal is allowed to assume a role in your account and call this API.

Allows you to create a batch of contacts in Connect Customer. The outbound campaigns capability ingests dial requests via the [PutDialRequestBatch](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_PutDialRequestBatch.html) API. It then uses BatchPutContact to create contacts corresponding to those dial requests. If agents are available, the dial requests are dialed out, which results in a voice call. The resulting voice call uses the same contactId that was created by BatchPutContact.

## Request Syntax
<a name="API_BatchPutContact_RequestSyntax"></a>

```
PUT /contact/batch/{{InstanceId}} HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "ContactDataRequestList": [
      {
         "Attributes": {
            "{{string}}" : "{{string}}"
         },
         "Campaign": {
            "CampaignId": "{{string}}"
         },
         "CustomerEndpoint": {
            "Address": "{{string}}",
            "Type": "{{string}}"
         },
         "OutboundStrategy": {
            "Config": {
               "AgentFirst": {
                  "Preview": {
                     "AllowedUserActions": [ "{{string}}" ],
                     "PostAcceptTimeoutConfig": {
                        "DurationInSeconds": {{number}}
                     }
                  }
               }
            },
            "Type": "{{string}}"
         },
         "QueueId": "{{string}}",
         "RequestIdentifier": "{{string}}",
         "SystemEndpoint": {
            "Address": "{{string}}",
            "Type": "{{string}}"
         }
      }
   ]
}
```

## URI Request Parameters
<a name="API_BatchPutContact_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_BatchPutContact_RequestSyntax) **   <a name="connect-BatchPutContact-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_BatchPutContact_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_BatchPutContact_RequestSyntax) **   <a name="connect-BatchPutContact-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** [ContactDataRequestList](#API_BatchPutContact_RequestSyntax) **   <a name="connect-BatchPutContact-request-ContactDataRequestList"></a>
List of individual contact requests.
Type: Array of [ContactDataRequest](API_ContactDataRequest.md) objects
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Required: Yes

## Response Syntax
<a name="API_BatchPutContact_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "FailedRequestList": [
      {
         "FailureReasonCode": "string",
         "FailureReasonMessage": "string",
         "RequestIdentifier": "string"
      }
   ],
   "SuccessfulRequestList": [
      {
         "ContactId": "string",
         "RequestIdentifier": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchPutContact_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FailedRequestList](#API_BatchPutContact_ResponseSyntax) **   <a name="connect-BatchPutContact-response-FailedRequestList"></a>
List of requests for which contact creation failed.
Type: Array of [FailedRequest](API_FailedRequest.md) objects

 ** [SuccessfulRequestList](#API_BatchPutContact_ResponseSyntax) **   <a name="connect-BatchPutContact-response-SuccessfulRequestList"></a>
List of requests for which contact was successfully created.
Type: Array of [SuccessfulRequest](API_SuccessfulRequest.md) objects

## Errors
<a name="API_BatchPutContact_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** IdempotencyException **
An entity with the same name already exists.
HTTP Status Code: 409

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** LimitExceededException **
The allowed limit for the resource has been exceeded.
 ** Message **
The message about the limit.
HTTP Status Code: 429

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

## See Also
<a name="API_BatchPutContact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/BatchPutContact)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/BatchPutContact)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/BatchPutContact)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/BatchPutContact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/BatchPutContact)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/BatchPutContact)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/BatchPutContact)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/BatchPutContact)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/BatchPutContact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/BatchPutContact)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
