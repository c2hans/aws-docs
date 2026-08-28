---
source_url: https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_ListResourcesAssociatedToCustomLineItem.html
---

# ListResourcesAssociatedToCustomLineItem
<a name="API_ListResourcesAssociatedToCustomLineItem"></a>

 List the resources that are associated to a custom line item.

## Request Syntax
<a name="API_ListResourcesAssociatedToCustomLineItem_RequestSyntax"></a>

```
POST /list-resources-associated-to-custom-line-item HTTP/1.1
Content-type: application/json

{
   "Arn": "{{string}}",
   "BillingPeriod": "{{string}}",
   "Filters": {
      "Relationship": "{{string}}"
   },
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListResourcesAssociatedToCustomLineItem_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListResourcesAssociatedToCustomLineItem_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Arn](#API_ListResourcesAssociatedToCustomLineItem_RequestSyntax) **   <a name="billingconductor-ListResourcesAssociatedToCustomLineItem-request-Arn"></a>
 The ARN of the custom line item for which the resource associations will be listed.
Type: String
Pattern: `(arn:aws(-cn)?:billingconductor::[0-9]{12}:customlineitem/)?[a-zA-Z0-9]{10}`
Required: Yes

 ** [BillingPeriod](#API_ListResourcesAssociatedToCustomLineItem_RequestSyntax) **   <a name="billingconductor-ListResourcesAssociatedToCustomLineItem-request-BillingPeriod"></a>
 The billing period for which the resource associations will be listed.
Type: String
Pattern: `\d{4}-(0?[1-9]|1[012])`
Required: No

 ** [Filters](#API_ListResourcesAssociatedToCustomLineItem_RequestSyntax) **   <a name="billingconductor-ListResourcesAssociatedToCustomLineItem-request-Filters"></a>
 (Optional) A `ListResourcesAssociatedToCustomLineItemFilter` that can specify the types of resources that should be retrieved.
Type: [ListResourcesAssociatedToCustomLineItemFilter](API_ListResourcesAssociatedToCustomLineItemFilter.md) object
Required: No

 ** [MaxResults](#API_ListResourcesAssociatedToCustomLineItem_RequestSyntax) **   <a name="billingconductor-ListResourcesAssociatedToCustomLineItem-request-MaxResults"></a>
 (Optional) The maximum number of resource associations to be retrieved.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListResourcesAssociatedToCustomLineItem_RequestSyntax) **   <a name="billingconductor-ListResourcesAssociatedToCustomLineItem-request-NextToken"></a>
 (Optional) The pagination token that's returned by a previous request.
Type: String
Required: No

## Response Syntax
<a name="API_ListResourcesAssociatedToCustomLineItem_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "AssociatedResources": [
      {
         "Arn": "string",
         "EndBillingPeriod": "string",
         "Relationship": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListResourcesAssociatedToCustomLineItem_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_ListResourcesAssociatedToCustomLineItem_ResponseSyntax) **   <a name="billingconductor-ListResourcesAssociatedToCustomLineItem-response-Arn"></a>
 The custom line item ARN for which the resource associations are listed.
Type: String
Pattern: `(arn:aws(-cn)?:billingconductor::[0-9]{12}:customlineitem/)?[a-zA-Z0-9]{10}`

 ** [AssociatedResources](#API_ListResourcesAssociatedToCustomLineItem_ResponseSyntax) **   <a name="billingconductor-ListResourcesAssociatedToCustomLineItem-response-AssociatedResources"></a>
 A list of `ListResourcesAssociatedToCustomLineItemResponseElement` for each resource association retrieved.
Type: Array of [ListResourcesAssociatedToCustomLineItemResponseElement](API_ListResourcesAssociatedToCustomLineItemResponseElement.md) objects

 ** [NextToken](#API_ListResourcesAssociatedToCustomLineItem_ResponseSyntax) **   <a name="billingconductor-ListResourcesAssociatedToCustomLineItem-response-NextToken"></a>
 The pagination token to be used in subsequent requests to retrieve additional results.
Type: String

## Errors
<a name="API_ListResourcesAssociatedToCustomLineItem_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred while processing a request.
 ** RetryAfterSeconds **
Number of seconds you can retry after the call.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request references a resource that doesn't exist.
 ** ResourceId **
Resource identifier that was not found.
 ** ResourceType **
Resource type that was not found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
 ** RetryAfterSeconds **
Number of seconds you can safely retry after the call.
HTTP Status Code: 429

 ** ValidationException **
The input doesn't match with the constraints specified by AWS services.
 ** Fields **
The fields that caused the error, if applicable.
 ** Reason **
The reason the request's validation failed.
HTTP Status Code: 400

## See Also
<a name="API_ListResourcesAssociatedToCustomLineItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/billingconductor-2021-07-30/ListResourcesAssociatedToCustomLineItem)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/billingconductor-2021-07-30/ListResourcesAssociatedToCustomLineItem)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billingconductor-2021-07-30/ListResourcesAssociatedToCustomLineItem)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/billingconductor-2021-07-30/ListResourcesAssociatedToCustomLineItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billingconductor-2021-07-30/ListResourcesAssociatedToCustomLineItem)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/billingconductor-2021-07-30/ListResourcesAssociatedToCustomLineItem)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/billingconductor-2021-07-30/ListResourcesAssociatedToCustomLineItem)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/billingconductor-2021-07-30/ListResourcesAssociatedToCustomLineItem)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/billingconductor-2021-07-30/ListResourcesAssociatedToCustomLineItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billingconductor-2021-07-30/ListResourcesAssociatedToCustomLineItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Billing Conductor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query billingconductor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
