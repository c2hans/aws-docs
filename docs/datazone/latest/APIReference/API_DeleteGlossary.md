---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_DeleteGlossary.html
---

# DeleteGlossary
<a name="API_DeleteGlossary"></a>

Deletes a business glossary in Amazon DataZone.

Prerequisites:
+ The glossary must be in DISABLED state.
+ The glossary must not have any glossary terms associated with it.
+ The glossary must exist in the specified domain.
+ The caller must have the `datazone:DeleteGlossary` permission in the domain and glossary.
+ Glossary should not be linked to any active metadata forms.

## Request Syntax
<a name="API_DeleteGlossary_RequestSyntax"></a>

```
DELETE /v2/domains/{{domainIdentifier}}/glossaries/{{identifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteGlossary_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_DeleteGlossary_RequestSyntax) **   <a name="datazone-DeleteGlossary-request-uri-domainIdentifier"></a>
The ID of the Amazon DataZone domain in which the business glossary is deleted.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_DeleteGlossary_RequestSyntax) **   <a name="datazone-DeleteGlossary-request-uri-identifier"></a>
The ID of the business glossary that is deleted.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_DeleteGlossary_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteGlossary_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteGlossary_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteGlossary_Errors"></a>

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
<a name="API_DeleteGlossary_Examples"></a>

### Example
<a name="API_DeleteGlossary_Example_1"></a>

This example illustrates one usage of DeleteGlossary.

#### Sample Request
<a name="API_DeleteGlossary_Example_1_Request"></a>

```
aws datazone delete-glossary \
--domain-identifier "dzd_53ielnpxktdilj" \
--identifier "gls8m3nqx2wkfp"
```

### Example
<a name="API_DeleteGlossary_Example_2"></a>

Failure case - glossary must be disabled:

#### Sample Request
<a name="API_DeleteGlossary_Example_2_Request"></a>

```
aws datazone delete-glossary \
--domain-identifier "dzd_53ielnpxktdilj" \
--identifier "gls8m3nqx2wkfp"
```

#### Sample Response
<a name="API_DeleteGlossary_Example_2_Response"></a>

```
An error occurred (ValidationException) when calling the DeleteGlossary operation: Glossary must be DISABLED for deletion
```

### Example
<a name="API_DeleteGlossary_Example_3"></a>

Failure case - conflict is data is associated with it:

#### Sample Request
<a name="API_DeleteGlossary_Example_3_Request"></a>

```
aws datazone delete-glossary \
--domain-identifier "dzd_53ielnpxktdilj" \
--identifier "gls8m3nqx2wkfp"
```

#### Sample Response
<a name="API_DeleteGlossary_Example_3_Response"></a>

```
An error occurred (ConflictException) when calling the DeleteGlossary operation: Glossary can't be deleted while having glossary terms attached
```

### Example
<a name="API_DeleteGlossary_Example_4"></a>

Failure case - resource does not exist:

#### Sample Request
<a name="API_DeleteGlossary_Example_4_Request"></a>

```
aws datazone delete-glossary \
--domain-identifier "dzd_53ielnpxktdilj" \
--identifier "gls_nonexistent"
```

#### Sample Response
<a name="API_DeleteGlossary_Example_4_Response"></a>

```
An error occurred (ResourceNotFoundException) when calling the DeleteGlossary operation: Requested businessGlossary cannot be found in domain
```

### Example
<a name="API_DeleteGlossary_Example_5"></a>

Failure case - missing required parameter

#### Sample Request
<a name="API_DeleteGlossary_Example_5_Request"></a>

```
 aws datazone delete-glossary \
--domain-identifier "dzd_53ielnpxktdilj"
```

#### Sample Response
<a name="API_DeleteGlossary_Example_5_Response"></a>

```
aws: error: the following arguments are required: --identifier
```

## See Also
<a name="API_DeleteGlossary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/DeleteGlossary)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/DeleteGlossary)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/DeleteGlossary)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/DeleteGlossary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/DeleteGlossary)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/DeleteGlossary)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/DeleteGlossary)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/DeleteGlossary)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/DeleteGlossary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/DeleteGlossary)
