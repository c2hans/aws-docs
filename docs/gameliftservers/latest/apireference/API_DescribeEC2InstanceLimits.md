---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeEC2InstanceLimits.html
---

# DescribeEC2InstanceLimits
<a name="API_DescribeEC2InstanceLimits"></a>

 **This API works with the following fleet types:** EC2

Retrieves the instance limits and current utilization for an AWS Region or location. Instance limits control the number of instances, per instance type, per location, that your AWS account can use. Learn more at [Amazon EC2 Instance Types](http://aws.amazon.com/ec2/instance-types/). The information returned includes the maximum number of instances allowed and your account's current usage across all fleets. This information can affect your ability to scale your Amazon GameLift Servers fleets. You can request a limit increase for your account by using the **Service limits** page in the Amazon GameLift Servers console.

Instance limits differ based on whether the instances are deployed in a fleet's home Region or in a remote location. For remote locations, limits also differ based on the combination of home Region and remote location. All requests must specify an AWS Region (either explicitly or as your default settings). To get the limit for a remote location, you must also specify the location. To learn more about how Amazon GameLift Servers handles locations, see [Amazon GameLift Servers service locations](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-regions.html). For example, the following requests all return different results:
+ Request specifies the Region `ap-northeast-1` with no location. The result is limits and usage data on all of the fleets that reside in `ap-northeast-1`, for all instance types that are deployed in `ap-northeast-1`.
+ Request specifies the Region `ap-northeast-1` with location `us-west-2`. The result is limits and usage data on all of the fleets that reside in `ap-northeast-1`, for all instance types that are deployed in `us-west-2`.
+ Request specifies the Region `us-east-1` with location `ap-northeast-1`. The result is limits and usage data on all of the fleets that reside in `us-east-1`, for all instance types that are deployed in `ap-northeast-1`. These limits do not affect fleets in any other Regions that deploy instances to `ap-northeast-1`.

This operation can be used in the following ways:
+ To get limit and usage data for all instance types that are deployed in an AWS Region by fleets that reside in the same Region: Specify the Region only. Optionally, specify a single instance type to retrieve information for.
+ To get limit and usage data for all instance types that are deployed to a remote location by fleets that reside in different AWS Region: Provide both the AWS Region and the remote location. Optionally, specify a single instance type to retrieve information for.

If successful, an `EC2InstanceLimits` object is returned with limits and usage data for each requested instance type.

 **Learn more**

 [Setting up Amazon GameLift Servers fleets](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html)

## Request Syntax
<a name="API_DescribeEC2InstanceLimits_RequestSyntax"></a>

```
{
   "EC2InstanceType": "{{string}}",
   "Location": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeEC2InstanceLimits_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [EC2InstanceType](#API_DescribeEC2InstanceLimits_RequestSyntax) **   <a name="gameliftservers-DescribeEC2InstanceLimits-request-EC2InstanceType"></a>
Name of an Amazon EC2 instance type that is supported in Amazon GameLift Servers. A fleet instance type determines the computing resources of each instance in the fleet, including CPU, memory, storage, and networking capacity. Do not specify a value for this parameter to retrieve limits for all instance types.
Type: String
Valid Values: `t2.micro | t2.small | t2.medium | t2.large | c3.large | c3.xlarge | c3.2xlarge | c3.4xlarge | c3.8xlarge | c4.large | c4.xlarge | c4.2xlarge | c4.4xlarge | c4.8xlarge | c5.large | c5.xlarge | c5.2xlarge | c5.4xlarge | c5.9xlarge | c5.12xlarge | c5.18xlarge | c5.24xlarge | c5a.large | c5a.xlarge | c5a.2xlarge | c5a.4xlarge | c5a.8xlarge | c5a.12xlarge | c5a.16xlarge | c5a.24xlarge | r3.large | r3.xlarge | r3.2xlarge | r3.4xlarge | r3.8xlarge | r4.large | r4.xlarge | r4.2xlarge | r4.4xlarge | r4.8xlarge | r4.16xlarge | r5.large | r5.xlarge | r5.2xlarge | r5.4xlarge | r5.8xlarge | r5.12xlarge | r5.16xlarge | r5.24xlarge | r5a.large | r5a.xlarge | r5a.2xlarge | r5a.4xlarge | r5a.8xlarge | r5a.12xlarge | r5a.16xlarge | r5a.24xlarge | m3.medium | m3.large | m3.xlarge | m3.2xlarge | m4.large | m4.xlarge | m4.2xlarge | m4.4xlarge | m4.10xlarge | m5.large | m5.xlarge | m5.2xlarge | m5.4xlarge | m5.8xlarge | m5.12xlarge | m5.16xlarge | m5.24xlarge | m5a.large | m5a.xlarge | m5a.2xlarge | m5a.4xlarge | m5a.8xlarge | m5a.12xlarge | m5a.16xlarge | m5a.24xlarge | c5d.large | c5d.xlarge | c5d.2xlarge | c5d.4xlarge | c5d.9xlarge | c5d.12xlarge | c5d.18xlarge | c5d.24xlarge | c6a.large | c6a.xlarge | c6a.2xlarge | c6a.4xlarge | c6a.8xlarge | c6a.12xlarge | c6a.16xlarge | c6a.24xlarge | c6i.large | c6i.xlarge | c6i.2xlarge | c6i.4xlarge | c6i.8xlarge | c6i.12xlarge | c6i.16xlarge | c6i.24xlarge | r5d.large | r5d.xlarge | r5d.2xlarge | r5d.4xlarge | r5d.8xlarge | r5d.12xlarge | r5d.16xlarge | r5d.24xlarge | m6g.medium | m6g.large | m6g.xlarge | m6g.2xlarge | m6g.4xlarge | m6g.8xlarge | m6g.12xlarge | m6g.16xlarge | c6g.medium | c6g.large | c6g.xlarge | c6g.2xlarge | c6g.4xlarge | c6g.8xlarge | c6g.12xlarge | c6g.16xlarge | r6g.medium | r6g.large | r6g.xlarge | r6g.2xlarge | r6g.4xlarge | r6g.8xlarge | r6g.12xlarge | r6g.16xlarge | c6gn.medium | c6gn.large | c6gn.xlarge | c6gn.2xlarge | c6gn.4xlarge | c6gn.8xlarge | c6gn.12xlarge | c6gn.16xlarge | c7g.medium | c7g.large | c7g.xlarge | c7g.2xlarge | c7g.4xlarge | c7g.8xlarge | c7g.12xlarge | c7g.16xlarge | r7g.medium | r7g.large | r7g.xlarge | r7g.2xlarge | r7g.4xlarge | r7g.8xlarge | r7g.12xlarge | r7g.16xlarge | m7g.medium | m7g.large | m7g.xlarge | m7g.2xlarge | m7g.4xlarge | m7g.8xlarge | m7g.12xlarge | m7g.16xlarge | g5g.xlarge | g5g.2xlarge | g5g.4xlarge | g5g.8xlarge | g5g.16xlarge | r6i.large | r6i.xlarge | r6i.2xlarge | r6i.4xlarge | r6i.8xlarge | r6i.12xlarge | r6i.16xlarge | c6gd.medium | c6gd.large | c6gd.xlarge | c6gd.2xlarge | c6gd.4xlarge | c6gd.8xlarge | c6gd.12xlarge | c6gd.16xlarge | c6in.large | c6in.xlarge | c6in.2xlarge | c6in.4xlarge | c6in.8xlarge | c6in.12xlarge | c6in.16xlarge | c7a.medium | c7a.large | c7a.xlarge | c7a.2xlarge | c7a.4xlarge | c7a.8xlarge | c7a.12xlarge | c7a.16xlarge | c7gd.medium | c7gd.large | c7gd.xlarge | c7gd.2xlarge | c7gd.4xlarge | c7gd.8xlarge | c7gd.12xlarge | c7gd.16xlarge | c7gn.medium | c7gn.large | c7gn.xlarge | c7gn.2xlarge | c7gn.4xlarge | c7gn.8xlarge | c7gn.12xlarge | c7gn.16xlarge | c7i.large | c7i.xlarge | c7i.2xlarge | c7i.4xlarge | c7i.8xlarge | c7i.12xlarge | c7i.16xlarge | m6a.large | m6a.xlarge | m6a.2xlarge | m6a.4xlarge | m6a.8xlarge | m6a.12xlarge | m6a.16xlarge | m6gd.medium | m6gd.large | m6gd.xlarge | m6gd.2xlarge | m6gd.4xlarge | m6gd.8xlarge | m6gd.12xlarge | m6gd.16xlarge | m6i.large | m6i.xlarge | m6i.2xlarge | m6i.4xlarge | m6i.8xlarge | m6i.12xlarge | m6i.16xlarge | m7a.medium | m7a.large | m7a.xlarge | m7a.2xlarge | m7a.4xlarge | m7a.8xlarge | m7a.12xlarge | m7a.16xlarge | m7gd.medium | m7gd.large | m7gd.xlarge | m7gd.2xlarge | m7gd.4xlarge | m7gd.8xlarge | m7gd.12xlarge | m7gd.16xlarge | m7i.large | m7i.xlarge | m7i.2xlarge | m7i.4xlarge | m7i.8xlarge | m7i.12xlarge | m7i.16xlarge | r6gd.medium | r6gd.large | r6gd.xlarge | r6gd.2xlarge | r6gd.4xlarge | r6gd.8xlarge | r6gd.12xlarge | r6gd.16xlarge | r7a.medium | r7a.large | r7a.xlarge | r7a.2xlarge | r7a.4xlarge | r7a.8xlarge | r7a.12xlarge | r7a.16xlarge | r7gd.medium | r7gd.large | r7gd.xlarge | r7gd.2xlarge | r7gd.4xlarge | r7gd.8xlarge | r7gd.12xlarge | r7gd.16xlarge | r7i.large | r7i.xlarge | r7i.2xlarge | r7i.4xlarge | r7i.8xlarge | r7i.12xlarge | r7i.16xlarge | r7i.24xlarge | r7i.48xlarge | c5ad.large | c5ad.xlarge | c5ad.2xlarge | c5ad.4xlarge | c5ad.8xlarge | c5ad.12xlarge | c5ad.16xlarge | c5ad.24xlarge | c5n.large | c5n.xlarge | c5n.2xlarge | c5n.4xlarge | c5n.9xlarge | c5n.18xlarge | r5ad.large | r5ad.xlarge | r5ad.2xlarge | r5ad.4xlarge | r5ad.8xlarge | r5ad.12xlarge | r5ad.16xlarge | r5ad.24xlarge | c6id.large | c6id.xlarge | c6id.2xlarge | c6id.4xlarge | c6id.8xlarge | c6id.12xlarge | c6id.16xlarge | c6id.24xlarge | c6id.32xlarge | c8g.medium | c8g.large | c8g.xlarge | c8g.2xlarge | c8g.4xlarge | c8g.8xlarge | c8g.12xlarge | c8g.16xlarge | c8g.24xlarge | c8g.48xlarge | m5ad.large | m5ad.xlarge | m5ad.2xlarge | m5ad.4xlarge | m5ad.8xlarge | m5ad.12xlarge | m5ad.16xlarge | m5ad.24xlarge | m5d.large | m5d.xlarge | m5d.2xlarge | m5d.4xlarge | m5d.8xlarge | m5d.12xlarge | m5d.16xlarge | m5d.24xlarge | m5dn.large | m5dn.xlarge | m5dn.2xlarge | m5dn.4xlarge | m5dn.8xlarge | m5dn.12xlarge | m5dn.16xlarge | m5dn.24xlarge | m5n.large | m5n.xlarge | m5n.2xlarge | m5n.4xlarge | m5n.8xlarge | m5n.12xlarge | m5n.16xlarge | m5n.24xlarge | m6id.large | m6id.xlarge | m6id.2xlarge | m6id.4xlarge | m6id.8xlarge | m6id.12xlarge | m6id.16xlarge | m6id.24xlarge | m6id.32xlarge | m6idn.large | m6idn.xlarge | m6idn.2xlarge | m6idn.4xlarge | m6idn.8xlarge | m6idn.12xlarge | m6idn.16xlarge | m6idn.24xlarge | m6idn.32xlarge | m6in.large | m6in.xlarge | m6in.2xlarge | m6in.4xlarge | m6in.8xlarge | m6in.12xlarge | m6in.16xlarge | m6in.24xlarge | m6in.32xlarge | m8g.medium | m8g.large | m8g.xlarge | m8g.2xlarge | m8g.4xlarge | m8g.8xlarge | m8g.12xlarge | m8g.16xlarge | m8g.24xlarge | m8g.48xlarge | r5dn.large | r5dn.xlarge | r5dn.2xlarge | r5dn.4xlarge | r5dn.8xlarge | r5dn.12xlarge | r5dn.16xlarge | r5dn.24xlarge | r5n.large | r5n.xlarge | r5n.2xlarge | r5n.4xlarge | r5n.8xlarge | r5n.12xlarge | r5n.16xlarge | r5n.24xlarge | r6a.large | r6a.xlarge | r6a.2xlarge | r6a.4xlarge | r6a.8xlarge | r6a.12xlarge | r6a.16xlarge | r6a.24xlarge | r6a.32xlarge | r6a.48xlarge | r6id.large | r6id.xlarge | r6id.2xlarge | r6id.4xlarge | r6id.8xlarge | r6id.12xlarge | r6id.16xlarge | r6id.24xlarge | r6id.32xlarge | r6idn.large | r6idn.xlarge | r6idn.2xlarge | r6idn.4xlarge | r6idn.8xlarge | r6idn.12xlarge | r6idn.16xlarge | r6idn.24xlarge | r6idn.32xlarge | r6in.large | r6in.xlarge | r6in.2xlarge | r6in.4xlarge | r6in.8xlarge | r6in.12xlarge | r6in.16xlarge | r6in.24xlarge | r6in.32xlarge | r8g.medium | r8g.large | r8g.xlarge | r8g.2xlarge | r8g.4xlarge | r8g.8xlarge | r8g.12xlarge | r8g.16xlarge | r8g.24xlarge | r8g.48xlarge | m4.16xlarge | c6a.32xlarge | c6a.48xlarge | c6i.32xlarge | r6i.24xlarge | r6i.32xlarge | c6in.24xlarge | c6in.32xlarge | c7a.24xlarge | c7a.32xlarge | c7a.48xlarge | c7i.24xlarge | c7i.48xlarge | m6a.24xlarge | m6a.32xlarge | m6a.48xlarge | m6i.24xlarge | m6i.32xlarge | m7a.24xlarge | m7a.32xlarge | m7a.48xlarge | m7i.24xlarge | m7i.48xlarge | r7a.24xlarge | r7a.32xlarge | r7a.48xlarge`
Required: No

 ** [Location](#API_DescribeEC2InstanceLimits_RequestSyntax) **   <a name="gameliftservers-DescribeEC2InstanceLimits-request-Location"></a>
The name of a remote location to request instance limits for, in the form of an AWS Region code such as `us-west-2`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[A-Za-z0-9\-]+`
Required: No

## Response Syntax
<a name="API_DescribeEC2InstanceLimits_ResponseSyntax"></a>

```
{
   "EC2InstanceLimits": [
      {
         "CurrentInstances": number,
         "EC2InstanceType": "string",
         "InstanceLimit": number,
         "Location": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeEC2InstanceLimits_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EC2InstanceLimits](#API_DescribeEC2InstanceLimits_ResponseSyntax) **   <a name="gameliftservers-DescribeEC2InstanceLimits-response-EC2InstanceLimits"></a>
The maximum number of instances for the specified instance type.
Type: Array of [EC2InstanceLimit](API_EC2InstanceLimit.md) objects

## Errors
<a name="API_DescribeEC2InstanceLimits_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.
HTTP Status Code: 500

 ** InvalidRequestException **
One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.
HTTP Status Code: 400

 ** UnauthorizedException **
The client failed authentication. Clients should not retry such requests.
HTTP Status Code: 400

 ** UnsupportedRegionException **
The requested operation is not supported in the Region specified.
HTTP Status Code: 400

## Examples
<a name="API_DescribeEC2InstanceLimits_Examples"></a>

### Request EC2 instance limits for home region (ap-northeast-1) with no location
<a name="API_DescribeEC2InstanceLimits_Example_1"></a>

In this example, we request the instance limits and current usage for the `m5.large` instance type. The API call is made to the AWS Region `ap-northeast-1` with no `Location` specified, so the results show limits and usage for fleets that reside in `ap-northeast-1`, for instances deployed in `ap-northeast-1`. The response indicates that our account allows up to 200 `m5.large` instances and currently has 25 deployed.

HTTP requests are authenticated using an [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) signature in the `Authorization` header field.

#### Sample Request
<a name="API_DescribeEC2InstanceLimits_Example_1_Request"></a>

```
{
    "EC2InstanceType": "m5.large"
}
```

#### Sample Response
<a name="API_DescribeEC2InstanceLimits_Example_1_Response"></a>

```
{
    "EC2InstanceLimits": [
        {
            "EC2InstanceType": "m5.large",
            "CurrentInstances": 25,
            "InstanceLimit": 200,
            "Location": "ap-northeast-1"
        }
    ]
}
```

### Request EC2 instance limits for home region (ap-northeast-1) with remote location (us-west-2)
<a name="API_DescribeEC2InstanceLimits_Example_2"></a>

In this example, we request the instance limits and current usage for the `m5.large` instance type at a remote location. The API call is made to the AWS Region `ap-northeast-1` with `Location` set to `us-west-2`. The results show limits and usage for fleets that reside in `ap-northeast-1`, for instances deployed in `us-west-2`. The response indicates that our account allows up to 100 `m5.large` instances and currently has 10 deployed.

HTTP requests are authenticated using an [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) signature in the `Authorization` header field.

#### Sample Request
<a name="API_DescribeEC2InstanceLimits_Example_2_Request"></a>

```
{
    "EC2InstanceType": "m5.large",
    "Location": "us-west-2"
}
```

#### Sample Response
<a name="API_DescribeEC2InstanceLimits_Example_2_Response"></a>

```
{
    "EC2InstanceLimits": [
        {
            "EC2InstanceType": "m5.large",
            "CurrentInstances": 10,
            "InstanceLimit": 100,
            "Location": "us-west-2"
        }
    ]
}
```

### Request EC2 instance limits for home region (us-east-1) with remote location (ap-northeast-1)
<a name="API_DescribeEC2InstanceLimits_Example_3"></a>

In this example, we request the instance limits and current usage for the `m5.large` instance type at a remote location. The API call is made to the AWS Region `us-east-1` with `Location` set to `ap-northeast-1`. The results show limits and usage for fleets that reside in `us-east-1`, for instances deployed in `ap-northeast-1`. These limits do not affect fleets in other Regions that also deploy instances to `ap-northeast-1`. The response indicates that our account allows up to 150 `m5.large` instances and currently has none deployed.

HTTP requests are authenticated using an [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) signature in the `Authorization` header field.

#### Sample Request
<a name="API_DescribeEC2InstanceLimits_Example_3_Request"></a>

```
{
    "EC2InstanceType": "m5.large",
    "Location": "ap-northeast-1"
}
```

#### Sample Response
<a name="API_DescribeEC2InstanceLimits_Example_3_Response"></a>

```
{
    "EC2InstanceLimits": [
        {
            "EC2InstanceType": "m5.large",
            "CurrentInstances": 0,
            "InstanceLimit": 150,
            "Location": "ap-northeast-1"
        }
    ]
}
```

## See Also
<a name="API_DescribeEC2InstanceLimits_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/DescribeEC2InstanceLimits)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/DescribeEC2InstanceLimits)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/DescribeEC2InstanceLimits)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/DescribeEC2InstanceLimits)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/DescribeEC2InstanceLimits)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/DescribeEC2InstanceLimits)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/DescribeEC2InstanceLimits)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/DescribeEC2InstanceLimits)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/DescribeEC2InstanceLimits)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/DescribeEC2InstanceLimits)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
