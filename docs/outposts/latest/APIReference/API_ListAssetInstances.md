---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_ListAssetInstances.html
---

# ListAssetInstances
<a name="API_ListAssetInstances"></a>

A list of Amazon EC2 instances, belonging to all accounts, running on the specified Outpost. Does not include Amazon EBS or Amazon S3 instances.

## Request Syntax
<a name="API_ListAssetInstances_RequestSyntax"></a>

```
GET /outposts/{{OutpostId}}/assetInstances?AccountIdFilter={{AccountIdFilter}}&AssetIdFilter={{AssetIdFilter}}&AwsServiceFilter={{AwsServiceFilter}}&InstanceTypeFilter={{InstanceTypeFilter}}&MaxResults={{MaxResults}}&NextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAssetInstances_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AccountIdFilter](#API_ListAssetInstances_RequestSyntax) **   <a name="outposts-ListAssetInstances-request-uri-AccountIdFilter"></a>
Filters the results by account ID.
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`

 ** [AssetIdFilter](#API_ListAssetInstances_RequestSyntax) **   <a name="outposts-ListAssetInstances-request-uri-AssetIdFilter"></a>
Filters the results by asset ID.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^(\w+)$`

 ** [AwsServiceFilter](#API_ListAssetInstances_RequestSyntax) **   <a name="outposts-ListAssetInstances-request-uri-AwsServiceFilter"></a>
Filters the results by AWS service.
Valid Values: `AWS | EC2 | EKS | ELASTICACHE | ELB | RDS | ROUTE53`

 ** [InstanceTypeFilter](#API_ListAssetInstances_RequestSyntax) **   <a name="outposts-ListAssetInstances-request-uri-InstanceTypeFilter"></a>
Filters the results by instance ID.
Length Constraints: Minimum length of 3. Maximum length of 30.
Pattern: `[a-z0-9\-\.]+`

 ** [MaxResults](#API_ListAssetInstances_RequestSyntax) **   <a name="outposts-ListAssetInstances-request-uri-MaxResults"></a>
The maximum page size.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [NextToken](#API_ListAssetInstances_RequestSyntax) **   <a name="outposts-ListAssetInstances-request-uri-NextToken"></a>
The pagination token.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^(\d+)##(\S+)$`

 ** [OutpostId](#API_ListAssetInstances_RequestSyntax) **   <a name="outposts-ListAssetInstances-request-uri-OutpostIdentifier"></a>
The ID of the Outpost.
Length Constraints: Minimum length of 1. Maximum length of 180.
Pattern: `^(arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:outpost/)?op-[a-f0-9]{17}$`
Required: Yes

## Request Body
<a name="API_ListAssetInstances_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAssetInstances_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AssetInstances": [
      {
         "AccountId": "string",
         "AssetId": "string",
         "AwsServiceName": "string",
         "InstanceId": "string",
         "InstanceType": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListAssetInstances_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AssetInstances](#API_ListAssetInstances_ResponseSyntax) **   <a name="outposts-ListAssetInstances-response-AssetInstances"></a>
List of instances owned by all accounts on the Outpost. Does not include Amazon EBS or Amazon S3 instances.
Type: Array of [AssetInstance](API_AssetInstance.md) objects

 ** [NextToken](#API_ListAssetInstances_ResponseSyntax) **   <a name="outposts-ListAssetInstances-response-NextToken"></a>
The pagination token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^(\d+)##(\S+)$`

## Errors
<a name="API_ListAssetInstances_Errors"></a>

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
<a name="API_ListAssetInstances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/outposts-2019-12-03/ListAssetInstances)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/outposts-2019-12-03/ListAssetInstances)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/ListAssetInstances)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/outposts-2019-12-03/ListAssetInstances)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/ListAssetInstances)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/outposts-2019-12-03/ListAssetInstances)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/outposts-2019-12-03/ListAssetInstances)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/outposts-2019-12-03/ListAssetInstances)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/outposts-2019-12-03/ListAssetInstances)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/ListAssetInstances)
