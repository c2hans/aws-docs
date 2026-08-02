---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ListPredefinedAttributes.html
---

# ListPredefinedAttributes
<a name="API_ListPredefinedAttributes"></a>

Lists predefined attributes for the specified Connect Customer instance. A *predefined attribute* is made up of a name and a value. You can use predefined attributes for:
+ Routing proficiency (for example, agent certification) that has predefined values (for example, a list of possible certifications). For more information, see [Create predefined attributes for routing contacts to agents](https://docs.aws.amazon.com/connect/latest/adminguide/predefined-attributes.html).
+ Contact information that varies between transfers or conferences, such as the name of the business unit handling the contact. For more information, see [Use contact segment attributes](https://docs.aws.amazon.com/connect/latest/adminguide/use-contact-segment-attributes.html).

For the predefined attributes per instance quota, see [Connect Customer quotas](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html#connect-quotas).

 **Endpoints**: See [Connect Customer endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/connect_region.html).

## Request Syntax
<a name="API_ListPredefinedAttributes_RequestSyntax"></a>

```
GET /predefined-attributes/{{InstanceId}}?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListPredefinedAttributes_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_ListPredefinedAttributes_RequestSyntax) **   <a name="connect-ListPredefinedAttributes-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can find the instance ID in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [MaxResults](#API_ListPredefinedAttributes_RequestSyntax) **   <a name="connect-ListPredefinedAttributes-request-uri-MaxResults"></a>
The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListPredefinedAttributes_RequestSyntax) **   <a name="connect-ListPredefinedAttributes-request-uri-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.

## Request Body
<a name="API_ListPredefinedAttributes_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListPredefinedAttributes_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "PredefinedAttributeSummaryList": [
      {
         "LastModifiedRegion": "string",
         "LastModifiedTime": number,
         "Name": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListPredefinedAttributes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListPredefinedAttributes_ResponseSyntax) **   <a name="connect-ListPredefinedAttributes-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String

 ** [PredefinedAttributeSummaryList](#API_ListPredefinedAttributes_ResponseSyntax) **   <a name="connect-ListPredefinedAttributes-response-PredefinedAttributeSummaryList"></a>
Summary of the predefined attributes.
Type: Array of [PredefinedAttributeSummary](API_PredefinedAttributeSummary.md) objects

## Errors
<a name="API_ListPredefinedAttributes_Errors"></a>

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

## Examples
<a name="API_ListPredefinedAttributes_Examples"></a>

### Example
<a name="API_ListPredefinedAttributes_Example_1"></a>

The following example shows a request and response.

```
GET https://connect.us-west-2.amazonaws.com/predefined-attributes/InstanceId?maxResults=MaxResults&nextToken=NextToken HTTP/1.1

Response:
{
    "NextToken": null,
    "PredefinedAttributeSummaryList": [
        {
            "LastModifiedRegion": "us-west-2",
            "LastModifiedTime": 1.75691948693E9,
            "Name": "Name1"
        },
        {
            "LastModifiedRegion": "us-west-2",
            "LastModifiedTime": 1.756919487004E9,
            "Name": "Name2
    ]
}
```

## See Also
<a name="API_ListPredefinedAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/ListPredefinedAttributes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/ListPredefinedAttributes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ListPredefinedAttributes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/ListPredefinedAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ListPredefinedAttributes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/ListPredefinedAttributes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/ListPredefinedAttributes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/ListPredefinedAttributes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/ListPredefinedAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ListPredefinedAttributes)
