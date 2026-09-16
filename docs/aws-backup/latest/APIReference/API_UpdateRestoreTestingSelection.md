---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_UpdateRestoreTestingSelection.html
---

# UpdateRestoreTestingSelection
<a name="API_UpdateRestoreTestingSelection"></a>

Updates the specified restore testing selection.

Most elements except the `RestoreTestingSelectionName` can be updated with this request.

You can use either protected resource ARNs or conditions, but not both.

## Request Syntax
<a name="API_UpdateRestoreTestingSelection_RequestSyntax"></a>

```
PUT /restore-testing/plans/{{RestoreTestingPlanName}}/selections/{{RestoreTestingSelectionName}} HTTP/1.1
Content-type: application/json

{
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
      "RestoreMetadataOverrides": {
         "{{string}}" : "{{string}}"
      },
      "ValidationWindowHours": {{number}}
   }
}
```

## URI Request Parameters
<a name="API_UpdateRestoreTestingSelection_RequestParameters"></a>

The request uses the following URI parameters.

 ** [RestoreTestingPlanName](#API_UpdateRestoreTestingSelection_RequestSyntax) **   <a name="Backup-UpdateRestoreTestingSelection-request-uri-RestoreTestingPlanName"></a>
The restore testing plan name is required to update the indicated testing plan.
Required: Yes

 ** [RestoreTestingSelectionName](#API_UpdateRestoreTestingSelection_RequestSyntax) **   <a name="Backup-UpdateRestoreTestingSelection-request-uri-RestoreTestingSelectionName"></a>
The required restore testing selection name of the restore testing selection you wish to update.
Required: Yes

## Request Body
<a name="API_UpdateRestoreTestingSelection_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [RestoreTestingSelection](#API_UpdateRestoreTestingSelection_RequestSyntax) **   <a name="Backup-UpdateRestoreTestingSelection-request-RestoreTestingSelection"></a>
To update your restore testing selection, you can use either protected resource ARNs or conditions, but not both. That is, if your selection has `ProtectedResourceArns`, requesting an update with the parameter `ProtectedResourceConditions` will be unsuccessful.
Type: [RestoreTestingSelectionForUpdate](API_RestoreTestingSelectionForUpdate.md) object
Required: Yes

## Response Syntax
<a name="API_UpdateRestoreTestingSelection_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CreationTime": number,
   "RestoreTestingPlanArn": "string",
   "RestoreTestingPlanName": "string",
   "RestoreTestingSelectionName": "string",
   "UpdateTime": number
}
```

## Response Elements
<a name="API_UpdateRestoreTestingSelection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreationTime](#API_UpdateRestoreTestingSelection_ResponseSyntax) **   <a name="Backup-UpdateRestoreTestingSelection-response-CreationTime"></a>
The time the resource testing selection was updated successfully.
Type: Timestamp

 ** [RestoreTestingPlanArn](#API_UpdateRestoreTestingSelection_ResponseSyntax) **   <a name="Backup-UpdateRestoreTestingSelection-response-RestoreTestingPlanArn"></a>
Unique string that is the name of the restore testing plan.
Type: String

 ** [RestoreTestingPlanName](#API_UpdateRestoreTestingSelection_ResponseSyntax) **   <a name="Backup-UpdateRestoreTestingSelection-response-RestoreTestingPlanName"></a>
The restore testing plan with which the updated restore testing selection is associated.
Type: String

 ** [RestoreTestingSelectionName](#API_UpdateRestoreTestingSelection_ResponseSyntax) **   <a name="Backup-UpdateRestoreTestingSelection-response-RestoreTestingSelectionName"></a>
The returned restore testing selection name.
Type: String

 ** [UpdateTime](#API_UpdateRestoreTestingSelection_ResponseSyntax) **   <a name="Backup-UpdateRestoreTestingSelection-response-UpdateTime"></a>
The time the update completed for the restore testing selection.
Type: Timestamp

## Errors
<a name="API_UpdateRestoreTestingSelection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_UpdateRestoreTestingSelection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/UpdateRestoreTestingSelection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/UpdateRestoreTestingSelection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/UpdateRestoreTestingSelection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/UpdateRestoreTestingSelection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/UpdateRestoreTestingSelection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/UpdateRestoreTestingSelection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/UpdateRestoreTestingSelection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/UpdateRestoreTestingSelection)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/UpdateRestoreTestingSelection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/UpdateRestoreTestingSelection)
