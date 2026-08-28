---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_ListIngressPoints.html
---

# ListIngressPoints
<a name="API_ListIngressPoints"></a>

List all ingress endpoint resources.

## Request Syntax
<a name="API_ListIngressPoints_RequestSyntax"></a>

```
{
   "NextToken": "{{string}}",
   "PageSize": {{number}}
}
```

## Request Parameters
<a name="API_ListIngressPoints_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [NextToken](#API_ListIngressPoints_RequestSyntax) **   <a name="sesmailmanager-ListIngressPoints-request-NextToken"></a>
If you received a pagination token from a previous call to this API, you can provide it here to continue paginating through the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [PageSize](#API_ListIngressPoints_RequestSyntax) **   <a name="sesmailmanager-ListIngressPoints-request-PageSize"></a>
The maximum number of ingress endpoint resources that are returned per call. You can use NextToken to obtain further ingress endpoints.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

## Response Syntax
<a name="API_ListIngressPoints_ResponseSyntax"></a>

```
{
   "IngressPoints": [
      {
         "ARecord": "string",
         "IngressPointId": "string",
         "IngressPointName": "string",
         "Status": "string",
         "Type": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListIngressPoints_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [IngressPoints](#API_ListIngressPoints_ResponseSyntax) **   <a name="sesmailmanager-ListIngressPoints-response-IngressPoints"></a>
The list of ingress endpoints.
Type: Array of [IngressPoint](API_IngressPoint.md) objects

 ** [NextToken](#API_ListIngressPoints_ResponseSyntax) **   <a name="sesmailmanager-ListIngressPoints-response-NextToken"></a>
If NextToken is returned, there are more results available. The value of NextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_ListIngressPoints_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ValidationException **
The request validation has failed. For details, see the accompanying error message.
HTTP Status Code: 400

## See Also
<a name="API_ListIngressPoints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mailmanager-2023-10-17/ListIngressPoints)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mailmanager-2023-10-17/ListIngressPoints)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/ListIngressPoints)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mailmanager-2023-10-17/ListIngressPoints)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/ListIngressPoints)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mailmanager-2023-10-17/ListIngressPoints)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mailmanager-2023-10-17/ListIngressPoints)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mailmanager-2023-10-17/ListIngressPoints)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mailmanager-2023-10-17/ListIngressPoints)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/ListIngressPoints)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Mail Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sesmailmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
