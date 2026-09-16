---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_GetAddressListImportJob.html
---

# GetAddressListImportJob
<a name="API_GetAddressListImportJob"></a>

Fetch attributes of an import job.

## Request Syntax
<a name="API_GetAddressListImportJob_RequestSyntax"></a>

```
{
   "JobId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetAddressListImportJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [JobId](#API_GetAddressListImportJob_RequestSyntax) **   <a name="sesmailmanager-GetAddressListImportJob-request-JobId"></a>
The identifier of the import job that needs to be retrieved.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

## Response Syntax
<a name="API_GetAddressListImportJob_ResponseSyntax"></a>

```
{
   "AddressListId": "string",
   "CompletedTimestamp": number,
   "CreatedTimestamp": number,
   "Error": "string",
   "FailedItemsCount": number,
   "ImportDataFormat": {
      "ImportDataType": "string"
   },
   "ImportedItemsCount": number,
   "JobId": "string",
   "Name": "string",
   "PreSignedUrl": "string",
   "StartTimestamp": number,
   "Status": "string"
}
```

## Response Elements
<a name="API_GetAddressListImportJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AddressListId](#API_GetAddressListImportJob_ResponseSyntax) **   <a name="sesmailmanager-GetAddressListImportJob-response-AddressListId"></a>
The unique identifier of the address list the import job was created for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9-]+`

 ** [CompletedTimestamp](#API_GetAddressListImportJob_ResponseSyntax) **   <a name="sesmailmanager-GetAddressListImportJob-response-CompletedTimestamp"></a>
The timestamp of when the import job was completed.
Type: Timestamp

 ** [CreatedTimestamp](#API_GetAddressListImportJob_ResponseSyntax) **   <a name="sesmailmanager-GetAddressListImportJob-response-CreatedTimestamp"></a>
The timestamp of when the import job was created.
Type: Timestamp

 ** [Error](#API_GetAddressListImportJob_ResponseSyntax) **   <a name="sesmailmanager-GetAddressListImportJob-response-Error"></a>
The reason for failure of an import job.
Type: String

 ** [FailedItemsCount](#API_GetAddressListImportJob_ResponseSyntax) **   <a name="sesmailmanager-GetAddressListImportJob-response-FailedItemsCount"></a>
The number of input addresses that failed to be imported into the address list.
Type: Integer

 ** [ImportDataFormat](#API_GetAddressListImportJob_ResponseSyntax) **   <a name="sesmailmanager-GetAddressListImportJob-response-ImportDataFormat"></a>
The format of the input for an import job.
Type: [ImportDataFormat](API_ImportDataFormat.md) object

 ** [ImportedItemsCount](#API_GetAddressListImportJob_ResponseSyntax) **   <a name="sesmailmanager-GetAddressListImportJob-response-ImportedItemsCount"></a>
The number of input addresses successfully imported into the address list.
Type: Integer

 ** [JobId](#API_GetAddressListImportJob_ResponseSyntax) **   <a name="sesmailmanager-GetAddressListImportJob-response-JobId"></a>
The identifier of the import job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9-]+`

 ** [Name](#API_GetAddressListImportJob_ResponseSyntax) **   <a name="sesmailmanager-GetAddressListImportJob-response-Name"></a>
A user-friendly name for the import job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`

 ** [PreSignedUrl](#API_GetAddressListImportJob_ResponseSyntax) **   <a name="sesmailmanager-GetAddressListImportJob-response-PreSignedUrl"></a>
The pre-signed URL target for uploading the input file.
Type: String

 ** [StartTimestamp](#API_GetAddressListImportJob_ResponseSyntax) **   <a name="sesmailmanager-GetAddressListImportJob-response-StartTimestamp"></a>
The timestamp of when the import job was started.
Type: Timestamp

 ** [Status](#API_GetAddressListImportJob_ResponseSyntax) **   <a name="sesmailmanager-GetAddressListImportJob-response-Status"></a>
The status of the import job.
Type: String
Valid Values: `CREATED | PROCESSING | COMPLETED | FAILED | STOPPED`

## Errors
<a name="API_GetAddressListImportJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Occurs when a user is denied access to a specific resource or action.
HTTP Status Code: 400

 ** ResourceNotFoundException **
Occurs when a requested resource is not found.
HTTP Status Code: 400

 ** ThrottlingException **
Occurs when a service's request rate limit is exceeded, resulting in throttling of further requests.
HTTP Status Code: 400

 ** ValidationException **
The request validation has failed. For details, see the accompanying error message.
HTTP Status Code: 400

## See Also
<a name="API_GetAddressListImportJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mailmanager-2023-10-17/GetAddressListImportJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mailmanager-2023-10-17/GetAddressListImportJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/GetAddressListImportJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mailmanager-2023-10-17/GetAddressListImportJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/GetAddressListImportJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mailmanager-2023-10-17/GetAddressListImportJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mailmanager-2023-10-17/GetAddressListImportJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mailmanager-2023-10-17/GetAddressListImportJob)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mailmanager-2023-10-17/GetAddressListImportJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/GetAddressListImportJob)
