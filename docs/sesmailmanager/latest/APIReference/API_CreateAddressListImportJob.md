---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_CreateAddressListImportJob.html
---

# CreateAddressListImportJob
<a name="API_CreateAddressListImportJob"></a>

Creates an import job for an address list.

## Request Syntax
<a name="API_CreateAddressListImportJob_RequestSyntax"></a>

```
{
   "AddressListId": "{{string}}",
   "ClientToken": "{{string}}",
   "ImportDataFormat": {
      "ImportDataType": "{{string}}"
   },
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateAddressListImportJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AddressListId](#API_CreateAddressListImportJob_RequestSyntax) **   <a name="sesmailmanager-CreateAddressListImportJob-request-AddressListId"></a>
The unique identifier of the address list for importing addresses to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

 ** [ClientToken](#API_CreateAddressListImportJob_RequestSyntax) **   <a name="sesmailmanager-CreateAddressListImportJob-request-ClientToken"></a>
A unique token that Amazon SES uses to recognize subsequent retries of the same request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [ImportDataFormat](#API_CreateAddressListImportJob_RequestSyntax) **   <a name="sesmailmanager-CreateAddressListImportJob-request-ImportDataFormat"></a>
The format of the input for an import job.
Type: [ImportDataFormat](API_ImportDataFormat.md) object
Required: Yes

 ** [Name](#API_CreateAddressListImportJob_RequestSyntax) **   <a name="sesmailmanager-CreateAddressListImportJob-request-Name"></a>
A user-friendly name for the import job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

## Response Syntax
<a name="API_CreateAddressListImportJob_ResponseSyntax"></a>

```
{
   "JobId": "string",
   "PreSignedUrl": "string"
}
```

## Response Elements
<a name="API_CreateAddressListImportJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [JobId](#API_CreateAddressListImportJob_ResponseSyntax) **   <a name="sesmailmanager-CreateAddressListImportJob-response-JobId"></a>
The identifier of the created import job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9-]+`

 ** [PreSignedUrl](#API_CreateAddressListImportJob_ResponseSyntax) **   <a name="sesmailmanager-CreateAddressListImportJob-response-PreSignedUrl"></a>
The pre-signed URL target for uploading the input file.
Type: String

## Errors
<a name="API_CreateAddressListImportJob_Errors"></a>

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
<a name="API_CreateAddressListImportJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mailmanager-2023-10-17/CreateAddressListImportJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mailmanager-2023-10-17/CreateAddressListImportJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/CreateAddressListImportJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mailmanager-2023-10-17/CreateAddressListImportJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/CreateAddressListImportJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mailmanager-2023-10-17/CreateAddressListImportJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mailmanager-2023-10-17/CreateAddressListImportJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mailmanager-2023-10-17/CreateAddressListImportJob)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mailmanager-2023-10-17/CreateAddressListImportJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/CreateAddressListImportJob)
