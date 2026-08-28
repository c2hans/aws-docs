---
source_url: https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_ListChannelGroups.html
---

# ListChannelGroups
<a name="API_ListChannelGroups"></a>

Retrieves all channel groups that are configured in AWS Elemental MediaPackage.

## Request Syntax
<a name="API_ListChannelGroups_RequestSyntax"></a>

```
GET /channelGroup?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListChannelGroups_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListChannelGroups_RequestSyntax) **   <a name="mediapackage-ListChannelGroups-request-uri-MaxResults"></a>
The maximum number of results to return in the response.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListChannelGroups_RequestSyntax) **   <a name="mediapackage-ListChannelGroups-request-uri-NextToken"></a>
The pagination token from the GET list request. Use the token to fetch the next page of results.

## Request Body
<a name="API_ListChannelGroups_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListChannelGroups_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Items": [
      {
         "Arn": "string",
         "ChannelGroupName": "string",
         "CreatedAt": number,
         "Description": "string",
         "ModifiedAt": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListChannelGroups_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Items](#API_ListChannelGroups_ResponseSyntax) **   <a name="mediapackage-ListChannelGroups-response-Items"></a>
The objects being returned.
Type: Array of [ChannelGroupListConfiguration](API_ChannelGroupListConfiguration.md) objects

 ** [NextToken](#API_ListChannelGroups_ResponseSyntax) **   <a name="mediapackage-ListChannelGroups-response-NextToken"></a>
The pagination token from the GET list request. Use the token to fetch the next page of results.
Type: String

## Errors
<a name="API_ListChannelGroups_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied because either you don't have permissions to perform the requested operation or MediaPackage is getting throttling errors with CDN authorization. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see Access Management in the IAM User Guide. Or, if you're using CDN authorization, you will receive this exception if MediaPackage receives a throttling error from Secrets Manager.
HTTP Status Code: 403

 ** InternalServerException **
Indicates that an error from the service occurred while trying to process a request.
HTTP Status Code: 500

 ** ThrottlingException **
The request throughput limit was exceeded.
HTTP Status Code: 429

 ** ValidationException **
The input failed to meet the constraints specified by the AWS service.
 ** ValidationExceptionType **
The type of ValidationException.
HTTP Status Code: 400

## See Also
<a name="API_ListChannelGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediapackagev2-2022-12-25/ListChannelGroups)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediapackagev2-2022-12-25/ListChannelGroups)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediapackagev2-2022-12-25/ListChannelGroups)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediapackagev2-2022-12-25/ListChannelGroups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediapackagev2-2022-12-25/ListChannelGroups)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediapackagev2-2022-12-25/ListChannelGroups)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediapackagev2-2022-12-25/ListChannelGroups)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediapackagev2-2022-12-25/ListChannelGroups)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mediapackagev2-2022-12-25/ListChannelGroups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediapackagev2-2022-12-25/ListChannelGroups)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V2 Live API. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
