---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ListAssociatedContacts.html
---

# ListAssociatedContacts
<a name="API_ListAssociatedContacts"></a>

Provides information about contact tree, a list of associated contacts with a unique identifier.

## Request Syntax
<a name="API_ListAssociatedContacts_RequestSyntax"></a>

```
GET /contact/associated/{{InstanceId}}?contactId={{ContactId}}&maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAssociatedContacts_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ContactId](#API_ListAssociatedContacts_RequestSyntax) **   <a name="connect-ListAssociatedContacts-request-uri-ContactId"></a>
The identifier of the contact in this instance of Connect Customer.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [InstanceId](#API_ListAssociatedContacts_RequestSyntax) **   <a name="connect-ListAssociatedContacts-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [MaxResults](#API_ListAssociatedContacts_RequestSyntax) **   <a name="connect-ListAssociatedContacts-request-uri-MaxResults"></a>
The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListAssociatedContacts_RequestSyntax) **   <a name="connect-ListAssociatedContacts-request-uri-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.

## Request Body
<a name="API_ListAssociatedContacts_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAssociatedContacts_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ContactSummaryList": [
      {
         "Channel": "string",
         "ContactArn": "string",
         "ContactId": "string",
         "DisconnectTimestamp": number,
         "InitialContactId": "string",
         "InitiationMethod": "string",
         "InitiationTimestamp": number,
         "PreviousContactId": "string",
         "RelatedContactId": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListAssociatedContacts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContactSummaryList](#API_ListAssociatedContacts_ResponseSyntax) **   <a name="connect-ListAssociatedContacts-response-ContactSummaryList"></a>
List of the contact summary for all the contacts in contact tree associated with unique identifier.
Type: Array of [AssociatedContactSummary](API_AssociatedContactSummary.md) objects

 ** [NextToken](#API_ListAssociatedContacts_ResponseSyntax) **   <a name="connect-ListAssociatedContacts-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String

## Errors
<a name="API_ListAssociatedContacts_Errors"></a>

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
<a name="API_ListAssociatedContacts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/ListAssociatedContacts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/ListAssociatedContacts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ListAssociatedContacts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/ListAssociatedContacts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ListAssociatedContacts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/ListAssociatedContacts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/ListAssociatedContacts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/ListAssociatedContacts)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/ListAssociatedContacts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ListAssociatedContacts)
