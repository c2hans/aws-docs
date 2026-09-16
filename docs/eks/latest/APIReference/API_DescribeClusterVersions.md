---
source_url: https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeClusterVersions.html
---

# DescribeClusterVersions
<a name="API_DescribeClusterVersions"></a>

Lists available Kubernetes versions for Amazon EKS clusters.

## Request Syntax
<a name="API_DescribeClusterVersions_RequestSyntax"></a>

```
GET /cluster-versions?clusterType={{clusterType}}&clusterVersions={{clusterVersions}}&defaultOnly={{defaultOnly}}&includeAll={{includeAll}}&maxResults={{maxResults}}&nextToken={{nextToken}}&status={{status}}&versionStatus={{versionStatus}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeClusterVersions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [clusterType](#API_DescribeClusterVersions_RequestSyntax) **   <a name="AmazonEKS-DescribeClusterVersions-request-uri-clusterType"></a>
The type of cluster to filter versions by.

 ** [clusterVersions](#API_DescribeClusterVersions_RequestSyntax) **   <a name="AmazonEKS-DescribeClusterVersions-request-uri-clusterVersions"></a>
List of specific cluster versions to describe.

 ** [defaultOnly](#API_DescribeClusterVersions_RequestSyntax) **   <a name="AmazonEKS-DescribeClusterVersions-request-uri-defaultOnly"></a>
Filter to show only default versions.

 ** [includeAll](#API_DescribeClusterVersions_RequestSyntax) **   <a name="AmazonEKS-DescribeClusterVersions-request-uri-includeAll"></a>
Include all available versions in the response.

 ** [maxResults](#API_DescribeClusterVersions_RequestSyntax) **   <a name="AmazonEKS-DescribeClusterVersions-request-uri-maxResults"></a>
Maximum number of results to return.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_DescribeClusterVersions_RequestSyntax) **   <a name="AmazonEKS-DescribeClusterVersions-request-uri-nextToken"></a>
Pagination token for the next set of results.

 ** [status](#API_DescribeClusterVersions_RequestSyntax) **   <a name="AmazonEKS-DescribeClusterVersions-request-uri-status"></a>
This field is deprecated. Use `versionStatus` instead, as that field matches for input and output of this action.
Filter versions by their current status.
Valid Values: `unsupported | standard-support | extended-support`

 ** [versionStatus](#API_DescribeClusterVersions_RequestSyntax) **   <a name="AmazonEKS-DescribeClusterVersions-request-uri-versionStatus"></a>
Filter versions by their current status.
Valid Values: `UNSUPPORTED | STANDARD_SUPPORT | EXTENDED_SUPPORT`

## Request Body
<a name="API_DescribeClusterVersions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeClusterVersions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "clusterVersions": [
      {
         "clusterType": "string",
         "clusterVersion": "string",
         "controlPlaneComponentConfig": {
            "kubeApiServerConfig": {
               "eventTtl": {
                  "constraints": {
                     "max": "string",
                     "min": "string"
                  },
                  "defaultValue": "string"
               },
               "serviceNodePortRange": {
                  "constraints": {
                     "maxPort": {
                        "max": number,
                        "min": number
                     },
                     "minPort": {
                        "max": number,
                        "min": number
                     }
                  },
                  "defaultValue": {
                     "maxPort": number,
                     "minPort": number
                  }
               }
            },
            "kubeControllerManagerConfig": {
               "horizontalPodAutoscalerControllerConfig": {
                  "horizontalPodAutoscalerSyncPeriod": {
                     "constraints": {
                        "max": "string",
                        "min": "string"
                     },
                     "defaultValue": "string"
                  }
               },
               "podGcControllerConfig": {
                  "terminatedPodGcThreshold": {
                     "constraints": {
                        "max": number,
                        "min": number
                     },
                     "defaultValue": number
                  }
               }
            },
            "kubeSchedulerConfig": {
               "nodeResourcesFit": {
                  "scoringStrategy": {
                     "constraints": {
                        "resources": {
                           "name": {
                              "allowedValues": [ "string" ]
                           },
                           "weight": {
                              "max": number,
                              "min": number
                           }
                        },
                        "scoringStrategy": {
                           "allowedValues": [ "string" ]
                        }
                     },
                     "defaultValue": {
                        "resources": [
                           {
                              "name": "string",
                              "weight": number
                           }
                        ],
                        "type": "string"
                     }
                  }
               }
            }
         },
         "controlPlaneScalingTiers": [
            {
               "apiRequestConcurrency": number,
               "clusterDatabaseSizeGb": number,
               "controlPlaneComponentConfigOverrides": {
                  "kubeApiServerConfig": {
                     "eventTtl": {
                        "constraints": {
                           "max": "string",
                           "min": "string"
                        },
                        "defaultValue": "string"
                     },
                     "serviceNodePortRange": {
                        "constraints": {
                           "maxPort": {
                              "max": number,
                              "min": number
                           },
                           "minPort": {
                              "max": number,
                              "min": number
                           }
                        },
                        "defaultValue": {
                           "maxPort": number,
                           "minPort": number
                        }
                     }
                  },
                  "kubeControllerManagerConfig": {
                     "horizontalPodAutoscalerControllerConfig": {
                        "horizontalPodAutoscalerSyncPeriod": {
                           "constraints": {
                              "max": "string",
                              "min": "string"
                           },
                           "defaultValue": "string"
                        }
                     },
                     "podGcControllerConfig": {
                        "terminatedPodGcThreshold": {
                           "constraints": {
                              "max": number,
                              "min": number
                           },
                           "defaultValue": number
                        }
                     }
                  },
                  "kubeSchedulerConfig": {
                     "nodeResourcesFit": {
                        "scoringStrategy": {
                           "constraints": {
                              "resources": {
                                 "name": {
                                    "allowedValues": [ "string" ]
                                 },
                                 "weight": {
                                    "max": number,
                                    "min": number
                                 }
                              },
                              "scoringStrategy": {
                                 "allowedValues": [ "string" ]
                              }
                           },
                           "defaultValue": {
                              "resources": [
                                 {
                                    "name": "string",
                                    "weight": number
                                 }
                              ],
                              "type": "string"
                           }
                        }
                     }
                  }
               },
               "podSchedulingRatePerSecond": number,
               "tierName": "string"
            }
         ],
         "defaultPlatformVersion": "string",
         "defaultVersion": boolean,
         "endOfExtendedSupportDate": number,
         "endOfStandardSupportDate": number,
         "kubernetesPatchVersion": "string",
         "releaseDate": number,
         "status": "string",
         "versionStatus": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeClusterVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [clusterVersions](#API_DescribeClusterVersions_ResponseSyntax) **   <a name="AmazonEKS-DescribeClusterVersions-response-clusterVersions"></a>
List of cluster version information objects.
Type: Array of [ClusterVersionInformation](API_ClusterVersionInformation.md) objects

 ** [nextToken](#API_DescribeClusterVersions_ResponseSyntax) **   <a name="AmazonEKS-DescribeClusterVersions-response-nextToken"></a>
Pagination token for the next set of results.
Type: String

## Errors
<a name="API_DescribeClusterVersions_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** InvalidParameterException **
The specified parameter is invalid. Review the available parameters for the API request.
 ** addonName **
The specified parameter for the add-on name is invalid. Review the available parameters for the API request
 ** clusterName **
The Amazon EKS cluster associated with the exception.
 ** fargateProfileName **
The Fargate profile associated with the exception.
 ** message **
The specified parameter is invalid. Review the available parameters for the API request.
 ** nodegroupName **
The Amazon EKS managed node group associated with the exception.
 ** subscriptionId **
The Amazon EKS subscription ID with the exception.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is invalid given the state of the cluster. Check the state of the cluster and the associated operations.
 ** addonName **
The request is invalid given the state of the add-on name. Check the state of the cluster and the associated operations.
 ** clusterName **
The Amazon EKS cluster associated with the exception.
 ** message **
The Amazon EKS add-on name associated with the exception.
 ** nodegroupName **
The Amazon EKS managed node group associated with the exception.
 ** subscriptionId **
The Amazon EKS subscription ID with the exception.
HTTP Status Code: 400

 ** ServerException **
These errors are usually caused by a server-side issue.
 ** addonName **
The Amazon EKS add-on name associated with the exception.
 ** clusterName **
The Amazon EKS cluster associated with the exception.
 ** message **
These errors are usually caused by a server-side issue.
 ** nodegroupName **
The Amazon EKS managed node group associated with the exception.
 ** subscriptionId **
The Amazon EKS subscription ID with the exception.
HTTP Status Code: 500

## See Also
<a name="API_DescribeClusterVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eks-2017-11-01/DescribeClusterVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eks-2017-11-01/DescribeClusterVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/DescribeClusterVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eks-2017-11-01/DescribeClusterVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/DescribeClusterVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eks-2017-11-01/DescribeClusterVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eks-2017-11-01/DescribeClusterVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eks-2017-11-01/DescribeClusterVersions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/eks-2017-11-01/DescribeClusterVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/DescribeClusterVersions)
