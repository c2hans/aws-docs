---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListFindings.html
---

# ListFindings
<a name="API_ListFindings"></a>

Lists findings for your environment.

## Request Syntax
<a name="API_ListFindings_RequestSyntax"></a>

```
POST /findings/list HTTP/1.1
Content-type: application/json

{
   "filterCriteria": {
      "awsAccountId": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "cloudImageArchitecture": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "cloudImageDigest": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "cloudImageInUseCount": [
         {
            "lowerInclusive": {{number}},
            "upperInclusive": {{number}}
         }
      ],
      "cloudImageLastInUseAt": [
         {
            "endInclusive": {{number}},
            "startInclusive": {{number}}
         }
      ],
      "cloudImagePushedAt": [
         {
            "endInclusive": {{number}},
            "startInclusive": {{number}}
         }
      ],
      "cloudImageRegistry": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "cloudImageRepositoryName": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "cloudImageTags": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "cloudProvider": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "cloudProviderAccountId": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "cloudProviderOrgId": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "cloudProviderRegion": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "cloudServerlessFunctionExecutionRole": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "cloudServerlessFunctionLastModifiedAt": [
         {
            "endInclusive": {{number}},
            "startInclusive": {{number}}
         }
      ],
      "cloudServerlessFunctionName": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "cloudServerlessFunctionRuntime": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "cloudVmImageReference": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "cloudVmNetworkId": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "cloudVmSubnetIds": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "codeRepositoryProjectName": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "codeRepositoryProviderType": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "codeVulnerabilityDetectorName": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "codeVulnerabilityDetectorTags": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "codeVulnerabilityFilePath": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "componentId": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "componentType": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "ec2InstanceImageId": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "ec2InstanceSubnetId": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "ec2InstanceVpcId": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "ecrImageArchitecture": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "ecrImageHash": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "ecrImageInUseCount": [
         {
            "lowerInclusive": {{number}},
            "upperInclusive": {{number}}
         }
      ],
      "ecrImageLastInUseAt": [
         {
            "endInclusive": {{number}},
            "startInclusive": {{number}}
         }
      ],
      "ecrImagePushedAt": [
         {
            "endInclusive": {{number}},
            "startInclusive": {{number}}
         }
      ],
      "ecrImageRegistry": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "ecrImageRepositoryName": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "ecrImageTags": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "epssScore": [
         {
            "lowerInclusive": {{number}},
            "upperInclusive": {{number}}
         }
      ],
      "exploitAvailable": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "findingArn": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "findingStatus": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "findingType": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "firstObservedAt": [
         {
            "endInclusive": {{number}},
            "startInclusive": {{number}}
         }
      ],
      "fixAvailable": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "inspectorScore": [
         {
            "lowerInclusive": {{number}},
            "upperInclusive": {{number}}
         }
      ],
      "lambdaFunctionExecutionRoleArn": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "lambdaFunctionLastModifiedAt": [
         {
            "endInclusive": {{number}},
            "startInclusive": {{number}}
         }
      ],
      "lambdaFunctionLayers": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "lambdaFunctionName": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "lambdaFunctionRuntime": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "lastObservedAt": [
         {
            "endInclusive": {{number}},
            "startInclusive": {{number}}
         }
      ],
      "networkProtocol": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "portRange": [
         {
            "beginInclusive": {{number}},
            "endInclusive": {{number}}
         }
      ],
      "relatedVulnerabilities": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "resourceId": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "resourceTags": [
         {
            "comparison": "{{string}}",
            "key": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "resourceType": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "severity": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "title": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "updatedAt": [
         {
            "endInclusive": {{number}},
            "startInclusive": {{number}}
         }
      ],
      "vendorSeverity": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "vulnerabilityId": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "vulnerabilitySource": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "vulnerablePackages": [
         {
            "architecture": {
               "comparison": "{{string}}",
               "value": "{{string}}"
            },
            "epoch": {
               "lowerInclusive": {{number}},
               "upperInclusive": {{number}}
            },
            "filePath": {
               "comparison": "{{string}}",
               "value": "{{string}}"
            },
            "name": {
               "comparison": "{{string}}",
               "value": "{{string}}"
            },
            "release": {
               "comparison": "{{string}}",
               "value": "{{string}}"
            },
            "sourceLambdaLayerArn": {
               "comparison": "{{string}}",
               "value": "{{string}}"
            },
            "sourceLayerHash": {
               "comparison": "{{string}}",
               "value": "{{string}}"
            },
            "version": {
               "comparison": "{{string}}",
               "value": "{{string}}"
            }
         }
      ]
   },
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "sortCriteria": {
      "field": "{{string}}",
      "sortOrder": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_ListFindings_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListFindings_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filterCriteria](#API_ListFindings_RequestSyntax) **   <a name="inspector2-ListFindings-request-filterCriteria"></a>
Details on the filters to apply to your finding results.
Type: [FilterCriteria](API_FilterCriteria.md) object
Required: No

 ** [maxResults](#API_ListFindings_RequestSyntax) **   <a name="inspector2-ListFindings-request-maxResults"></a>
The maximum number of results the response can return. If your request would return more than the maximum the response will return a `nextToken` value, use this value when you call the action again to get the remaining results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListFindings_RequestSyntax) **   <a name="inspector2-ListFindings-request-nextToken"></a>
A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. If your response returns more than the `maxResults` maximum value it will also return a `nextToken` value. For subsequent calls, use the `nextToken` value returned from the previous request to continue listing results after the first page.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000000.
Required: No

 ** [sortCriteria](#API_ListFindings_RequestSyntax) **   <a name="inspector2-ListFindings-request-sortCriteria"></a>
Details on the sort criteria to apply to your finding results.
Type: [SortCriteria](API_SortCriteria.md) object
Required: No

## Response Syntax
<a name="API_ListFindings_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "findings": [
      {
         "awsAccountId": "string",
         "codeVulnerabilityDetails": {
            "cwes": [ "string" ],
            "detectorId": "string",
            "detectorName": "string",
            "detectorTags": [ "string" ],
            "filePath": {
               "endLine": number,
               "fileName": "string",
               "filePath": "string",
               "startLine": number
            },
            "referenceUrls": [ "string" ],
            "ruleId": "string",
            "sourceLambdaLayerArn": "string"
         },
         "description": "string",
         "epss": {
            "score": number
         },
         "exploitabilityDetails": {
            "lastKnownExploitAt": number
         },
         "exploitAvailable": "string",
         "findingArn": "string",
         "firstObservedAt": number,
         "fixAvailable": "string",
         "inspectorScore": number,
         "inspectorScoreDetails": {
            "adjustedCvss": {
               "adjustments": [
                  {
                     "metric": "string",
                     "reason": "string"
                  }
               ],
               "cvssSource": "string",
               "score": number,
               "scoreSource": "string",
               "scoringVector": "string",
               "version": "string"
            }
         },
         "lastObservedAt": number,
         "networkReachabilityDetails": {
            "networkPath": {
               "steps": [
                  {
                     "componentArn": "string",
                     "componentId": "string",
                     "componentType": "string"
                  }
               ]
            },
            "openPortRange": {
               "begin": number,
               "end": number
            },
            "protocol": "string"
         },
         "packageVulnerabilityDetails": {
            "cvss": [
               {
                  "baseScore": number,
                  "scoringVector": "string",
                  "source": "string",
                  "version": "string"
               }
            ],
            "referenceUrls": [ "string" ],
            "relatedVulnerabilities": [ "string" ],
            "source": "string",
            "sourceUrl": "string",
            "vendorCreatedAt": number,
            "vendorSeverity": "string",
            "vendorUpdatedAt": number,
            "vulnerabilityId": "string",
            "vulnerablePackages": [
               {
                  "arch": "string",
                  "epoch": number,
                  "filePath": "string",
                  "fixedInVersion": "string",
                  "name": "string",
                  "packageManager": "string",
                  "release": "string",
                  "remediation": "string",
                  "sourceLambdaLayerArn": "string",
                  "sourceLayerHash": "string",
                  "version": "string"
               }
            ]
         },
         "remediation": {
            "recommendation": {
               "text": "string",
               "Url": "string"
            }
         },
         "resources": [
            {
               "details": {
                  "awsEc2Instance": {
                     "iamInstanceProfileArn": "string",
                     "imageId": "string",
                     "ipV4Addresses": [ "string" ],
                     "ipV6Addresses": [ "string" ],
                     "keyName": "string",
                     "launchedAt": number,
                     "platform": "string",
                     "subnetId": "string",
                     "type": "string",
                     "vpcId": "string"
                  },
                  "awsEcrContainerImage": {
                     "architecture": "string",
                     "author": "string",
                     "imageHash": "string",
                     "imageTags": [ "string" ],
                     "inUseCount": number,
                     "lastInUseAt": number,
                     "platform": "string",
                     "pushedAt": number,
                     "registry": "string",
                     "repositoryName": "string"
                  },
                  "awsLambdaFunction": {
                     "architectures": [ "string" ],
                     "codeSha256": "string",
                     "executionRoleArn": "string",
                     "functionName": "string",
                     "lastModifiedAt": number,
                     "layers": [ "string" ],
                     "packageType": "string",
                     "runtime": "string",
                     "version": "string",
                     "vpcConfig": {
                        "securityGroupIds": [ "string" ],
                        "subnetIds": [ "string" ],
                        "vpcId": "string"
                     }
                  },
                  "codeRepository": {
                     "integrationArn": "string",
                     "projectName": "string",
                     "providerType": "string"
                  },
                  "image": {
                     "architecture": "string",
                     "author": "string",
                     "imageDigest": "string",
                     "imageTags": [ "string" ],
                     "inUseCount": number,
                     "lastInUseAt": number,
                     "platform": "string",
                     "pushedAt": number,
                     "registry": "string",
                     "repositoryName": "string"
                  },
                  "serverlessFunction": {
                     "architectures": [ "string" ],
                     "codeDigest": "string",
                     "executionRole": "string",
                     "lastModifiedAt": number,
                     "layers": [ "string" ],
                     "networkId": "string",
                     "packageType": "string",
                     "runtime": "string",
                     "securityGroupIds": [ "string" ],
                     "serverlessFunctionName": "string",
                     "subnetIds": [ "string" ],
                     "version": "string"
                  },
                  "vm": {
                     "executionRole": "string",
                     "ipV4Addresses": [ "string" ],
                     "ipV6Addresses": [ "string" ],
                     "keyName": "string",
                     "launchedAt": number,
                     "networkId": "string",
                     "platform": "string",
                     "securityGroupIds": [ "string" ],
                     "subnetIds": [ "string" ],
                     "type": "string",
                     "vmImageReference": "string",
                     "vmName": "string"
                  }
               },
               "id": "string",
               "partition": "string",
               "provider": "string",
               "providerAccountId": "string",
               "providerOrgId": "string",
               "region": "string",
               "tags": {
                  "string" : "string"
               },
               "type": "string"
            }
         ],
         "severity": "string",
         "status": "string",
         "title": "string",
         "type": "string",
         "updatedAt": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListFindings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [findings](#API_ListFindings_ResponseSyntax) **   <a name="inspector2-ListFindings-response-findings"></a>
Contains details on the findings in your environment.
Type: Array of [Finding](API_Finding.md) objects
Array Members: Minimum number of 0 items. Maximum number of 25 items.

 ** [nextToken](#API_ListFindings_ResponseSyntax) **   <a name="inspector2-ListFindings-response-nextToken"></a>
A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the `NextToken` value returned from the previous request to continue listing results after the first page.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000000.

## Errors
<a name="API_ListFindings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The request has failed due to an internal failure of the Amazon Inspector service.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 ** ThrottlingException **
The limit on the number of requests per second was exceeded.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 429

 ** ValidationException **
The request has failed validation due to missing required fields or having invalid inputs.
 ** fields **
The fields that failed validation.
 ** reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_ListFindings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector2-2020-06-08/ListFindings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector2-2020-06-08/ListFindings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/ListFindings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector2-2020-06-08/ListFindings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/ListFindings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector2-2020-06-08/ListFindings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector2-2020-06-08/ListFindings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector2-2020-06-08/ListFindings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/inspector2-2020-06-08/ListFindings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/ListFindings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
