---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_ListExportImageTasks.html
---

# ListExportImageTasks
<a name="API_ListExportImageTasks"></a>

Lists export image tasks, with optional filtering and pagination. Use this operation to monitor the status of multiple export operations.

## Request Syntax
<a name="API_ListExportImageTasks_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Name": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListExportImageTasks_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_ListExportImageTasks_RequestSyntax) **   <a name="WorkSpacesApplications-ListExportImageTasks-request-Filters"></a>
Optional filters to apply when listing export image tasks. Filters help you narrow down the results based on specific criteria.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 ** [MaxResults](#API_ListExportImageTasks_RequestSyntax) **   <a name="WorkSpacesApplications-ListExportImageTasks-request-MaxResults"></a>
The maximum number of export image tasks to return in a single request. The valid range is 1-500, with a default of 50.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 500.
Required: No

 ** [NextToken](#API_ListExportImageTasks_RequestSyntax) **   <a name="WorkSpacesApplications-ListExportImageTasks-request-NextToken"></a>
The pagination token from a previous request. Use this to retrieve the next page of results when there are more tasks than the MaxResults limit.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## Response Syntax
<a name="API_ListExportImageTasks_ResponseSyntax"></a>

```
{
   "ExportImageTasks": [
      {
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
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListExportImageTasks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ExportImageTasks](#API_ListExportImageTasks_ResponseSyntax) **   <a name="WorkSpacesApplications-ListExportImageTasks-response-ExportImageTasks"></a>
The list of export image tasks that match the specified criteria.
Type: Array of [ExportImageTask](API_ExportImageTask.md) objects

 ** [NextToken](#API_ListExportImageTasks_ResponseSyntax) **   <a name="WorkSpacesApplications-ListExportImageTasks-response-NextToken"></a>
The pagination token to use for retrieving the next page of results. This field is only present when there are more results available.
Type: String
Length Constraints: Minimum length of 1.

## Errors
<a name="API_ListExportImageTasks_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** OperationNotPermittedException **
The attempted operation is not permitted.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

## See Also
<a name="API_ListExportImageTasks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appstream-2016-12-01/ListExportImageTasks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appstream-2016-12-01/ListExportImageTasks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/ListExportImageTasks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appstream-2016-12-01/ListExportImageTasks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/ListExportImageTasks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appstream-2016-12-01/ListExportImageTasks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appstream-2016-12-01/ListExportImageTasks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appstream-2016-12-01/ListExportImageTasks)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appstream-2016-12-01/ListExportImageTasks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/ListExportImageTasks)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
