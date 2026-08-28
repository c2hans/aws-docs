---
source_url: https://docs.aws.amazon.com/fsx/latest/APIReference/API_DescribeFileCaches.html
---

# DescribeFileCaches
<a name="API_DescribeFileCaches"></a>

Returns the description of a specific Amazon File Cache resource, if a `FileCacheIds` value is provided for that cache. Otherwise, it returns descriptions of all caches owned by your AWS account in the AWS Region of the endpoint that you're calling.

When retrieving all cache descriptions, you can optionally specify the `MaxResults` parameter to limit the number of descriptions in a response. If more cache descriptions remain, the operation returns a `NextToken` value in the response. In this case, send a later request with the `NextToken` request parameter set to the value of `NextToken` from the last response.

This operation is used in an iterative process to retrieve a list of your cache descriptions. `DescribeFileCaches` is called first without a `NextToken`value. Then the operation continues to be called with the `NextToken` parameter set to the value of the last `NextToken` value until a response has no `NextToken`.

When using this operation, keep the following in mind:
+ The implementation might return fewer than `MaxResults` cache descriptions while still including a `NextToken` value.
+ The order of caches returned in the response of one `DescribeFileCaches` call and the order of caches returned across the responses of a multicall iteration is unspecified.

## Request Syntax
<a name="API_DescribeFileCaches_RequestSyntax"></a>

```
{
   "FileCacheIds": [ "{{string}}" ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeFileCaches_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [FileCacheIds](#API_DescribeFileCaches_RequestSyntax) **   <a name="FSx-DescribeFileCaches-request-FileCacheIds"></a>
IDs of the caches whose descriptions you want to retrieve (String).
Type: Array of strings
Array Members: Maximum number of 50 items.
Length Constraints: Minimum length of 11. Maximum length of 21.
Pattern: `^(fc-[0-9a-f]{8,})$`
Required: No

 ** [MaxResults](#API_DescribeFileCaches_RequestSyntax) **   <a name="FSx-DescribeFileCaches-request-MaxResults"></a>
The maximum number of resources to return in the response. This value must be an integer greater than zero.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 2147483647.
Required: No

 ** [NextToken](#API_DescribeFileCaches_RequestSyntax) **   <a name="FSx-DescribeFileCaches-request-NextToken"></a>
(Optional) Opaque pagination token returned from a previous operation (String). If present, this token indicates from what point you can continue processing the request, where the previous `NextToken` value left off.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$`
Required: No

## Response Syntax
<a name="API_DescribeFileCaches_ResponseSyntax"></a>

```
{
   "FileCaches": [
      {
         "CreationTime": number,
         "DataRepositoryAssociationIds": [ "string" ],
         "DNSName": "string",
         "FailureDetails": {
            "Message": "string"
         },
         "FileCacheId": "string",
         "FileCacheType": "string",
         "FileCacheTypeVersion": "string",
         "KmsKeyId": "string",
         "Lifecycle": "string",
         "LustreConfiguration": {
            "DeploymentType": "string",
            "LogConfiguration": {
               "Destination": "string",
               "Level": "string"
            },
            "MetadataConfiguration": {
               "StorageCapacity": number
            },
            "MountName": "string",
            "PerUnitStorageThroughput": number,
            "WeeklyMaintenanceStartTime": "string"
         },
         "NetworkInterfaceIds": [ "string" ],
         "OwnerId": "string",
         "ResourceARN": "string",
         "StorageCapacity": number,
         "SubnetIds": [ "string" ],
         "VpcId": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeFileCaches_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FileCaches](#API_DescribeFileCaches_ResponseSyntax) **   <a name="FSx-DescribeFileCaches-response-FileCaches"></a>
The response object for the `DescribeFileCaches` operation.
Type: Array of [FileCache](API_FileCache.md) objects
Array Members: Maximum number of 50 items.

 ** [NextToken](#API_DescribeFileCaches_ResponseSyntax) **   <a name="FSx-DescribeFileCaches-response-NextToken"></a>
(Optional) Opaque pagination token returned from a previous operation (String). If present, this token indicates from what point you can continue processing the request, where the previous `NextToken` value left off.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$`

## Errors
<a name="API_DescribeFileCaches_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequest **
A generic error indicating a failure with a client request.
 ** Message **
A detailed error message.
HTTP Status Code: 400

 ** FileCacheNotFound **
No caches were found based upon supplied parameters.
 ** Message **
A detailed error message.
HTTP Status Code: 400

 ** InternalServerError **
A generic error indicating a server-side failure.
 ** Message **
A detailed error message.
HTTP Status Code: 500

## See Also
<a name="API_DescribeFileCaches_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fsx-2018-03-01/DescribeFileCaches)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fsx-2018-03-01/DescribeFileCaches)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/DescribeFileCaches)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fsx-2018-03-01/DescribeFileCaches)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/DescribeFileCaches)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fsx-2018-03-01/DescribeFileCaches)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fsx-2018-03-01/DescribeFileCaches)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fsx-2018-03-01/DescribeFileCaches)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fsx-2018-03-01/DescribeFileCaches)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/DescribeFileCaches)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FSx. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fsx` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
