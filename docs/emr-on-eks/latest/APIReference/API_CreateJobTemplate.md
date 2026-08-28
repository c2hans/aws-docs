---
source_url: https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_CreateJobTemplate.html
---

# CreateJobTemplate
<a name="API_CreateJobTemplate"></a>

Creates a job template. Job template stores values of StartJobRun API request in a template and can be used to start a job run. Job template allows two use cases: avoid repeating recurring StartJobRun API request values, enforcing certain values in StartJobRun API request.

## Request Syntax
<a name="API_CreateJobTemplate_RequestSyntax"></a>

```
POST /jobtemplates HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "jobTemplateData": {
      "configurationOverrides": {
         "applicationConfiguration": [
            {
               "classification": "{{string}}",
               "configurations": [
                  "Configuration"
               ],
               "properties": {
                  "{{string}}" : "{{string}}"
               }
            }
         ],
         "monitoringConfiguration": {
            "cloudWatchMonitoringConfiguration": {
               "logGroupName": "{{string}}",
               "logStreamNamePrefix": "{{string}}"
            },
            "persistentAppUI": "{{string}}",
            "s3MonitoringConfiguration": {
               "logUri": "{{string}}"
            }
         }
      },
      "executionRoleArn": "{{string}}",
      "jobDriver": {
         "sparkSqlJobDriver": {
            "entryPoint": "{{string}}",
            "sparkSqlParameters": "{{string}}"
         },
         "sparkSubmitJobDriver": {
            "entryPoint": "{{string}}",
            "entryPointArguments": [ "{{string}}" ],
            "sparkSubmitParameters": "{{string}}"
         }
      },
      "jobTags": {
         "{{string}}" : "{{string}}"
      },
      "parameterConfiguration": {
         "{{string}}" : {
            "defaultValue": "{{string}}",
            "type": "{{string}}"
         }
      },
      "releaseLabel": "{{string}}"
   },
   "kmsKeyArn": "{{string}}",
   "name": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateJobTemplate_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateJobTemplate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateJobTemplate_RequestSyntax) **   <a name="emroneks-CreateJobTemplate-request-clientToken"></a>
The client token of the job template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*\S.*`
Required: Yes

 ** [jobTemplateData](#API_CreateJobTemplate_RequestSyntax) **   <a name="emroneks-CreateJobTemplate-request-jobTemplateData"></a>
The job template data which holds values of StartJobRun API request.
Type: [JobTemplateData](API_JobTemplateData.md) object
Required: Yes

 ** [kmsKeyArn](#API_CreateJobTemplate_RequestSyntax) **   <a name="emroneks-CreateJobTemplate-request-kmsKeyArn"></a>
The KMS key ARN used to encrypt the job template.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 2048.
Pattern: `^(arn:(aws[a-zA-Z0-9-]*):kms:.+:(\d{12})?:key\/[(0-9a-zA-Z)-?]+|\$\{[a-zA-Z]\w*\})$`
Required: No

 ** [name](#API_CreateJobTemplate_RequestSyntax) **   <a name="emroneks-CreateJobTemplate-request-name"></a>
The specified name of the job template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_/#A-Za-z0-9]+`
Required: Yes

 ** [tags](#API_CreateJobTemplate_RequestSyntax) **   <a name="emroneks-CreateJobTemplate-request-tags"></a>
The tags that are associated with the job template.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `.*\S.*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `.*\S.*`
Required: No

## Response Syntax
<a name="API_CreateJobTemplate_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "createdAt": "string",
   "id": "string",
   "name": "string"
}
```

## Response Elements
<a name="API_CreateJobTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateJobTemplate_ResponseSyntax) **   <a name="emroneks-CreateJobTemplate-response-arn"></a>
This output display the ARN of the created job template.
Type: String
Length Constraints: Minimum length of 60. Maximum length of 1024.
Pattern: `^arn:(aws[a-zA-Z0-9-]*):emr-containers:.+:(\d{12}):\/jobtemplates\/[0-9a-zA-Z]+$`

 ** [createdAt](#API_CreateJobTemplate_ResponseSyntax) **   <a name="emroneks-CreateJobTemplate-response-createdAt"></a>
This output displays the date and time when the job template was created.
Type: Timestamp

 ** [id](#API_CreateJobTemplate_ResponseSyntax) **   <a name="emroneks-CreateJobTemplate-response-id"></a>
This output display the created job template ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`

 ** [name](#API_CreateJobTemplate_ResponseSyntax) **   <a name="emroneks-CreateJobTemplate-response-name"></a>
This output displays the name of the created job template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_/#A-Za-z0-9]+`

## Errors
<a name="API_CreateJobTemplate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
This is an internal server exception.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

 ** ValidationException **
There are invalid parameters in the client request.
HTTP Status Code: 400

## See Also
<a name="API_CreateJobTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/emr-containers-2020-10-01/CreateJobTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/emr-containers-2020-10-01/CreateJobTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-containers-2020-10-01/CreateJobTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/emr-containers-2020-10-01/CreateJobTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-containers-2020-10-01/CreateJobTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/emr-containers-2020-10-01/CreateJobTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/emr-containers-2020-10-01/CreateJobTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/emr-containers-2020-10-01/CreateJobTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/emr-containers-2020-10-01/CreateJobTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-containers-2020-10-01/CreateJobTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR on EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr-on-eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
