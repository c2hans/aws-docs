---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_DeleteLineageEvent.html
---

# DeleteLineageEvent
<a name="API_DeleteLineageEvent"></a>

Deletes the specified lineage event.

## Request Syntax
<a name="API_DeleteLineageEvent_RequestSyntax"></a>

```
DELETE /v2/domains/{{domainIdentifier}}/lineage/events/{{identifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteLineageEvent_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_DeleteLineageEvent_RequestSyntax) **   <a name="datazone-DeleteLineageEvent-request-uri-domainIdentifier"></a>
The ID of the domain.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_DeleteLineageEvent_RequestSyntax) **   <a name="datazone-DeleteLineageEvent-request-uri-identifier"></a>
The ID of the lineage event.
Pattern: `[a-z0-9]{14}`
Required: Yes

## Request Body
<a name="API_DeleteLineageEvent_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteLineageEvent_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "domainId": "string",
   "id": "string",
   "processingStatus": "string"
}
```

## Response Elements
<a name="API_DeleteLineageEvent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [domainId](#API_DeleteLineageEvent_ResponseSyntax) **   <a name="datazone-DeleteLineageEvent-response-domainId"></a>
The ID of the domain.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

 ** [id](#API_DeleteLineageEvent_ResponseSyntax) **   <a name="datazone-DeleteLineageEvent-response-id"></a>
The ID of the lineage event.
Type: String
Pattern: `[a-z0-9]{14}`

 ** [processingStatus](#API_DeleteLineageEvent_ResponseSyntax) **   <a name="datazone-DeleteLineageEvent-response-processingStatus"></a>
The progressing status of the lineage event.
Type: String
Valid Values: `REQUESTED | PROCESSING | SUCCESS | FAILED`

## Errors
<a name="API_DeleteLineageEvent_Errors"></a>

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
<a name="API_DeleteLineageEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/DeleteLineageEvent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/DeleteLineageEvent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/DeleteLineageEvent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/DeleteLineageEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/DeleteLineageEvent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/DeleteLineageEvent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/DeleteLineageEvent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/DeleteLineageEvent)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/DeleteLineageEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/DeleteLineageEvent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
