---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_CreateSubnetGroup.html
---

# CreateSubnetGroup
<a name="API_CreateSubnetGroup"></a>

Creates a subnet group. A subnet group is a collection of subnets (typically private) that you can designate for your clusters running in an Amazon Virtual Private Cloud (VPC) environment. When you create a cluster in an Amazon VPC, you must specify a subnet group. MemoryDB uses that subnet group to choose a subnet and IP addresses within that subnet to associate with your nodes. For more information, see [Subnets and subnet groups](https://docs.aws.amazon.com/MemoryDB/latest/devguide/subnetgroups.html).

## Request Syntax
<a name="API_CreateSubnetGroup_RequestSyntax"></a>

```
{
   "Description": "{{string}}",
   "SubnetGroupName": "{{string}}",
   "SubnetIds": [ "{{string}}" ],
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateSubnetGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Description](#API_CreateSubnetGroup_RequestSyntax) **   <a name="MemoryDB-CreateSubnetGroup-request-Description"></a>
A description for the subnet group.
Type: String
Required: No

 ** [SubnetGroupName](#API_CreateSubnetGroup_RequestSyntax) **   <a name="MemoryDB-CreateSubnetGroup-request-SubnetGroupName"></a>
The name of the subnet group. This value is stored as a lowercase string.
Type: String
Required: Yes

 ** [SubnetIds](#API_CreateSubnetGroup_RequestSyntax) **   <a name="MemoryDB-CreateSubnetGroup-request-SubnetIds"></a>
A list of VPC subnet IDs for the subnet group.
Type: Array of strings
Required: Yes

 ** [Tags](#API_CreateSubnetGroup_RequestSyntax) **   <a name="MemoryDB-CreateSubnetGroup-request-Tags"></a>
A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_CreateSubnetGroup_ResponseSyntax"></a>

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
<a name="API_CreateSubnetGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SubnetGroup](#API_CreateSubnetGroup_ResponseSyntax) **   <a name="MemoryDB-CreateSubnetGroup-response-SubnetGroup"></a>
The newly-created subnet group.
Type: [SubnetGroup](API_SubnetGroup.md) object

## Errors
<a name="API_CreateSubnetGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidSubnet **

HTTP Status Code: 400

 ** ServiceLinkedRoleNotFoundFault **

HTTP Status Code: 400

 ** SubnetGroupAlreadyExistsFault **

HTTP Status Code: 400

 ** SubnetGroupQuotaExceededFault **

HTTP Status Code: 400

 ** SubnetNotAllowedFault **

HTTP Status Code: 400

 ** SubnetQuotaExceededFault **

HTTP Status Code: 400

 ** TagQuotaPerResourceExceeded **

HTTP Status Code: 400

## See Also
<a name="API_CreateSubnetGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/memorydb-2021-01-01/CreateSubnetGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/memorydb-2021-01-01/CreateSubnetGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/CreateSubnetGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/memorydb-2021-01-01/CreateSubnetGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/CreateSubnetGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/memorydb-2021-01-01/CreateSubnetGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/memorydb-2021-01-01/CreateSubnetGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/memorydb-2021-01-01/CreateSubnetGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/memorydb-2021-01-01/CreateSubnetGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/CreateSubnetGroup)
