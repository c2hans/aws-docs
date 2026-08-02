---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateClusterSettings.html
---

# UpdateClusterSettings
<a name="API_UpdateClusterSettings"></a>

Modifies the settings to use for a cluster.

## Request Syntax
<a name="API_UpdateClusterSettings_RequestSyntax"></a>

```
{
   "cluster": "{{string}}",
   "settings": [
      {
         "name": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_UpdateClusterSettings_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [cluster](#API_UpdateClusterSettings_RequestSyntax) **   <a name="ECS-UpdateClusterSettings-request-cluster"></a>
The name of the cluster to modify the settings for.
Type: String
Required: Yes

 ** [settings](#API_UpdateClusterSettings_RequestSyntax) **   <a name="ECS-UpdateClusterSettings-request-settings"></a>
The setting to use by default for a cluster. This parameter is used to turn on CloudWatch Container Insights for a cluster. If this value is specified, it overrides the `containerInsights` value set with [PutAccountSetting](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutAccountSetting.html) or [PutAccountSettingDefault](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutAccountSettingDefault.html).
Currently, if you delete an existing cluster that does not have Container Insights turned on, and then create a new cluster with the same name with Container Insights tuned on, Container Insights will not actually be turned on. If you want to preserve the same name for your existing cluster and turn on Container Insights, you must wait 7 days before you can re-create it.
Type: Array of [ClusterSetting](API_ClusterSetting.md) objects
Required: Yes

## Response Syntax
<a name="API_UpdateClusterSettings_ResponseSyntax"></a>

```
{
   "cluster": {
      "activeServicesCount": number,
      "attachments": [
         {
            "details": [
               {
                  "name": "string",
                  "value": "string"
               }
            ],
            "id": "string",
            "status": "string",
            "type": "string"
         }
      ],
      "attachmentsStatus": "string",
      "capacityProviders": [ "string" ],
      "clusterArn": "string",
      "clusterName": "string",
      "configuration": {
         "executeCommandConfiguration": {
            "kmsKeyId": "string",
            "logConfiguration": {
               "cloudWatchEncryptionEnabled": boolean,
               "cloudWatchLogGroupName": "string",
               "s3BucketName": "string",
               "s3EncryptionEnabled": boolean,
               "s3KeyPrefix": "string"
            },
            "logging": "string"
         },
         "managedStorageConfiguration": {
            "fargateEphemeralStorageKmsKeyId": "string",
            "kmsKeyId": "string"
         }
      },
      "defaultCapacityProviderStrategy": [
         {
            "base": number,
            "capacityProvider": "string",
            "weight": number
         }
      ],
      "pendingTasksCount": number,
      "registeredContainerInstancesCount": number,
      "runningTasksCount": number,
      "serviceConnectDefaults": {
         "namespace": "string"
      },
      "settings": [
         {
            "name": "string",
            "value": "string"
         }
      ],
      "statistics": [
         {
            "name": "string",
            "value": "string"
         }
      ],
      "status": "string",
      "tags": [
         {
            "key": "string",
            "value": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_UpdateClusterSettings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [cluster](#API_UpdateClusterSettings_ResponseSyntax) **   <a name="ECS-UpdateClusterSettings-response-cluster"></a>
Details about the cluster
Type: [Cluster](API_Cluster.md) object

## Errors
<a name="API_UpdateClusterSettings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have authorization to perform the requested action.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** ClientException **
These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** ClusterNotFoundException **
The specified cluster wasn't found. You can view your available clusters with [ListClusters](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html). Amazon ECS clusters are Region specific.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** InvalidParameterException **
The specified parameter isn't valid. Review the available parameters for the API request.
For more information about service event errors, see [Amazon ECS service event messages](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html).
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** ServerException **
These errors are usually caused by a server issue.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 500

 ** UpdateInProgressException **
There's already a current Amazon ECS container agent update in progress on the container instance that's specified. If the container agent becomes disconnected while it's in a transitional stage, such as `PENDING` or `STAGING`, the update process can get stuck in that state. However, when the agent reconnects, it resumes where it stopped previously.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

## See Also
<a name="API_UpdateClusterSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/UpdateClusterSettings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/UpdateClusterSettings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/UpdateClusterSettings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/UpdateClusterSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/UpdateClusterSettings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/UpdateClusterSettings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/UpdateClusterSettings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/UpdateClusterSettings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/UpdateClusterSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/UpdateClusterSettings)
