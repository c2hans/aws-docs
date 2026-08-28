---
source_url: https://docs.aws.amazon.com/apprunner/latest/api/API_ListVpcConnectors.html
---

# ListVpcConnectors
<a name="API_ListVpcConnectors"></a>

**Important**
 AWS App Runner will no longer be open to new customers starting March 31, 2026. If you would like to use App Runner, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html).

Returns a list of AWS App Runner VPC connectors in your AWS account.

## Request Syntax
<a name="API_ListVpcConnectors_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListVpcConnectors_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListVpcConnectors_RequestSyntax) **   <a name="apprunner-ListVpcConnectors-request-MaxResults"></a>
The maximum number of results to include in each response (result page). It's used for a paginated request.
If you don't specify `MaxResults`, the request retrieves all available results in a single response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListVpcConnectors_RequestSyntax) **   <a name="apprunner-ListVpcConnectors-request-NextToken"></a>
A token from a previous result page. It's used for a paginated request. The request retrieves the next result page. All other parameter values must be identical to the ones that are specified in the initial request.
If you don't specify `NextToken`, the request retrieves the first result page.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`
Required: No

## Response Syntax
<a name="API_ListVpcConnectors_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "VpcConnectors": [
      {
         "CreatedAt": number,
         "DeletedAt": number,
         "SecurityGroups": [ "string" ],
         "Status": "string",
         "Subnets": [ "string" ],
         "VpcConnectorArn": "string",
         "VpcConnectorName": "string",
         "VpcConnectorRevision": number
      }
   ]
}
```

## Response Elements
<a name="API_ListVpcConnectors_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListVpcConnectors_ResponseSyntax) **   <a name="apprunner-ListVpcConnectors-response-NextToken"></a>
The token that you can pass in a subsequent request to get the next result page. It's returned in a paginated request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`

 ** [VpcConnectors](#API_ListVpcConnectors_ResponseSyntax) **   <a name="apprunner-ListVpcConnectors-response-VpcConnectors"></a>
A list of information records for VPC connectors. In a paginated request, the request returns up to `MaxResults` records for each call.
Type: Array of [VpcConnector](API_VpcConnector.md) objects

## Errors
<a name="API_ListVpcConnectors_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceErrorException **
An unexpected service exception occurred.
HTTP Status Code: 500

 ** InvalidRequestException **
One or more input parameters aren't valid. Refer to the API action's document page, correct the input parameters, and try the action again.
HTTP Status Code: 400

## Examples
<a name="API_ListVpcConnectors_Examples"></a>

### Paginated listing of App Runner VPC connectors
<a name="API_ListVpcConnectors_Example_1"></a>

This example illustrates how to list all App Runner VPC connectors in your AWS account. Up to five VPC connectors are listed in each response.

In this example, the response includes one result and there aren't additional ones, so no `NextToken` is returned.

#### Sample Request
<a name="API_ListVpcConnectors_Example_1_Request"></a>

```
$ aws apprunner list-vpc-connectors --cli-input-json "`cat`"
{
  "MaxResults": 5
}
```

#### Sample Response
<a name="API_ListVpcConnectors_Example_1_Response"></a>

```
{
  "VpcConnectors": [
    {
      "VpcConnectorArn": "arn:aws:apprunner:us-east-1:123456789012:vpcconnector/my-vpc-connector/1/3f2eb10e2c494674952026f646844e3d",
      "VpcConnectorName": "my-vpc-connector",
      "VpcConnectorRevision": 1,
      "Subnets": ["subnet-123", "subnet-456"],
      "SecurityGroups": ["sg-123", "sg-456"],
      "Status": "ACTIVE",
      "CreatedAt": "2021-08-18T23:36:45.374Z"
    }
  ]
}
```

## See Also
<a name="API_ListVpcConnectors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apprunner-2020-05-15/ListVpcConnectors)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apprunner-2020-05-15/ListVpcConnectors)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apprunner-2020-05-15/ListVpcConnectors)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apprunner-2020-05-15/ListVpcConnectors)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apprunner-2020-05-15/ListVpcConnectors)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apprunner-2020-05-15/ListVpcConnectors)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apprunner-2020-05-15/ListVpcConnectors)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apprunner-2020-05-15/ListVpcConnectors)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/apprunner-2020-05-15/ListVpcConnectors)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apprunner-2020-05-15/ListVpcConnectors)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Runner. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apprunner` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
