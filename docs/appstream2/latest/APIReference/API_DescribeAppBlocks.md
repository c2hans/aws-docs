---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DescribeAppBlocks.html
---

# DescribeAppBlocks
<a name="API_DescribeAppBlocks"></a>

Retrieves a list that describes one or more app blocks.

## Request Syntax
<a name="API_DescribeAppBlocks_RequestSyntax"></a>

```
{
   "Arns": [ "{{string}}" ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeAppBlocks_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Arns](#API_DescribeAppBlocks_RequestSyntax) **   <a name="WorkSpacesApplications-DescribeAppBlocks-request-Arns"></a>
The ARNs of the app blocks.
Type: Array of strings
Pattern: `^arn:aws(?:\-cn|\-iso\-b|\-iso|\-us\-gov)?:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.\\-]{0,1023}$`
Required: No

 ** [MaxResults](#API_DescribeAppBlocks_RequestSyntax) **   <a name="WorkSpacesApplications-DescribeAppBlocks-request-MaxResults"></a>
The maximum size of each page of results.
Type: Integer
Required: No

 ** [NextToken](#API_DescribeAppBlocks_RequestSyntax) **   <a name="WorkSpacesApplications-DescribeAppBlocks-request-NextToken"></a>
The pagination token used to retrieve the next page of results for this operation.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## Response Syntax
<a name="API_DescribeAppBlocks_ResponseSyntax"></a>

```
{
   "AppBlocks": [
      {
         "AppBlockErrors": [
            {
               "ErrorCode": "string",
               "ErrorMessage": "string"
            }
         ],
         "Arn": "string",
         "CreatedTime": number,
         "Description": "string",
         "DisplayName": "string",
         "Name": "string",
         "PackagingType": "string",
         "PostSetupScriptDetails": {
            "ExecutableParameters": "string",
            "ExecutablePath": "string",
            "ScriptS3Location": {
               "S3Bucket": "string",
               "S3Key": "string"
            },
            "TimeoutInSeconds": number
         },
         "SetupScriptDetails": {
            "ExecutableParameters": "string",
            "ExecutablePath": "string",
            "ScriptS3Location": {
               "S3Bucket": "string",
               "S3Key": "string"
            },
            "TimeoutInSeconds": number
         },
         "SourceS3Location": {
            "S3Bucket": "string",
            "S3Key": "string"
         },
         "State": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeAppBlocks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AppBlocks](#API_DescribeAppBlocks_ResponseSyntax) **   <a name="WorkSpacesApplications-DescribeAppBlocks-response-AppBlocks"></a>
The app blocks in the list.
Type: Array of [AppBlock](API_AppBlock.md) objects

 ** [NextToken](#API_DescribeAppBlocks_ResponseSyntax) **   <a name="WorkSpacesApplications-DescribeAppBlocks-response-NextToken"></a>
The pagination token used to retrieve the next page of results for this operation.
Type: String
Length Constraints: Minimum length of 1.

## Errors
<a name="API_DescribeAppBlocks_Errors"></a>

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
<a name="API_DescribeAppBlocks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appstream-2016-12-01/DescribeAppBlocks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appstream-2016-12-01/DescribeAppBlocks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/DescribeAppBlocks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appstream-2016-12-01/DescribeAppBlocks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/DescribeAppBlocks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appstream-2016-12-01/DescribeAppBlocks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appstream-2016-12-01/DescribeAppBlocks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appstream-2016-12-01/DescribeAppBlocks)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/appstream-2016-12-01/DescribeAppBlocks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/DescribeAppBlocks)
