---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_CancelLegalHold.html
---

# CancelLegalHold
<a name="API_CancelLegalHold"></a>

Removes the specified legal hold on a recovery point. This action can only be performed by a user with sufficient permissions.

## Request Syntax
<a name="API_CancelLegalHold_RequestSyntax"></a>

```
DELETE /legal-holds/{{legalHoldId}}?cancelDescription={{CancelDescription}}&retainRecordInDays={{RetainRecordInDays}} HTTP/1.1
```

## URI Request Parameters
<a name="API_CancelLegalHold_RequestParameters"></a>

The request uses the following URI parameters.

 ** [CancelDescription](#API_CancelLegalHold_RequestSyntax) **   <a name="Backup-CancelLegalHold-request-uri-CancelDescription"></a>
A string the describes the reason for removing the legal hold.
Required: Yes

 ** [legalHoldId](#API_CancelLegalHold_RequestSyntax) **   <a name="Backup-CancelLegalHold-request-uri-LegalHoldId"></a>
The ID of the legal hold.
Required: Yes

 ** [RetainRecordInDays](#API_CancelLegalHold_RequestSyntax) **   <a name="Backup-CancelLegalHold-request-uri-RetainRecordInDays"></a>
The integer amount, in days, after which to remove legal hold.

## Request Body
<a name="API_CancelLegalHold_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_CancelLegalHold_ResponseSyntax"></a>

```
HTTP/1.1 201
```

## Response Elements
<a name="API_CancelLegalHold_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response with an empty HTTP body.

## Errors
<a name="API_CancelLegalHold_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **
Indicates that something is wrong with a parameter's value. For example, the value is out of range.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** InvalidResourceStateException **
 AWS Backup is already performing an action on this recovery point. It can't perform the action you requested until the first action finishes. Try again later.
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
<a name="API_CancelLegalHold_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/CancelLegalHold)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/CancelLegalHold)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/CancelLegalHold)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/CancelLegalHold)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/CancelLegalHold)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/CancelLegalHold)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/CancelLegalHold)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/CancelLegalHold)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/CancelLegalHold)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/CancelLegalHold)
