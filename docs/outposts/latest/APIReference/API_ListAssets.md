---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_ListAssets.html
---

# ListAssets
<a name="API_ListAssets"></a>

Lists the hardware assets for the specified Outpost.

Use filters to return specific results. If you specify multiple filters, the results include only the resources that match all of the specified filters. For a filter where you can specify multiple values, the results include items that match any of the values that you specify for the filter.

## Request Syntax
<a name="API_ListAssets_RequestSyntax"></a>

```
GET /outposts/{{OutpostId}}/assets?AssetTypeFilter={{AssetTypeFilter}}&HostIdFilter={{HostIdFilter}}&MaxResults={{MaxResults}}&NextToken={{NextToken}}&StatusFilter={{StatusFilter}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAssets_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AssetTypeFilter](#API_ListAssets_RequestSyntax) **   <a name="outposts-ListAssets-request-uri-AssetTypeFilter"></a>
Filters the results by asset type.
+ COMPUTE - Server asset used for customer compute
+ STORAGE - Server asset used by storage services
+ POWERSHELF - Powershelf assets
+ SWITCH - Switch assets
+ NETWORKING - Asset managed by AWS for networking purposes
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Valid Values: `COMPUTE | STORAGE | POWERSHELF | SWITCH | NETWORKING`

 ** [HostIdFilter](#API_ListAssets_RequestSyntax) **   <a name="outposts-ListAssets-request-uri-HostIdFilter"></a>
Filters the results by the host ID of a Dedicated Host.
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `^[A-Za-z0-9-]*$`

 ** [MaxResults](#API_ListAssets_RequestSyntax) **   <a name="outposts-ListAssets-request-uri-MaxResults"></a>
The maximum page size.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [NextToken](#API_ListAssets_RequestSyntax) **   <a name="outposts-ListAssets-request-uri-NextToken"></a>
The pagination token.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^(\d+)##(\S+)$`

 ** [OutpostId](#API_ListAssets_RequestSyntax) **   <a name="outposts-ListAssets-request-uri-OutpostIdentifier"></a>
 The ID or the Amazon Resource Name (ARN) of the Outpost.
Length Constraints: Minimum length of 1. Maximum length of 180.
Pattern: `^(arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:outpost/)?op-[a-f0-9]{17}$`
Required: Yes

 ** [StatusFilter](#API_ListAssets_RequestSyntax) **   <a name="outposts-ListAssets-request-uri-StatusFilter"></a>
Filters the results by state.
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Valid Values: `ACTIVE | RETIRING | ISOLATED | INSTALLING`

## Request Body
<a name="API_ListAssets_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAssets_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Assets": [
      {
         "AssetId": "string",
         "AssetLocation": {
            "RackElevation": number
         },
         "AssetType": "string",
         "ComputeAttributes": {
            "HostId": "string",
            "InstanceFamilies": [ "string" ],
            "InstanceTypeCapacities": [
               {
                  "Count": number,
                  "InstanceType": "string"
               }
            ],
            "MaxVcpus": number,
            "State": "string"
         },
         "RackId": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListAssets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Assets](#API_ListAssets_ResponseSyntax) **   <a name="outposts-ListAssets-response-Assets"></a>
Information about the hardware assets.
Type: Array of [AssetInfo](API_AssetInfo.md) objects

 ** [NextToken](#API_ListAssets_ResponseSyntax) **   <a name="outposts-ListAssets-response-NextToken"></a>
The pagination token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^(\d+)##(\S+)$`

## Errors
<a name="API_ListAssets_Errors"></a>

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
<a name="API_ListAssets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/outposts-2019-12-03/ListAssets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/outposts-2019-12-03/ListAssets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/ListAssets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/outposts-2019-12-03/ListAssets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/ListAssets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/outposts-2019-12-03/ListAssets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/outposts-2019-12-03/ListAssets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/outposts-2019-12-03/ListAssets)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/outposts-2019-12-03/ListAssets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/ListAssets)
