---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ListCostCategoryResourceAssociations.html
---

# ListCostCategoryResourceAssociations
<a name="API_ListCostCategoryResourceAssociations"></a>

Returns resource associations of all cost categories defined in the account. You have the option to use `CostCategoryArn` to get the association for a specific cost category. `ListCostCategoryResourceAssociations` supports pagination. The request can have a `MaxResults` range up to 100.

## Request Syntax
<a name="API_ListCostCategoryResourceAssociations_RequestSyntax"></a>

```
{
   "CostCategoryArn": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListCostCategoryResourceAssociations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CostCategoryArn](#API_ListCostCategoryResourceAssociations_RequestSyntax) **   <a name="awscostmanagement-ListCostCategoryResourceAssociations-request-CostCategoryArn"></a>
The unique identifier for your cost category.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:[-a-zA-Z0-9/:_]+`
Required: No

 ** [MaxResults](#API_ListCostCategoryResourceAssociations_RequestSyntax) **   <a name="awscostmanagement-ListCostCategoryResourceAssociations-request-MaxResults"></a>
 The number of entries a paginated response contains.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListCostCategoryResourceAssociations_RequestSyntax) **   <a name="awscostmanagement-ListCostCategoryResourceAssociations-request-NextToken"></a>
 The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[\S\s]*`
Required: No

## Response Syntax
<a name="API_ListCostCategoryResourceAssociations_ResponseSyntax"></a>

```
{
   "CostCategoryResourceAssociations": [
      {
         "CostCategoryArn": "string",
         "CostCategoryName": "string",
         "ResourceArn": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListCostCategoryResourceAssociations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CostCategoryResourceAssociations](#API_ListCostCategoryResourceAssociations_ResponseSyntax) **   <a name="awscostmanagement-ListCostCategoryResourceAssociations-response-CostCategoryResourceAssociations"></a>
 A reference to a cost category association that contains information on an associated resource.
Type: Array of [CostCategoryResourceAssociation](API_CostCategoryResourceAssociation.md) objects

 ** [NextToken](#API_ListCostCategoryResourceAssociations_ResponseSyntax) **   <a name="awscostmanagement-ListCostCategoryResourceAssociations-response-NextToken"></a>
 The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[\S\s]*`

## Errors
<a name="API_ListCostCategoryResourceAssociations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** LimitExceededException **
You made too many calls in a short period of time. Try again later.
HTTP Status Code: 400

 ** ResourceNotFoundException **
 The specified ARN in the request doesn't exist.
HTTP Status Code: 400

## Examples
<a name="API_ListCostCategoryResourceAssociations_Examples"></a>

The following is a sample response of the `ListCostCategoryResourceAssociations` operation that you can use to retrieve all associated cost categories and corresponding associated resources.

### Example
<a name="API_ListCostCategoryResourceAssociations_Example_1"></a>

This example illustrates one usage of ListCostCategoryResourceAssociations.

#### Sample Response
<a name="API_ListCostCategoryResourceAssociations_Example_1_Response"></a>

```
{
  "CostCategoryResourceAssociations": [
    {
      "CostCategoryArn": "arn:aws:ce::111122223333:costcategory/f595cb52-91ec-4575-b99f-15829f405ba3",
      "CostCategoryName": "MyCostCategory",
      "ResourceArn": "arn:aws:billing::111122223333:rispgroupsharing/111122223333"
    }
  ]
}
```

## See Also
<a name="API_ListCostCategoryResourceAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ce-2017-10-25/ListCostCategoryResourceAssociations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ce-2017-10-25/ListCostCategoryResourceAssociations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/ListCostCategoryResourceAssociations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ce-2017-10-25/ListCostCategoryResourceAssociations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/ListCostCategoryResourceAssociations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ce-2017-10-25/ListCostCategoryResourceAssociations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ce-2017-10-25/ListCostCategoryResourceAssociations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ce-2017-10-25/ListCostCategoryResourceAssociations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ce-2017-10-25/ListCostCategoryResourceAssociations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/ListCostCategoryResourceAssociations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
