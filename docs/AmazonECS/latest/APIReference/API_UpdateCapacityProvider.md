---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateCapacityProvider.html
---

# UpdateCapacityProvider
<a name="API_UpdateCapacityProvider"></a>

Modifies the parameters for a capacity provider.

These changes only apply to new Amazon ECS Managed Instances, or EC2 instances, not existing ones.

## Request Syntax
<a name="API_UpdateCapacityProvider_RequestSyntax"></a>

```
{
   "autoScalingGroupProvider": {
      "managedDraining": "{{string}}",
      "managedScaling": {
         "instanceWarmupPeriod": {{number}},
         "maximumScalingStepSize": {{number}},
         "minimumScalingStepSize": {{number}},
         "status": "{{string}}",
         "targetCapacity": {{number}}
      },
      "managedTerminationProtection": "{{string}}"
   },
   "cluster": "{{string}}",
   "managedInstancesProvider": {
      "autoRepairConfiguration": {
         "actionsStatus": "{{string}}"
      },
      "infrastructureOptimization": {
         "scaleInAfter": {{number}}
      },
      "infrastructureRoleArn": "{{string}}",
      "instanceLaunchTemplate": {
         "capacityReservations": {
            "reservationGroupArn": "{{string}}",
            "reservationPreference": "{{string}}"
         },
         "ec2InstanceProfileArn": "{{string}}",
         "instanceMetadataTagsPropagation": {{boolean}},
         "instanceRequirements": {
            "acceleratorCount": {
               "max": {{number}},
               "min": {{number}}
            },
            "acceleratorManufacturers": [ "{{string}}" ],
            "acceleratorNames": [ "{{string}}" ],
            "acceleratorTotalMemoryMiB": {
               "max": {{number}},
               "min": {{number}}
            },
            "acceleratorTypes": [ "{{string}}" ],
            "allowedInstanceTypes": [ "{{string}}" ],
            "bareMetal": "{{string}}",
            "baselineEbsBandwidthMbps": {
               "max": {{number}},
               "min": {{number}}
            },
            "burstablePerformance": "{{string}}",
            "cpuManufacturers": [ "{{string}}" ],
            "excludedInstanceTypes": [ "{{string}}" ],
            "instanceGenerations": [ "{{string}}" ],
            "localStorage": "{{string}}",
            "localStorageTypes": [ "{{string}}" ],
            "maxSpotPriceAsPercentageOfOptimalOnDemandPrice": {{number}},
            "memoryGiBPerVCpu": {
               "max": {{number}},
               "min": {{number}}
            },
            "memoryMiB": {
               "max": {{number}},
               "min": {{number}}
            },
            "networkBandwidthGbps": {
               "max": {{number}},
               "min": {{number}}
            },
            "networkInterfaceCount": {
               "max": {{number}},
               "min": {{number}}
            },
            "onDemandMaxPricePercentageOverLowestPrice": {{number}},
            "requireHibernateSupport": {{boolean}},
            "spotMaxPricePercentageOverLowestPrice": {{number}},
            "totalLocalStorageGB": {
               "max": {{number}},
               "min": {{number}}
            },
            "vCpuCount": {
               "max": {{number}},
               "min": {{number}}
            }
         },
         "localStorageConfiguration": {
            "useLocalStorage": {{boolean}}
         },
         "monitoring": "{{string}}",
         "networkConfiguration": {
            "securityGroups": [ "{{string}}" ],
            "subnets": [ "{{string}}" ]
         },
         "storageConfiguration": {
            "storageSizeGiB": {{number}}
         }
      },
      "propagateTags": "{{string}}"
   },
   "name": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateCapacityProvider_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [autoScalingGroupProvider](#API_UpdateCapacityProvider_RequestSyntax) **   <a name="ECS-UpdateCapacityProvider-request-autoScalingGroupProvider"></a>
An object that represent the parameters to update for the Auto Scaling group capacity provider.
Type: [AutoScalingGroupProviderUpdate](API_AutoScalingGroupProviderUpdate.md) object
Required: No

 ** [cluster](#API_UpdateCapacityProvider_RequestSyntax) **   <a name="ECS-UpdateCapacityProvider-request-cluster"></a>
The name of the cluster that contains the capacity provider to update. Managed instances capacity providers are cluster-scoped and can only be updated within their associated cluster.
Type: String
Required: No

 ** [managedInstancesProvider](#API_UpdateCapacityProvider_RequestSyntax) **   <a name="ECS-UpdateCapacityProvider-request-managedInstancesProvider"></a>
The updated configuration for the Amazon ECS Managed Instances provider. You can modify the infrastructure role, instance launch template, and tag propagation settings. Changes take effect for new instances launched after the update.
Type: [UpdateManagedInstancesProviderConfiguration](API_UpdateManagedInstancesProviderConfiguration.md) object
Required: No

 ** [name](#API_UpdateCapacityProvider_RequestSyntax) **   <a name="ECS-UpdateCapacityProvider-request-name"></a>
The name of the capacity provider to update.
Type: String
Required: Yes

## Response Syntax
<a name="API_UpdateCapacityProvider_ResponseSyntax"></a>

```
{
   "capacityProvider": {
      "autoScalingGroupProvider": {
         "autoScalingGroupArn": "string",
         "managedDraining": "string",
         "managedScaling": {
            "instanceWarmupPeriod": number,
            "maximumScalingStepSize": number,
            "minimumScalingStepSize": number,
            "status": "string",
            "targetCapacity": number
         },
         "managedTerminationProtection": "string"
      },
      "capacityProviderArn": "string",
      "cluster": "string",
      "managedInstancesProvider": {
         "autoRepairConfiguration": {
            "actionsStatus": "string"
         },
         "infrastructureOptimization": {
            "scaleInAfter": number
         },
         "infrastructureRoleArn": "string",
         "instanceLaunchTemplate": {
            "capacityOptionType": "string",
            "capacityReservations": {
               "reservationGroupArn": "string",
               "reservationPreference": "string"
            },
            "ec2InstanceProfileArn": "string",
            "fipsEnabled": boolean,
            "instanceMetadataTagsPropagation": boolean,
            "instanceRequirements": {
               "acceleratorCount": {
                  "max": number,
                  "min": number
               },
               "acceleratorManufacturers": [ "string" ],
               "acceleratorNames": [ "string" ],
               "acceleratorTotalMemoryMiB": {
                  "max": number,
                  "min": number
               },
               "acceleratorTypes": [ "string" ],
               "allowedInstanceTypes": [ "string" ],
               "bareMetal": "string",
               "baselineEbsBandwidthMbps": {
                  "max": number,
                  "min": number
               },
               "burstablePerformance": "string",
               "cpuManufacturers": [ "string" ],
               "excludedInstanceTypes": [ "string" ],
               "instanceGenerations": [ "string" ],
               "localStorage": "string",
               "localStorageTypes": [ "string" ],
               "maxSpotPriceAsPercentageOfOptimalOnDemandPrice": number,
               "memoryGiBPerVCpu": {
                  "max": number,
                  "min": number
               },
               "memoryMiB": {
                  "max": number,
                  "min": number
               },
               "networkBandwidthGbps": {
                  "max": number,
                  "min": number
               },
               "networkInterfaceCount": {
                  "max": number,
                  "min": number
               },
               "onDemandMaxPricePercentageOverLowestPrice": number,
               "requireHibernateSupport": boolean,
               "spotMaxPricePercentageOverLowestPrice": number,
               "totalLocalStorageGB": {
                  "max": number,
                  "min": number
               },
               "vCpuCount": {
                  "max": number,
                  "min": number
               }
            },
            "localStorageConfiguration": {
               "useLocalStorage": boolean
            },
            "monitoring": "string",
            "networkConfiguration": {
               "securityGroups": [ "string" ],
               "subnets": [ "string" ]
            },
            "storageConfiguration": {
               "storageSizeGiB": number
            }
         },
         "propagateTags": "string"
      },
      "name": "string",
      "status": "string",
      "tags": [
         {
            "key": "string",
            "value": "string"
         }
      ],
      "type": "string",
      "updateStatus": "string",
      "updateStatusReason": "string"
   }
}
```

## Response Elements
<a name="API_UpdateCapacityProvider_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [capacityProvider](#API_UpdateCapacityProvider_ResponseSyntax) **   <a name="ECS-UpdateCapacityProvider-response-capacityProvider"></a>
Details about the capacity provider.
Type: [CapacityProvider](API_CapacityProvider.md) object

## Errors
<a name="API_UpdateCapacityProvider_Errors"></a>

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

 ** UnsupportedFeatureException **
The specified task isn't supported in this Region.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

## See Also
<a name="API_UpdateCapacityProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/UpdateCapacityProvider)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/UpdateCapacityProvider)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/UpdateCapacityProvider)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/UpdateCapacityProvider)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/UpdateCapacityProvider)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/UpdateCapacityProvider)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/UpdateCapacityProvider)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/UpdateCapacityProvider)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/UpdateCapacityProvider)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/UpdateCapacityProvider)
