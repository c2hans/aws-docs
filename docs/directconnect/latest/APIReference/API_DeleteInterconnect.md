---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DeleteInterconnect.html
---

# DeleteInterconnect
<a name="API_DeleteInterconnect"></a>

Deletes the specified interconnect.

**Note**
Intended for use by Direct Connect Partners only.

## Request Syntax
<a name="API_DeleteInterconnect_RequestSyntax"></a>

```
{
   "interconnectId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteInterconnect_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [interconnectId](#API_DeleteInterconnect_RequestSyntax) **   <a name="DX-DeleteInterconnect-request-interconnectId"></a>
The ID of the interconnect.
Type: String
Required: Yes

## Response Syntax
<a name="API_DeleteInterconnect_ResponseSyntax"></a>

```
{
   "interconnectState": "string"
}
```

## Response Elements
<a name="API_DeleteInterconnect_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [interconnectState](#API_DeleteInterconnect_ResponseSyntax) **   <a name="DX-DeleteInterconnect-response-interconnectState"></a>
The state of the interconnect. The following are the possible values:
+  `requested`: The initial state of an interconnect. The interconnect stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.
+  `pending`: The interconnect is approved, and is being initialized.
+  `available`: The network link is up, and the interconnect is ready for use.
+  `down`: The network link is down.
+  `deleting`: The interconnect is being deleted.
+  `deleted`: The interconnect is deleted.
+  `unknown`: The state of the interconnect is not available.
Type: String
Valid Values: `requested | pending | available | down | deleting | deleted | unknown`

## Errors
<a name="API_DeleteInterconnect_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DirectConnectClientException **
One or more parameters are not valid.
HTTP Status Code: 400

 ** DirectConnectServerException **
A server-side error occurred.
HTTP Status Code: 400

## See Also
<a name="API_DeleteInterconnect_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/directconnect-2012-10-25/DeleteInterconnect)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/directconnect-2012-10-25/DeleteInterconnect)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/DeleteInterconnect)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/directconnect-2012-10-25/DeleteInterconnect)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/DeleteInterconnect)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/directconnect-2012-10-25/DeleteInterconnect)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/directconnect-2012-10-25/DeleteInterconnect)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/directconnect-2012-10-25/DeleteInterconnect)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/directconnect-2012-10-25/DeleteInterconnect)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/DeleteInterconnect)
