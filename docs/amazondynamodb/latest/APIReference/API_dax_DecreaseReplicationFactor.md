---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_DecreaseReplicationFactor.html
---

# DecreaseReplicationFactor
<a name="API_dax_DecreaseReplicationFactor"></a>

Removes one or more nodes from a DAX cluster.

**Note**
You cannot use `DecreaseReplicationFactor` to remove the last node in a DAX cluster. If you need to do this, use `DeleteCluster` instead.

## Request Syntax
<a name="API_dax_DecreaseReplicationFactor_RequestSyntax"></a>

```
{
   "AvailabilityZones": [ "{{string}}" ],
   "ClusterName": "{{string}}",
   "NewReplicationFactor": {{number}},
   "NodeIdsToRemove": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_dax_DecreaseReplicationFactor_RequestParameters"></a>

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [ClusterName](#API_dax_DecreaseReplicationFactor_RequestSyntax) **   <a name="DDB-dax_DecreaseReplicationFactor-request-ClusterName"></a>
The name of the DAX cluster from which you want to remove nodes.
Type: String
Required: Yes

 ** [NewReplicationFactor](#API_dax_DecreaseReplicationFactor_RequestSyntax) **   <a name="DDB-dax_DecreaseReplicationFactor-request-NewReplicationFactor"></a>
The new number of nodes for the DAX cluster.
Type: Integer
Required: Yes

 ** [AvailabilityZones](#API_dax_DecreaseReplicationFactor_RequestSyntax) **   <a name="DDB-dax_DecreaseReplicationFactor-request-AvailabilityZones"></a>
The Availability Zone(s) from which to remove nodes.
Type: Array of strings
Required: No

 ** [NodeIdsToRemove](#API_dax_DecreaseReplicationFactor_RequestSyntax) **   <a name="DDB-dax_DecreaseReplicationFactor-request-NodeIdsToRemove"></a>
The unique identifiers of the nodes to be removed from the cluster.
Type: Array of strings
Required: No

## Response Syntax
<a name="API_dax_DecreaseReplicationFactor_ResponseSyntax"></a>

```
{
   "Cluster": {
      "ActiveNodes": number,
      "ClusterArn": "string",
      "ClusterDiscoveryEndpoint": {
         "Address": "string",
         "Port": number,
         "URL": "string"
      },
      "ClusterEndpointEncryptionType": "string",
      "ClusterName": "string",
      "Description": "string",
      "IamRoleArn": "string",
      "NetworkType": "string",
      "NodeIdsToRemove": [ "string" ],
      "Nodes": [
         {
            "AvailabilityZone": "string",
            "Endpoint": {
               "Address": "string",
               "Port": number,
               "URL": "string"
            },
            "NodeCreateTime": number,
            "NodeId": "string",
            "NodeStatus": "string",
            "ParameterGroupStatus": "string"
         }
      ],
      "NodeType": "string",
      "NotificationConfiguration": {
         "TopicArn": "string",
         "TopicStatus": "string"
      },
      "ParameterGroup": {
         "NodeIdsToReboot": [ "string" ],
         "ParameterApplyStatus": "string",
         "ParameterGroupName": "string"
      },
      "PreferredMaintenanceWindow": "string",
      "SecurityGroups": [
         {
            "SecurityGroupIdentifier": "string",
            "Status": "string"
         }
      ],
      "SSEDescription": {
         "Status": "string"
      },
      "Status": "string",
      "SubnetGroup": "string",
      "TotalNodes": number
   }
}
```

## Response Elements
<a name="API_dax_DecreaseReplicationFactor_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Cluster](#API_dax_DecreaseReplicationFactor_ResponseSyntax) **   <a name="DDB-dax_DecreaseReplicationFactor-response-Cluster"></a>
A description of the DAX cluster, after you have decreased its replication factor.
Type: [Cluster](API_dax_Cluster.md) object

## Errors
<a name="API_dax_DecreaseReplicationFactor_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterNotFoundFault **
The requested cluster ID does not refer to an existing DAX cluster.
HTTP Status Code: 400

 ** InvalidClusterStateFault **
The requested DAX cluster is not in the *available* state.
HTTP Status Code: 400

 ** InvalidParameterCombinationException **
Two or more incompatible parameters were specified.
HTTP Status Code: 400

 ** InvalidParameterValueException **
The value for a parameter is invalid.
HTTP Status Code: 400

 ** NodeNotFoundFault **
None of the nodes in the cluster have the given node ID.
HTTP Status Code: 400

 ** ServiceLinkedRoleNotFoundFault **
The specified service linked role (SLR) was not found.
HTTP Status Code: 400

## See Also
<a name="API_dax_DecreaseReplicationFactor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dax-2017-04-19/DecreaseReplicationFactor)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dax-2017-04-19/DecreaseReplicationFactor)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dax-2017-04-19/DecreaseReplicationFactor)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dax-2017-04-19/DecreaseReplicationFactor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dax-2017-04-19/DecreaseReplicationFactor)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dax-2017-04-19/DecreaseReplicationFactor)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dax-2017-04-19/DecreaseReplicationFactor)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dax-2017-04-19/DecreaseReplicationFactor)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dax-2017-04-19/DecreaseReplicationFactor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dax-2017-04-19/DecreaseReplicationFactor)
