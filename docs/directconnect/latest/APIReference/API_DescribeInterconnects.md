---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeInterconnects.html
---

# DescribeInterconnects
<a name="API_DescribeInterconnects"></a>

Lists the interconnects owned by the AWS account or only the specified interconnect.

## Request Syntax
<a name="API_DescribeInterconnects_RequestSyntax"></a>

```
{
   "interconnectId": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeInterconnects_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [interconnectId](#API_DescribeInterconnects_RequestSyntax) **   <a name="DX-DescribeInterconnects-request-interconnectId"></a>
The ID of the interconnect.
Type: String
Required: No

 ** [maxResults](#API_DescribeInterconnects_RequestSyntax) **   <a name="DX-DescribeInterconnects-request-maxResults"></a>
The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned `nextToken` value.
If `MaxResults` is given a value larger than 100, only 100 results are returned.
Type: Integer
Required: No

 ** [nextToken](#API_DescribeInterconnects_RequestSyntax) **   <a name="DX-DescribeInterconnects-request-nextToken"></a>
The token for the next page of results.
Type: String
Required: No

## Response Syntax
<a name="API_DescribeInterconnects_ResponseSyntax"></a>

```
{
   "interconnects": [
      {
         "awsDevice": "string",
         "awsDeviceV2": "string",
         "awsLogicalDeviceId": "string",
         "bandwidth": "string",
         "encryptionMode": "string",
         "hasLogicalRedundancy": "string",
         "interconnectId": "string",
         "interconnectName": "string",
         "interconnectState": "string",
         "jumboFrameCapable": boolean,
         "lagId": "string",
         "loaIssueTime": number,
         "location": "string",
         "macSecCapable": boolean,
         "macSecKeys": [
            {
               "ckn": "string",
               "secretARN": "string",
               "startOn": "string",
               "state": "string"
            }
         ],
         "portEncryptionStatus": "string",
         "providerName": "string",
         "region": "string",
         "tags": [
            {
               "key": "string",
               "value": "string"
            }
         ]
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeInterconnects_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [interconnects](#API_DescribeInterconnects_ResponseSyntax) **   <a name="DX-DescribeInterconnects-response-interconnects"></a>
The interconnects.
Type: Array of [Interconnect](API_Interconnect.md) objects

 ** [nextToken](#API_DescribeInterconnects_ResponseSyntax) **   <a name="DX-DescribeInterconnects-response-nextToken"></a>
The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

## Errors
<a name="API_DescribeInterconnects_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DirectConnectClientException **
One or more parameters are not valid.
HTTP Status Code: 400

 ** DirectConnectServerException **
A server-side error occurred.
HTTP Status Code: 400

## See Also
<a name="API_DescribeInterconnects_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/directconnect-2012-10-25/DescribeInterconnects)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/directconnect-2012-10-25/DescribeInterconnects)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/DescribeInterconnects)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/directconnect-2012-10-25/DescribeInterconnects)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/DescribeInterconnects)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/directconnect-2012-10-25/DescribeInterconnects)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/directconnect-2012-10-25/DescribeInterconnects)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/directconnect-2012-10-25/DescribeInterconnects)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/directconnect-2012-10-25/DescribeInterconnects)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/DescribeInterconnects)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Direct Connect Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query directconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
