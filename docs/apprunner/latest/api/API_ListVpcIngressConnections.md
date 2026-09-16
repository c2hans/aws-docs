---
source_url: https://docs.aws.amazon.com/apprunner/latest/api/API_ListVpcIngressConnections.html
---

# ListVpcIngressConnections
<a name="API_ListVpcIngressConnections"></a>

**Important**
 AWS App Runner will no longer be open to new customers starting March 31, 2026. If you would like to use App Runner, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html).

Return a list of App Runner VPC Ingress Connections in your AWS account.

## Request Syntax
<a name="API_ListVpcIngressConnections_RequestSyntax"></a>

```
{
   "Filter": {
      "ServiceArn": "{{string}}",
      "VpcEndpointId": "{{string}}"
   },
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListVpcIngressConnections_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filter](#API_ListVpcIngressConnections_RequestSyntax) **   <a name="apprunner-ListVpcIngressConnections-request-Filter"></a>
The VPC Ingress Connections to be listed based on either the Service Arn or Vpc Endpoint Id, or both.
Type: [ListVpcIngressConnectionsFilter](API_ListVpcIngressConnectionsFilter.md) object
Required: No

 ** [MaxResults](#API_ListVpcIngressConnections_RequestSyntax) **   <a name="apprunner-ListVpcIngressConnections-request-MaxResults"></a>
The maximum number of results to include in each response (result page). It's used for a paginated request.
If you don't specify `MaxResults`, the request retrieves all available results in a single response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListVpcIngressConnections_RequestSyntax) **   <a name="apprunner-ListVpcIngressConnections-request-NextToken"></a>
A token from a previous result page. It's used for a paginated request. The request retrieves the next result page. All other parameter values must be identical to the ones that are specified in the initial request.
If you don't specify `NextToken`, the request retrieves the first result page.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`
Required: No

## Response Syntax
<a name="API_ListVpcIngressConnections_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "VpcIngressConnectionSummaryList": [
      {
         "ServiceArn": "string",
         "VpcIngressConnectionArn": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListVpcIngressConnections_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListVpcIngressConnections_ResponseSyntax) **   <a name="apprunner-ListVpcIngressConnections-response-NextToken"></a>
The token that you can pass in a subsequent request to get the next result page. It's returned in a paginated request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`

 ** [VpcIngressConnectionSummaryList](#API_ListVpcIngressConnections_ResponseSyntax) **   <a name="apprunner-ListVpcIngressConnections-response-VpcIngressConnectionSummaryList"></a>
A list of summary information records for VPC Ingress Connections. In a paginated request, the request returns up to `MaxResults` records for each call.
Type: Array of [VpcIngressConnectionSummary](API_VpcIngressConnectionSummary.md) objects

## Errors
<a name="API_ListVpcIngressConnections_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceErrorException **
An unexpected service exception occurred.
HTTP Status Code: 500

 ** InvalidRequestException **
One or more input parameters aren't valid. Refer to the API action's document page, correct the input parameters, and try the action again.
HTTP Status Code: 400

## Examples
<a name="API_ListVpcIngressConnections_Examples"></a>

### Paginated listing of App Runner VPC Ingress Connections
<a name="API_ListVpcIngressConnections_Example_1"></a>

 This example illustrates how to list all App Runner VPC Ingress Connections in your AWS account. Up to five VPC Ingress Connections are listed in each response.

In this example, the response includes one result and there aren't additional ones, so no `NextToken` is returned.

#### Sample Request
<a name="API_ListVpcIngressConnections_Example_1_Request"></a>

```
$ aws apprunner list-vpc-ingress-connections --cli-input-json "`cat`"
{
    "MaxResults": 5
}
```

#### Sample Response
<a name="API_ListVpcIngressConnections_Example_1_Response"></a>

```
{
    "VpcIngressConnectionSummaryList": [
        {
            "ServiceArn": "arn:aws:apprunner:us-east-1:123456789012:service/my-service",
            "VpcIngressConnectionArn": "arn:aws:apprunner:us-east-1:123456789012:vpcingressconnection/my-ingress-connection-name/3f2eb10e2c494674952026f646844e3d"
        }
    ]
}
```

## See Also
<a name="API_ListVpcIngressConnections_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apprunner-2020-05-15/ListVpcIngressConnections)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apprunner-2020-05-15/ListVpcIngressConnections)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apprunner-2020-05-15/ListVpcIngressConnections)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apprunner-2020-05-15/ListVpcIngressConnections)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apprunner-2020-05-15/ListVpcIngressConnections)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apprunner-2020-05-15/ListVpcIngressConnections)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apprunner-2020-05-15/ListVpcIngressConnections)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apprunner-2020-05-15/ListVpcIngressConnections)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/apprunner-2020-05-15/ListVpcIngressConnections)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apprunner-2020-05-15/ListVpcIngressConnections)
