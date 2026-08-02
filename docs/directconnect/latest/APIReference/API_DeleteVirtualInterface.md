---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DeleteVirtualInterface.html
---

# DeleteVirtualInterface
<a name="API_DeleteVirtualInterface"></a>

Deletes a virtual interface.

## Request Syntax
<a name="API_DeleteVirtualInterface_RequestSyntax"></a>

```
{
   "virtualInterfaceId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteVirtualInterface_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [virtualInterfaceId](#API_DeleteVirtualInterface_RequestSyntax) **   <a name="DX-DeleteVirtualInterface-request-virtualInterfaceId"></a>
The ID of the virtual interface.
Type: String
Required: Yes

## Response Syntax
<a name="API_DeleteVirtualInterface_ResponseSyntax"></a>

```
{
   "virtualInterfaceState": "string"
}
```

## Response Elements
<a name="API_DeleteVirtualInterface_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [virtualInterfaceState](#API_DeleteVirtualInterface_ResponseSyntax) **   <a name="DX-DeleteVirtualInterface-response-virtualInterfaceState"></a>
The state of the virtual interface. The following are the possible values:
+  `confirming`: The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner.
+  `verifying`: This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created.
+  `pending`: A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic.
+  `available`: A virtual interface that is able to forward traffic.
+  `down`: A virtual interface that is BGP down.
+  `testing`: A virtual interface is in this state immediately after calling [StartBgpFailoverTest](API_StartBgpFailoverTest.md) and remains in this state during the duration of the test.
+  `deleting`: A virtual interface is in this state immediately after calling [DeleteVirtualInterface](#API_DeleteVirtualInterface) until it can no longer forward traffic.
+  `deleted`: A virtual interface that cannot forward traffic.
+  `rejected`: The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the `Confirming` state is deleted by the virtual interface owner, the virtual interface enters the `Rejected` state.
+  `unknown`: The state of the virtual interface is not available.
Type: String
Valid Values: `confirming | verifying | pending | available | down | testing | deleting | deleted | rejected | unknown`

## Errors
<a name="API_DeleteVirtualInterface_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DirectConnectClientException **
One or more parameters are not valid.
HTTP Status Code: 400

 ** DirectConnectServerException **
A server-side error occurred.
HTTP Status Code: 400

## See Also
<a name="API_DeleteVirtualInterface_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/directconnect-2012-10-25/DeleteVirtualInterface)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/directconnect-2012-10-25/DeleteVirtualInterface)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/DeleteVirtualInterface)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/directconnect-2012-10-25/DeleteVirtualInterface)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/DeleteVirtualInterface)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/directconnect-2012-10-25/DeleteVirtualInterface)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/directconnect-2012-10-25/DeleteVirtualInterface)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/directconnect-2012-10-25/DeleteVirtualInterface)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/directconnect-2012-10-25/DeleteVirtualInterface)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/DeleteVirtualInterface)
