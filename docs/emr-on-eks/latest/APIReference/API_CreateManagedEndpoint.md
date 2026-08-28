---
source_url: https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_CreateManagedEndpoint.html
---

# CreateManagedEndpoint
<a name="API_CreateManagedEndpoint"></a>

Creates a managed endpoint. A managed endpoint is a gateway that connects Amazon EMR Studio to Amazon EMR on EKS so that Amazon EMR Studio can communicate with your virtual cluster.

## Request Syntax
<a name="API_CreateManagedEndpoint_RequestSyntax"></a>

```
POST /virtualclusters/{{virtualClusterId}}/endpoints HTTP/1.1
Content-type: application/json

{
   "certificateArn": "{{string}}",
   "clientToken": "{{string}}",
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
         "containerLogRotationConfiguration": {
            "maxFilesToKeep": {{number}},
            "rotationSize": "{{string}}"
         },
         "managedLogs": {
            "allowAWSToRetainLogs": "{{string}}",
            "encryptionKeyArn": "{{string}}"
         },
         "persistentAppUI": "{{string}}",
         "s3MonitoringConfiguration": {
            "encryptionKeyArn": "{{string}}",
            "logUri": "{{string}}"
         }
      }
   },
   "executionRoleArn": "{{string}}",
   "name": "{{string}}",
   "releaseLabel": "{{string}}",
   "sessionIdleTimeoutInMinutes": {{number}},
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "type": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateManagedEndpoint_RequestParameters"></a>

The request uses the following URI parameters.

 ** [virtualClusterId](#API_CreateManagedEndpoint_RequestSyntax) **   <a name="emroneks-CreateManagedEndpoint-request-uri-virtualClusterId"></a>
The ID of the virtual cluster for which a managed endpoint is created.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`
Required: Yes

## Request Body
<a name="API_CreateManagedEndpoint_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [certificateArn](#API_CreateManagedEndpoint_RequestSyntax) **   <a name="emroneks-CreateManagedEndpoint-request-certificateArn"></a>
 *This parameter has been deprecated.*
The certificate ARN provided by users for the managed endpoint. This field is under deprecation and will be removed in future releases.
Type: String
Length Constraints: Minimum length of 44. Maximum length of 2048.
Pattern: `^arn:(aws[a-zA-Z0-9-]*):acm:.+:(\d{12}):certificate/.+$`
Required: No

 ** [clientToken](#API_CreateManagedEndpoint_RequestSyntax) **   <a name="emroneks-CreateManagedEndpoint-request-clientToken"></a>
The client idempotency token for this create call.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*\S.*`
Required: Yes

 ** [configurationOverrides](#API_CreateManagedEndpoint_RequestSyntax) **   <a name="emroneks-CreateManagedEndpoint-request-configurationOverrides"></a>
The configuration settings that will be used to override existing configurations.
Type: [ConfigurationOverrides](API_ConfigurationOverrides.md) object
Required: No

 ** [executionRoleArn](#API_CreateManagedEndpoint_RequestSyntax) **   <a name="emroneks-CreateManagedEndpoint-request-executionRoleArn"></a>
The ARN of the execution role.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:(aws[a-zA-Z0-9-]*):iam::(\d{12})?:(role((\u002F)|(\u002F[\u0021-\u007F]+\u002F))[\w+=,.@-]+)$`
Required: Yes

 ** [name](#API_CreateManagedEndpoint_RequestSyntax) **   <a name="emroneks-CreateManagedEndpoint-request-name"></a>
The name of the managed endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_/#A-Za-z0-9]+`
Required: Yes

 ** [releaseLabel](#API_CreateManagedEndpoint_RequestSyntax) **   <a name="emroneks-CreateManagedEndpoint-request-releaseLabel"></a>
The Amazon EMR release version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_/A-Za-z0-9]+`
Required: Yes

 ** [sessionIdleTimeoutInMinutes](#API_CreateManagedEndpoint_RequestSyntax) **   <a name="emroneks-CreateManagedEndpoint-request-sessionIdleTimeoutInMinutes"></a>
The number of idle minutes before the managed endpoint session times out.
Type: Integer
Required: No

 ** [tags](#API_CreateManagedEndpoint_RequestSyntax) **   <a name="emroneks-CreateManagedEndpoint-request-tags"></a>
The tags of the managed endpoint.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `.*\S.*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `.*\S.*`
Required: No

 ** [type](#API_CreateManagedEndpoint_RequestSyntax) **   <a name="emroneks-CreateManagedEndpoint-request-type"></a>
The type of the managed endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*\S.*`
Required: Yes

## Response Syntax
<a name="API_CreateManagedEndpoint_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "id": "string",
   "name": "string",
   "virtualClusterId": "string"
}
```

## Response Elements
<a name="API_CreateManagedEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateManagedEndpoint_ResponseSyntax) **   <a name="emroneks-CreateManagedEndpoint-response-arn"></a>
The output contains the ARN of the managed endpoint.
Type: String
Length Constraints: Minimum length of 60. Maximum length of 1024.
Pattern: `^arn:(aws[a-zA-Z0-9-]*):emr-containers:.+:(\d{12}):\/virtualclusters\/[0-9a-zA-Z]+\/endpoints\/[0-9a-zA-Z]+$`

 ** [id](#API_CreateManagedEndpoint_ResponseSyntax) **   <a name="emroneks-CreateManagedEndpoint-response-id"></a>
The output contains the ID of the managed endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`

 ** [name](#API_CreateManagedEndpoint_ResponseSyntax) **   <a name="emroneks-CreateManagedEndpoint-response-name"></a>
The output contains the name of the managed endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_/#A-Za-z0-9]+`

 ** [virtualClusterId](#API_CreateManagedEndpoint_ResponseSyntax) **   <a name="emroneks-CreateManagedEndpoint-response-virtualClusterId"></a>
The output contains the ID of the virtual cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`

## Errors
<a name="API_CreateManagedEndpoint_Errors"></a>

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
<a name="API_CreateManagedEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/emr-containers-2020-10-01/CreateManagedEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/emr-containers-2020-10-01/CreateManagedEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-containers-2020-10-01/CreateManagedEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/emr-containers-2020-10-01/CreateManagedEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-containers-2020-10-01/CreateManagedEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/emr-containers-2020-10-01/CreateManagedEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/emr-containers-2020-10-01/CreateManagedEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/emr-containers-2020-10-01/CreateManagedEndpoint)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/emr-containers-2020-10-01/CreateManagedEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-containers-2020-10-01/CreateManagedEndpoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR on EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr-on-eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
