---
source_url: https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_DescribeExportConfigurations.html
---

# DescribeExportConfigurations
<a name="API_DescribeExportConfigurations"></a>

**Important**
 AWS Application Discovery Service is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).

 `DescribeExportConfigurations` is deprecated. Use [DescribeExportTasks](https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_DescribeExportTasks.html), instead.

## Request Syntax
<a name="API_DescribeExportConfigurations_RequestSyntax"></a>

```
{
   "exportIds": [ "{{string}}" ],
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeExportConfigurations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [exportIds](#API_DescribeExportConfigurations_RequestSyntax) **   <a name="DiscServ-DescribeExportConfigurations-request-exportIds"></a>
A list of continuous export IDs to search for.
Type: Array of strings
Length Constraints: Maximum length of 200.
Pattern: `\S*`
Required: No

 ** [maxResults](#API_DescribeExportConfigurations_RequestSyntax) **   <a name="DiscServ-DescribeExportConfigurations-request-maxResults"></a>
A number between 1 and 100 specifying the maximum number of continuous export descriptions returned.
Type: Integer
Required: No

 ** [nextToken](#API_DescribeExportConfigurations_RequestSyntax) **   <a name="DiscServ-DescribeExportConfigurations-request-nextToken"></a>
The token from the previous call to describe-export-tasks.
Type: String
Required: No

## Response Syntax
<a name="API_DescribeExportConfigurations_ResponseSyntax"></a>

```
{
   "exportsInfo": [
      {
         "configurationsDownloadUrl": "string",
         "exportId": "string",
         "exportRequestTime": number,
         "exportStatus": "string",
         "isTruncated": boolean,
         "requestedEndTime": number,
         "requestedStartTime": number,
         "statusMessage": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeExportConfigurations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [exportsInfo](#API_DescribeExportConfigurations_ResponseSyntax) **   <a name="DiscServ-DescribeExportConfigurations-response-exportsInfo"></a>

Type: Array of [ExportInfo](API_ExportInfo.md) objects

 ** [nextToken](#API_DescribeExportConfigurations_ResponseSyntax) **   <a name="DiscServ-DescribeExportConfigurations-response-nextToken"></a>
The token from the previous call to describe-export-tasks.
Type: String

## Errors
<a name="API_DescribeExportConfigurations_Errors"></a>

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

 ** ResourceNotFoundException **
The specified configuration ID was not located. Verify the configuration ID and try again.
HTTP Status Code: 400

 ** ServerInternalErrorException **
The server experienced an internal error. Try again.
HTTP Status Code: 500

## See Also
<a name="API_DescribeExportConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/discovery-2015-11-01/DescribeExportConfigurations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/discovery-2015-11-01/DescribeExportConfigurations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/discovery-2015-11-01/DescribeExportConfigurations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/discovery-2015-11-01/DescribeExportConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/discovery-2015-11-01/DescribeExportConfigurations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/discovery-2015-11-01/DescribeExportConfigurations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/discovery-2015-11-01/DescribeExportConfigurations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/discovery-2015-11-01/DescribeExportConfigurations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/discovery-2015-11-01/DescribeExportConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/discovery-2015-11-01/DescribeExportConfigurations)
