---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_ListOrderableInstanceTypes.html
---

# ListOrderableInstanceTypes
<a name="API_ListOrderableInstanceTypes"></a>

Lists the instance types that can be ordered for an Outpost. You can filter the results by Outpost generation.

## Request Syntax
<a name="API_ListOrderableInstanceTypes_RequestSyntax"></a>

```
GET /instanceTypes?MaxResults={{MaxResults}}&NextToken={{NextToken}}&OutpostGenerationFilter={{OutpostGenerationFilter}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListOrderableInstanceTypes_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListOrderableInstanceTypes_RequestSyntax) **   <a name="outposts-ListOrderableInstanceTypes-request-uri-MaxResults"></a>
The maximum page size.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [NextToken](#API_ListOrderableInstanceTypes_RequestSyntax) **   <a name="outposts-ListOrderableInstanceTypes-request-uri-NextToken"></a>
The pagination token.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^(\d+)##(\S+)$`

 ** [OutpostGenerationFilter](#API_ListOrderableInstanceTypes_RequestSyntax) **   <a name="outposts-ListOrderableInstanceTypes-request-uri-OutpostGenerationFilter"></a>
Filters the results by Outpost generation. Specify `GENERATION_1` for first-generation rack deployments or `GENERATION_2` for second-generation rack deployments.
Valid Values: `GENERATION_2 | GENERATION_1`

## Request Body
<a name="API_ListOrderableInstanceTypes_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListOrderableInstanceTypes_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "InstanceTypes": [
      {
         "FormFactorConfigs": [
            {
               "FormFactor": "string",
               "OutpostGeneration": "string"
            }
         ],
         "InstanceType": "string",
         "MemoryInMib": number,
         "NetworkPerformance": "string",
         "VCPUs": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListOrderableInstanceTypes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [InstanceTypes](#API_ListOrderableInstanceTypes_ResponseSyntax) **   <a name="outposts-ListOrderableInstanceTypes-response-InstanceTypes"></a>
Information about the instance types that can be ordered for the Outpost.
Type: Array of [DetailedInstanceTypeItem](API_DetailedInstanceTypeItem.md) objects

 ** [NextToken](#API_ListOrderableInstanceTypes_ResponseSyntax) **   <a name="outposts-ListOrderableInstanceTypes-response-NextToken"></a>
The pagination token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^(\d+)##(\S+)$`

## Errors
<a name="API_ListOrderableInstanceTypes_Errors"></a>

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
<a name="API_ListOrderableInstanceTypes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/outposts-2019-12-03/ListOrderableInstanceTypes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/outposts-2019-12-03/ListOrderableInstanceTypes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/ListOrderableInstanceTypes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/outposts-2019-12-03/ListOrderableInstanceTypes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/ListOrderableInstanceTypes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/outposts-2019-12-03/ListOrderableInstanceTypes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/outposts-2019-12-03/ListOrderableInstanceTypes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/outposts-2019-12-03/ListOrderableInstanceTypes)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/outposts-2019-12-03/ListOrderableInstanceTypes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/ListOrderableInstanceTypes)
