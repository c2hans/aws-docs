---
source_url: https://docs.aws.amazon.com/apprunner/latest/api/API_ListConnections.html
---

# ListConnections
<a name="API_ListConnections"></a>

**Important**
 AWS App Runner will no longer be open to new customers starting March 31, 2026. If you would like to use App Runner, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html).

Returns a list of AWS App Runner connections that are associated with your AWS account.

## Request Syntax
<a name="API_ListConnections_RequestSyntax"></a>

```
{
   "ConnectionName": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListConnections_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConnectionName](#API_ListConnections_RequestSyntax) **   <a name="apprunner-ListConnections-request-ConnectionName"></a>
If specified, only this connection is returned. If not specified, the result isn't filtered by name.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 32.
Pattern: `[A-Za-z0-9][A-Za-z0-9\-_]{3,31}`
Required: No

 ** [MaxResults](#API_ListConnections_RequestSyntax) **   <a name="apprunner-ListConnections-request-MaxResults"></a>
The maximum number of results to include in each response (result page). Used for a paginated request.
If you don't specify `MaxResults`, the request retrieves all available results in a single response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListConnections_RequestSyntax) **   <a name="apprunner-ListConnections-request-NextToken"></a>
A token from a previous result page. Used for a paginated request. The request retrieves the next result page. All other parameter values must be identical to the ones specified in the initial request.
If you don't specify `NextToken`, the request retrieves the first result page.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`
Required: No

## Response Syntax
<a name="API_ListConnections_ResponseSyntax"></a>

```
{
   "ConnectionSummaryList": [
      {
         "ConnectionArn": "string",
         "ConnectionName": "string",
         "CreatedAt": number,
         "ProviderType": "string",
         "Status": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListConnections_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConnectionSummaryList](#API_ListConnections_ResponseSyntax) **   <a name="apprunner-ListConnections-response-ConnectionSummaryList"></a>
A list of summary information records for connections. In a paginated request, the request returns up to `MaxResults` records for each call.
Type: Array of [ConnectionSummary](API_ConnectionSummary.md) objects

 ** [NextToken](#API_ListConnections_ResponseSyntax) **   <a name="apprunner-ListConnections-response-NextToken"></a>
The token that you can pass in a subsequent request to get the next result page. Returned in a paginated request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`

## Errors
<a name="API_ListConnections_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceErrorException **
An unexpected service exception occurred.
HTTP Status Code: 500

 ** InvalidRequestException **
One or more input parameters aren't valid. Refer to the API action's document page, correct the input parameters, and try the action again.
HTTP Status Code: 400

## Examples
<a name="API_ListConnections_Examples"></a>

### List all connections
<a name="API_ListConnections_Example_1"></a>

This example illustrates how to list all App Runner connections in the AWS account.

#### Sample Request
<a name="API_ListConnections_Example_1_Request"></a>

```
$ aws apprunner list-connections --cli-input-json "`cat`"
{
}
```

#### Sample Response
<a name="API_ListConnections_Example_1_Response"></a>

```
{
  "ConnectionSummaryList": [
    {
      "ConnectionArn": "arn:aws:apprunner:us-east-1:123456789012:connection/my-github-connection",
      "ConnectionName": "my-github-connection",
      "Status": "AVAILABLE",
      "CreatedAt": "2020-11-03T00:32:51Z",
      "ProviderType": "GITHUB"
    },
    {
      "ConnectionArn": "arn:aws:apprunner:us-east-1:123456789012:connection/my-github-org-connection",
      "ConnectionName": "my-github-org-connection",
      "Status": "AVAILABLE",
      "CreatedAt": "2020-11-03T02:54:17Z",
      "ProviderType": "GITHUB"
    }
  ]
}
```

### List connection by name
<a name="API_ListConnections_Example_2"></a>

This example illustrates how to list a connection by its name.

#### Sample Request
<a name="API_ListConnections_Example_2_Request"></a>

```
$ aws apprunner list-connections --cli-input-json "`cat`"
{
  "ConnectionName": "my-github-org-connection"
}
```

#### Sample Response
<a name="API_ListConnections_Example_2_Response"></a>

```
{
  "ConnectionSummaryList": [
    {
      "ConnectionArn": "arn:aws:apprunner:us-east-1:123456789012:connection/my-github-org-connection",
      "ConnectionName": "my-github-org-connection",
      "Status": "AVAILABLE",
      "CreatedAt": "2020-11-03T02:54:17Z",
      "ProviderType": "GITHUB"
    }
  ]
}
```

## See Also
<a name="API_ListConnections_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apprunner-2020-05-15/ListConnections)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apprunner-2020-05-15/ListConnections)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apprunner-2020-05-15/ListConnections)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apprunner-2020-05-15/ListConnections)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apprunner-2020-05-15/ListConnections)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apprunner-2020-05-15/ListConnections)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apprunner-2020-05-15/ListConnections)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apprunner-2020-05-15/ListConnections)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/apprunner-2020-05-15/ListConnections)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apprunner-2020-05-15/ListConnections)
