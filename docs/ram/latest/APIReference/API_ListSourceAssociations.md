---
source_url: https://docs.aws.amazon.com/ram/latest/APIReference/API_ListSourceAssociations.html
---

# ListSourceAssociations
<a name="API_ListSourceAssociations"></a>

Lists source associations for resource shares. Source associations control which sources can be used with service principals in resource shares. This operation provides visibility into source associations for resource share owners.

You can filter the results by resource share Amazon Resource Name (ARN), source ID, source type, or association status. We recommend using pagination to ensure that the operation returns quickly and successfully.

## Request Syntax
<a name="API_ListSourceAssociations_RequestSyntax"></a>

```
POST /listsourceassociations HTTP/1.1
Content-type: application/json

{
   "associationStatus": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "resourceShareArns": [ "{{string}}" ],
   "sourceId": "{{string}}",
   "sourceType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListSourceAssociations_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListSourceAssociations_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [associationStatus](#API_ListSourceAssociations_RequestSyntax) **   <a name="ram-ListSourceAssociations-request-associationStatus"></a>
The status of the source associations that you want to retrieve.
Type: String
Valid Values: `ASSOCIATING | ASSOCIATED | FAILED | DISASSOCIATING | DISASSOCIATED | SUSPENDED | SUSPENDING | RESTORING`
Required: No

 ** [maxResults](#API_ListSourceAssociations_RequestSyntax) **   <a name="ram-ListSourceAssociations-request-maxResults"></a>
The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned `nextToken` value.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 500.
Required: No

 ** [nextToken](#API_ListSourceAssociations_RequestSyntax) **   <a name="ram-ListSourceAssociations-request-nextToken"></a>
The pagination token that indicates the next set of results to retrieve.
Type: String
Required: No

 ** [resourceShareArns](#API_ListSourceAssociations_RequestSyntax) **   <a name="ram-ListSourceAssociations-request-resourceShareArns"></a>
The Amazon Resource Names (ARNs) of the resource shares for which you want to retrieve source associations.
Type: Array of strings
Required: No

 ** [sourceId](#API_ListSourceAssociations_RequestSyntax) **   <a name="ram-ListSourceAssociations-request-sourceId"></a>
The identifier of the source for which you want to retrieve associations. This can be an account ID, Amazon Resource Name (ARN), organization ID, or organization path.
Type: String
Required: No

 ** [sourceType](#API_ListSourceAssociations_RequestSyntax) **   <a name="ram-ListSourceAssociations-request-sourceType"></a>
The type of source for which you want to retrieve associations.
Type: String
Required: No

## Response Syntax
<a name="API_ListSourceAssociations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "sourceAssociations": [
      {
         "creationTime": number,
         "lastUpdatedTime": number,
         "resourceShareArn": "string",
         "sourceId": "string",
         "sourceType": "string",
         "status": "string",
         "statusMessage": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListSourceAssociations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListSourceAssociations_ResponseSyntax) **   <a name="ram-ListSourceAssociations-response-nextToken"></a>
The pagination token to use to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

 ** [sourceAssociations](#API_ListSourceAssociations_ResponseSyntax) **   <a name="ram-ListSourceAssociations-response-sourceAssociations"></a>
Information about the source associations.
Type: Array of [AssociatedSource](API_AssociatedSource.md) objects

## Errors
<a name="API_ListSourceAssociations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidNextTokenException **
The operation failed because the specified value for `NextToken` isn't valid. You must specify a value you received in the `NextToken` response of a previous call to this operation.
HTTP Status Code: 400

 ** InvalidParameterException **
The operation failed because a parameter you specified isn't valid.
HTTP Status Code: 400

 ** MalformedArnException **
The operation failed because the specified [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) has a format that isn't valid.
HTTP Status Code: 400

 ** ServerInternalException **
The operation failed because the service could not respond to the request due to an internal problem. Try again later.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The operation failed because the service isn't available. Try again later.
HTTP Status Code: 503

 ** UnknownResourceException **
The operation failed because a specified resource couldn't be found.
HTTP Status Code: 400

## See Also
<a name="API_ListSourceAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ram-2018-01-04/ListSourceAssociations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ram-2018-01-04/ListSourceAssociations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ram-2018-01-04/ListSourceAssociations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ram-2018-01-04/ListSourceAssociations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ram-2018-01-04/ListSourceAssociations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ram-2018-01-04/ListSourceAssociations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ram-2018-01-04/ListSourceAssociations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ram-2018-01-04/ListSourceAssociations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ram-2018-01-04/ListSourceAssociations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ram-2018-01-04/ListSourceAssociations)
