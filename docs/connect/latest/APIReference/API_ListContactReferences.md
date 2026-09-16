---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ListContactReferences.html
---

# ListContactReferences
<a name="API_ListContactReferences"></a>

This API is in preview release for Connect Customer and is subject to change.

For the specified `referenceTypes`, returns a list of references associated with the contact. *References* are links to documents that are related to a contact, such as emails, attachments, or URLs.

## Request Syntax
<a name="API_ListContactReferences_RequestSyntax"></a>

```
GET /contact/references/{{InstanceId}}/{{ContactId}}?nextToken={{NextToken}}&referenceTypes={{ReferenceTypes}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListContactReferences_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ContactId](#API_ListContactReferences_RequestSyntax) **   <a name="connect-ListContactReferences-request-uri-ContactId"></a>
The identifier of the initial contact.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [InstanceId](#API_ListContactReferences_RequestSyntax) **   <a name="connect-ListContactReferences-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [NextToken](#API_ListContactReferences_RequestSyntax) **   <a name="connect-ListContactReferences-request-uri-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
This is not expected to be set, because the value returned in the previous response is always null.

 ** [ReferenceTypes](#API_ListContactReferences_RequestSyntax) **   <a name="connect-ListContactReferences-request-uri-ReferenceTypes"></a>
The type of reference.
Array Members: Maximum number of 6 items.
Valid Values: `URL | ATTACHMENT | CONTACT_ANALYSIS | NUMBER | STRING | DATE | EMAIL | EMAIL_MESSAGE | EMAIL_MESSAGE_PLAIN_TEXT | EMAIL_MESSAGE_PLAIN_TEXT_REDACTED | EMAIL_MESSAGE_REDACTED`
Required: Yes

## Request Body
<a name="API_ListContactReferences_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListContactReferences_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "ReferenceSummaryList": [
      { ... }
   ]
}
```

## Response Elements
<a name="API_ListContactReferences_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListContactReferences_ResponseSyntax) **   <a name="connect-ListContactReferences-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
This is always returned as null in the response.
Type: String

 ** [ReferenceSummaryList](#API_ListContactReferences_ResponseSyntax) **   <a name="connect-ListContactReferences-response-ReferenceSummaryList"></a>
Information about the flows.
Type: Array of [ReferenceSummary](API_ReferenceSummary.md) objects

## Errors
<a name="API_ListContactReferences_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_ListContactReferences_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/ListContactReferences)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/ListContactReferences)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ListContactReferences)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/ListContactReferences)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ListContactReferences)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/ListContactReferences)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/ListContactReferences)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/ListContactReferences)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/ListContactReferences)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ListContactReferences)
