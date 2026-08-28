---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_CreateRestoreTestingSelection.html
---

# CreateRestoreTestingSelection
<a name="API_CreateRestoreTestingSelection"></a>

This request can be sent after CreateRestoreTestingPlan request returns successfully. This is the second part of creating a resource testing plan, and it must be completed sequentially.

This consists of `RestoreTestingSelectionName`, `ProtectedResourceType`, and one of the following:
+  `ProtectedResourceArns`
+  `ProtectedResourceConditions`

Each protected resource type can have one single value.

A restore testing selection can include a wildcard value ("\*") for `ProtectedResourceArns` along with `ProtectedResourceConditions`. Alternatively, you can include up to 30 specific protected resource ARNs in `ProtectedResourceArns`.

Cannot select by both protected resource types AND specific ARNs. Request will fail if both are included.

## Request Syntax
<a name="API_CreateRestoreTestingSelection_RequestSyntax"></a>

```
PUT /restore-testing/plans/{{RestoreTestingPlanName}}/selections HTTP/1.1
Content-type: application/json

{
   "CreatorRequestId": "{{string}}",
   "RestoreTestingSelection": {
      "IamRoleArn": "{{string}}",
      "ProtectedResourceArns": [ "{{string}}" ],
      "ProtectedResourceConditions": {
         "StringEquals": [
            {
               "Key": "{{string}}",
               "Value": "{{string}}"
            }
         ],
         "StringNotEquals": [
            {
               "Key": "{{string}}",
               "Value": "{{string}}"
            }
         ]
      },
      "ProtectedResourceType": "{{string}}",
      "RestoreMetadataOverrides": {
         "{{string}}" : "{{string}}"
      },
      "RestoreTestingSelectionName": "{{string}}",
      "ValidationWindowHours": {{number}}
   }
}
```

## URI Request Parameters
<a name="API_CreateRestoreTestingSelection_RequestParameters"></a>

The request uses the following URI parameters.

 ** [RestoreTestingPlanName](#API_CreateRestoreTestingSelection_RequestSyntax) **   <a name="Backup-CreateRestoreTestingSelection-request-uri-RestoreTestingPlanName"></a>
Input the restore testing plan name that was returned from the related CreateRestoreTestingPlan request.
Required: Yes

## Request Body
<a name="API_CreateRestoreTestingSelection_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CreatorRequestId](#API_CreateRestoreTestingSelection_RequestSyntax) **   <a name="Backup-CreateRestoreTestingSelection-request-CreatorRequestId"></a>
This is an optional unique string that identifies the request and allows failed requests to be retried without the risk of running the operation twice. If used, this parameter must contain 1 to 50 alphanumeric or '-\_.' characters.
Type: String
Required: No

 ** [RestoreTestingSelection](#API_CreateRestoreTestingSelection_RequestSyntax) **   <a name="Backup-CreateRestoreTestingSelection-request-RestoreTestingSelection"></a>
This consists of `RestoreTestingSelectionName`, `ProtectedResourceType`, and one of the following:
+  `ProtectedResourceArns`
+  `ProtectedResourceConditions`
Each protected resource type can have one single value.
A restore testing selection can include a wildcard value ("\*") for `ProtectedResourceArns` along with `ProtectedResourceConditions`. Alternatively, you can include up to 30 specific protected resource ARNs in `ProtectedResourceArns`.
Type: [RestoreTestingSelectionForCreate](API_RestoreTestingSelectionForCreate.md) object
Required: Yes

## Response Syntax
<a name="API_CreateRestoreTestingSelection_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "CreationTime": number,
   "RestoreTestingPlanArn": "string",
   "RestoreTestingPlanName": "string",
   "RestoreTestingSelectionName": "string"
}
```

## Response Elements
<a name="API_CreateRestoreTestingSelection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [CreationTime](#API_CreateRestoreTestingSelection_ResponseSyntax) **   <a name="Backup-CreateRestoreTestingSelection-response-CreationTime"></a>
The time that the resource testing selection was created.
Type: Timestamp

 ** [RestoreTestingPlanArn](#API_CreateRestoreTestingSelection_ResponseSyntax) **   <a name="Backup-CreateRestoreTestingSelection-response-RestoreTestingPlanArn"></a>
The ARN of the restore testing plan with which the restore testing selection is associated.
Type: String

 ** [RestoreTestingPlanName](#API_CreateRestoreTestingSelection_ResponseSyntax) **   <a name="Backup-CreateRestoreTestingSelection-response-RestoreTestingPlanName"></a>
The name of the restore testing plan.
The name cannot be changed after creation. The name consists of only alphanumeric characters and underscores. Maximum length is 50.
Type: String

 ** [RestoreTestingSelectionName](#API_CreateRestoreTestingSelection_ResponseSyntax) **   <a name="Backup-CreateRestoreTestingSelection-response-RestoreTestingSelectionName"></a>
The name of the restore testing selection for the related restore testing plan.
The name cannot be changed after creation. The name consists of only alphanumeric characters and underscores. Maximum length is 50.
Type: String

## Errors
<a name="API_CreateRestoreTestingSelection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AlreadyExistsException **
The required resource already exists.
 ** Arn **

 ** Context **

 ** CreatorRequestId **

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
<a name="API_CreateRestoreTestingSelection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/CreateRestoreTestingSelection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/CreateRestoreTestingSelection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/CreateRestoreTestingSelection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/CreateRestoreTestingSelection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/CreateRestoreTestingSelection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/CreateRestoreTestingSelection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/CreateRestoreTestingSelection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/CreateRestoreTestingSelection)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/CreateRestoreTestingSelection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/CreateRestoreTestingSelection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
