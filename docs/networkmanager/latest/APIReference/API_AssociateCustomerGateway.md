---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_AssociateCustomerGateway.html
---

# AssociateCustomerGateway
<a name="API_AssociateCustomerGateway"></a>

Associates a customer gateway with a device and optionally, with a link. If you specify a link, it must be associated with the specified device.

You can only associate customer gateways that are connected to a VPN attachment on a transit gateway or core network registered in your global network. When you register a transit gateway or core network, customer gateways that are connected to the transit gateway are automatically included in the global network. To list customer gateways that are connected to a transit gateway, use the [DescribeVpnConnections](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpnConnections.html) EC2 API and filter by `transit-gateway-id`.

You cannot associate a customer gateway with more than one device and link.

## Request Syntax
<a name="API_AssociateCustomerGateway_RequestSyntax"></a>

```
POST /global-networks/{{globalNetworkId}}/customer-gateway-associations HTTP/1.1
Content-type: application/json

{
   "CustomerGatewayArn": "{{string}}",
   "DeviceId": "{{string}}",
   "LinkId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_AssociateCustomerGateway_RequestParameters"></a>

The request uses the following URI parameters.

 ** [globalNetworkId](#API_AssociateCustomerGateway_RequestSyntax) **   <a name="networkmanager-AssociateCustomerGateway-request-uri-GlobalNetworkId"></a>
The ID of the global network.
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[\s\S]*`
Required: Yes

## Request Body
<a name="API_AssociateCustomerGateway_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CustomerGatewayArn](#API_AssociateCustomerGateway_RequestSyntax) **   <a name="networkmanager-AssociateCustomerGateway-request-CustomerGatewayArn"></a>
The Amazon Resource Name (ARN) of the customer gateway.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `[\s\S]*`
Required: Yes

 ** [DeviceId](#API_AssociateCustomerGateway_RequestSyntax) **   <a name="networkmanager-AssociateCustomerGateway-request-DeviceId"></a>
The ID of the device.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[\s\S]*`
Required: Yes

 ** [LinkId](#API_AssociateCustomerGateway_RequestSyntax) **   <a name="networkmanager-AssociateCustomerGateway-request-LinkId"></a>
The ID of the link.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[\s\S]*`
Required: No

## Response Syntax
<a name="API_AssociateCustomerGateway_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CustomerGatewayAssociation": {
      "CustomerGatewayArn": "string",
      "DeviceId": "string",
      "GlobalNetworkId": "string",
      "LinkId": "string",
      "State": "string"
   }
}
```

## Response Elements
<a name="API_AssociateCustomerGateway_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CustomerGatewayAssociation](#API_AssociateCustomerGateway_ResponseSyntax) **   <a name="networkmanager-AssociateCustomerGateway-response-CustomerGatewayAssociation"></a>
The customer gateway association.
Type: [CustomerGatewayAssociation](API_CustomerGatewayAssociation.md) object

## Errors
<a name="API_AssociateCustomerGateway_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
There was a conflict processing the request. Updating or deleting the resource can cause an inconsistent state.
 ** ResourceId **
The ID of the resource.
 ** ResourceType **
The resource type.
HTTP Status Code: 409

 ** InternalServerException **
The request has failed due to an internal error.
 ** RetryAfterSeconds **
Indicates when to retry the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource could not be found.
 ** Context **
The specified resource could not be found.
 ** ResourceId **
The ID of the resource.
 ** ResourceType **
The resource type.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
A service limit was exceeded.
 ** LimitCode **
The limit code.
 ** Message **
The error message.
 ** ResourceId **
The ID of the resource.
 ** ResourceType **
The resource type.
 ** ServiceCode **
The service code.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
 ** RetryAfterSeconds **
Indicates when to retry the request.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints.
 ** Fields **
The fields that caused the error, if applicable.
 ** Reason **
The reason for the error.
HTTP Status Code: 400

## See Also
<a name="API_AssociateCustomerGateway_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/AssociateCustomerGateway)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/networkmanager-2019-07-05/AssociateCustomerGateway)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/AssociateCustomerGateway)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/AssociateCustomerGateway)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/AssociateCustomerGateway)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/AssociateCustomerGateway)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/AssociateCustomerGateway)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/AssociateCustomerGateway)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/AssociateCustomerGateway)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/AssociateCustomerGateway)
