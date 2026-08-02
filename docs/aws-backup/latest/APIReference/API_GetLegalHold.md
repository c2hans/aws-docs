---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_GetLegalHold.html
---

# GetLegalHold
<a name="API_GetLegalHold"></a>

This action returns details for a specified legal hold. The details are the body of a legal hold in JSON format, in addition to metadata.

## Request Syntax
<a name="API_GetLegalHold_RequestSyntax"></a>

```
GET /legal-holds/{{legalHoldId}}/ HTTP/1.1
```

## URI Request Parameters
<a name="API_GetLegalHold_RequestParameters"></a>

The request uses the following URI parameters.

 ** [legalHoldId](#API_GetLegalHold_RequestSyntax) **   <a name="Backup-GetLegalHold-request-uri-LegalHoldId"></a>
The ID of the legal hold.
Required: Yes

## Request Body
<a name="API_GetLegalHold_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetLegalHold_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CancelDescription": "string",
   "CancellationDate": number,
   "CreationDate": number,
   "Description": "string",
   "LegalHoldArn": "string",
   "LegalHoldId": "string",
   "RecoveryPointSelection": {
      "DateRange": {
         "FromDate": number,
         "ToDate": number
      },
      "ResourceIdentifiers": [ "string" ],
      "VaultNames": [ "string" ]
   },
   "RetainRecordUntil": number,
   "Status": "string",
   "Title": "string"
}
```

## Response Elements
<a name="API_GetLegalHold_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CancelDescription](#API_GetLegalHold_ResponseSyntax) **   <a name="Backup-GetLegalHold-response-CancelDescription"></a>
The reason for removing the legal hold.
Type: String

 ** [CancellationDate](#API_GetLegalHold_ResponseSyntax) **   <a name="Backup-GetLegalHold-response-CancellationDate"></a>
The time when the legal hold was cancelled.
Type: Timestamp

 ** [CreationDate](#API_GetLegalHold_ResponseSyntax) **   <a name="Backup-GetLegalHold-response-CreationDate"></a>
The time when the legal hold was created.
Type: Timestamp

 ** [Description](#API_GetLegalHold_ResponseSyntax) **   <a name="Backup-GetLegalHold-response-Description"></a>
The description of the legal hold.
Type: String

 ** [LegalHoldArn](#API_GetLegalHold_ResponseSyntax) **   <a name="Backup-GetLegalHold-response-LegalHoldArn"></a>
The framework ARN for the specified legal hold. The format of the ARN depends on the resource type.
Type: String

 ** [LegalHoldId](#API_GetLegalHold_ResponseSyntax) **   <a name="Backup-GetLegalHold-response-LegalHoldId"></a>
The ID of the legal hold.
Type: String

 ** [RecoveryPointSelection](#API_GetLegalHold_ResponseSyntax) **   <a name="Backup-GetLegalHold-response-RecoveryPointSelection"></a>
The criteria to assign a set of resources, such as resource types or backup vaults.
Type: [RecoveryPointSelection](API_RecoveryPointSelection.md) object

 ** [RetainRecordUntil](#API_GetLegalHold_ResponseSyntax) **   <a name="Backup-GetLegalHold-response-RetainRecordUntil"></a>
The date and time until which the legal hold record is retained.
Type: Timestamp

 ** [Status](#API_GetLegalHold_ResponseSyntax) **   <a name="Backup-GetLegalHold-response-Status"></a>
The status of the legal hold.
Type: String
Valid Values: `CREATING | ACTIVE | CANCELING | CANCELED`

 ** [Title](#API_GetLegalHold_ResponseSyntax) **   <a name="Backup-GetLegalHold-response-Title"></a>
The title of the legal hold.
Type: String

## Errors
<a name="API_GetLegalHold_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_GetLegalHold_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/GetLegalHold)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/GetLegalHold)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/GetLegalHold)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/GetLegalHold)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/GetLegalHold)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/GetLegalHold)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/GetLegalHold)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/GetLegalHold)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/GetLegalHold)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/GetLegalHold)
