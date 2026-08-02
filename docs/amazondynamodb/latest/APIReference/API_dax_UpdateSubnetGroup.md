---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_UpdateSubnetGroup.html
---

# UpdateSubnetGroup
<a name="API_dax_UpdateSubnetGroup"></a>

Modifies an existing subnet group.

## Request Syntax
<a name="API_dax_UpdateSubnetGroup_RequestSyntax"></a>

```
{
   "Description": "{{string}}",
   "SubnetGroupName": "{{string}}",
   "SubnetIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_dax_UpdateSubnetGroup_RequestParameters"></a>

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [SubnetGroupName](#API_dax_UpdateSubnetGroup_RequestSyntax) **   <a name="DDB-dax_UpdateSubnetGroup-request-SubnetGroupName"></a>
The name of the subnet group.
Type: String
Required: Yes

 ** [Description](#API_dax_UpdateSubnetGroup_RequestSyntax) **   <a name="DDB-dax_UpdateSubnetGroup-request-Description"></a>
A description of the subnet group.
Type: String
Required: No

 ** [SubnetIds](#API_dax_UpdateSubnetGroup_RequestSyntax) **   <a name="DDB-dax_UpdateSubnetGroup-request-SubnetIds"></a>
A list of subnet IDs in the subnet group.
Type: Array of strings
Required: No

## Response Syntax
<a name="API_dax_UpdateSubnetGroup_ResponseSyntax"></a>

```
{
   "SubnetGroup": {
      "Description": "string",
      "SubnetGroupName": "string",
      "Subnets": [
         {
            "SubnetAvailabilityZone": "string",
            "SubnetIdentifier": "string",
            "SupportedNetworkTypes": [ "string" ]
         }
      ],
      "SupportedNetworkTypes": [ "string" ],
      "VpcId": "string"
   }
}
```

## Response Elements
<a name="API_dax_UpdateSubnetGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SubnetGroup](#API_dax_UpdateSubnetGroup_ResponseSyntax) **   <a name="DDB-dax_UpdateSubnetGroup-response-SubnetGroup"></a>
The subnet group that has been modified.
Type: [SubnetGroup](API_dax_SubnetGroup.md) object

## Errors
<a name="API_dax_UpdateSubnetGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidSubnet **
An invalid subnet identifier was specified.
HTTP Status Code: 400

 ** ServiceLinkedRoleNotFoundFault **
The specified service linked role (SLR) was not found.
HTTP Status Code: 400

 ** SubnetGroupNotFoundFault **
The requested subnet group name does not refer to an existing subnet group.
HTTP Status Code: 400

 ** SubnetInUse **
The requested subnet is being used by another subnet group.
HTTP Status Code: 400

 ** SubnetNotAllowedFault **
The specified subnet can't be used for the requested network type. This error occurs when either there aren't enough subnets of the required network type to create the cluster, or when you try to use a subnet that doesn't support the requested network type (for example, trying to create a dual-stack cluster with a subnet that doesn't have IPv6 CIDR).
HTTP Status Code: 400

 ** SubnetQuotaExceededFault **
The request cannot be processed because it would exceed the allowed number of subnets in a subnet group.
HTTP Status Code: 400

## See Also
<a name="API_dax_UpdateSubnetGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dax-2017-04-19/UpdateSubnetGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dax-2017-04-19/UpdateSubnetGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dax-2017-04-19/UpdateSubnetGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dax-2017-04-19/UpdateSubnetGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dax-2017-04-19/UpdateSubnetGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dax-2017-04-19/UpdateSubnetGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dax-2017-04-19/UpdateSubnetGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dax-2017-04-19/UpdateSubnetGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dax-2017-04-19/UpdateSubnetGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dax-2017-04-19/UpdateSubnetGroup)
