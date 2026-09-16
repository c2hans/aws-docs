---
source_url: https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetResources.html
---

# GetResources
<a name="API_GetResources"></a>

Returns all the tagged or previously tagged resources that are located in the specified AWS Region for the account.

Depending on what information you want returned, you can also specify the following:
+  *Filters* that specify what tags and resource types you want returned. The response includes all tags that are associated with the requested resources.
+ Information about compliance with the account's effective tag policy. For more information on tag policies, see [Tag Policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html) in the * AWS Organizations User Guide.*

**Note**
This operation has a rate limit that specifies the maximum number of times you can call it per second. For the current value of this limit, see [Service Quotas for Resource Groups Tagging API](https://docs.aws.amazon.com/tag-editor/latest/userguide/reference.html) in the *Tag Editor Users Guide*.

This operation supports pagination, where the response can be sent in multiple pages. You should check the `PaginationToken` response parameter to determine if there are additional results available to return. Repeat the query, passing the `PaginationToken` response parameter value as an input to the next request until you recieve a `null` value. A null value for `PaginationToken` indicates that there are no more results waiting to be returned.

**Note**
 `GetResources` does not return untagged resources.
To find untagged resources in your account, use AWS Resource Explorer with a query that uses `tag:none`. For more information, see [ Search query syntax reference for Resource Explorer](https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html).

## Request Syntax
<a name="API_GetResources_RequestSyntax"></a>

```
{
   "ExcludeCompliantResources": {{boolean}},
   "IncludeComplianceDetails": {{boolean}},
   "PaginationToken": "{{string}}",
   "ResourceARNList": [ "{{string}}" ],
   "ResourcesPerPage": {{number}},
   "ResourceTypeFilters": [ "{{string}}" ],
   "TagFilters": [
      {
         "Key": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "TagsPerPage": {{number}}
}
```

## Request Parameters
<a name="API_GetResources_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ExcludeCompliantResources](#API_GetResources_RequestSyntax) **   <a name="resourcegrouptagging-GetResources-request-ExcludeCompliantResources"></a>
Specifies whether to exclude resources that are compliant with the tag policy. Set this to `true` if you are interested in retrieving information on noncompliant resources only.
You can use this parameter only if the `IncludeComplianceDetails` parameter is also set to `true`.
Type: Boolean
Required: No

 ** [IncludeComplianceDetails](#API_GetResources_RequestSyntax) **   <a name="resourcegrouptagging-GetResources-request-IncludeComplianceDetails"></a>
Specifies whether to include details regarding the compliance with the effective tag policy. Set this to `true` to determine whether resources are compliant with the tag policy and to get details.
Type: Boolean
Required: No

 ** [PaginationToken](#API_GetResources_RequestSyntax) **   <a name="resourcegrouptagging-GetResources-request-PaginationToken"></a>
Specifies a `PaginationToken` response value from a previous request to indicate that you want the next page of results. Leave this parameter empty in your initial request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\s\S]*`
Required: No

 ** [ResourceARNList](#API_GetResources_RequestSyntax) **   <a name="resourcegrouptagging-GetResources-request-ResourceARNList"></a>
Specifies a list of ARNs of resources for which you want to retrieve tag data.
You can't specify both this parameter and the `ResourceTypeFilters` parameter in the same request. If you do, you get an `Invalid Parameter` exception.
You can't specify both this parameter and the `TagFilters` parameter in the same request. If you do, you get an `Invalid Parameter` exception.
You can't specify both this parameter and any of the pagination parameters (`ResourcesPerPage`, `TagsPerPage`, `PaginationToken`) in the same request. If you do, you get an `Invalid Parameter` exception.
If a resource specified by this parameter doesn't exist, it doesn't generate an error; it simply isn't included in the response.
An ARN (Amazon Resource Name) uniquely identifies a resource. For more information, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `[\s\S]*`
Required: No

 ** [ResourcesPerPage](#API_GetResources_RequestSyntax) **   <a name="resourcegrouptagging-GetResources-request-ResourcesPerPage"></a>
Specifies the maximum number of results to be returned in each page. A query can return fewer than this maximum, even if there are more results still to return. You should always check the `PaginationToken` response value to see if there are more results. You can specify a minimum of 1 and a maximum value of 100.
Type: Integer
Required: No

 ** [ResourceTypeFilters](#API_GetResources_RequestSyntax) **   <a name="resourcegrouptagging-GetResources-request-ResourceTypeFilters"></a>
Specifies the resource types that you want included in the response. The format of each resource type is `service[:resourceType]`. For example, specifying a service of `ec2` returns all Amazon EC2 resources (which includes EC2 instances). Specifying a resource type of `ec2:instance` returns only EC2 instances.
You can't specify both this parameter and the `ResourceArnList` parameter in the same request. If you do, you get an `Invalid Parameter` exception.
The string for each service name and resource type is the same as that embedded in a resource's Amazon Resource Name (ARN).
For the list of services whose resources you can tag using the Resource Groups Tagging API, see [Services that support the Resource Groups Tagging API](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/supported-services.html). If an AWS service isn't listed on that page, you might still be able to tag that service's resources by using that service's native tagging operations instead of using Resource Groups Tagging API operations. All tagged resources, whether the tagging used the Resource Groups Tagging API or not, are returned by the `Get*` operation.
You can specify multiple resource types by using an array. The array can include up to 100 items. Note that the length constraint requirement applies to each resource type filter. For example, the following string would limit the response to only Amazon EC2 instances, Amazon S3 buckets, or any AWS Audit Manager resource:
 `ec2:instance,s3:bucket,auditmanager`
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** [TagFilters](#API_GetResources_RequestSyntax) **   <a name="resourcegrouptagging-GetResources-request-TagFilters"></a>
Specifies a list of TagFilters (keys and values) to restrict the output to only those resources that have tags with the specified keys and, if included, the specified values. Each `TagFilter` must contain a key with values optional. A request can include up to 50 keys, and each key can include up to 20 values.
You can't specify both this parameter and the `ResourceArnList` parameter in the same request. If you do, you get an `Invalid Parameter` exception.
Note the following when deciding how to use TagFilters:
+ If you *don't* specify a `TagFilter`, the response includes all resources that are currently tagged or ever had a tag. Resources that were previously tagged, *but do not currently* have tags, are shown with an empty tag set, like this: `"Tags": []`.
+ If you specify more than one filter in a single request, the response returns only those resources that satisfy all filters.
+ If you specify a filter that contains more than one value for a key, the response returns resources that match *any* of the specified values for that key.
+ If you don't specify a value for a key, the response returns all resources that are tagged with that key, with any or no value.

  For example, for the following filters: `filter1= {key1,{value1}}`, `filter2={key2,{value2,value3,value4}}`, `filter3= {key3}`:
  +  `GetResources({filter1})` returns resources tagged with `key1=value1`
  +  `GetResources({filter2})` returns resources tagged with `key2=value2` or `key2=value3` or `key2=value4`
  +  `GetResources({filter3})` returns resources tagged with any tag with the key `key3`, and with any or no value
  +  `GetResources({filter1,filter2,filter3})` returns resources tagged with `(key1=value1) and (key2=value2 or key2=value3 or key2=value4) and (key3, any or no value)`
Type: Array of [TagFilter](API_TagFilter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [TagsPerPage](#API_GetResources_RequestSyntax) **   <a name="resourcegrouptagging-GetResources-request-TagsPerPage"></a>
 AWS recommends using `ResourcesPerPage` instead of this parameter.
A limit that restricts the number of tags (key and value pairs) returned by `GetResources` in paginated output. A resource with no tags is counted as having one tag (one key and value pair).
 `GetResources` does not split a resource and its associated tags across pages. If the specified `TagsPerPage` would cause such a break, a `PaginationToken` is returned in place of the affected resource and its tags. Use that token in another request to get the remaining data. For example, if you specify a `TagsPerPage` of `100` and the account has 22 resources with 10 tags each (meaning that each resource has 10 key and value pairs), the output will consist of three pages. The first page displays the first 10 resources, each with its 10 tags. The second page displays the next 10 resources, each with its 10 tags. The third page displays the remaining 2 resources, each with its 10 tags.
You can set `TagsPerPage` to a minimum of 100 items up to a maximum of 500 items.
Type: Integer
Required: No

## Response Syntax
<a name="API_GetResources_ResponseSyntax"></a>

```
{
   "PaginationToken": "string",
   "ResourceTagMappingList": [
      {
         "ComplianceDetails": {
            "ComplianceStatus": boolean,
            "KeysWithNoncompliantValues": [ "string" ],
            "MissingTagKeys": [ "string" ],
            "NoncompliantKeys": [ "string" ]
         },
         "ResourceARN": "string",
         "Tags": [
            {
               "Key": "string",
               "Value": "string"
            }
         ]
      }
   ]
}
```

## Response Elements
<a name="API_GetResources_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PaginationToken](#API_GetResources_ResponseSyntax) **   <a name="resourcegrouptagging-GetResources-response-PaginationToken"></a>
A string that indicates that there is more data available than this response contains. To receive the next part of the response, specify this response value as the `PaginationToken` value in the request for the next page.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\s\S]*`

 ** [ResourceTagMappingList](#API_GetResources_ResponseSyntax) **   <a name="resourcegrouptagging-GetResources-response-ResourceTagMappingList"></a>
A list of resource ARNs and the tags (keys and values) associated with each.
Type: Array of [ResourceTagMapping](API_ResourceTagMapping.md) objects

## Errors
<a name="API_GetResources_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
The request processing failed because of an unknown error, exception, or failure. You can retry the request.
HTTP Status Code: 500

 ** InvalidParameterException **
The request failed because of one of the following reasons:
+ A required parameter is missing.
+ A provided string parameter is malformed.
+ An provided parameter value is out of range.
+ The target ID is invalid, unsupported, or doesn't exist.
+ You can't access the Amazon S3 bucket for report storage. For more information, see [Amazon S3 bucket policy for report storage](https://docs.aws.amazon.com/tag-editor/latest/userguide/tag-policies-orgs.html#bucket-policy) in the *Tagging AWS resources and Tag Editor* user guide.
+ The partition specified in an ARN parameter in the request doesn't match the partition where you invoked the operation. The partition is specified by the second field of the ARN.
HTTP Status Code: 400

 ** PaginationTokenExpiredException **
The request failed because the specified `PaginationToken` has expired. A `PaginationToken` is valid for a maximum of 15 minutes.
HTTP Status Code: 400

 ** ThrottledException **
The request failed because it exceeded the allowed frequency of submitted requests.
HTTP Status Code: 400

## Examples
<a name="API_GetResources_Examples"></a>

### Example
<a name="API_GetResources_Example_1"></a>

This example illustrates one usage of GetResources.

#### Sample Request
<a name="API_GetResources_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: tagging.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 80
X-Amz-Target: ResourceGroupsTaggingAPI_20170126.GetResources
X-Amz-Date: 20191201T214524Z
User-Agent: aws-cli/1.11.79 Python/2.7.9 Windows/7 botocore/1.5.42
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
    "ExcludeCompliantResources": null,
    "IncludeComplianceDetails": true,
    "PaginationToken": 1
}
```

#### Sample Response
<a name="API_GetResources_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 14bc735b-26da-11e7-a933-67e2d2f3ef37
Content-Type: application/x-amz-json-1.1
Content-Length: 4060
Date: Sun, 1 Dec 2019 21:45:25 GMT
{
    "PaginationToken": "",
    "ResourceTagMappingList": [
        {
            "ComplianceDetails": {
                "ComplianceStatus":true,
                "KeysWithNoncompliantValues":[],
                "NoncompliantKeys":[]
            },
            "ResourceARN": "arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX/template/0-7sbz2Kz0",
            "Tags": []
        }
    ]
}
```

## See Also
<a name="API_GetResources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resourcegroupstaggingapi-2017-01-26/GetResources)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resourcegroupstaggingapi-2017-01-26/GetResources)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resourcegroupstaggingapi-2017-01-26/GetResources)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resourcegroupstaggingapi-2017-01-26/GetResources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resourcegroupstaggingapi-2017-01-26/GetResources)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resourcegroupstaggingapi-2017-01-26/GetResources)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resourcegroupstaggingapi-2017-01-26/GetResources)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resourcegroupstaggingapi-2017-01-26/GetResources)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/resourcegroupstaggingapi-2017-01-26/GetResources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resourcegroupstaggingapi-2017-01-26/GetResources)
