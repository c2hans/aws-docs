---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_EndpointAccess.html
---

# EndpointAccess
<a name="API_EndpointAccess"></a>

Information about an Amazon Redshift Serverless VPC endpoint.

## Contents
<a name="API_EndpointAccess_Contents"></a>

 ** address **   <a name="redshiftserverless-Type-EndpointAccess-address"></a>
The DNS address of the endpoint.
Type: String
Required: No

 ** endpointArn **   <a name="redshiftserverless-Type-EndpointAccess-endpointArn"></a>
The Amazon Resource Name (ARN) of the VPC endpoint.
Type: String
Required: No

 ** endpointCreateTime **   <a name="redshiftserverless-Type-EndpointAccess-endpointCreateTime"></a>
The time that the endpoint was created.
Type: Timestamp
Required: No

 ** endpointName **   <a name="redshiftserverless-Type-EndpointAccess-endpointName"></a>
The name of the VPC endpoint.
Type: String
Required: No

 ** endpointStatus **   <a name="redshiftserverless-Type-EndpointAccess-endpointStatus"></a>
The status of the VPC endpoint.
Type: String
Required: No

 ** port **   <a name="redshiftserverless-Type-EndpointAccess-port"></a>
The port number on which Amazon Redshift Serverless accepts incoming connections.
Type: Integer
Required: No

 ** subnetIds **   <a name="redshiftserverless-Type-EndpointAccess-subnetIds"></a>
The unique identifier of subnets where Amazon Redshift Serverless choose to deploy the VPC endpoint.
Type: Array of strings
Required: No

 ** vpcEndpoint **   <a name="redshiftserverless-Type-EndpointAccess-vpcEndpoint"></a>
The connection endpoint for connecting to Amazon Redshift Serverless.
Type: [VpcEndpoint](API_VpcEndpoint.md) object
Required: No

 ** vpcSecurityGroups **   <a name="redshiftserverless-Type-EndpointAccess-vpcSecurityGroups"></a>
The security groups associated with the endpoint.
Type: Array of [VpcSecurityGroupMembership](API_VpcSecurityGroupMembership.md) objects
Required: No

 ** workgroupName **   <a name="redshiftserverless-Type-EndpointAccess-workgroupName"></a>
The name of the workgroup associated with the endpoint.
Type: String
Required: No

## See Also
<a name="API_EndpointAccess_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/EndpointAccess)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/EndpointAccess)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/EndpointAccess)
