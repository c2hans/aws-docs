---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateCapacityProvider.html
---

# CreateCapacityProvider
<a name="API_CreateCapacityProvider"></a>

Creates a capacity provider. Capacity providers are associated with a cluster and are used in capacity provider strategies to facilitate cluster auto scaling. You can create capacity providers for Amazon ECS Managed Instances and EC2 instances. AWS Fargate has the predefined `FARGATE` and `FARGATE_SPOT` capacity providers.

## Request Syntax
<a name="API_CreateCapacityProvider_RequestSyntax"></a>

```
{
   "autoScalingGroupProvider": {
      "autoScalingGroupArn": "{{string}}",
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
         "capacityOptionType": "{{string}}",
         "capacityReservations": {
            "reservationGroupArn": "{{string}}",
            "reservationPreference": "{{string}}"
         },
         "ec2InstanceProfileArn": "{{string}}",
         "fipsEnabled": {{boolean}},
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
   "name": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateCapacityProvider_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [autoScalingGroupProvider](#API_CreateCapacityProvider_RequestSyntax) **   <a name="ECS-CreateCapacityProvider-request-autoScalingGroupProvider"></a>
The details of the Auto Scaling group for the capacity provider.
Type: [AutoScalingGroupProvider](API_AutoScalingGroupProvider.md) object
Required: No

 ** [cluster](#API_CreateCapacityProvider_RequestSyntax) **   <a name="ECS-CreateCapacityProvider-request-cluster"></a>
The name of the cluster to associate with the capacity provider. When you create a capacity provider with Amazon ECS Managed Instances, it becomes available only within the specified cluster.
Type: String
Required: No

 ** [managedInstancesProvider](#API_CreateCapacityProvider_RequestSyntax) **   <a name="ECS-CreateCapacityProvider-request-managedInstancesProvider"></a>
The configuration for the Amazon ECS Managed Instances provider. This configuration specifies how Amazon ECS manages Amazon EC2 instances on your behalf, including the infrastructure role, instance launch template, and tag propagation settings.
Type: [CreateManagedInstancesProviderConfiguration](API_CreateManagedInstancesProviderConfiguration.md) object
Required: No

 ** [name](#API_CreateCapacityProvider_RequestSyntax) **   <a name="ECS-CreateCapacityProvider-request-name"></a>
The name of the capacity provider. Up to 255 characters are allowed. They include letters (both upper and lowercase letters), numbers, underscores (\_), and hyphens (-). The name can't be prefixed with "`aws`", "`ecs`", or "`fargate`".
Type: String
Required: Yes

 ** [tags](#API_CreateCapacityProvider_RequestSyntax) **   <a name="ECS-CreateCapacityProvider-request-tags"></a>
The metadata that you apply to the capacity provider to categorize and organize them more conveniently. Each tag consists of a key and an optional value. You define both of them.
The following basic restrictions apply to tags:
+ Maximum number of tags per resource - 50
+ For each resource, each tag key must be unique, and each tag key can have only one value.
+ Maximum key length - 128 Unicode characters in UTF-8
+ Maximum value length - 256 Unicode characters in UTF-8
+ If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: \+ - = . \_ : / @.
+ Tag keys and values are case-sensitive.
+ Do not use `aws:`, `AWS:`, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for AWS use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateCapacityProvider_ResponseSyntax"></a>

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
<a name="API_CreateCapacityProvider_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [capacityProvider](#API_CreateCapacityProvider_ResponseSyntax) **   <a name="ECS-CreateCapacityProvider-response-capacityProvider"></a>
The full description of the new capacity provider.
Type: [CapacityProvider](API_CapacityProvider.md) object

## Errors
<a name="API_CreateCapacityProvider_Errors"></a>

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

 ** LimitExceededException **
The limit for the resource was exceeded.
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

 ** UpdateInProgressException **
There's already a current Amazon ECS container agent update in progress on the container instance that's specified. If the container agent becomes disconnected while it's in a transitional stage, such as `PENDING` or `STAGING`, the update process can get stuck in that state. However, when the agent reconnects, it resumes where it stopped previously.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

## See Also
<a name="API_CreateCapacityProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/CreateCapacityProvider)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/CreateCapacityProvider)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/CreateCapacityProvider)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/CreateCapacityProvider)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/CreateCapacityProvider)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/CreateCapacityProvider)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/CreateCapacityProvider)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/CreateCapacityProvider)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/CreateCapacityProvider)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/CreateCapacityProvider)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
