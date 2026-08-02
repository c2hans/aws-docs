---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ListSourcesForS3TableIntegration.html
---

# ListSourcesForS3TableIntegration
<a name="API_ListSourcesForS3TableIntegration"></a>

Returns a list of data source associations for a specified S3 Table Integration, showing which data sources are currently associated for query access.

## Request Syntax
<a name="API_ListSourcesForS3TableIntegration_RequestSyntax"></a>

```
{
   "integrationArn": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListSourcesForS3TableIntegration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [integrationArn](#API_ListSourcesForS3TableIntegration_RequestSyntax) **   <a name="CWL-ListSourcesForS3TableIntegration-request-integrationArn"></a>
The Amazon Resource Name (ARN) of the S3 Table Integration to list associations for.
Type: String
Required: Yes

 ** [maxResults](#API_ListSourcesForS3TableIntegration_RequestSyntax) **   <a name="CWL-ListSourcesForS3TableIntegration-request-maxResults"></a>
The maximum number of associations to return in a single call. Valid range is 1 to 100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListSourcesForS3TableIntegration_RequestSyntax) **   <a name="CWL-ListSourcesForS3TableIntegration-request-nextToken"></a>
The token for the next set of items to return. The token expires after 24 hours.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## Response Syntax
<a name="API_ListSourcesForS3TableIntegration_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "sources": [
      {
         "createdTimeStamp": number,
         "dataSource": {
            "name": "string",
            "type": "string"
         },
         "identifier": "string",
         "parentSourceIdentifier": "string",
         "status": "string",
         "statusReason": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListSourcesForS3TableIntegration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListSourcesForS3TableIntegration_ResponseSyntax) **   <a name="CWL-ListSourcesForS3TableIntegration-response-nextToken"></a>
The token for the next set of items to return. The token expires after 24 hours.
Type: String
Length Constraints: Minimum length of 1.

 ** [sources](#API_ListSourcesForS3TableIntegration_ResponseSyntax) **   <a name="CWL-ListSourcesForS3TableIntegration-response-sources"></a>
The list of data source associations for the specified S3 Table Integration.
Type: Array of [S3TableIntegrationSource](API_S3TableIntegrationSource.md) objects

## Errors
<a name="API_ListSourcesForS3TableIntegration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permissions to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
An internal server error occurred while processing the request. This exception is returned when the service encounters an unexpected condition that prevents it from fulfilling the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 400

 ** ThrottlingException **
The request was throttled because of quota limits.
HTTP Status Code: 400

 ** ValidationException **
One of the parameters for the request is not valid.
HTTP Status Code: 400

## See Also
<a name="API_ListSourcesForS3TableIntegration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/ListSourcesForS3TableIntegration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/ListSourcesForS3TableIntegration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/ListSourcesForS3TableIntegration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/ListSourcesForS3TableIntegration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/ListSourcesForS3TableIntegration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/ListSourcesForS3TableIntegration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/ListSourcesForS3TableIntegration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/ListSourcesForS3TableIntegration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/ListSourcesForS3TableIntegration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/ListSourcesForS3TableIntegration)
