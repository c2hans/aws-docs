---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeCapacityProviders.html
---

# DescribeCapacityProviders
<a name="API_DescribeCapacityProviders"></a>

Describes one or more of your capacity providers.

## Request Syntax
<a name="API_DescribeCapacityProviders_RequestSyntax"></a>

```
{
   "capacityProviders": [ "{{string}}" ],
   "cluster": "{{string}}",
   "include": [ "{{string}}" ],
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeCapacityProviders_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [capacityProviders](#API_DescribeCapacityProviders_RequestSyntax) **   <a name="ECS-DescribeCapacityProviders-request-capacityProviders"></a>
The short name or full Amazon Resource Name (ARN) of one or more capacity providers. Up to `100` capacity providers can be described in an action.
Type: Array of strings
Required: No

 ** [cluster](#API_DescribeCapacityProviders_RequestSyntax) **   <a name="ECS-DescribeCapacityProviders-request-cluster"></a>
The name of the cluster to describe capacity providers for. When specified, only capacity providers associated with this cluster are returned, including Amazon ECS Managed Instances capacity providers.
Type: String
Required: No

 ** [include](#API_DescribeCapacityProviders_RequestSyntax) **   <a name="ECS-DescribeCapacityProviders-request-include"></a>
Specifies whether or not you want to see the resource tags for the capacity provider. If `TAGS` is specified, the tags are included in the response. If this field is omitted, tags aren't included in the response.
Type: Array of strings
Valid Values: `TAGS`
Required: No

 ** [maxResults](#API_DescribeCapacityProviders_RequestSyntax) **   <a name="ECS-DescribeCapacityProviders-request-maxResults"></a>
The maximum number of account setting results returned by `DescribeCapacityProviders` in paginated output. When this parameter is used, `DescribeCapacityProviders` only returns `maxResults` results in a single page along with a `nextToken` response element. The remaining results of the initial request can be seen by sending another `DescribeCapacityProviders` request with the returned `nextToken` value. This value can be between 1 and 10. If this parameter is not used, then `DescribeCapacityProviders` returns up to 10 results and a `nextToken` value if applicable.
Type: Integer
Required: No

 ** [nextToken](#API_DescribeCapacityProviders_RequestSyntax) **   <a name="ECS-DescribeCapacityProviders-request-nextToken"></a>
The `nextToken` value returned from a previous paginated `DescribeCapacityProviders` request where `maxResults` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the `nextToken` value.
This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
Type: String
Required: No

## Response Syntax
<a name="API_DescribeCapacityProviders_ResponseSyntax"></a>

```
{
   "capacityProviders": [
      {
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
   ],
   "failures": [
      {
         "arn": "string",
         "detail": "string",
         "reason": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeCapacityProviders_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [capacityProviders](#API_DescribeCapacityProviders_ResponseSyntax) **   <a name="ECS-DescribeCapacityProviders-response-capacityProviders"></a>
The list of capacity providers.
Type: Array of [CapacityProvider](API_CapacityProvider.md) objects

 ** [failures](#API_DescribeCapacityProviders_ResponseSyntax) **   <a name="ECS-DescribeCapacityProviders-response-failures"></a>
Any failures associated with the call.
Type: Array of [Failure](API_Failure.md) objects

 ** [nextToken](#API_DescribeCapacityProviders_ResponseSyntax) **   <a name="ECS-DescribeCapacityProviders-response-nextToken"></a>
The `nextToken` value to include in a future `DescribeCapacityProviders` request. When the results of a `DescribeCapacityProviders` request exceed `maxResults`, this value can be used to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

## Errors
<a name="API_DescribeCapacityProviders_Errors"></a>

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
<a name="API_DescribeCapacityProviders_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/DescribeCapacityProviders)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/DescribeCapacityProviders)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/DescribeCapacityProviders)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/DescribeCapacityProviders)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/DescribeCapacityProviders)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/DescribeCapacityProviders)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/DescribeCapacityProviders)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/DescribeCapacityProviders)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/DescribeCapacityProviders)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/DescribeCapacityProviders)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
