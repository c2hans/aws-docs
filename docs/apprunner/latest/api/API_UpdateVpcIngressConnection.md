---
source_url: https://docs.aws.amazon.com/apprunner/latest/api/API_UpdateVpcIngressConnection.html
---

# UpdateVpcIngressConnection
<a name="API_UpdateVpcIngressConnection"></a>

**Important**
 AWS App Runner will no longer be open to new customers starting March 31, 2026. If you would like to use App Runner, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html).

Update an existing App Runner VPC Ingress Connection resource. The VPC Ingress Connection must be in one of the following states to be updated:
+  AVAILABLE
+  FAILED\_CREATION
+  FAILED\_UPDATE

## Request Syntax
<a name="API_UpdateVpcIngressConnection_RequestSyntax"></a>

```
{
   "IngressVpcConfiguration": {
      "VpcEndpointId": "{{string}}",
      "VpcId": "{{string}}"
   },
   "VpcIngressConnectionArn": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateVpcIngressConnection_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [IngressVpcConfiguration](#API_UpdateVpcIngressConnection_RequestSyntax) **   <a name="apprunner-UpdateVpcIngressConnection-request-IngressVpcConfiguration"></a>
Specifications for the customer’s Amazon VPC and the related AWS PrivateLink VPC endpoint that are used to update the VPC Ingress Connection resource.
Type: [IngressVpcConfiguration](API_IngressVpcConfiguration.md) object
Required: Yes

 ** [VpcIngressConnectionArn](#API_UpdateVpcIngressConnection_RequestSyntax) **   <a name="apprunner-UpdateVpcIngressConnection-request-VpcIngressConnectionArn"></a>
The Amazon Resource Name (Arn) for the App Runner VPC Ingress Connection resource that you want to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[\w]+)*:[a-z0-9-\\.]{0,63}:[a-z0-9-\\.]{0,63}:[0-9]{12}:(\w|\/|-){1,1011}`
Required: Yes

## Response Syntax
<a name="API_UpdateVpcIngressConnection_ResponseSyntax"></a>

```
{
   "VpcIngressConnection": {
      "AccountId": "string",
      "CreatedAt": number,
      "DeletedAt": number,
      "DomainName": "string",
      "IngressVpcConfiguration": {
         "VpcEndpointId": "string",
         "VpcId": "string"
      },
      "ServiceArn": "string",
      "Status": "string",
      "VpcIngressConnectionArn": "string",
      "VpcIngressConnectionName": "string"
   }
}
```

## Response Elements
<a name="API_UpdateVpcIngressConnection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [VpcIngressConnection](#API_UpdateVpcIngressConnection_ResponseSyntax) **   <a name="apprunner-UpdateVpcIngressConnection-response-VpcIngressConnection"></a>
A description of the AWS App Runner VPC Ingress Connection resource that's updated by this request.
Type: [VpcIngressConnection](API_VpcIngressConnection.md) object

## Errors
<a name="API_UpdateVpcIngressConnection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceErrorException **
An unexpected service exception occurred.
HTTP Status Code: 500

 ** InvalidRequestException **
One or more input parameters aren't valid. Refer to the API action's document page, correct the input parameters, and try the action again.
HTTP Status Code: 400

 ** InvalidStateException **
You can't perform this action when the resource is in its current state.
HTTP Status Code: 400

 ** ResourceNotFoundException **
A resource doesn't exist for the specified Amazon Resource Name (ARN) in your AWS account.
HTTP Status Code: 400

## Examples
<a name="API_UpdateVpcIngressConnection_Examples"></a>

### Updating App Runner VPC Ingress Connections
<a name="API_UpdateVpcIngressConnection_Example_1"></a>

 This example illustrates how to update App Runner VPC Ingress Connections.

#### Sample Request
<a name="API_UpdateVpcIngressConnection_Example_1_Request"></a>

```
$ aws apprunner update-vpc-ingress-connection --cli-input-json "`cat`"
{
    "IngressVpcConfiguration": {
        "VpcEndpointId": "vpce-1a2b3c4d",
        "VpcId": "vpc-4a5b6c7d"
    },
    "VpcIngressConnectionArn": "arn:aws:apprunner:us-east-1:123456789012:vpcingressconnection/my-ingress-connection-name/3f2eb10e2c494674952026f646844e3d"
}
```

#### Sample Response
<a name="API_UpdateVpcIngressConnection_Example_1_Response"></a>

```
{
    "VpcIngressConnection": {
        "AccountId": "123456789012",
        "CreatedAt": "2022-09-18T23:36:45.374Z",
        "DomainName": "psbqam834h.us-east-1.awsapprunner.com",
        "IngressVpcConfiguration": {
            "VpcEndpointId": "vpce-1a2b3c4d",
            "VpcId": "vpc-4a5b6c7d"
        },
        "ServiceArn": "arn:aws:apprunner:us-east-1:123456789012:service/my-service",
        "Status": "PENDING_UPDATE",
        "VpcIngressConnectionArn": "arn:aws:apprunner:us-east-1:123456789012:vpcingressconnection/my-ingress-connection-name/3f2eb10e2c494674952026f646844e3d",
        "VpcIngressConnectionName": "my-ingress-connection-name"
    }
}
```

## See Also
<a name="API_UpdateVpcIngressConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apprunner-2020-05-15/UpdateVpcIngressConnection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apprunner-2020-05-15/UpdateVpcIngressConnection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apprunner-2020-05-15/UpdateVpcIngressConnection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apprunner-2020-05-15/UpdateVpcIngressConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apprunner-2020-05-15/UpdateVpcIngressConnection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apprunner-2020-05-15/UpdateVpcIngressConnection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apprunner-2020-05-15/UpdateVpcIngressConnection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apprunner-2020-05-15/UpdateVpcIngressConnection)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/apprunner-2020-05-15/UpdateVpcIngressConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apprunner-2020-05-15/UpdateVpcIngressConnection)
