---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcEndpointServicePermissions.html
---

# DescribeVpcEndpointServicePermissions
<a name="API_DescribeVpcEndpointServicePermissions"></a>

Describes the principals (service consumers) that are permitted to discover your VPC endpoint service. Principal ARNs with path components aren't supported.

## Request Parameters
<a name="API_DescribeVpcEndpointServicePermissions_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
The filters.
+  `principal` - The ARN of the principal.
+  `principal-type` - The principal type (`All` \| `Service` \| `OrganizationUnit` \| `Account` \| `User` \| `Role`).
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **MaxResults**
The maximum number of results to return for the request in a single page. The remaining results of the initial request can be seen by sending another request with the returned `NextToken` value. This value can be between 5 and 1,000; if `MaxResults` is given a value larger than 1,000, only 1,000 results are returned.
Type: Integer
Required: No

 **NextToken**
The token to retrieve the next page of results.
Type: String
Required: No

 **ServiceId**
The ID of the service.
Type: String
Required: Yes

## Response Elements
<a name="API_DescribeVpcEndpointServicePermissions_ResponseElements"></a>

The following elements are returned by the service.

 **allowedPrincipals**
Information about the allowed principals.
Type: Array of [AllowedPrincipal](API_AllowedPrincipal.md) objects

 **nextToken**
The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DescribeVpcEndpointServicePermissions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeVpcEndpointServicePermissions_Examples"></a>

### Example
<a name="API_DescribeVpcEndpointServicePermissions_Example_1"></a>

This example describes the permissions for service `vpce-svc-03d5ebb7d9579a123`.

#### Sample Request
<a name="API_DescribeVpcEndpointServicePermissions_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeVpcEndpointServicePermissions
&ServiceId=vpce-svc-03d5ebb7d9579a123
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeVpcEndpointServicePermissions_Example_1_Response"></a>

```
<DescribeVpcEndpointServicePermissionsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>5359c8a3-9151-4964-abed-b4422example</requestId>
    <allowedPrincipals>
        <item>
            <principal>arn:aws:iam::123456789012:root</principal>
            <principalType>Account</principalType>
        </item>
    </allowedPrincipals>
</DescribeVpcEndpointServicePermissionsResponse>
```

## See Also
<a name="API_DescribeVpcEndpointServicePermissions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeVpcEndpointServicePermissions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeVpcEndpointServicePermissions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeVpcEndpointServicePermissions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeVpcEndpointServicePermissions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeVpcEndpointServicePermissions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeVpcEndpointServicePermissions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeVpcEndpointServicePermissions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeVpcEndpointServicePermissions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeVpcEndpointServicePermissions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeVpcEndpointServicePermissions)
