---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_UpdateFramework.html
---

# UpdateFramework
<a name="API_UpdateFramework"></a>

Updates the specified framework.

## Request Syntax
<a name="API_UpdateFramework_RequestSyntax"></a>

```
PUT /audit/frameworks/{{frameworkName}} HTTP/1.1
Content-type: application/json

{
   "FrameworkControls": [
      {
         "ControlInputParameters": [
            {
               "ParameterName": "{{string}}",
               "ParameterValue": "{{string}}"
            }
         ],
         "ControlName": "{{string}}",
         "ControlScope": {
            "ComplianceResourceIds": [ "{{string}}" ],
            "ComplianceResourceTypes": [ "{{string}}" ],
            "Tags": {
               "{{string}}" : "{{string}}"
            }
         }
      }
   ],
   "FrameworkDescription": "{{string}}",
   "IdempotencyToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateFramework_RequestParameters"></a>

The request uses the following URI parameters.

 ** [frameworkName](#API_UpdateFramework_RequestSyntax) **   <a name="Backup-UpdateFramework-request-uri-FrameworkName"></a>
The unique name of a framework. This name is between 1 and 256 characters, starting with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and underscores (\_).
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z][_a-zA-Z0-9]*`
Required: Yes

## Request Body
<a name="API_UpdateFramework_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [FrameworkControls](#API_UpdateFramework_RequestSyntax) **   <a name="Backup-UpdateFramework-request-FrameworkControls"></a>
The controls that make up the framework. Each control in the list has a name, input parameters, and scope.
Type: Array of [FrameworkControl](API_FrameworkControl.md) objects
Required: No

 ** [FrameworkDescription](#API_UpdateFramework_RequestSyntax) **   <a name="Backup-UpdateFramework-request-FrameworkDescription"></a>
An optional description of the framework with a maximum 1,024 characters.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*\S.*`
Required: No

 ** [IdempotencyToken](#API_UpdateFramework_RequestSyntax) **   <a name="Backup-UpdateFramework-request-IdempotencyToken"></a>
A customer-chosen string that you can use to distinguish between otherwise identical calls to `UpdateFrameworkInput`. Retrying a successful request with the same idempotency token results in a success message with no action taken.
Type: String
Required: No

## Response Syntax
<a name="API_UpdateFramework_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CreationTime": number,
   "FrameworkArn": "string",
   "FrameworkName": "string"
}
```

## Response Elements
<a name="API_UpdateFramework_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreationTime](#API_UpdateFramework_ResponseSyntax) **   <a name="Backup-UpdateFramework-response-CreationTime"></a>
The date and time that a framework is created, in ISO 8601 representation. The value of `CreationTime` is accurate to milliseconds. For example, 2020-07-10T15:00:00.000-08:00 represents the 10th of July 2020 at 3:00 PM 8 hours behind UTC.
Type: Timestamp

 ** [FrameworkArn](#API_UpdateFramework_ResponseSyntax) **   <a name="Backup-UpdateFramework-response-FrameworkArn"></a>
An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN depends on the resource type.
Type: String

 ** [FrameworkName](#API_UpdateFramework_ResponseSyntax) **   <a name="Backup-UpdateFramework-response-FrameworkName"></a>
The unique name of a framework. This name is between 1 and 256 characters, starting with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and underscores (\_).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z][_a-zA-Z0-9]*`

## Errors
<a name="API_UpdateFramework_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AlreadyExistsException **
The required resource already exists.
 ** Arn **

 ** Context **

 ** CreatorRequestId **

 ** Type **

HTTP Status Code: 400

 ** ConflictException **
 AWS Backup can't perform the action that you requested until it finishes performing a previous action. Try again later.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** InvalidParameterValueException **
Indicates that something is wrong with a parameter's value. For example, the value is out of range.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** LimitExceededException **
A limit in the request has been exceeded; for example, a maximum number of items allowed in a request.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** MissingParameterValueException **
Indicates that a required parameter is missing.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** ResourceNotFoundException **
A resource that is required for the action doesn't exist.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** ServiceUnavailableException **
The request failed due to a temporary failure of the server.
 ** Context **

 ** Type **

HTTP Status Code: 500

## See Also
<a name="API_UpdateFramework_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/UpdateFramework)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/UpdateFramework)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/UpdateFramework)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/UpdateFramework)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/UpdateFramework)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/UpdateFramework)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/UpdateFramework)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/UpdateFramework)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/UpdateFramework)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/UpdateFramework)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
