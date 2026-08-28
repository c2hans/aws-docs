---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_CancelOrder.html
---

# CancelOrder
<a name="API_CancelOrder"></a>

Cancels the specified order for an Outpost.

## Request Syntax
<a name="API_CancelOrder_RequestSyntax"></a>

```
POST /orders/{{OrderId}}/cancel HTTP/1.1
```

## URI Request Parameters
<a name="API_CancelOrder_RequestParameters"></a>

The request uses the following URI parameters.

 ** [OrderId](#API_CancelOrder_RequestSyntax) **   <a name="outposts-CancelOrder-request-uri-OrderId"></a>
 The ID of the order.
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `oo-[a-f0-9]{17}$`
Required: Yes

## Request Body
<a name="API_CancelOrder_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_CancelOrder_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_CancelOrder_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_CancelOrder_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have permission to perform this operation.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting this resource can cause an inconsistent state.
 ** ResourceId **
The ID of the resource causing the conflict.
 ** ResourceType **
The type of the resource causing the conflict.
HTTP Status Code: 409

 ** InternalServerException **
An internal error has occurred.
HTTP Status Code: 500

 ** NotFoundException **
The specified request is not valid.
HTTP Status Code: 404

 ** ValidationException **
A parameter is not valid.
HTTP Status Code: 400

## See Also
<a name="API_CancelOrder_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/outposts-2019-12-03/CancelOrder)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/outposts-2019-12-03/CancelOrder)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/CancelOrder)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/outposts-2019-12-03/CancelOrder)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/CancelOrder)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/outposts-2019-12-03/CancelOrder)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/outposts-2019-12-03/CancelOrder)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/outposts-2019-12-03/CancelOrder)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/outposts-2019-12-03/CancelOrder)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/CancelOrder)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Outposts. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query outposts` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
