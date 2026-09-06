---
source_url: https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_BatchDeleteImportData.html
---

# BatchDeleteImportData
<a name="API_BatchDeleteImportData"></a>

**Important**
 AWS Application Discovery Service is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).

Deletes one or more import tasks, each identified by their import ID. Each import task has a number of records that can identify servers or applications.

 AWS Application Discovery Service has built-in matching logic that will identify when discovered servers match existing entries that you've previously discovered, the information for the already-existing discovered server is updated. When you delete an import task that contains records that were used to match, the information in those matched records that comes from the deleted records will also be deleted.

## Request Syntax
<a name="API_BatchDeleteImportData_RequestSyntax"></a>

```
{
   "deleteHistory": {{boolean}},
   "importTaskIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_BatchDeleteImportData_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [deleteHistory](#API_BatchDeleteImportData_RequestSyntax) **   <a name="DiscServ-BatchDeleteImportData-request-deleteHistory"></a>
 Set to `true` to remove the deleted import task from [DescribeImportTasks](API_DescribeImportTasks.md).
Type: Boolean
Required: No

 ** [importTaskIds](#API_BatchDeleteImportData_RequestSyntax) **   <a name="DiscServ-BatchDeleteImportData-request-importTaskIds"></a>
The IDs for the import tasks that you want to delete.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Maximum length of 200.
Pattern: `^import-task-[a-fA-F0-9]{32}$`
Required: Yes

## Response Syntax
<a name="API_BatchDeleteImportData_ResponseSyntax"></a>

```
{
   "errors": [
      {
         "errorCode": "string",
         "errorDescription": "string",
         "importTaskId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchDeleteImportData_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errors](#API_BatchDeleteImportData_ResponseSyntax) **   <a name="DiscServ-BatchDeleteImportData-response-errors"></a>
Error messages returned for each import task that you deleted as a response for this command.
Type: Array of [BatchDeleteImportDataError](API_BatchDeleteImportDataError.md) objects

## Errors
<a name="API_BatchDeleteImportData_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AuthorizationErrorException **
The user does not have permission to perform the action. Check the IAM policy associated with this user.
HTTP Status Code: 400

 ** HomeRegionNotSetException **
 AWS Application Discovery Service is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).
The home Region is not set. Set the home Region to continue.
HTTP Status Code: 400

 ** InvalidParameterException **
One or more parameters are not valid. Verify the parameters and try again.
HTTP Status Code: 400

 ** InvalidParameterValueException **
The value of one or more parameters are either invalid or out of range. Verify the parameter values and try again.
HTTP Status Code: 400

 ** ServerInternalErrorException **
The server experienced an internal error. Try again.
HTTP Status Code: 500

## See Also
<a name="API_BatchDeleteImportData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/discovery-2015-11-01/BatchDeleteImportData)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/discovery-2015-11-01/BatchDeleteImportData)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/discovery-2015-11-01/BatchDeleteImportData)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/discovery-2015-11-01/BatchDeleteImportData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/discovery-2015-11-01/BatchDeleteImportData)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/discovery-2015-11-01/BatchDeleteImportData)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/discovery-2015-11-01/BatchDeleteImportData)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/discovery-2015-11-01/BatchDeleteImportData)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/discovery-2015-11-01/BatchDeleteImportData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/discovery-2015-11-01/BatchDeleteImportData)
