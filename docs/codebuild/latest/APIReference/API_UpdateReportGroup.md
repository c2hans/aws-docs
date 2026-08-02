---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_UpdateReportGroup.html
---

# UpdateReportGroup
<a name="API_UpdateReportGroup"></a>

 Updates a report group.

## Request Syntax
<a name="API_UpdateReportGroup_RequestSyntax"></a>

```
{
   "arn": "{{string}}",
   "exportConfig": {
      "exportConfigType": "{{string}}",
      "s3Destination": {
         "bucket": "{{string}}",
         "bucketOwner": "{{string}}",
         "encryptionDisabled": {{boolean}},
         "encryptionKey": "{{string}}",
         "packaging": "{{string}}",
         "path": "{{string}}"
      }
   },
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_UpdateReportGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [arn](#API_UpdateReportGroup_RequestSyntax) **   <a name="CodeBuild-UpdateReportGroup-request-arn"></a>
 The ARN of the report group to update.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** [exportConfig](#API_UpdateReportGroup_RequestSyntax) **   <a name="CodeBuild-UpdateReportGroup-request-exportConfig"></a>
 Used to specify an updated export type. Valid values are:
+  `S3`: The report results are exported to an S3 bucket.
+  `NO_EXPORT`: The report results are not exported.
Type: [ReportExportConfig](API_ReportExportConfig.md) object
Required: No

 ** [tags](#API_UpdateReportGroup_RequestSyntax) **   <a name="CodeBuild-UpdateReportGroup-request-tags"></a>
 An updated list of tag key and value pairs associated with this report group.
These tags are available for use by AWS services that support AWS CodeBuild report group tags.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_UpdateReportGroup_ResponseSyntax"></a>

```
{
   "reportGroup": {
      "arn": "string",
      "created": number,
      "exportConfig": {
         "exportConfigType": "string",
         "s3Destination": {
            "bucket": "string",
            "bucketOwner": "string",
            "encryptionDisabled": boolean,
            "encryptionKey": "string",
            "packaging": "string",
            "path": "string"
         }
      },
      "lastModified": number,
      "name": "string",
      "status": "string",
      "tags": [
         {
            "key": "string",
            "value": "string"
         }
      ],
      "type": "string"
   }
}
```

## Response Elements
<a name="API_UpdateReportGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [reportGroup](#API_UpdateReportGroup_ResponseSyntax) **   <a name="CodeBuild-UpdateReportGroup-response-reportGroup"></a>
 Information about the updated report group.
Type: [ReportGroup](API_ReportGroup.md) object

## Errors
<a name="API_UpdateReportGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInputException **
The input value that was provided is not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified AWS resource cannot be found.
HTTP Status Code: 400

## See Also
<a name="API_UpdateReportGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codebuild-2016-10-06/UpdateReportGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codebuild-2016-10-06/UpdateReportGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/UpdateReportGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codebuild-2016-10-06/UpdateReportGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/UpdateReportGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codebuild-2016-10-06/UpdateReportGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codebuild-2016-10-06/UpdateReportGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codebuild-2016-10-06/UpdateReportGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codebuild-2016-10-06/UpdateReportGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/UpdateReportGroup)
