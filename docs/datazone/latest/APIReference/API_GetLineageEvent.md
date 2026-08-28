---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_GetLineageEvent.html
---

# GetLineageEvent
<a name="API_GetLineageEvent"></a>

Describes the lineage event.

## Request Syntax
<a name="API_GetLineageEvent_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/lineage/events/{{identifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetLineageEvent_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_GetLineageEvent_RequestSyntax) **   <a name="datazone-GetLineageEvent-request-uri-domainIdentifier"></a>
The ID of the domain.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_GetLineageEvent_RequestSyntax) **   <a name="datazone-GetLineageEvent-request-uri-identifier"></a>
The ID of the lineage event.
Pattern: `[a-z0-9]{14}`
Required: Yes

## Request Body
<a name="API_GetLineageEvent_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetLineageEvent_ResponseSyntax"></a>

```
HTTP/1.1 200
Domain-Id: {{domainId}}
Id: {{id}}
Created-By: {{createdBy}}
Processing-Status: {{processingStatus}}
Event-Time: {{eventTime}}
Created-At: {{createdAt}}

{{event}}
```

## Response Elements
<a name="API_GetLineageEvent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [createdAt](#API_GetLineageEvent_ResponseSyntax) **   <a name="datazone-GetLineageEvent-response-createdAt"></a>
The timestamp of when the lineage event was created.

 ** [createdBy](#API_GetLineageEvent_ResponseSyntax) **   <a name="datazone-GetLineageEvent-response-createdBy"></a>
The user who created the lineage event.

 ** [domainId](#API_GetLineageEvent_ResponseSyntax) **   <a name="datazone-GetLineageEvent-response-domainId"></a>
The ID of the domain.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [eventTime](#API_GetLineageEvent_ResponseSyntax) **   <a name="datazone-GetLineageEvent-response-eventTime"></a>
The time of the lineage event.

 ** [id](#API_GetLineageEvent_ResponseSyntax) **   <a name="datazone-GetLineageEvent-response-id"></a>
The ID of the lineage event.
Pattern: `[a-z0-9]{14}`

 ** [processingStatus](#API_GetLineageEvent_ResponseSyntax) **   <a name="datazone-GetLineageEvent-response-processingStatus"></a>
The progressing status of the lineage event.
Valid Values: `REQUESTED | PROCESSING | SUCCESS | FAILED`

The response returns the following as the HTTP body.

 ** [event](#API_GetLineageEvent_ResponseSyntax) **   <a name="datazone-GetLineageEvent-response-event"></a>
The lineage event details.
Length Constraints: Minimum length of 0. Maximum length of 300000.

## Errors
<a name="API_GetLineageEvent_Errors"></a>

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
<a name="API_GetLineageEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/GetLineageEvent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/GetLineageEvent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/GetLineageEvent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/GetLineageEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/GetLineageEvent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/GetLineageEvent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/GetLineageEvent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/GetLineageEvent)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/GetLineageEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/GetLineageEvent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
