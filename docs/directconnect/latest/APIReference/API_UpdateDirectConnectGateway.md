---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_UpdateDirectConnectGateway.html
---

# UpdateDirectConnectGateway
<a name="API_UpdateDirectConnectGateway"></a>

Updates the name of a current Direct Connect gateway.

## Request Syntax
<a name="API_UpdateDirectConnectGateway_RequestSyntax"></a>

```
{
   "directConnectGatewayId": "{{string}}",
   "newDirectConnectGatewayName": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateDirectConnectGateway_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [directConnectGatewayId](#API_UpdateDirectConnectGateway_RequestSyntax) **   <a name="DX-UpdateDirectConnectGateway-request-directConnectGatewayId"></a>
The ID of the Direct Connect gateway to update.
Type: String
Required: Yes

 ** [newDirectConnectGatewayName](#API_UpdateDirectConnectGateway_RequestSyntax) **   <a name="DX-UpdateDirectConnectGateway-request-newDirectConnectGatewayName"></a>
The new name for the Direct Connect gateway.
Type: String
Required: Yes

## Response Syntax
<a name="API_UpdateDirectConnectGateway_ResponseSyntax"></a>

```
{
   "directConnectGateway": {
      "amazonSideAsn": number,
      "directConnectGatewayId": "string",
      "directConnectGatewayName": "string",
      "directConnectGatewayState": "string",
      "ownerAccount": "string",
      "stateChangeError": "string",
      "tags": [
         {
            "key": "string",
            "value": "string"
         }
      ],
      "totalPrefixPoolAllocations": number
   }
}
```

## Response Elements
<a name="API_UpdateDirectConnectGateway_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [directConnectGateway](#API_UpdateDirectConnectGateway_ResponseSyntax) **   <a name="DX-UpdateDirectConnectGateway-response-directConnectGateway"></a>
Informaiton about a Direct Connect gateway, which enables you to connect virtual interfaces and virtual private gateways or transit gateways.
Type: [DirectConnectGateway](API_DirectConnectGateway.md) object

## Errors
<a name="API_UpdateDirectConnectGateway_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DirectConnectClientException **
One or more parameters are not valid.
HTTP Status Code: 400

 ** DirectConnectServerException **
A server-side error occurred.
HTTP Status Code: 400

## See Also
<a name="API_UpdateDirectConnectGateway_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/directconnect-2012-10-25/UpdateDirectConnectGateway)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/directconnect-2012-10-25/UpdateDirectConnectGateway)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/UpdateDirectConnectGateway)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/directconnect-2012-10-25/UpdateDirectConnectGateway)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/UpdateDirectConnectGateway)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/directconnect-2012-10-25/UpdateDirectConnectGateway)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/directconnect-2012-10-25/UpdateDirectConnectGateway)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/directconnect-2012-10-25/UpdateDirectConnectGateway)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/directconnect-2012-10-25/UpdateDirectConnectGateway)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/UpdateDirectConnectGateway)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Direct Connect Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query directconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
