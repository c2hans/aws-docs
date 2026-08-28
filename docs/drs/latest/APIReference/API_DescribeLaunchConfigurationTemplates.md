---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_DescribeLaunchConfigurationTemplates.html
---

# DescribeLaunchConfigurationTemplates
<a name="API_DescribeLaunchConfigurationTemplates"></a>

Lists all Launch Configuration Templates, filtered by Launch Configuration Template IDs

## Request Syntax
<a name="API_DescribeLaunchConfigurationTemplates_RequestSyntax"></a>

```
POST /DescribeLaunchConfigurationTemplates HTTP/1.1
Content-type: application/json

{
   "launchConfigurationTemplateIDs": [ "{{string}}" ],
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DescribeLaunchConfigurationTemplates_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeLaunchConfigurationTemplates_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [launchConfigurationTemplateIDs](#API_DescribeLaunchConfigurationTemplates_RequestSyntax) **   <a name="drs-DescribeLaunchConfigurationTemplates-request-launchConfigurationTemplateIDs"></a>
Request to filter Launch Configuration Templates list by Launch Configuration Template ID.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Length Constraints: Fixed length of 21.
Pattern: `lct-[0-9a-zA-Z]{17}`
Required: No

 ** [maxResults](#API_DescribeLaunchConfigurationTemplates_RequestSyntax) **   <a name="drs-DescribeLaunchConfigurationTemplates-request-maxResults"></a>
Maximum results to be returned in DescribeLaunchConfigurationTemplates.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_DescribeLaunchConfigurationTemplates_RequestSyntax) **   <a name="drs-DescribeLaunchConfigurationTemplates-request-nextToken"></a>
The token of the next Launch Configuration Template to retrieve.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_DescribeLaunchConfigurationTemplates_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "arn": "string",
         "copyPrivateIp": boolean,
         "copyTags": boolean,
         "exportBucketArn": "string",
         "launchConfigurationTemplateID": "string",
         "launchDisposition": "string",
         "launchIntoSourceInstance": boolean,
         "licensing": {
            "osByol": boolean
         },
         "postLaunchEnabled": boolean,
         "recoveryMode": "string",
         "tags": {
            "string" : "string"
         },
         "targetInstanceTypeRightSizingMethod": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeLaunchConfigurationTemplates_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_DescribeLaunchConfigurationTemplates_ResponseSyntax) **   <a name="drs-DescribeLaunchConfigurationTemplates-response-items"></a>
List of items returned by DescribeLaunchConfigurationTemplates.
Type: Array of [LaunchConfigurationTemplate](API_LaunchConfigurationTemplate.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.

 ** [nextToken](#API_DescribeLaunchConfigurationTemplates_ResponseSyntax) **   <a name="drs-DescribeLaunchConfigurationTemplates-response-nextToken"></a>
The token of the next Launch Configuration Template to retrieve.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

## Errors
<a name="API_DescribeLaunchConfigurationTemplates_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
 ** retryAfterSeconds **
The number of seconds after which the request should be safe to retry.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource for this operation was not found.
 ** resourceId **
The ID of the resource.
 ** resourceType **
The type of the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
 ** quotaCode **
Quota code.
 ** retryAfterSeconds **
The number of seconds after which the request should be safe to retry.
 ** serviceCode **
Service code.
HTTP Status Code: 429

 ** UninitializedAccountException **
The account performing the request has not been initialized.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by the AWS service.
 ** fieldList **
A list of fields that failed validation.
 ** reason **
Validation exception reason.
HTTP Status Code: 400

## See Also
<a name="API_DescribeLaunchConfigurationTemplates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/drs-2020-02-26/DescribeLaunchConfigurationTemplates)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/drs-2020-02-26/DescribeLaunchConfigurationTemplates)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/DescribeLaunchConfigurationTemplates)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/drs-2020-02-26/DescribeLaunchConfigurationTemplates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/DescribeLaunchConfigurationTemplates)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/drs-2020-02-26/DescribeLaunchConfigurationTemplates)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/drs-2020-02-26/DescribeLaunchConfigurationTemplates)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/drs-2020-02-26/DescribeLaunchConfigurationTemplates)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/drs-2020-02-26/DescribeLaunchConfigurationTemplates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/DescribeLaunchConfigurationTemplates)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Disaster Recovery. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query drs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
