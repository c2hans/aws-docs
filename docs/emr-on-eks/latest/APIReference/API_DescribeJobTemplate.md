---
source_url: https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_DescribeJobTemplate.html
---

# DescribeJobTemplate
<a name="API_DescribeJobTemplate"></a>

Displays detailed information about a specified job template. Job template stores values of StartJobRun API request in a template and can be used to start a job run. Job template allows two use cases: avoid repeating recurring StartJobRun API request values, enforcing certain values in StartJobRun API request.

## Request Syntax
<a name="API_DescribeJobTemplate_RequestSyntax"></a>

```
GET /jobtemplates/{{templateId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeJobTemplate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [templateId](#API_DescribeJobTemplate_RequestSyntax) **   <a name="emroneks-DescribeJobTemplate-request-uri-id"></a>
The ID of the job template that will be described.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`
Required: Yes

## Request Body
<a name="API_DescribeJobTemplate_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeJobTemplate_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "jobTemplate": {
      "arn": "string",
      "createdAt": "string",
      "createdBy": "string",
      "decryptionError": "string",
      "id": "string",
      "jobTemplateData": {
         "configurationOverrides": {
            "applicationConfiguration": [
               {
                  "classification": "string",
                  "configurations": [
                     "Configuration"
                  ],
                  "properties": {
                     "string" : "string"
                  }
               }
            ],
            "monitoringConfiguration": {
               "cloudWatchMonitoringConfiguration": {
                  "logGroupName": "string",
                  "logStreamNamePrefix": "string"
               },
               "persistentAppUI": "string",
               "s3MonitoringConfiguration": {
                  "logUri": "string"
               }
            }
         },
         "executionRoleArn": "string",
         "jobDriver": {
            "sparkSqlJobDriver": {
               "entryPoint": "string",
               "sparkSqlParameters": "string"
            },
            "sparkSubmitJobDriver": {
               "entryPoint": "string",
               "entryPointArguments": [ "string" ],
               "sparkSubmitParameters": "string"
            }
         },
         "jobTags": {
            "string" : "string"
         },
         "parameterConfiguration": {
            "string" : {
               "defaultValue": "string",
               "type": "string"
            }
         },
         "releaseLabel": "string"
      },
      "kmsKeyArn": "string",
      "name": "string",
      "tags": {
         "string" : "string"
      }
   }
}
```

## Response Elements
<a name="API_DescribeJobTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [jobTemplate](#API_DescribeJobTemplate_ResponseSyntax) **   <a name="emroneks-DescribeJobTemplate-response-jobTemplate"></a>
This output displays information about the specified job template.
Type: [JobTemplate](API_JobTemplate.md) object

## Errors
<a name="API_DescribeJobTemplate_Errors"></a>

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
<a name="API_DescribeJobTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/emr-containers-2020-10-01/DescribeJobTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/emr-containers-2020-10-01/DescribeJobTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-containers-2020-10-01/DescribeJobTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/emr-containers-2020-10-01/DescribeJobTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-containers-2020-10-01/DescribeJobTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/emr-containers-2020-10-01/DescribeJobTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/emr-containers-2020-10-01/DescribeJobTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/emr-containers-2020-10-01/DescribeJobTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/emr-containers-2020-10-01/DescribeJobTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-containers-2020-10-01/DescribeJobTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR on EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr-on-eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
