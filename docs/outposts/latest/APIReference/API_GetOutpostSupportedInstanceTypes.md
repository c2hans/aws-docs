---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_GetOutpostSupportedInstanceTypes.html
---

# GetOutpostSupportedInstanceTypes
<a name="API_GetOutpostSupportedInstanceTypes"></a>

Gets the instance types that an Outpost can support in `InstanceTypeCapacity`. This will generally include instance types that are not currently configured and therefore cannot be launched with the current Outpost capacity configuration.

## Request Syntax
<a name="API_GetOutpostSupportedInstanceTypes_RequestSyntax"></a>

```
GET /outposts/{{OutpostId}}/supportedInstanceTypes?AssetId={{AssetId}}&MaxResults={{MaxResults}}&NextToken={{NextToken}}&OrderId={{OrderId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetOutpostSupportedInstanceTypes_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AssetId](#API_GetOutpostSupportedInstanceTypes_RequestSyntax) **   <a name="outposts-GetOutpostSupportedInstanceTypes-request-uri-AssetId"></a>
The ID of the Outpost asset. An Outpost asset can be a single server within an Outposts rack or an Outposts server configuration.
Length Constraints: Fixed length of 10.
Pattern: `\d{10}`

 ** [MaxResults](#API_GetOutpostSupportedInstanceTypes_RequestSyntax) **   <a name="outposts-GetOutpostSupportedInstanceTypes-request-uri-MaxResults"></a>
The maximum page size.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [NextToken](#API_GetOutpostSupportedInstanceTypes_RequestSyntax) **   <a name="outposts-GetOutpostSupportedInstanceTypes-request-uri-NextToken"></a>
The pagination token.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^(\d+)##(\S+)$`

 ** [OrderId](#API_GetOutpostSupportedInstanceTypes_RequestSyntax) **   <a name="outposts-GetOutpostSupportedInstanceTypes-request-uri-OrderId"></a>
The ID for the AWS Outposts order.
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `oo-[a-f0-9]{17}$`

 ** [OutpostId](#API_GetOutpostSupportedInstanceTypes_RequestSyntax) **   <a name="outposts-GetOutpostSupportedInstanceTypes-request-uri-OutpostIdentifier"></a>
The ID or ARN of the Outpost.
Length Constraints: Minimum length of 1. Maximum length of 180.
Pattern: `^(arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:outpost/)?op-[a-f0-9]{17}$`
Required: Yes

## Request Body
<a name="API_GetOutpostSupportedInstanceTypes_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetOutpostSupportedInstanceTypes_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "InstanceTypes": [
      {
         "InstanceType": "string",
         "VCPUs": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_GetOutpostSupportedInstanceTypes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [InstanceTypes](#API_GetOutpostSupportedInstanceTypes_ResponseSyntax) **   <a name="outposts-GetOutpostSupportedInstanceTypes-response-InstanceTypes"></a>
Information about the instance types.
Type: Array of [InstanceTypeItem](API_InstanceTypeItem.md) objects

 ** [NextToken](#API_GetOutpostSupportedInstanceTypes_ResponseSyntax) **   <a name="outposts-GetOutpostSupportedInstanceTypes-response-NextToken"></a>
The pagination token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^(\d+)##(\S+)$`

## Errors
<a name="API_GetOutpostSupportedInstanceTypes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have permission to perform this operation.
HTTP Status Code: 403

 ** InternalServerException **
An internal error has occurred.
HTTP Status Code: 500

 ** NotFoundException **
The specified request is not valid.
HTTP Status Code: 404

 ** ValidationException **
A parameter is not valid.
HTTP Status Code: 400

## See Also
<a name="API_GetOutpostSupportedInstanceTypes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/outposts-2019-12-03/GetOutpostSupportedInstanceTypes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/outposts-2019-12-03/GetOutpostSupportedInstanceTypes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/GetOutpostSupportedInstanceTypes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/outposts-2019-12-03/GetOutpostSupportedInstanceTypes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/GetOutpostSupportedInstanceTypes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/outposts-2019-12-03/GetOutpostSupportedInstanceTypes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/outposts-2019-12-03/GetOutpostSupportedInstanceTypes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/outposts-2019-12-03/GetOutpostSupportedInstanceTypes)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/outposts-2019-12-03/GetOutpostSupportedInstanceTypes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/GetOutpostSupportedInstanceTypes)
