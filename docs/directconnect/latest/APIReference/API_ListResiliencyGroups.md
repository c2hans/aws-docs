---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_ListResiliencyGroups.html
---

# ListResiliencyGroups
<a name="API_ListResiliencyGroups"></a>

Lists the resiliency groups owned by your AWS account in the current AWS Region.

## Request Syntax
<a name="API_ListResiliencyGroups_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListResiliencyGroups_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListResiliencyGroups_RequestSyntax) **   <a name="DX-ListResiliencyGroups-request-maxResults"></a>
The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned `nextToken` value.
If `MaxResults` is given a value larger than 100, only 100 results are returned.
Type: Integer
Required: No

 ** [nextToken](#API_ListResiliencyGroups_RequestSyntax) **   <a name="DX-ListResiliencyGroups-request-nextToken"></a>
The token for the next page of results.
Type: String
Required: No

## Response Syntax
<a name="API_ListResiliencyGroups_ResponseSyntax"></a>

```
{
   "items": [
      {
         "ownerAccount": "string",
         "resiliencyGroupArn": "string",
         "resiliencyGroupId": "string",
         "resiliencyGroupName": "string",
         "resiliencyGroupType": "string",
         "state": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListResiliencyGroups_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListResiliencyGroups_ResponseSyntax) **   <a name="DX-ListResiliencyGroups-response-items"></a>
Summary information about the resiliency groups.
Type: Array of [ResiliencyGroupSummary](API_ResiliencyGroupSummary.md) objects

 ** [nextToken](#API_ListResiliencyGroups_ResponseSyntax) **   <a name="DX-ListResiliencyGroups-response-nextToken"></a>
The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

## Errors
<a name="API_ListResiliencyGroups_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DirectConnectClientException **
One or more parameters are not valid.
HTTP Status Code: 400

 ** DirectConnectServerException **
A server-side error occurred.
HTTP Status Code: 400

## See Also
<a name="API_ListResiliencyGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/directconnect-2012-10-25/ListResiliencyGroups)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/directconnect-2012-10-25/ListResiliencyGroups)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/ListResiliencyGroups)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/directconnect-2012-10-25/ListResiliencyGroups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/ListResiliencyGroups)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/directconnect-2012-10-25/ListResiliencyGroups)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/directconnect-2012-10-25/ListResiliencyGroups)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/directconnect-2012-10-25/ListResiliencyGroups)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/directconnect-2012-10-25/ListResiliencyGroups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/ListResiliencyGroups)
