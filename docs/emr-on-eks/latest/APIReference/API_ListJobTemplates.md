---
source_url: https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_ListJobTemplates.html
---

# ListJobTemplates
<a name="API_ListJobTemplates"></a>

Lists job templates based on a set of parameters. Job template stores values of StartJobRun API request in a template and can be used to start a job run. Job template allows two use cases: avoid repeating recurring StartJobRun API request values, enforcing certain values in StartJobRun API request.

## Request Syntax
<a name="API_ListJobTemplates_RequestSyntax"></a>

```
GET /jobtemplates?createdAfter={{createdAfter}}&createdBefore={{createdBefore}}&maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListJobTemplates_RequestParameters"></a>

The request uses the following URI parameters.

 ** [createdAfter](#API_ListJobTemplates_RequestSyntax) **   <a name="emroneks-ListJobTemplates-request-uri-createdAfter"></a>
The date and time after which the job templates were created.

 ** [createdBefore](#API_ListJobTemplates_RequestSyntax) **   <a name="emroneks-ListJobTemplates-request-uri-createdBefore"></a>
 The date and time before which the job templates were created.

 ** [maxResults](#API_ListJobTemplates_RequestSyntax) **   <a name="emroneks-ListJobTemplates-request-uri-maxResults"></a>
 The maximum number of job templates that can be listed.

 ** [nextToken](#API_ListJobTemplates_RequestSyntax) **   <a name="emroneks-ListJobTemplates-request-uri-nextToken"></a>
 The token for the next set of job templates to return.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`

## Request Body
<a name="API_ListJobTemplates_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListJobTemplates_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "templates": [
      {
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
   ]
}
```

## Response Elements
<a name="API_ListJobTemplates_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListJobTemplates_ResponseSyntax) **   <a name="emroneks-ListJobTemplates-response-nextToken"></a>
 This output displays the token for the next set of job templates.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`

 ** [templates](#API_ListJobTemplates_ResponseSyntax) **   <a name="emroneks-ListJobTemplates-response-templates"></a>
This output lists information about the specified job templates.
Type: Array of [JobTemplate](API_JobTemplate.md) objects

## Errors
<a name="API_ListJobTemplates_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
This is an internal server exception.
HTTP Status Code: 500

 ** ValidationException **
There are invalid parameters in the client request.
HTTP Status Code: 400

## See Also
<a name="API_ListJobTemplates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/emr-containers-2020-10-01/ListJobTemplates)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/emr-containers-2020-10-01/ListJobTemplates)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-containers-2020-10-01/ListJobTemplates)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/emr-containers-2020-10-01/ListJobTemplates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-containers-2020-10-01/ListJobTemplates)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/emr-containers-2020-10-01/ListJobTemplates)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/emr-containers-2020-10-01/ListJobTemplates)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/emr-containers-2020-10-01/ListJobTemplates)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/emr-containers-2020-10-01/ListJobTemplates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-containers-2020-10-01/ListJobTemplates)
