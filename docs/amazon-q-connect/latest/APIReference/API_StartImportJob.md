---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_StartImportJob.html
---

# StartImportJob
<a name="API_amazon-q-connect_StartImportJob"></a>

Start an asynchronous job to import Amazon Q in Connect resources from an uploaded source file. Before calling this API, use [StartContentUpload](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_StartContentUpload.html) to upload an asset that contains the resource data.
+ For importing Amazon Q in Connect quick responses, you need to upload a csv file including the quick responses. For information about how to format the csv file for importing quick responses, see [Import quick responses](https://docs.aws.amazon.com/console/connect/quick-responses/add-data).

## Request Syntax
<a name="API_amazon-q-connect_StartImportJob_RequestSyntax"></a>

```
POST /knowledgeBases/{{knowledgeBaseId}}/importJobs HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "externalSourceConfiguration": {
      "configuration": { ... },
      "source": "{{string}}"
   },
   "importJobType": "{{string}}",
   "metadata": {
      "{{string}}" : "{{string}}"
   },
   "uploadId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_amazon-q-connect_StartImportJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [knowledgeBaseId](#API_amazon-q-connect_StartImportJob_RequestSyntax) **   <a name="connect-amazon-q-connect_StartImportJob-request-uri-knowledgeBaseId"></a>
The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.
+ For importing Amazon Q in Connect quick responses, this should be a `QUICK_RESPONSES` type knowledge base.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

## Request Body
<a name="API_amazon-q-connect_StartImportJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_amazon-q-connect_StartImportJob_RequestSyntax) **   <a name="connect-amazon-q-connect_StartImportJob-request-clientToken"></a>
The tags used to organize, track, or control access for this resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** [externalSourceConfiguration](#API_amazon-q-connect_StartImportJob_RequestSyntax) **   <a name="connect-amazon-q-connect_StartImportJob-request-externalSourceConfiguration"></a>
The configuration information of the external source that the resource data are imported from.
Type: [ExternalSourceConfiguration](API_amazon-q-connect_ExternalSourceConfiguration.md) object
Required: No

 ** [importJobType](#API_amazon-q-connect_StartImportJob_RequestSyntax) **   <a name="connect-amazon-q-connect_StartImportJob-request-importJobType"></a>
The type of the import job.
+ For importing quick response resource, set the value to `QUICK_RESPONSES`.
Type: String
Valid Values: `QUICK_RESPONSES`
Required: Yes

 ** [metadata](#API_amazon-q-connect_StartImportJob_RequestSyntax) **   <a name="connect-amazon-q-connect_StartImportJob-request-metadata"></a>
The metadata fields of the imported Amazon Q in Connect resources.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 10 items.
Key Length Constraints: Minimum length of 1. Maximum length of 4096.
Value Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** [uploadId](#API_amazon-q-connect_StartImportJob_RequestSyntax) **   <a name="connect-amazon-q-connect_StartImportJob-request-uploadId"></a>
A pointer to the uploaded asset. This value is returned by [StartContentUpload](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_StartContentUpload.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1200.
Required: Yes

## Response Syntax
<a name="API_amazon-q-connect_StartImportJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "importJob": {
      "createdTime": number,
      "externalSourceConfiguration": {
         "configuration": { ... },
         "source": "string"
      },
      "failedRecordReport": "string",
      "importJobId": "string",
      "importJobType": "string",
      "knowledgeBaseArn": "string",
      "knowledgeBaseId": "string",
      "lastModifiedTime": number,
      "metadata": {
         "string" : "string"
      },
      "status": "string",
      "uploadId": "string",
      "url": "string",
      "urlExpiry": number
   }
}
```

## Response Elements
<a name="API_amazon-q-connect_StartImportJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [importJob](#API_amazon-q-connect_StartImportJob_ResponseSyntax) **   <a name="connect-amazon-q-connect_StartImportJob-response-importJob"></a>
The import job.
Type: [ImportJobData](API_amazon-q-connect_ImportJobData.md) object

## Errors
<a name="API_amazon-q-connect_StartImportJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request could not be processed because of conflict in the current state of the resource. For example, if you're using a `Create` API (such as `CreateAssistant`) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** resourceName **
The specified resource name.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
You've exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use service quotas to request a service quota increase.
HTTP Status Code: 402

 ** UnauthorizedException **
You do not have permission to perform this action.
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by a service.
HTTP Status Code: 400

## See Also
<a name="API_amazon-q-connect_StartImportJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qconnect-2020-10-19/StartImportJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qconnect-2020-10-19/StartImportJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/StartImportJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qconnect-2020-10-19/StartImportJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/StartImportJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qconnect-2020-10-19/StartImportJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qconnect-2020-10-19/StartImportJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qconnect-2020-10-19/StartImportJob)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/qconnect-2020-10-19/StartImportJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/StartImportJob)
