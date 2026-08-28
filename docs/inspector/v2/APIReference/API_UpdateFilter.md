---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_UpdateFilter.html
---

# UpdateFilter
<a name="API_UpdateFilter"></a>

Specifies the action that is to be applied to the findings that match the filter.

## Request Syntax
<a name="API_UpdateFilter_RequestSyntax"></a>

```
POST /filters/update HTTP/1.1
Content-type: application/json

{
   "action": "{{string}}",
   "description": "{{string}}",
   "filterArn": "{{string}}",
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
   "name": "{{string}}",
   "reason": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateFilter_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateFilter_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [action](#API_UpdateFilter_RequestSyntax) **   <a name="inspector2-UpdateFilter-request-action"></a>
Specifies the action that is to be applied to the findings that match the filter.
Type: String
Valid Values: `NONE | SUPPRESS`
Required: No

 ** [description](#API_UpdateFilter_RequestSyntax) **   <a name="inspector2-UpdateFilter-request-description"></a>
A description of the filter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** [filterArn](#API_UpdateFilter_RequestSyntax) **   <a name="inspector2-UpdateFilter-request-filterArn"></a>
The Amazon Resource Number (ARN) of the filter to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** [filterCriteria](#API_UpdateFilter_RequestSyntax) **   <a name="inspector2-UpdateFilter-request-filterCriteria"></a>
Defines the criteria to be update in the filter.
Type: [FilterCriteria](API_FilterCriteria.md) object
Required: No

 ** [name](#API_UpdateFilter_RequestSyntax) **   <a name="inspector2-UpdateFilter-request-name"></a>
The name of the filter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [reason](#API_UpdateFilter_RequestSyntax) **   <a name="inspector2-UpdateFilter-request-reason"></a>
The reason the filter was updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

## Response Syntax
<a name="API_UpdateFilter_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string"
}
```

## Response Elements
<a name="API_UpdateFilter_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_UpdateFilter_ResponseSyntax) **   <a name="inspector2-UpdateFilter-response-arn"></a>
The Amazon Resource Number (ARN) of the successfully updated filter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

## Errors
<a name="API_UpdateFilter_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 For `Enable`, you receive this error if you attempt to use a feature in an unsupported AWS Region.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed due to an internal failure of the Amazon Inspector service.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The operation tried to access an invalid resource. Make sure the resource is specified correctly.
HTTP Status Code: 404

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
<a name="API_UpdateFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector2-2020-06-08/UpdateFilter)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector2-2020-06-08/UpdateFilter)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/UpdateFilter)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector2-2020-06-08/UpdateFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/UpdateFilter)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector2-2020-06-08/UpdateFilter)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector2-2020-06-08/UpdateFilter)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector2-2020-06-08/UpdateFilter)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/inspector2-2020-06-08/UpdateFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/UpdateFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
