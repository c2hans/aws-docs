---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_PutFormType.html
---

# PutFormType
<a name="API_PutFormType"></a>

Creates or updates a form type in AWS Glue Data Catalog. A form type defines the schema for structured metadata that can be attached to assets.

## Request Syntax
<a name="API_PutFormType_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "Name": "{{string}}",
   "Schema": "{{string}}"
}
```

## Request Parameters
<a name="API_PutFormType_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientToken](#API_PutFormType_RequestSyntax) **   <a name="Glue-PutFormType-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [Name](#API_PutFormType_RequestSyntax) **   <a name="Glue-PutFormType-request-Name"></a>
The name of the form type. Must start with an uppercase letter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[A-Z]\w*$`
Required: Yes

 ** [Schema](#API_PutFormType_RequestSyntax) **   <a name="Glue-PutFormType-request-Schema"></a>
The Smithy IDL schema definition for the form type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100000.
Required: Yes

## Response Syntax
<a name="API_PutFormType_ResponseSyntax"></a>

```
{
   "Id": "string",
   "Name": "string",
   "Schema": "string"
}
```

## Response Elements
<a name="API_PutFormType_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Id](#API_PutFormType_ResponseSyntax) **   <a name="Glue-PutFormType-response-Id"></a>
The identifier of the form type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [Name](#API_PutFormType_ResponseSyntax) **   <a name="Glue-PutFormType-response-Name"></a>
The name of the form type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[A-Z]\w*$`

 ** [Schema](#API_PutFormType_ResponseSyntax) **   <a name="Glue-PutFormType-response-Schema"></a>
The Smithy IDL schema of the form type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100000.

## Errors
<a name="API_PutFormType_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** ConcurrentModificationException **
Two processes are trying to modify a resource simultaneously.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** InternalServiceException **
An internal service error occurred.
 ** Message **
A message describing the problem.
HTTP Status Code: 500

 ** InvalidInputException **
The input provided was not valid.
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** ThrottlingException **
The throttling threshhold was exceeded.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## Examples
<a name="API_PutFormType_Examples"></a>

### Example
<a name="API_PutFormType_Example_1"></a>

The following example creates a form type with a Smithy schema.

```
aws glue put-form-type \
    --name DataClassification \
    --schema 'structure DataClassification {
    classification: String
    owner: String
}'

{
    "Id": "DataClassification",
    "Name": "DataClassification",
    "Schema": "structure DataClassification {\n    classification: String\n    owner: String\n}"
}
```

## See Also
<a name="API_PutFormType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/PutFormType)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/PutFormType)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/PutFormType)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/PutFormType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/PutFormType)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/PutFormType)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/PutFormType)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/PutFormType)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/PutFormType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/PutFormType)
