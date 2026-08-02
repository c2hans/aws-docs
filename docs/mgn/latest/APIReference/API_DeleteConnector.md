---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_DeleteConnector.html
---

# DeleteConnector
<a name="API_DeleteConnector"></a>

Delete Connector.

## Request Syntax
<a name="API_DeleteConnector_RequestSyntax"></a>

```
POST /DeleteConnector HTTP/1.1
Content-type: application/json

{
   "connectorID": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DeleteConnector_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteConnector_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [connectorID](#API_DeleteConnector_RequestSyntax) **   <a name="mgn-DeleteConnector-request-connectorID"></a>
Delete Connector request connector ID.
Type: String
Length Constraints: Fixed length of 27.
Pattern: `connector-[0-9a-zA-Z]{17}`
Required: Yes

## Response Syntax
<a name="API_DeleteConnector_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteConnector_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteConnector_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
Resource not found exception.
 ** resourceId **
Resource ID not found error.
 ** resourceType **
Resource type not found error.
HTTP Status Code: 404

 ** UninitializedAccountException **
Uninitialized account exception.
HTTP Status Code: 400

 ** ValidationException **
Validate exception.
 ** fieldList **
Validate exception field list.
 ** reason **
Validate exception reason.
HTTP Status Code: 400

## See Also
<a name="API_DeleteConnector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mgn-2020-02-26/DeleteConnector)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mgn-2020-02-26/DeleteConnector)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/DeleteConnector)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mgn-2020-02-26/DeleteConnector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/DeleteConnector)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mgn-2020-02-26/DeleteConnector)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mgn-2020-02-26/DeleteConnector)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mgn-2020-02-26/DeleteConnector)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mgn-2020-02-26/DeleteConnector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/DeleteConnector)
