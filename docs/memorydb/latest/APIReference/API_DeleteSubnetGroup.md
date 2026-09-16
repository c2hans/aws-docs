---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DeleteSubnetGroup.html
---

# DeleteSubnetGroup
<a name="API_DeleteSubnetGroup"></a>

Deletes a subnet group. You cannot delete a default subnet group or one that is associated with any clusters.

## Request Syntax
<a name="API_DeleteSubnetGroup_RequestSyntax"></a>

```
{
   "SubnetGroupName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteSubnetGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [SubnetGroupName](#API_DeleteSubnetGroup_RequestSyntax) **   <a name="MemoryDB-DeleteSubnetGroup-request-SubnetGroupName"></a>
The name of the subnet group to delete.
Type: String
Required: Yes

## Response Syntax
<a name="API_DeleteSubnetGroup_ResponseSyntax"></a>

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
<a name="API_DeleteSubnetGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SubnetGroup](#API_DeleteSubnetGroup_ResponseSyntax) **   <a name="MemoryDB-DeleteSubnetGroup-response-SubnetGroup"></a>
The subnet group object that has been deleted.
Type: [SubnetGroup](API_SubnetGroup.md) object

## Errors
<a name="API_DeleteSubnetGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ServiceLinkedRoleNotFoundFault **

HTTP Status Code: 400

 ** SubnetGroupInUseFault **

HTTP Status Code: 400

 ** SubnetGroupNotFoundFault **

HTTP Status Code: 400

## See Also
<a name="API_DeleteSubnetGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/memorydb-2021-01-01/DeleteSubnetGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/memorydb-2021-01-01/DeleteSubnetGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/DeleteSubnetGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/memorydb-2021-01-01/DeleteSubnetGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/DeleteSubnetGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/memorydb-2021-01-01/DeleteSubnetGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/memorydb-2021-01-01/DeleteSubnetGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/memorydb-2021-01-01/DeleteSubnetGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/memorydb-2021-01-01/DeleteSubnetGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/DeleteSubnetGroup)
