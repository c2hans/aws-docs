---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ListCloudConnectors.html
---

# ListCloudConnectors
<a name="API_ListCloudConnectors"></a>

Returns a list of cloud connectors in the current AWS account and AWS Region.

## Request Syntax
<a name="API_ListCloudConnectors_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "FilterKey": "{{string}}",
         "FilterValues": [ "{{string}}" ]
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListCloudConnectors_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_ListCloudConnectors_RequestSyntax) **   <a name="systemsmanager-ListCloudConnectors-request-Filters"></a>
One or more filters to limit the cloud connectors returned in the response.
Type: Array of [CloudConnectorFilter](API_CloudConnectorFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: No

 ** [MaxResults](#API_ListCloudConnectors_RequestSyntax) **   <a name="systemsmanager-ListCloudConnectors-request-MaxResults"></a>
The maximum number of items to return for this call.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 10.
Required: No

 ** [NextToken](#API_ListCloudConnectors_RequestSyntax) **   <a name="systemsmanager-ListCloudConnectors-request-NextToken"></a>
The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Required: No

## Response Syntax
<a name="API_ListCloudConnectors_ResponseSyntax"></a>

```
{
   "CloudConnectors": [
      {
         "CloudConnectorId": "string",
         "CreatedAt": number,
         "Description": "string",
         "DisplayName": "string",
         "RoleArn": "string",
         "UpdatedAt": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListCloudConnectors_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CloudConnectors](#API_ListCloudConnectors_ResponseSyntax) **   <a name="systemsmanager-ListCloudConnectors-response-CloudConnectors"></a>
A list of cloud connector summary objects.
Type: Array of [CloudConnectorSummary](API_CloudConnectorSummary.md) objects

 ** [NextToken](#API_ListCloudConnectors_ResponseSyntax) **   <a name="systemsmanager-ListCloudConnectors-response-NextToken"></a>
The token to use when requesting the next set of items.
Type: String

## Errors
<a name="API_ListCloudConnectors_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

## Examples
<a name="API_ListCloudConnectors_Examples"></a>

### Example
<a name="API_ListCloudConnectors_Example_1"></a>

This example illustrates one usage of ListCloudConnectors.

#### Sample Request
<a name="API_ListCloudConnectors_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.ListCloudConnectors
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.0.0 Python/3.7.5 Windows/10 botocore/2.0.0dev4
X-Amz-Date: 20240220T232503Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240220/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 2

{}
```

#### Sample Response
<a name="API_ListCloudConnectors_Example_1_Response"></a>

```
{
    "CloudConnectors": [
        {
            "CloudConnectorId": "8077bdca-72e6-4cda-8fd9-09bae51454f6",
            "DisplayName": "MyAzureConnector",
            "Description": "Azure connector for production workloads",
            "RoleArn": "arn:aws:iam::123456789012:role/SSMAzureConnectorRole",
            "CreatedAt": "2024-02-20T23:25:03.000Z",
            "UpdatedAt": "2024-02-20T23:25:03.000Z"
        }
    ]
}
```

## See Also
<a name="API_ListCloudConnectors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/ListCloudConnectors)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/ListCloudConnectors)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/ListCloudConnectors)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/ListCloudConnectors)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/ListCloudConnectors)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/ListCloudConnectors)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/ListCloudConnectors)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/ListCloudConnectors)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/ListCloudConnectors)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/ListCloudConnectors)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
