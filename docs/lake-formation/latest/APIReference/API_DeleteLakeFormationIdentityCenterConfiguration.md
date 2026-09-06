---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_DeleteLakeFormationIdentityCenterConfiguration.html
---

# DeleteLakeFormationIdentityCenterConfiguration
<a name="API_DeleteLakeFormationIdentityCenterConfiguration"></a>

Deletes an IAM Identity Center connection with Lake Formation.

## Request Syntax
<a name="API_DeleteLakeFormationIdentityCenterConfiguration_RequestSyntax"></a>

```
POST /DeleteLakeFormationIdentityCenterConfiguration HTTP/1.1
Content-type: application/json

{
   "CatalogId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DeleteLakeFormationIdentityCenterConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteLakeFormationIdentityCenterConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CatalogId](#API_DeleteLakeFormationIdentityCenterConfiguration_RequestSyntax) **   <a name="lakeformation-DeleteLakeFormationIdentityCenterConfiguration-request-CatalogId"></a>
The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, view definition, and other control information to manage your Lake Formation environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## Response Syntax
<a name="API_DeleteLakeFormationIdentityCenterConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteLakeFormationIdentityCenterConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteLakeFormationIdentityCenterConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
 ** Message **
A message describing the problem.
HTTP Status Code: 403

 ** ConcurrentModificationException **
Two processes are trying to modify a resource simultaneously.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** EntityNotFoundException **
A specified entity does not exist.
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

## See Also
<a name="API_DeleteLakeFormationIdentityCenterConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lakeformation-2017-03-31/DeleteLakeFormationIdentityCenterConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lakeformation-2017-03-31/DeleteLakeFormationIdentityCenterConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/DeleteLakeFormationIdentityCenterConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lakeformation-2017-03-31/DeleteLakeFormationIdentityCenterConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/DeleteLakeFormationIdentityCenterConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lakeformation-2017-03-31/DeleteLakeFormationIdentityCenterConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lakeformation-2017-03-31/DeleteLakeFormationIdentityCenterConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lakeformation-2017-03-31/DeleteLakeFormationIdentityCenterConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lakeformation-2017-03-31/DeleteLakeFormationIdentityCenterConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/DeleteLakeFormationIdentityCenterConfiguration)
