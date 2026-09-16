---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_CreateEndpointAccess.html
---

# CreateEndpointAccess
<a name="API_CreateEndpointAccess"></a>

Creates an Amazon Redshift Serverless managed VPC endpoint.

## Request Syntax
<a name="API_CreateEndpointAccess_RequestSyntax"></a>

```
{
   "endpointName": "{{string}}",
   "ownerAccount": "{{string}}",
   "subnetIds": [ "{{string}}" ],
   "vpcSecurityGroupIds": [ "{{string}}" ],
   "workgroupName": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateEndpointAccess_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [endpointName](#API_CreateEndpointAccess_RequestSyntax) **   <a name="redshiftserverless-CreateEndpointAccess-request-endpointName"></a>
The name of the VPC endpoint. An endpoint name must contain 1-30 characters. Valid characters are A-Z, a-z, 0-9, and hyphen(-). The first character must be a letter. The name can't contain two consecutive hyphens or end with a hyphen.
Type: String
Required: Yes

 ** [ownerAccount](#API_CreateEndpointAccess_RequestSyntax) **   <a name="redshiftserverless-CreateEndpointAccess-request-ownerAccount"></a>
The owner AWS account for the Amazon Redshift Serverless workgroup.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 12.
Pattern: `.*(\d{12}).*`
Required: No

 ** [subnetIds](#API_CreateEndpointAccess_RequestSyntax) **   <a name="redshiftserverless-CreateEndpointAccess-request-subnetIds"></a>
The unique identifers of subnets from which Amazon Redshift Serverless chooses one to deploy a VPC endpoint.
Type: Array of strings
Required: Yes

 ** [vpcSecurityGroupIds](#API_CreateEndpointAccess_RequestSyntax) **   <a name="redshiftserverless-CreateEndpointAccess-request-vpcSecurityGroupIds"></a>
The unique identifiers of the security group that defines the ports, protocols, and sources for inbound traffic that you are authorizing into your endpoint.
Type: Array of strings
Required: No

 ** [workgroupName](#API_CreateEndpointAccess_RequestSyntax) **   <a name="redshiftserverless-CreateEndpointAccess-request-workgroupName"></a>
The name of the workgroup to associate with the VPC endpoint.
Type: String
Required: Yes

## Response Syntax
<a name="API_CreateEndpointAccess_ResponseSyntax"></a>

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
<a name="API_CreateEndpointAccess_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [endpoint](#API_CreateEndpointAccess_ResponseSyntax) **   <a name="redshiftserverless-CreateEndpointAccess-response-endpoint"></a>
The created VPC endpoint.
Type: [EndpointAccess](API_EndpointAccess.md) object

## Errors
<a name="API_CreateEndpointAccess_Errors"></a>

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

 ** ServiceQuotaExceededException **
The service limit was exceeded.
HTTP Status Code: 400

 ** ValidationException **
The input failed to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_CreateEndpointAccess_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-serverless-2021-04-21/CreateEndpointAccess)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-serverless-2021-04-21/CreateEndpointAccess)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/CreateEndpointAccess)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-serverless-2021-04-21/CreateEndpointAccess)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/CreateEndpointAccess)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-serverless-2021-04-21/CreateEndpointAccess)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-serverless-2021-04-21/CreateEndpointAccess)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-serverless-2021-04-21/CreateEndpointAccess)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/redshift-serverless-2021-04-21/CreateEndpointAccess)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/CreateEndpointAccess)
