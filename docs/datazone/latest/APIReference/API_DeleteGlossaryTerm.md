---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_DeleteGlossaryTerm.html
---

# DeleteGlossaryTerm
<a name="API_DeleteGlossaryTerm"></a>

Deletes a business glossary term in Amazon DataZone.

Prerequisites:
+ Glossary term must exist and be active.
+ The term must not be linked to other assets or child terms.
+ Caller must have delete permissions in the domain/glossary.
+ Ensure all associations (such as to assets or parent terms) are removed before deletion.

## Request Syntax
<a name="API_DeleteGlossaryTerm_RequestSyntax"></a>

```
DELETE /v2/domains/{{domainIdentifier}}/glossary-terms/{{identifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteGlossaryTerm_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_DeleteGlossaryTerm_RequestSyntax) **   <a name="datazone-DeleteGlossaryTerm-request-uri-domainIdentifier"></a>
The ID of the Amazon DataZone domain in which the business glossary term is deleted.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_DeleteGlossaryTerm_RequestSyntax) **   <a name="datazone-DeleteGlossaryTerm-request-uri-identifier"></a>
The ID of the business glossary term that is deleted.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_DeleteGlossaryTerm_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteGlossaryTerm_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteGlossaryTerm_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteGlossaryTerm_Errors"></a>

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

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** UnauthorizedException **
You do not have permission to perform this action.
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by the AWS service.
HTTP Status Code: 400

## Examples
<a name="API_DeleteGlossaryTerm_Examples"></a>

### Example
<a name="API_DeleteGlossaryTerm_Example_1"></a>

This example illustrates one usage of DeleteGlossaryTerm.

#### Sample Request
<a name="API_DeleteGlossaryTerm_Example_1_Request"></a>

```
aws datazone delete-glossary-term \
--domain-identifier "dzd_53ielnpxktdilj" \
--identifier "trm9k4pq7xwnmh"
```

### Example
<a name="API_DeleteGlossaryTerm_Example_2"></a>

Failure case - resource does not exist:

#### Sample Request
<a name="API_DeleteGlossaryTerm_Example_2_Request"></a>

```
aws datazone delete-glossary-term \
--domain-identifier "dzd_53ielnpxktdilj" \
--identifier "trm_nonexistent"
```

#### Sample Response
<a name="API_DeleteGlossaryTerm_Example_2_Response"></a>

```
An error occurred (ResourceNotFoundException) when calling the DeleteGlossaryTerm operation: Requested glossaryTerm cannot be found in domain
```

### Example
<a name="API_DeleteGlossaryTerm_Example_3"></a>

Failure case - missing parameter:

#### Sample Request
<a name="API_DeleteGlossaryTerm_Example_3_Request"></a>

```
aws datazone delete-glossary-term \
--domain-identifier "dzd_53ielnpxktdilj"
```

#### Sample Response
<a name="API_DeleteGlossaryTerm_Example_3_Response"></a>

```
aws: error: the following arguments are required: --identifier
```

## See Also
<a name="API_DeleteGlossaryTerm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/DeleteGlossaryTerm)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/DeleteGlossaryTerm)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/DeleteGlossaryTerm)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/DeleteGlossaryTerm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/DeleteGlossaryTerm)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/DeleteGlossaryTerm)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/DeleteGlossaryTerm)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/DeleteGlossaryTerm)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/DeleteGlossaryTerm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/DeleteGlossaryTerm)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
