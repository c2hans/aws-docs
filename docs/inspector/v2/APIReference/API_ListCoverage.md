---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListCoverage.html
---

# ListCoverage
<a name="API_ListCoverage"></a>

Lists coverage details for your environment.

## Request Syntax
<a name="API_ListCoverage_RequestSyntax"></a>

```
POST /coverage/list HTTP/1.1
Content-type: application/json

{
   "filterCriteria": {
      "accountId": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "cloudContainerImageTags": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "cloudContainerRegistryName": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "cloudContainerRepositoryName": [
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
      "cloudServerlessFunctionTags": [
         {
            "comparison": "{{string}}",
            "key": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "cloudVmInstanceTags": [
         {
            "comparison": "{{string}}",
            "key": "{{string}}",
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
      "codeRepositoryProviderTypeVisibility": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "ec2InstanceTags": [
         {
            "comparison": "{{string}}",
            "key": "{{string}}",
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
      "ecrImageTags": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "ecrRepositoryName": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "imagePulledAt": [
         {
            "endInclusive": {{number}},
            "startInclusive": {{number}}
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
      "lambdaFunctionTags": [
         {
            "comparison": "{{string}}",
            "key": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "lastScannedAt": [
         {
            "endInclusive": {{number}},
            "startInclusive": {{number}}
         }
      ],
      "lastScannedCommitId": [
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
      "resourceType": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "scanMode": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "scanStatusCode": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "scanStatusReason": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "scanType": [
         {
            "comparison": "{{string}}",
            "value": "{{string}}"
         }
      ]
   },
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListCoverage_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListCoverage_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filterCriteria](#API_ListCoverage_RequestSyntax) **   <a name="inspector2-ListCoverage-request-filterCriteria"></a>
An object that contains details on the filters to apply to the coverage data for your environment.
Type: [CoverageFilterCriteria](API_CoverageFilterCriteria.md) object
Required: No

 ** [maxResults](#API_ListCoverage_RequestSyntax) **   <a name="inspector2-ListCoverage-request-maxResults"></a>
The maximum number of results the response can return. If your request would return more than the maximum the response will return a `nextToken` value, use this value when you call the action again to get the remaining results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 200.
Required: No

 ** [nextToken](#API_ListCoverage_RequestSyntax) **   <a name="inspector2-ListCoverage-request-nextToken"></a>
A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. If your response returns more than the `maxResults` maximum value it will also return a `nextToken` value. For subsequent calls, use the `nextToken` value returned from the previous request to continue listing results after the first page.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000000.
Required: No

## Response Syntax
<a name="API_ListCoverage_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "coveredResources": [
      {
         "accountId": "string",
         "lastScannedAt": number,
         "provider": "string",
         "providerAccountId": "string",
         "providerOrgId": "string",
         "providerPartition": "string",
         "providerRegion": "string",
         "resourceId": "string",
         "resourceMetadata": {
            "codeRepository": {
               "integrationArn": "string",
               "lastScannedCommitId": "string",
               "onDemandScan": {
                  "lastScanAt": number,
                  "lastScannedCommitId": "string",
                  "scanStatus": {
                     "reason": "string",
                     "statusCode": "string"
                  }
               },
               "projectName": "string",
               "providerType": "string",
               "providerTypeVisibility": "string",
               "scanConfiguration": {
                  "continuousIntegrationScanConfigurations": [
                     {
                        "ruleSetCategories": [ "string" ],
                        "supportedEvent": "string"
                     }
                  ],
                  "periodicScanConfigurations": [
                     {
                        "frequencyExpression": "string",
                        "ruleSetCategories": [ "string" ]
                     }
                  ]
               }
            },
            "containerImage": {
               "imagePulledAt": number,
               "imageTags": [ "string" ],
               "inUseCount": number,
               "lastInUseAt": number
            },
            "containerRegistry": {
               "name": "string"
            },
            "containerRepository": {
               "name": "string",
               "scanFrequency": "string"
            },
            "ec2": {
               "amiId": "string",
               "platform": "string",
               "tags": {
                  "string" : "string"
               }
            },
            "ecrImage": {
               "imagePulledAt": number,
               "inUseCount": number,
               "lastInUseAt": number,
               "tags": [ "string" ]
            },
            "ecrRepository": {
               "name": "string",
               "scanFrequency": "string"
            },
            "lambdaFunction": {
               "functionName": "string",
               "functionTags": {
                  "string" : "string"
               },
               "layers": [ "string" ],
               "runtime": "string"
            },
            "serverlessFunction": {
               "functionTags": {
                  "string" : "string"
               },
               "runtime": "string",
               "serverlessFunctionName": "string"
            },
            "vmInstance": {
               "inventoryHash": "string",
               "platform": "string",
               "tags": {
                  "string" : "string"
               },
               "vmImageReference": "string"
            }
         },
         "resourceType": "string",
         "scanMode": "string",
         "scanStatus": {
            "reason": "string",
            "statusCode": "string"
         },
         "scanType": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListCoverage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [coveredResources](#API_ListCoverage_ResponseSyntax) **   <a name="inspector2-ListCoverage-response-coveredResources"></a>
An object that contains details on the covered resources in your environment.
Type: Array of [CoveredResource](API_CoveredResource.md) objects

 ** [nextToken](#API_ListCoverage_ResponseSyntax) **   <a name="inspector2-ListCoverage-response-nextToken"></a>
A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the `NextToken` value returned from the previous request to continue listing results after the first page.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000000.

## Errors
<a name="API_ListCoverage_Errors"></a>

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
<a name="API_ListCoverage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector2-2020-06-08/ListCoverage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector2-2020-06-08/ListCoverage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/ListCoverage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector2-2020-06-08/ListCoverage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/ListCoverage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector2-2020-06-08/ListCoverage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector2-2020-06-08/ListCoverage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector2-2020-06-08/ListCoverage)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/inspector2-2020-06-08/ListCoverage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/ListCoverage)
