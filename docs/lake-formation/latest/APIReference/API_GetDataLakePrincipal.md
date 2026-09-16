---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_GetDataLakePrincipal.html
---

# GetDataLakePrincipal
<a name="API_GetDataLakePrincipal"></a>

Returns the identity of the invoking principal.

## Request Syntax
<a name="API_GetDataLakePrincipal_RequestSyntax"></a>

```
POST /GetDataLakePrincipal HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDataLakePrincipal_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetDataLakePrincipal_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDataLakePrincipal_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Identity": "string"
}
```

## Response Elements
<a name="API_GetDataLakePrincipal_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Identity](#API_GetDataLakePrincipal_ResponseSyntax) **   <a name="lakeformation-GetDataLakePrincipal-response-Identity"></a>
A unique identifier of the invoking principal.
Type: String

## Errors
<a name="API_GetDataLakePrincipal_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
 ** Message **
A message describing the problem.
HTTP Status Code: 403

 ** InternalServiceException **
An internal service error occurred.
 ** Message **
A message describing the problem.
HTTP Status Code: 500

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## Examples
<a name="API_GetDataLakePrincipal_Examples"></a>

### Response example
<a name="API_GetDataLakePrincipal_Example_1"></a>

This example illustrates one usage of GetDataLakePrincipal.

```
{
   "Identity": "arn:aws:iam::<111221110200>:role/user "

}
```

## See Also
<a name="API_GetDataLakePrincipal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lakeformation-2017-03-31/GetDataLakePrincipal)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lakeformation-2017-03-31/GetDataLakePrincipal)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/GetDataLakePrincipal)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lakeformation-2017-03-31/GetDataLakePrincipal)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/GetDataLakePrincipal)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lakeformation-2017-03-31/GetDataLakePrincipal)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lakeformation-2017-03-31/GetDataLakePrincipal)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lakeformation-2017-03-31/GetDataLakePrincipal)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lakeformation-2017-03-31/GetDataLakePrincipal)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/GetDataLakePrincipal)
