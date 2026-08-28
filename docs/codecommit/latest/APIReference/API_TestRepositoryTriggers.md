---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_TestRepositoryTriggers.html
---

# TestRepositoryTriggers
<a name="API_TestRepositoryTriggers"></a>

Tests the functionality of repository triggers by sending information to the trigger target. If real data is available in the repository, the test sends data from the last commit. If no data is available, sample data is generated.

## Request Syntax
<a name="API_TestRepositoryTriggers_RequestSyntax"></a>

```
{
   "repositoryName": "{{string}}",
   "triggers": [
      {
         "branches": [ "{{string}}" ],
         "customData": "{{string}}",
         "destinationArn": "{{string}}",
         "events": [ "{{string}}" ],
         "name": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_TestRepositoryTriggers_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [repositoryName](#API_TestRepositoryTriggers_RequestSyntax) **   <a name="CodeCommit-TestRepositoryTriggers-request-repositoryName"></a>
The name of the repository in which to test the triggers.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\.-]+`
Required: Yes

 ** [triggers](#API_TestRepositoryTriggers_RequestSyntax) **   <a name="CodeCommit-TestRepositoryTriggers-request-triggers"></a>
The list of triggers to test.
Type: Array of [RepositoryTrigger](API_RepositoryTrigger.md) objects
Required: Yes

## Response Syntax
<a name="API_TestRepositoryTriggers_ResponseSyntax"></a>

```
{
   "failedExecutions": [
      {
         "failureMessage": "string",
         "trigger": "string"
      }
   ],
   "successfulExecutions": [ "string" ]
}
```

## Response Elements
<a name="API_TestRepositoryTriggers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [failedExecutions](#API_TestRepositoryTriggers_ResponseSyntax) **   <a name="CodeCommit-TestRepositoryTriggers-response-failedExecutions"></a>
The list of triggers that were not tested. This list provides the names of the triggers that could not be tested, separated by commas.
Type: Array of [RepositoryTriggerExecutionFailure](API_RepositoryTriggerExecutionFailure.md) objects

 ** [successfulExecutions](#API_TestRepositoryTriggers_ResponseSyntax) **   <a name="CodeCommit-TestRepositoryTriggers-response-successfulExecutions"></a>
The list of triggers that were successfully tested. This list provides the names of the triggers that were successfully tested, separated by commas.
Type: Array of strings

## Errors
<a name="API_TestRepositoryTriggers_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** EncryptionIntegrityChecksFailedException **
An encryption integrity check failed.
HTTP Status Code: 500

 ** EncryptionKeyAccessDeniedException **
An encryption key could not be accessed.
HTTP Status Code: 400

 ** EncryptionKeyDisabledException **
The encryption key is disabled.
HTTP Status Code: 400

 ** EncryptionKeyNotFoundException **
No encryption key was found.
HTTP Status Code: 400

 ** EncryptionKeyUnavailableException **
The encryption key is not available.
HTTP Status Code: 400

 ** InvalidRepositoryNameException **
A specified repository name is not valid.
This exception occurs only when a specified repository name is not valid. Other exceptions occur when a required repository parameter is missing, or when a specified repository does not exist.
HTTP Status Code: 400

 ** InvalidRepositoryTriggerBranchNameException **
One or more branch names specified for the trigger is not valid.
HTTP Status Code: 400

 ** InvalidRepositoryTriggerCustomDataException **
The custom data provided for the trigger is not valid.
HTTP Status Code: 400

 ** InvalidRepositoryTriggerDestinationArnException **
The Amazon Resource Name (ARN) for the trigger is not valid for the specified destination. The most common reason for this error is that the ARN does not meet the requirements for the service type.
HTTP Status Code: 400

 ** InvalidRepositoryTriggerEventsException **
One or more events specified for the trigger is not valid. Check to make sure that all events specified match the requirements for allowed events.
HTTP Status Code: 400

 ** InvalidRepositoryTriggerNameException **
The name of the trigger is not valid.
HTTP Status Code: 400

 ** InvalidRepositoryTriggerRegionException **
The AWS Region for the trigger target does not match the AWS Region for the repository. Triggers must be created in the same AWS Region as the target for the trigger.
HTTP Status Code: 400

 ** MaximumBranchesExceededException **
The number of branches for the trigger was exceeded.
HTTP Status Code: 400

 ** MaximumRepositoryTriggersExceededException **
The number of triggers allowed for the repository was exceeded.
HTTP Status Code: 400

 ** RepositoryDoesNotExistException **
The specified repository does not exist.
HTTP Status Code: 400

 ** RepositoryNameRequiredException **
A repository name is required, but was not specified.
HTTP Status Code: 400

 ** RepositoryTriggerBranchNameListRequiredException **
At least one branch name is required, but was not specified in the trigger configuration.
HTTP Status Code: 400

 ** RepositoryTriggerDestinationArnRequiredException **
A destination ARN for the target service for the trigger is required, but was not specified.
HTTP Status Code: 400

 ** RepositoryTriggerEventsListRequiredException **
At least one event for the trigger is required, but was not specified.
HTTP Status Code: 400

 ** RepositoryTriggerNameRequiredException **
A name for the trigger is required, but was not specified.
HTTP Status Code: 400

 ** RepositoryTriggersListRequiredException **
The list of triggers for the repository is required, but was not specified.
HTTP Status Code: 400

## Examples
<a name="API_TestRepositoryTriggers_Examples"></a>

### Example
<a name="API_TestRepositoryTriggers_Example_1"></a>

This example illustrates one usage of TestRepositoryTriggers.

#### Sample Request
<a name="API_TestRepositoryTriggers_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codecommit.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 33
X-Amz-Target: CodeCommit_20150413.TestRepositoryTriggers
X-Amz-Date: 20151028T230050Z
User-Agent: aws-cli/1.7.38 Python/2.7.9 Windows/7
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20151028/us-east-1/codecommit/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
      "repositoryName": "MyDemoRepo",
      "triggers": [
        {
          "name": "MyFirstTrigger",
          "destinationArn": "arn:aws:sns:us-east-1:123456789012:MyCodeCommitTopic",
          "branches": [
            "main",
            "preprod"
          ],
          "events": [
            "all"
          ]
        }
```

#### Sample Response
<a name="API_TestRepositoryTriggers_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 0728aaa8-EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 107
Date: Wed, 28 Oct 2015 23:00:52 GMT

{
      "successfulExecutions": [
        "MyFirstTrigger"
      ],
      "failedExecutions": []
}
```

## See Also
<a name="API_TestRepositoryTriggers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecommit-2015-04-13/TestRepositoryTriggers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecommit-2015-04-13/TestRepositoryTriggers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/TestRepositoryTriggers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecommit-2015-04-13/TestRepositoryTriggers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/TestRepositoryTriggers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecommit-2015-04-13/TestRepositoryTriggers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecommit-2015-04-13/TestRepositoryTriggers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecommit-2015-04-13/TestRepositoryTriggers)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codecommit-2015-04-13/TestRepositoryTriggers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/TestRepositoryTriggers)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeCommit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecommit` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
