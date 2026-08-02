---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ListQueueEmailAddresses.html
---

# ListQueueEmailAddresses
<a name="API_ListQueueEmailAddresses"></a>

Lists all email addresses that are currently associated with a specific queue, providing details about which "From" email addresses agents can select when handling email contacts. This helps administrators manage agent email address options and understand the available choices for different brands and business units.

 **Important things to know**
+ The response includes metadata about each email address available for agent selection, including whether it's configured as the default outbound email.
+ Agents can select from these email addresses when replying to inbound contacts or initiating outbound contacts in this queue.
+ The list includes both explicitly associated email addresses and any default outbound email address configured for the queue.
+ Results are paginated to handle queues with many associated email addresses (up to 50 per queue).

## Request Syntax
<a name="API_ListQueueEmailAddresses_RequestSyntax"></a>

```
GET /queues/{{InstanceId}}/{{QueueId}}/email-addresses?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListQueueEmailAddresses_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_ListQueueEmailAddresses_RequestSyntax) **   <a name="connect-ListQueueEmailAddresses-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [MaxResults](#API_ListQueueEmailAddresses_RequestSyntax) **   <a name="connect-ListQueueEmailAddresses-request-uri-MaxResults"></a>
The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListQueueEmailAddresses_RequestSyntax) **   <a name="connect-ListQueueEmailAddresses-request-uri-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.

 ** [QueueId](#API_ListQueueEmailAddresses_RequestSyntax) **   <a name="connect-ListQueueEmailAddresses-request-uri-QueueId"></a>
The identifier for the queue.
Required: Yes

## Request Body
<a name="API_ListQueueEmailAddresses_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListQueueEmailAddresses_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "EmailAddressMetadataList": [
      {
         "Arn": "string",
         "Id": "string",
         "IsDefaultOutboundEmail": boolean
      }
   ],
   "LastModifiedRegion": "string",
   "LastModifiedTime": number,
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListQueueEmailAddresses_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EmailAddressMetadataList](#API_ListQueueEmailAddresses_ResponseSyntax) **   <a name="connect-ListQueueEmailAddresses-response-EmailAddressMetadataList"></a>
List of email address summary information for all email addresses associated with the queue. Each item contains the email address identifier, ARN, and configuration details.
Type: Array of [EmailAddressSummary](API_EmailAddressSummary.md) objects

 ** [LastModifiedRegion](#API_ListQueueEmailAddresses_ResponseSyntax) **   <a name="connect-ListQueueEmailAddresses-response-LastModifiedRegion"></a>
The AWS Region where this resource was last modified.
Type: String
Pattern: `[a-z]{2}(-[a-z]+){1,2}(-[0-9])?`

 ** [LastModifiedTime](#API_ListQueueEmailAddresses_ResponseSyntax) **   <a name="connect-ListQueueEmailAddresses-response-LastModifiedTime"></a>
The timestamp when this resource was last modified.
Type: Timestamp

 ** [NextToken](#API_ListQueueEmailAddresses_ResponseSyntax) **   <a name="connect-ListQueueEmailAddresses-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String

## Errors
<a name="API_ListQueueEmailAddresses_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_ListQueueEmailAddresses_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/ListQueueEmailAddresses)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/ListQueueEmailAddresses)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ListQueueEmailAddresses)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/ListQueueEmailAddresses)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ListQueueEmailAddresses)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/ListQueueEmailAddresses)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/ListQueueEmailAddresses)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/ListQueueEmailAddresses)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/ListQueueEmailAddresses)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ListQueueEmailAddresses)
