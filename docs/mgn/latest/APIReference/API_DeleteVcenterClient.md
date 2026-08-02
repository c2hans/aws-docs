---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_DeleteVcenterClient.html
---

# DeleteVcenterClient
<a name="API_DeleteVcenterClient"></a>

Deletes a given vCenter client by ID.

## Request Syntax
<a name="API_DeleteVcenterClient_RequestSyntax"></a>

```
POST /DeleteVcenterClient HTTP/1.1
Content-type: application/json

{
   "vcenterClientID": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DeleteVcenterClient_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteVcenterClient_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [vcenterClientID](#API_DeleteVcenterClient_RequestSyntax) **   <a name="mgn-DeleteVcenterClient-request-vcenterClientID"></a>
ID of resource to be deleted.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `vcc-[0-9a-zA-Z]{17}`
Required: Yes

## Response Syntax
<a name="API_DeleteVcenterClient_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteVcenterClient_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteVcenterClient_Errors"></a>

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
<a name="API_DeleteVcenterClient_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mgn-2020-02-26/DeleteVcenterClient)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mgn-2020-02-26/DeleteVcenterClient)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/DeleteVcenterClient)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mgn-2020-02-26/DeleteVcenterClient)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/DeleteVcenterClient)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mgn-2020-02-26/DeleteVcenterClient)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mgn-2020-02-26/DeleteVcenterClient)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mgn-2020-02-26/DeleteVcenterClient)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mgn-2020-02-26/DeleteVcenterClient)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/DeleteVcenterClient)
