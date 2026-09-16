---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_UpdateCluster.html
---

# UpdateCluster
<a name="API_dax_UpdateCluster"></a>

Modifies the settings for a DAX cluster. You can use this action to change one or more cluster configuration parameters by specifying the parameters and the new values.

## Request Syntax
<a name="API_dax_UpdateCluster_RequestSyntax"></a>

```
{
   "ClusterName": "{{string}}",
   "Description": "{{string}}",
   "NotificationTopicArn": "{{string}}",
   "NotificationTopicStatus": "{{string}}",
   "ParameterGroupName": "{{string}}",
   "PreferredMaintenanceWindow": "{{string}}",
   "SecurityGroupIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_dax_UpdateCluster_RequestParameters"></a>

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [ClusterName](#API_dax_UpdateCluster_RequestSyntax) **   <a name="DDB-dax_UpdateCluster-request-ClusterName"></a>
The name of the DAX cluster to be modified.
Type: String
Required: Yes

 ** [Description](#API_dax_UpdateCluster_RequestSyntax) **   <a name="DDB-dax_UpdateCluster-request-Description"></a>
A description of the changes being made to the cluster.
Type: String
Required: No

 ** [NotificationTopicArn](#API_dax_UpdateCluster_RequestSyntax) **   <a name="DDB-dax_UpdateCluster-request-NotificationTopicArn"></a>
The Amazon Resource Name (ARN) that identifies the topic.
Type: String
Required: No

 ** [NotificationTopicStatus](#API_dax_UpdateCluster_RequestSyntax) **   <a name="DDB-dax_UpdateCluster-request-NotificationTopicStatus"></a>
The current state of the topic. A value of “active” means that notifications will be sent to the topic. A value of “inactive” means that notifications will not be sent to the topic.
Type: String
Required: No

 ** [ParameterGroupName](#API_dax_UpdateCluster_RequestSyntax) **   <a name="DDB-dax_UpdateCluster-request-ParameterGroupName"></a>
The name of a parameter group for this cluster.
Type: String
Required: No

 ** [PreferredMaintenanceWindow](#API_dax_UpdateCluster_RequestSyntax) **   <a name="DDB-dax_UpdateCluster-request-PreferredMaintenanceWindow"></a>
A range of time when maintenance of DAX cluster software will be performed. For example: `sun:01:00-sun:09:00`. Cluster maintenance normally takes less than 30 minutes, and is performed automatically within the maintenance window.
Type: String
Required: No

 ** [SecurityGroupIds](#API_dax_UpdateCluster_RequestSyntax) **   <a name="DDB-dax_UpdateCluster-request-SecurityGroupIds"></a>
A list of user-specified security group IDs to be assigned to each node in the DAX cluster. If this parameter is not specified, DAX assigns the default VPC security group to each node.
Type: Array of strings
Required: No

## Response Syntax
<a name="API_dax_UpdateCluster_ResponseSyntax"></a>

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
<a name="API_dax_UpdateCluster_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Cluster](#API_dax_UpdateCluster_ResponseSyntax) **   <a name="DDB-dax_UpdateCluster-response-Cluster"></a>
A description of the DAX cluster, after it has been modified.
Type: [Cluster](API_dax_Cluster.md) object

## Errors
<a name="API_dax_UpdateCluster_Errors"></a>

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

 ** InvalidParameterGroupStateFault **
One or more parameters in a parameter group are in an invalid state.
HTTP Status Code: 400

 ** InvalidParameterValueException **
The value for a parameter is invalid.
HTTP Status Code: 400

 ** ParameterGroupNotFoundFault **
The specified parameter group does not exist.
HTTP Status Code: 400

 ** ServiceLinkedRoleNotFoundFault **
The specified service linked role (SLR) was not found.
HTTP Status Code: 400

## See Also
<a name="API_dax_UpdateCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dax-2017-04-19/UpdateCluster)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dax-2017-04-19/UpdateCluster)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dax-2017-04-19/UpdateCluster)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dax-2017-04-19/UpdateCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dax-2017-04-19/UpdateCluster)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dax-2017-04-19/UpdateCluster)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dax-2017-04-19/UpdateCluster)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dax-2017-04-19/UpdateCluster)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dax-2017-04-19/UpdateCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dax-2017-04-19/UpdateCluster)
