---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_DeleteCluster.html
---

# DeleteCluster
<a name="API_dax_DeleteCluster"></a>

Deletes a previously provisioned DAX cluster. *DeleteCluster* deletes all associated nodes, node endpoints and the DAX cluster itself. When you receive a successful response from this action, DAX immediately begins deleting the cluster; you cannot cancel or revert this action.

## Request Syntax
<a name="API_dax_DeleteCluster_RequestSyntax"></a>

```
{
   "ClusterName": "{{string}}"
}
```

## Request Parameters
<a name="API_dax_DeleteCluster_RequestParameters"></a>

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [ClusterName](#API_dax_DeleteCluster_RequestSyntax) **   <a name="DDB-dax_DeleteCluster-request-ClusterName"></a>
The name of the cluster to be deleted.
Type: String
Required: Yes

## Response Syntax
<a name="API_dax_DeleteCluster_ResponseSyntax"></a>

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
<a name="API_dax_DeleteCluster_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Cluster](#API_dax_DeleteCluster_ResponseSyntax) **   <a name="DDB-dax_DeleteCluster-response-Cluster"></a>
A description of the DAX cluster that is being deleted.
Type: [Cluster](API_dax_Cluster.md) object

## Errors
<a name="API_dax_DeleteCluster_Errors"></a>

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

 ** ServiceLinkedRoleNotFoundFault **
The specified service linked role (SLR) was not found.
HTTP Status Code: 400

## See Also
<a name="API_dax_DeleteCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dax-2017-04-19/DeleteCluster)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dax-2017-04-19/DeleteCluster)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dax-2017-04-19/DeleteCluster)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dax-2017-04-19/DeleteCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dax-2017-04-19/DeleteCluster)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dax-2017-04-19/DeleteCluster)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dax-2017-04-19/DeleteCluster)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dax-2017-04-19/DeleteCluster)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dax-2017-04-19/DeleteCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dax-2017-04-19/DeleteCluster)
