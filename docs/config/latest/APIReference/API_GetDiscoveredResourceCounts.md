---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_GetDiscoveredResourceCounts.html
---

# GetDiscoveredResourceCounts
<a name="API_GetDiscoveredResourceCounts"></a>

Returns the resource types, the number of each resource type, and the total number of resources that AWS Config is recording in this region for your AWS account.

**Example**

1.  AWS Config is recording three resource types in the US East (Ohio) Region for your account: 25 EC2 instances, 20 IAM users, and 15 S3 buckets.

1. You make a call to the `GetDiscoveredResourceCounts` action and specify that you want all resource types.

1.  AWS Config returns the following:
   + The resource types (EC2 instances, IAM users, and S3 buckets).
   + The number of each resource type (25, 20, and 15).
   + The total number of all resources (60).

The response is paginated. By default, AWS Config lists 100 [ResourceCount](API_ResourceCount.md) objects on each page. You can customize this number with the `limit` parameter. The response includes a `nextToken` string. To get the next page of results, run the request again and specify the string for the `nextToken` parameter.

**Note**
If you make a call to the [GetDiscoveredResourceCounts](#API_GetDiscoveredResourceCounts) action, you might not immediately receive resource counts in the following situations:
You are a new AWS Config customer.
You just enabled resource recording.
It might take a few minutes for AWS Config to record and count your resources. Wait a few minutes and then retry the [GetDiscoveredResourceCounts](#API_GetDiscoveredResourceCounts) action.

## Request Syntax
<a name="API_GetDiscoveredResourceCounts_RequestSyntax"></a>

```
{
   "limit": {{number}},
   "nextToken": "{{string}}",
   "resourceTypes": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_GetDiscoveredResourceCounts_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [limit](#API_GetDiscoveredResourceCounts_RequestSyntax) **   <a name="config-GetDiscoveredResourceCounts-request-limit"></a>
The maximum number of [ResourceCount](API_ResourceCount.md) objects returned on each page. The default is 100. You cannot specify a number greater than 100. If you specify 0, AWS Config uses the default.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** [nextToken](#API_GetDiscoveredResourceCounts_RequestSyntax) **   <a name="config-GetDiscoveredResourceCounts-request-nextToken"></a>
The `nextToken` string returned on a previous page that you use to get the next page of results in a paginated response.
Type: String
Required: No

 ** [resourceTypes](#API_GetDiscoveredResourceCounts_RequestSyntax) **   <a name="config-GetDiscoveredResourceCounts-request-resourceTypes"></a>
The comma-separated list that specifies the resource types that you want AWS Config to return (for example, `"AWS::EC2::Instance"`, `"AWS::IAM::User"`).
If a value for `resourceTypes` is not specified, AWS Config returns all resource types that AWS Config is recording in the region for your account.
If the configuration recorder is turned off, AWS Config returns an empty list of [ResourceCount](API_ResourceCount.md) objects. If the configuration recorder is not recording a specific resource type (for example, S3 buckets), that resource type is not returned in the list of [ResourceCount](API_ResourceCount.md) objects.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_GetDiscoveredResourceCounts_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "resourceCounts": [
      {
         "count": number,
         "resourceType": "string"
      }
   ],
   "totalDiscoveredResources": number
}
```

## Response Elements
<a name="API_GetDiscoveredResourceCounts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_GetDiscoveredResourceCounts_ResponseSyntax) **   <a name="config-GetDiscoveredResourceCounts-response-nextToken"></a>
The string that you use in a subsequent request to get the next page of results in a paginated response.
Type: String

 ** [resourceCounts](#API_GetDiscoveredResourceCounts_ResponseSyntax) **   <a name="config-GetDiscoveredResourceCounts-response-resourceCounts"></a>
The list of `ResourceCount` objects. Each object is listed in descending order by the number of resources.
Type: Array of [ResourceCount](API_ResourceCount.md) objects

 ** [totalDiscoveredResources](#API_GetDiscoveredResourceCounts_ResponseSyntax) **   <a name="config-GetDiscoveredResourceCounts-response-totalDiscoveredResources"></a>
The total number of resources that AWS Config is recording in the region for your account. If you specify resource types in the request, AWS Config returns only the total number of resources for those resource types.

**Example**

1.  AWS Config is recording three resource types in the US East (Ohio) Region for your account: 25 EC2 instances, 20 IAM users, and 15 S3 buckets, for a total of 60 resources.

1. You make a call to the `GetDiscoveredResourceCounts` action and specify the resource type, `"AWS::EC2::Instances"`, in the request.

1.  AWS Config returns 25 for `totalDiscoveredResources`.
Type: Long

## Errors
<a name="API_GetDiscoveredResourceCounts_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidLimitException **
The specified limit is outside the allowable range.
HTTP Status Code: 400

 ** InvalidNextTokenException **
The specified next token is not valid. Specify the `nextToken` string that was returned in the previous response to get the next page of results.
HTTP Status Code: 400

 ** ValidationException **
The requested operation is not valid. You will see this exception if there are missing required fields or if the input value fails the validation.
For [PutStoredQuery](https://docs.aws.amazon.com/config/latest/APIReference/API_PutStoredQuery.html), one of the following errors:
+ There are missing required fields.
+ The input value fails the validation.
+ You are trying to create more than 300 queries.
For [DescribeConfigurationRecorders](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorders.html) and [DescribeConfigurationRecorderStatus](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorderStatus.html), one of the following errors:
+ You have specified more than one configuration recorder.
+ You have provided a service principal for service-linked configuration recorder that is not valid.
For [AssociateResourceTypes](https://docs.aws.amazon.com/config/latest/APIReference/API_AssociateResourceTypes.html) and [DisassociateResourceTypes](https://docs.aws.amazon.com/config/latest/APIReference/API_DisassociateResourceTypes.html), one of the following errors:
+ Your configuraiton recorder has a recording strategy that does not allow the association or disassociation of resource types.
+ One or more of the specified resource types are already associated or disassociated with the configuration recorder.
+ For service-linked configuration recorders, the configuration recorder does not record one or more of the specified resource types.
For [DeleteServiceLinkedConfigurationRecorder](https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteServiceLinkedConfigurationRecorder.html), one of the following errors:
+ You have provided both `Arn` and `ServicePrincipal`. Only one of `Arn` or `ServicePrincipal` can be specified.
+ You have provided a service principal for service-linked configuration recorder that is not valid.
HTTP Status Code: 400

## See Also
<a name="API_GetDiscoveredResourceCounts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/GetDiscoveredResourceCounts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/GetDiscoveredResourceCounts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/GetDiscoveredResourceCounts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/GetDiscoveredResourceCounts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/GetDiscoveredResourceCounts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/GetDiscoveredResourceCounts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/GetDiscoveredResourceCounts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/GetDiscoveredResourceCounts)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/GetDiscoveredResourceCounts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/GetDiscoveredResourceCounts)
