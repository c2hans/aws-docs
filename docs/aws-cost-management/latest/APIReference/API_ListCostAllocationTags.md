---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ListCostAllocationTags.html
---

# ListCostAllocationTags
<a name="API_ListCostAllocationTags"></a>

Get a list of cost allocation tags. All inputs in the API are optional and serve as filters. By default, all cost allocation tags are returned.

## Request Syntax
<a name="API_ListCostAllocationTags_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "Status": "{{string}}",
   "TagKeys": [ "{{string}}" ],
   "Type": "{{string}}"
}
```

## Request Parameters
<a name="API_ListCostAllocationTags_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListCostAllocationTags_RequestSyntax) **   <a name="awscostmanagement-ListCostAllocationTags-request-MaxResults"></a>
The maximum number of objects that are returned for this request. By default, the request returns 100 results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_ListCostAllocationTags_RequestSyntax) **   <a name="awscostmanagement-ListCostAllocationTags-request-NextToken"></a>
The token to retrieve the next set of results. AWS provides the token when the response from a previous call has more results than the maximum page size.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[\S\s]*`
Required: No

 ** [Status](#API_ListCostAllocationTags_RequestSyntax) **   <a name="awscostmanagement-ListCostAllocationTags-request-Status"></a>
The status of cost allocation tag keys that are returned for this request.
Type: String
Valid Values: `Active | Inactive`
Required: No

 ** [TagKeys](#API_ListCostAllocationTags_RequestSyntax) **   <a name="awscostmanagement-ListCostAllocationTags-request-TagKeys"></a>
The list of cost allocation tag keys that are returned for this request.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** [Type](#API_ListCostAllocationTags_RequestSyntax) **   <a name="awscostmanagement-ListCostAllocationTags-request-Type"></a>
The type of `CostAllocationTag` object that are returned for this request. The `AWSGenerated` type tags are tags that AWS defines and applies to support AWS resources for cost allocation purposes. The `UserDefined` type tags are tags that you define, create, and apply to resources.
Type: String
Valid Values: `AWSGenerated | UserDefined`
Required: No

## Response Syntax
<a name="API_ListCostAllocationTags_ResponseSyntax"></a>

```
{
   "CostAllocationTags": [
      {
         "LastUpdatedDate": "string",
         "LastUsedDate": "string",
         "Status": "string",
         "TagKey": "string",
         "Type": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListCostAllocationTags_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CostAllocationTags](#API_ListCostAllocationTags_ResponseSyntax) **   <a name="awscostmanagement-ListCostAllocationTags-response-CostAllocationTags"></a>
A list of cost allocation tags that includes the detailed metadata for each one.
Type: Array of [CostAllocationTag](API_CostAllocationTag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [NextToken](#API_ListCostAllocationTags_ResponseSyntax) **   <a name="awscostmanagement-ListCostAllocationTags-response-NextToken"></a>
The token to retrieve the next set of results. AWS provides the token when the response from a previous call has more results than the maximum page size.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[\S\s]*`

## Errors
<a name="API_ListCostAllocationTags_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidNextTokenException **
The pagination token is invalid. Try again without a pagination token.
HTTP Status Code: 400

 ** LimitExceededException **
You made too many calls in a short period of time. Try again later.
HTTP Status Code: 400

## Examples
<a name="API_ListCostAllocationTags_Examples"></a>

The following are sample requests and responses of the `ListCostAllocationTags` operations.

### Example 1: List all user defined active tags
<a name="API_ListCostAllocationTags_Example_1"></a>

This example illustrates one usage of ListCostAllocationTags.

#### Sample Request
<a name="API_ListCostAllocationTags_Example_1_Request"></a>

```
{
    "Type": "UserDefined",
    "Status": "Active"
}
```

#### Sample Response
<a name="API_ListCostAllocationTags_Example_1_Response"></a>

```
{
    "CostAllocationTags": [
        {
            "TagKey": "tagA",
            "Type": "UserDefined",
            "Status": "Active"
        }
    ],
    "NextToken": null
}
```

### Example 2: List all tags by tag keys
<a name="API_ListCostAllocationTags_Example_2"></a>

This example illustrates one usage of ListCostAllocationTags.

#### Sample Request
<a name="API_ListCostAllocationTags_Example_2_Request"></a>

```
{
    "TagKeys": ["tagA", "tagB"]
}
```

#### Sample Response
<a name="API_ListCostAllocationTags_Example_2_Response"></a>

```
{
    "CostAllocationTags": [
        {
            "TagKey": "tagA",
            "Type": "UserDefined",
            "Status": "Active"
        },
        {
            "TagKey": "tagB",
            "Type": "UserDefined",
            "Status": "Inactive"
        }
    ],
    "NextToken": null
}
```

## See Also
<a name="API_ListCostAllocationTags_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ce-2017-10-25/ListCostAllocationTags)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ce-2017-10-25/ListCostAllocationTags)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/ListCostAllocationTags)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ce-2017-10-25/ListCostAllocationTags)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/ListCostAllocationTags)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ce-2017-10-25/ListCostAllocationTags)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ce-2017-10-25/ListCostAllocationTags)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ce-2017-10-25/ListCostAllocationTags)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ce-2017-10-25/ListCostAllocationTags)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/ListCostAllocationTags)
