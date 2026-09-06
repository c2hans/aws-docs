---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_GetExportImageTask.html
---

# GetExportImageTask
<a name="API_GetExportImageTask"></a>

Retrieves information about an export image task, including its current state, progress, and any error details.

## Request Syntax
<a name="API_GetExportImageTask_RequestSyntax"></a>

```
{
   "TaskId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetExportImageTask_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [TaskId](#API_GetExportImageTask_RequestSyntax) **   <a name="WorkSpacesApplications-GetExportImageTask-request-TaskId"></a>
The unique identifier of the export image task to retrieve information about.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

## Response Syntax
<a name="API_GetExportImageTask_ResponseSyntax"></a>

```
{
   "ExportImageTask": {
      "AmiDescription": "string",
      "AmiId": "string",
      "AmiName": "string",
      "CreatedDate": number,
      "ErrorDetails": [
         {
            "ErrorCode": "string",
            "ErrorMessage": "string"
         }
      ],
      "ImageArn": "string",
      "State": "string",
      "TagSpecifications": {
         "string" : "string"
      },
      "TaskId": "string"
   }
}
```

## Response Elements
<a name="API_GetExportImageTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ExportImageTask](#API_GetExportImageTask_ResponseSyntax) **   <a name="WorkSpacesApplications-GetExportImageTask-response-ExportImageTask"></a>
Information about the export image task, including its current state, created date, and any error details.
Type: [ExportImageTask](API_ExportImageTask.md) object

## Errors
<a name="API_GetExportImageTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** OperationNotPermittedException **
The attempted operation is not permitted.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

## See Also
<a name="API_GetExportImageTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appstream-2016-12-01/GetExportImageTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appstream-2016-12-01/GetExportImageTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/GetExportImageTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appstream-2016-12-01/GetExportImageTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/GetExportImageTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appstream-2016-12-01/GetExportImageTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appstream-2016-12-01/GetExportImageTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appstream-2016-12-01/GetExportImageTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appstream-2016-12-01/GetExportImageTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/GetExportImageTask)
