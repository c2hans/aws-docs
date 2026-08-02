---
source_url: https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetComplianceSummary.html
---

# GetComplianceSummary
<a name="API_GetComplianceSummary"></a>

Returns a table that shows counts of resources that are noncompliant with their tag policies.

For more information on tag policies, see [Tag Policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html) in the * AWS Organizations User Guide.*

You can call this operation only from the organization's management account and from the us-east-1 Region.

This operation supports pagination, where the response can be sent in multiple pages. You should check the `PaginationToken` response parameter to determine if there are additional results available to return. Repeat the query, passing the `PaginationToken` response parameter value as an input to the next request until you recieve a `null` value. A null value for `PaginationToken` indicates that there are no more results waiting to be returned.

## Request Syntax
<a name="API_GetComplianceSummary_RequestSyntax"></a>

```
{
   "GroupBy": [ "{{string}}" ],
   "MaxResults": {{number}},
   "PaginationToken": "{{string}}",
   "RegionFilters": [ "{{string}}" ],
   "ResourceTypeFilters": [ "{{string}}" ],
   "TagKeyFilters": [ "{{string}}" ],
   "TargetIdFilters": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_GetComplianceSummary_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [GroupBy](#API_GetComplianceSummary_RequestSyntax) **   <a name="resourcegrouptagging-GetComplianceSummary-request-GroupBy"></a>
Specifies a list of attributes to group the counts of noncompliant resources by. If supplied, the counts are sorted by those attributes.
Type: Array of strings
Valid Values: `TARGET_ID | REGION | RESOURCE_TYPE`
Required: No

 ** [MaxResults](#API_GetComplianceSummary_RequestSyntax) **   <a name="resourcegrouptagging-GetComplianceSummary-request-MaxResults"></a>
Specifies the maximum number of results to be returned in each page. A query can return fewer than this maximum, even if there are more results still to return. You should always check the `PaginationToken` response value to see if there are more results. You can specify a minimum of 1 and a maximum value of 100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [PaginationToken](#API_GetComplianceSummary_RequestSyntax) **   <a name="resourcegrouptagging-GetComplianceSummary-request-PaginationToken"></a>
Specifies a `PaginationToken` response value from a previous request to indicate that you want the next page of results. Leave this parameter empty in your initial request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\s\S]*`
Required: No

 ** [RegionFilters](#API_GetComplianceSummary_RequestSyntax) **   <a name="resourcegrouptagging-GetComplianceSummary-request-RegionFilters"></a>
Specifies a list of AWS Regions to limit the output to. If you use this parameter, the count of returned noncompliant resources includes only resources in the specified Regions.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** [ResourceTypeFilters](#API_GetComplianceSummary_RequestSyntax) **   <a name="resourcegrouptagging-GetComplianceSummary-request-ResourceTypeFilters"></a>
Specifies that you want the response to include information for only resources of the specified types. The format of each resource type is `service[:resourceType]`. For example, specifying a resource type of `ec2` returns all Amazon EC2 resources (which includes EC2 instances). Specifying a resource type of `ec2:instance` returns only EC2 instances.
The string for each service name and resource type is the same as that embedded in a resource's Amazon Resource Name (ARN). Consult the * [AWS General Reference](https://docs.aws.amazon.com/general/latest/gr/) * for the following:
+ For a list of service name strings, see [AWS Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces).
+ For resource type strings, see [Example ARNs](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arns-syntax).
+ For more information about ARNs, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html).
For the list of services whose resources you can tag using the Resource Groups Tagging API, see [Services that support the Resource Groups Tagging API](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/supported-services.html). If an AWS service isn't listed on that page, you might still be able to tag that service's resources by using that service's native tagging operations instead of using Resource Groups Tagging API operations. All tagged resources, whether the tagging used the Resource Groups Tagging API or not, are returned by the `Get*` operation.
You can specify multiple resource types by using a comma separated array. The array can include up to 100 items. Note that the length constraint requirement applies to each resource type filter.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** [TagKeyFilters](#API_GetComplianceSummary_RequestSyntax) **   <a name="resourcegrouptagging-GetComplianceSummary-request-TagKeyFilters"></a>
Specifies that you want the response to include information for only resources that have tags with the specified tag keys. If you use this parameter, the count of returned noncompliant resources includes only resources that have the specified tag keys.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\s\S]*`
Required: No

 ** [TargetIdFilters](#API_GetComplianceSummary_RequestSyntax) **   <a name="resourcegrouptagging-GetComplianceSummary-request-TargetIdFilters"></a>
Specifies target identifiers (usually, specific account IDs) to limit the output by. If you use this parameter, the count of returned noncompliant resources includes only resources with the specified target IDs.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 6. Maximum length of 68.
Pattern: `[a-zA-Z0-9-]*`
Required: No

## Response Syntax
<a name="API_GetComplianceSummary_ResponseSyntax"></a>

```
{
   "PaginationToken": "string",
   "SummaryList": [
      {
         "LastUpdated": "string",
         "NonCompliantResources": number,
         "Region": "string",
         "ResourceType": "string",
         "TargetId": "string",
         "TargetIdType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetComplianceSummary_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PaginationToken](#API_GetComplianceSummary_ResponseSyntax) **   <a name="resourcegrouptagging-GetComplianceSummary-response-PaginationToken"></a>
A string that indicates that there is more data available than this response contains. To receive the next part of the response, specify this response value as the `PaginationToken` value in the request for the next page.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\s\S]*`

 ** [SummaryList](#API_GetComplianceSummary_ResponseSyntax) **   <a name="resourcegrouptagging-GetComplianceSummary-response-SummaryList"></a>
A table that shows counts of noncompliant resources.
Type: Array of [Summary](API_Summary.md) objects

## Errors
<a name="API_GetComplianceSummary_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConstraintViolationException **
The request failed because performing the operation would violate a constraint.
Some of the reasons in the following list might not apply to this specific operation.
+ You must meet the prerequisites for using tag policies. For information, see [Prerequisites and permissions](https://docs.aws.amazon.com/tag-editor/latest/userguide/tag-policies-orgs.html#tag-policies-prereqs) in the *Tagging AWS resources and Tag Editor* user guide.
+ You must enable the tag policies service principal (`tagpolicies.tag.amazonaws.com`) to integrate with AWS Organizations For information, see [EnableAWSServiceAccess](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnableAWSServiceAccess.html).
+ You must have a tag policy attached to the organization root, an OU, or an account.
HTTP Status Code: 400

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

 ** ThrottledException **
The request failed because it exceeded the allowed frequency of submitted requests.
HTTP Status Code: 400

## Examples
<a name="API_GetComplianceSummary_Examples"></a>

### Example
<a name="API_GetComplianceSummary_Example_1"></a>

This example illustrates one usage of GetComplianceSummary.

#### Sample Request
<a name="API_GetComplianceSummary_Example_1_Request"></a>

```
HTTP/1.1
Host: tagging.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 663
X-Amz-Target: ResourceGroupsTaggingAPI_20170126.GetComplianceSummary
X-Amz-Date: 20191201T214524Z
User-Agent: aws-cli/1.11.79 Python/2.7.9 Windows/7 botocore/1.5.42
Content-Type: application/x-amz-json-1.1
Authorization:  AUTHPARAMS
{
   "GroupBy": [
        "TARGET_ID",
        "REGION",
        "RESOURCE_TYPE"
    ]
}
```

#### Sample Response
<a name="API_GetComplianceSummary_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestID: d3cf21f0-26db-11e7-a532-75e05382c8b1
Content-Type: application/x-amz-json-1.1
Date: Sun, 1 Dec 2019 21:45:25 GMT

{
    "SummaryList": [
        {
            "LastUpdated":"2019-10-28T21:53:16Z",
            "NonCompliantResources":1,
            "Region":"us-east-1",
            "ResourceType":"ec2:instance",
            "TargetId":"333333333333",
            "TargetIdType":"ACCOUNT"
        },
        {
            "LastUpdated":"2019-10-28T21:53:17Z",
            "NonCompliantResources":0,
            "Region":"us-east-1",
            "ResourceType":"ec2:snapshot",
            "TargetId":"222222222222",
            "TargetIdType":"ACCOUNT"
        },
        {
            "LastUpdated":"2019-10-28T21:53:16Z",
            "NonCompliantResources":1,
            "Region":"us-east-1",
            "ResourceType":"ec2:volume",
            "TargetId":"111111111111",
            "TargetIdType":"ACCOUNT"
        }
    ]
}
```

## See Also
<a name="API_GetComplianceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resourcegroupstaggingapi-2017-01-26/GetComplianceSummary)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resourcegroupstaggingapi-2017-01-26/GetComplianceSummary)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resourcegroupstaggingapi-2017-01-26/GetComplianceSummary)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resourcegroupstaggingapi-2017-01-26/GetComplianceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resourcegroupstaggingapi-2017-01-26/GetComplianceSummary)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resourcegroupstaggingapi-2017-01-26/GetComplianceSummary)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resourcegroupstaggingapi-2017-01-26/GetComplianceSummary)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resourcegroupstaggingapi-2017-01-26/GetComplianceSummary)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resourcegroupstaggingapi-2017-01-26/GetComplianceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resourcegroupstaggingapi-2017-01-26/GetComplianceSummary)
