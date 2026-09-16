---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_UpdateSubnetGroup.html
---

# UpdateSubnetGroup
<a name="API_UpdateSubnetGroup"></a>

Updates a subnet group. For more information, see [Updating a subnet group](https://docs.aws.amazon.com/MemoryDB/latest/devguide/ubnetGroups.Modifying.html)

## Request Syntax
<a name="API_UpdateSubnetGroup_RequestSyntax"></a>

```
{
   "Description": "{{string}}",
   "SubnetGroupName": "{{string}}",
   "SubnetIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_UpdateSubnetGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Description](#API_UpdateSubnetGroup_RequestSyntax) **   <a name="MemoryDB-UpdateSubnetGroup-request-Description"></a>
A description of the subnet group
Type: String
Required: No

 ** [SubnetGroupName](#API_UpdateSubnetGroup_RequestSyntax) **   <a name="MemoryDB-UpdateSubnetGroup-request-SubnetGroupName"></a>
The name of the subnet group
Type: String
Required: Yes

 ** [SubnetIds](#API_UpdateSubnetGroup_RequestSyntax) **   <a name="MemoryDB-UpdateSubnetGroup-request-SubnetIds"></a>
The EC2 subnet IDs for the subnet group.
Type: Array of strings
Required: No

## Response Syntax
<a name="API_UpdateSubnetGroup_ResponseSyntax"></a>

```
{
   "SubnetGroup": {
      "ARN": "string",
      "Description": "string",
      "Name": "string",
      "Subnets": [
         {
            "AvailabilityZone": {
               "Name": "string"
            },
            "Identifier": "string",
            "SupportedNetworkTypes": [ "string" ]
         }
      ],
      "SupportedNetworkTypes": [ "string" ],
      "VpcId": "string"
   }
}
```

## Response Elements
<a name="API_UpdateSubnetGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SubnetGroup](#API_UpdateSubnetGroup_ResponseSyntax) **   <a name="MemoryDB-UpdateSubnetGroup-response-SubnetGroup"></a>
The updated subnet group
Type: [SubnetGroup](API_SubnetGroup.md) object

## Errors
<a name="API_UpdateSubnetGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidSubnet **

HTTP Status Code: 400

 ** ServiceLinkedRoleNotFoundFault **

HTTP Status Code: 400

 ** SubnetGroupNotFoundFault **

HTTP Status Code: 400

 ** SubnetInUse **

HTTP Status Code: 400

 ** SubnetNotAllowedFault **

HTTP Status Code: 400

 ** SubnetQuotaExceededFault **

HTTP Status Code: 400

## See Also
<a name="API_UpdateSubnetGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/memorydb-2021-01-01/UpdateSubnetGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/memorydb-2021-01-01/UpdateSubnetGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/UpdateSubnetGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/memorydb-2021-01-01/UpdateSubnetGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/UpdateSubnetGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/memorydb-2021-01-01/UpdateSubnetGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/memorydb-2021-01-01/UpdateSubnetGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/memorydb-2021-01-01/UpdateSubnetGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/memorydb-2021-01-01/UpdateSubnetGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/UpdateSubnetGroup)
