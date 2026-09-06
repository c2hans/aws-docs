---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_UpdateEndpointAccess.html
---

# UpdateEndpointAccess
<a name="API_UpdateEndpointAccess"></a>

Updates an Amazon Redshift Serverless managed endpoint.

## Request Syntax
<a name="API_UpdateEndpointAccess_RequestSyntax"></a>

```
{
   "endpointName": "{{string}}",
   "vpcSecurityGroupIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_UpdateEndpointAccess_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [endpointName](#API_UpdateEndpointAccess_RequestSyntax) **   <a name="redshiftserverless-UpdateEndpointAccess-request-endpointName"></a>
The name of the VPC endpoint to update.
Type: String
Required: Yes

 ** [vpcSecurityGroupIds](#API_UpdateEndpointAccess_RequestSyntax) **   <a name="redshiftserverless-UpdateEndpointAccess-request-vpcSecurityGroupIds"></a>
The list of VPC security groups associated with the endpoint after the endpoint is modified.
Type: Array of strings
Required: No

## Response Syntax
<a name="API_UpdateEndpointAccess_ResponseSyntax"></a>

```
{
   "endpoint": {
      "address": "string",
      "endpointArn": "string",
      "endpointCreateTime": "string",
      "endpointName": "string",
      "endpointStatus": "string",
      "port": number,
      "subnetIds": [ "string" ],
      "vpcEndpoint": {
         "networkInterfaces": [
            {
               "availabilityZone": "string",
               "ipv6Address": "string",
               "networkInterfaceId": "string",
               "privateIpAddress": "string",
               "subnetId": "string"
            }
         ],
         "vpcEndpointId": "string",
         "vpcId": "string"
      },
      "vpcSecurityGroups": [
         {
            "status": "string",
            "vpcSecurityGroupId": "string"
         }
      ],
      "workgroupName": "string"
   }
}
```

## Response Elements
<a name="API_UpdateEndpointAccess_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [endpoint](#API_UpdateEndpointAccess_ResponseSyntax) **   <a name="redshiftserverless-UpdateEndpointAccess-response-endpoint"></a>
The updated VPC endpoint.
Type: [EndpointAccess](API_EndpointAccess.md) object

## Errors
<a name="API_UpdateEndpointAccess_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 400

 ** ConflictException **
The submitted action has conflicts.
HTTP Status Code: 400

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource could not be found.
 ** resourceName **
The name of the resource that could not be found.
HTTP Status Code: 400

 ** ValidationException **
The input failed to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_UpdateEndpointAccess_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-serverless-2021-04-21/UpdateEndpointAccess)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-serverless-2021-04-21/UpdateEndpointAccess)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/UpdateEndpointAccess)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-serverless-2021-04-21/UpdateEndpointAccess)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/UpdateEndpointAccess)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-serverless-2021-04-21/UpdateEndpointAccess)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-serverless-2021-04-21/UpdateEndpointAccess)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-serverless-2021-04-21/UpdateEndpointAccess)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-serverless-2021-04-21/UpdateEndpointAccess)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/UpdateEndpointAccess)
