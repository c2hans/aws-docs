---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_ListClusters.html
---

# ListClusters
<a name="API_ListClusters"></a>

**Note**
 AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

Returns an array of `ClusterListEntry` objects of the specified length. Each `ClusterListEntry` object contains a cluster's state, a cluster's ID, and other important status information.

## Request Syntax
<a name="API_ListClusters_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListClusters_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListClusters_RequestSyntax) **   <a name="Snowball-ListClusters-request-MaxResults"></a>
The number of `ClusterListEntry` objects to return.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListClusters_RequestSyntax) **   <a name="Snowball-ListClusters-request-NextToken"></a>
HTTP requests are stateless. To identify what object comes "next" in the list of `ClusterListEntry` objects, you have the option of specifying `NextToken` as the starting point for your returned list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`
Required: No

## Response Syntax
<a name="API_ListClusters_ResponseSyntax"></a>

```
{
   "ClusterListEntries": [
      {
         "ClusterId": "string",
         "ClusterState": "string",
         "CreationDate": number,
         "Description": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListClusters_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ClusterListEntries](#API_ListClusters_ResponseSyntax) **   <a name="Snowball-ListClusters-response-ClusterListEntries"></a>
Each `ClusterListEntry` object contains a cluster's state, a cluster's ID, and other important status information.
Type: Array of [ClusterListEntry](API_ClusterListEntry.md) objects

 ** [NextToken](#API_ListClusters_ResponseSyntax) **   <a name="Snowball-ListClusters-response-NextToken"></a>
HTTP requests are stateless. If you use the automatically generated `NextToken` value in your next `ClusterListEntry` call, your list of returned clusters will start from this point in the array.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`

## Errors
<a name="API_ListClusters_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidNextTokenException **
The `NextToken` string was altered unexpectedly, and the operation has stopped. Run the operation without changing the `NextToken` string, and try again.
HTTP Status Code: 400

## See Also
<a name="API_ListClusters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/snowball-2016-06-30/ListClusters)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/snowball-2016-06-30/ListClusters)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snowball-2016-06-30/ListClusters)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/snowball-2016-06-30/ListClusters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snowball-2016-06-30/ListClusters)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/snowball-2016-06-30/ListClusters)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/snowball-2016-06-30/ListClusters)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/snowball-2016-06-30/ListClusters)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/snowball-2016-06-30/ListClusters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snowball-2016-06-30/ListClusters)
