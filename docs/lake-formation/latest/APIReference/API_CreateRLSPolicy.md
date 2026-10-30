---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_CreateRLSPolicy.html
---

# CreateRLSPolicy
<a name="API_CreateRLSPolicy"></a>

Creates a row-level security (RLS) policy. A row-level security policy defines a filter expression that AWS Lake Formation evaluates to determine which rows of a table a principal is allowed to see. The policy is created independently of any resource, and is later associated with a resource and principal using `AttachRLSPolicy`.

## Request Syntax
<a name="API_CreateRLSPolicy_RequestSyntax"></a>

```
POST /CreateRLSPolicy HTTP/1.1
Content-type: application/json

{
   "AttachmentColumns": [
      {
         "Name": "{{string}}",
         "Type": "{{string}}"
      }
   ],
   "FilterExpression": "{{string}}",
   "Name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateRLSPolicy_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateRLSPolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AttachmentColumns](#API_CreateRLSPolicy_RequestSyntax) **   <a name="lakeformation-CreateRLSPolicy-request-AttachmentColumns"></a>
The list of columns that the filter expression references. These columns define the shape of the data that the policy can be attached to.
Type: Array of [Column](API_Column.md) objects
Required: Yes

 ** [FilterExpression](#API_CreateRLSPolicy_RequestSyntax) **   <a name="lakeformation-CreateRLSPolicy-request-FilterExpression"></a>
A filter predicate, written in a SQL-like syntax, that AWS Lake Formation evaluates against each row. Only the rows for which the expression evaluates to true are returned to the principal.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** [Name](#API_CreateRLSPolicy_RequestSyntax) **   <a name="lakeformation-CreateRLSPolicy-request-Name"></a>
A unique name for the row-level security policy within the Data Catalog.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_CreateRLSPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_CreateRLSPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_CreateRLSPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
 ** Message **
A message describing the problem.
HTTP Status Code: 403

 ** AlreadyExistsException **
A resource to be created or added already exists.
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
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** ResourceNumberLimitExceededException **
A resource numerical limit was exceeded.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## Examples
<a name="API_CreateRLSPolicy_Examples"></a>

### Request example
<a name="API_CreateRLSPolicy_Example_1"></a>

This example illustrates one usage of CreateRLSPolicy.

```
{
   "Name": "sales-east-region",
   "AttachmentColumns": [
      { "Name": "region", "Type": "string" }
   ],
   "FilterExpression": "region = 'east'"
}
```

## See Also
<a name="API_CreateRLSPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lakeformation-2017-03-31/CreateRLSPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lakeformation-2017-03-31/CreateRLSPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/CreateRLSPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lakeformation-2017-03-31/CreateRLSPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/CreateRLSPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lakeformation-2017-03-31/CreateRLSPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lakeformation-2017-03-31/CreateRLSPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lakeformation-2017-03-31/CreateRLSPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lakeformation-2017-03-31/CreateRLSPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/CreateRLSPolicy)
