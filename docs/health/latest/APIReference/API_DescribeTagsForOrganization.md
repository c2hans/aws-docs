---
source_url: https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeTagsForOrganization.html
---

# DescribeTagsForOrganization

Returns the tags associated with Health events across all accounts in your organization.

## Request Syntax
<a name="API_DescribeTagsForOrganization_RequestSyntax"></a>

```
{
   "filter": {
      "tagTypes": [ "{{string}}" ]
   },
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeTagsForOrganization_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [filter](#API_DescribeTagsForOrganization_RequestSyntax) **   <a name="AWSHealth-DescribeTagsForOrganization-request-filter"></a>
Values to narrow the results returned.
Type: [DescribeTagsForOrganizationFilter](API_DescribeTagsForOrganizationFilter.md) object
Required: No

 ** [maxResults](#API_DescribeTagsForOrganization_RequestSyntax) **   <a name="AWSHealth-DescribeTagsForOrganization-request-maxResults"></a>
The maximum number of items to return in one batch, between 10 and 100, inclusive.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_DescribeTagsForOrganization_RequestSyntax) **   <a name="AWSHealth-DescribeTagsForOrganization-request-nextToken"></a>
If the results of a search are large, only a portion of the results are returned, and a `nextToken` pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 10000.
Pattern: `[a-zA-Z0-9=/+_.-]{4,10000}`
Required: No

## Response Syntax
<a name="API_DescribeTagsForOrganization_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "tags": [
      {
         "key": "string",
         "type": "string",
         "value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeTagsForOrganization_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_DescribeTagsForOrganization_ResponseSyntax) **   <a name="AWSHealth-DescribeTagsForOrganization-response-nextToken"></a>
If the results of a search are large, only a portion of the results are returned, and a `nextToken` pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 10000.
Pattern: `[a-zA-Z0-9=/+_.-]{4,10000}`

 ** [tags](#API_DescribeTagsForOrganization_ResponseSyntax) **   <a name="AWSHealth-DescribeTagsForOrganization-response-tags"></a>
The list of tags associated with Health events across the organization.
Type: Array of [OrganizationTag](API_OrganizationTag.md) objects

## Errors
<a name="API_DescribeTagsForOrganization_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidPaginationToken **
The specified pagination token (`nextToken`) is not valid.
HTTP Status Code: 400

## See Also
<a name="API_DescribeTagsForOrganization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/health-2016-08-04/DescribeTagsForOrganization)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/health-2016-08-04/DescribeTagsForOrganization)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/health-2016-08-04/DescribeTagsForOrganization)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/health-2016-08-04/DescribeTagsForOrganization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/health-2016-08-04/DescribeTagsForOrganization)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/health-2016-08-04/DescribeTagsForOrganization)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/health-2016-08-04/DescribeTagsForOrganization)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/health-2016-08-04/DescribeTagsForOrganization)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/health-2016-08-04/DescribeTagsForOrganization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/health-2016-08-04/DescribeTagsForOrganization)
