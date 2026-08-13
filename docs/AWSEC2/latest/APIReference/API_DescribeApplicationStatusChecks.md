---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeApplicationStatusChecks.html
---

# DescribeApplicationStatusChecks
<a name="API_DescribeApplicationStatusChecks"></a>

Describes application status checks, including configuration details such as protocol, port, path, thresholds, and associations. Results are paginated. Use the `NextToken` parameter to retrieve additional results. The following rules apply:
+ If you do not specify any application status check IDs, all checks in your account are returned.
+ Use `DescribeApplicationStatus` to see the actual health status of instances.

## Request Parameters
<a name="API_DescribeApplicationStatusChecks_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ApplicationStatusCheckId.N**
The IDs of the application status checks to describe.
Type: Array of strings
Required: No

 **DryRun**
Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
The filters.
+  `aggregation` – The aggregation setting. Valid values: `included` and `excluded`.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **IncludeAll**
Specifies whether to include recently deleted application status checks that remain available during the deletion grace period. If you omit this parameter or set it to `false`, the response includes only active checks.
Type: Boolean
Required: No

 **MaxResults**
The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see [Pagination](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination).
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 100.
Required: No

 **NextToken**
The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.
Type: String
Required: No

## Response Elements
<a name="API_DescribeApplicationStatusChecks_ResponseElements"></a>

The following elements are returned by the service.

 **applicationStatusCheckSet**
Information about the application status checks.
Type: Array of [ApplicationStatusCheckResponseObject](API_ApplicationStatusCheckResponseObject.md) objects

 **nextToken**
The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DescribeApplicationStatusChecks_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeApplicationStatusChecks_Examples"></a>

### To describe application status checks
<a name="API_DescribeApplicationStatusChecks_Example_1"></a>

This example describes the specified application status check.

#### Sample Request
<a name="API_DescribeApplicationStatusChecks_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeApplicationStatusChecks
&ApplicationStatusCheckId.1=asc-0123456789abcdef0
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeApplicationStatusChecks_Example_1_Response"></a>

```
<DescribeApplicationStatusChecksResult xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
    <applicationStatusCheckSet>
        <item>
            <applicationStatusCheckId>asc-0123456789abcdef0</applicationStatusCheckId>
            <protocol>http</protocol>
            <port>80</port>
        </item>
    </applicationStatusCheckSet>
</DescribeApplicationStatusChecksResult>
```

## See Also
<a name="API_DescribeApplicationStatusChecks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeApplicationStatusChecks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeApplicationStatusChecks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeApplicationStatusChecks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeApplicationStatusChecks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeApplicationStatusChecks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeApplicationStatusChecks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeApplicationStatusChecks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeApplicationStatusChecks)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeApplicationStatusChecks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeApplicationStatusChecks)
