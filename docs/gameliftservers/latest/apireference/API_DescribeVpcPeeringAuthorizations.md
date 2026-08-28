---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeVpcPeeringAuthorizations.html
---

# DescribeVpcPeeringAuthorizations
<a name="API_DescribeVpcPeeringAuthorizations"></a>

 **This API works with the following fleet types:** EC2

Retrieves valid VPC peering authorizations that are pending for the AWS account. This operation returns all VPC peering authorizations and requests for peering. This includes those initiated and received by this account.

 **Related actions**

 [All APIs by task](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets)

## Response Syntax
<a name="API_DescribeVpcPeeringAuthorizations_ResponseSyntax"></a>

```
{
   "VpcPeeringAuthorizations": [
      {
         "CreationTime": number,
         "ExpirationTime": number,
         "GameLiftAwsAccountId": "string",
         "PeerVpcAwsAccountId": "string",
         "PeerVpcId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeVpcPeeringAuthorizations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [VpcPeeringAuthorizations](#API_DescribeVpcPeeringAuthorizations_ResponseSyntax) **   <a name="gameliftservers-DescribeVpcPeeringAuthorizations-response-VpcPeeringAuthorizations"></a>
A collection of objects that describe all valid VPC peering operations for the current AWS account.
Type: Array of [VpcPeeringAuthorization](API_VpcPeeringAuthorization.md) objects

## Errors
<a name="API_DescribeVpcPeeringAuthorizations_Errors"></a>

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

## See Also
<a name="API_DescribeVpcPeeringAuthorizations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/DescribeVpcPeeringAuthorizations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/DescribeVpcPeeringAuthorizations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/DescribeVpcPeeringAuthorizations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/DescribeVpcPeeringAuthorizations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/DescribeVpcPeeringAuthorizations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/DescribeVpcPeeringAuthorizations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/DescribeVpcPeeringAuthorizations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/DescribeVpcPeeringAuthorizations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/DescribeVpcPeeringAuthorizations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/DescribeVpcPeeringAuthorizations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
