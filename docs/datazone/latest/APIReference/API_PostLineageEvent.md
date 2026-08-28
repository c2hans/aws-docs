---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_PostLineageEvent.html
---

# PostLineageEvent
<a name="API_PostLineageEvent"></a>

Posts a data lineage event.

## Request Syntax
<a name="API_PostLineageEvent_RequestSyntax"></a>

```
POST /v2/domains/{{domainIdentifier}}/lineage/events HTTP/1.1
Client-Token: {{clientToken}}

{{event}}
```

## URI Request Parameters
<a name="API_PostLineageEvent_RequestParameters"></a>

The request uses the following URI parameters.

 ** [clientToken](#API_PostLineageEvent_RequestSyntax) **   <a name="datazone-PostLineageEvent-request-clientToken"></a>
A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\x21-\x7E]+`

 ** [domainIdentifier](#API_PostLineageEvent_RequestSyntax) **   <a name="datazone-PostLineageEvent-request-uri-domainIdentifier"></a>
The ID of the domain where you want to post a data lineage event.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_PostLineageEvent_RequestBody"></a>

The request accepts the following binary data.

 ** [event](#API_PostLineageEvent_RequestSyntax) **   <a name="datazone-PostLineageEvent-request-event"></a>
The data lineage event that you want to post. Only open-lineage run event are supported as events.
Length Constraints: Minimum length of 0. Maximum length of 300000.
Required: Yes

## Response Syntax
<a name="API_PostLineageEvent_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "domainId": "string",
   "id": "string"
}
```

## Response Elements
<a name="API_PostLineageEvent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [domainId](#API_PostLineageEvent_ResponseSyntax) **   <a name="datazone-PostLineageEvent-response-domainId"></a>
The ID of the domain.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [id](#API_PostLineageEvent_ResponseSyntax) **   <a name="datazone-PostLineageEvent-response-id"></a>
The ID of the lineage event.
Type: String
Pattern: `[a-z0-9]{14}`

## Errors
<a name="API_PostLineageEvent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
There is a conflict while performing this action.
HTTP Status Code: 409

 ** InternalServerException **
The request has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource cannot be found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request has exceeded the specified service quota.
HTTP Status Code: 402

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
<a name="API_PostLineageEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/PostLineageEvent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/PostLineageEvent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/PostLineageEvent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/PostLineageEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/PostLineageEvent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/PostLineageEvent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/PostLineageEvent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/PostLineageEvent)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/PostLineageEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/PostLineageEvent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
