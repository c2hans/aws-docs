---
source_url: https://docs.aws.amazon.com/license-manager/latest/APIReference/API_ListResourceInventory.html
---

# ListResourceInventory
<a name="API_ListResourceInventory"></a>

Lists resources managed using Systems Manager inventory.

## Request Syntax
<a name="API_ListResourceInventory_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Condition": "{{string}}",
         "Name": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListResourceInventory_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_ListResourceInventory_RequestSyntax) **   <a name="licensemanager-ListResourceInventory-request-Filters"></a>
Filters to scope the results. The following filters and logical operators are supported:
+  `account_id` - The ID of the AWS account that owns the resource. Logical operators are `EQUALS` \| `NOT_EQUALS`.
+  `application_name` - The name of the application. Logical operators are `EQUALS` \| `BEGINS_WITH`.
+  `license_included` - The type of license included. Logical operators are `EQUALS` \| `NOT_EQUALS`. Possible values are `sql-server-enterprise` \| `sql-server-standard` \| `sql-server-web` \| `windows-server-datacenter`.
+  `platform` - The platform of the resource. Logical operators are `EQUALS` \| `BEGINS_WITH`.
+  `resource_id` - The ID of the resource. Logical operators are `EQUALS` \| `NOT_EQUALS`.
+  `tag:<key>` - The key/value combination of a tag assigned to the resource. Logical operators are `EQUALS` (single account) or `EQUALS` \| `NOT_EQUALS` (cross account).
Type: Array of [InventoryFilter](API_InventoryFilter.md) objects
Required: No

 ** [MaxResults](#API_ListResourceInventory_RequestSyntax) **   <a name="licensemanager-ListResourceInventory-request-MaxResults"></a>
Maximum number of results to return in a single call.
Type: Integer
Required: No

 ** [NextToken](#API_ListResourceInventory_RequestSyntax) **   <a name="licensemanager-ListResourceInventory-request-NextToken"></a>
Token for the next set of results.
Type: String
Required: No

## Response Syntax
<a name="API_ListResourceInventory_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "ResourceInventoryList": [
      {
         "AmiId": "string",
         "HostId": "string",
         "InstanceType": "string",
         "MarketplaceProductCodes": [ "string" ],
         "Platform": "string",
         "PlatformVersion": "string",
         "Region": "string",
         "ResourceArn": "string",
         "ResourceId": "string",
         "ResourceOwningAccountId": "string",
         "ResourceType": "string",
         "UsageOperation": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListResourceInventory_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListResourceInventory_ResponseSyntax) **   <a name="licensemanager-ListResourceInventory-response-NextToken"></a>
Token for the next set of results.
Type: String

 ** [ResourceInventoryList](#API_ListResourceInventory_ResponseSyntax) **   <a name="licensemanager-ListResourceInventory-response-ResourceInventoryList"></a>
Information about the resources.
Type: Array of [ResourceInventory](API_ResourceInventory.md) objects

## Errors
<a name="API_ListResourceInventory_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to resource denied.
HTTP Status Code: 400

 ** AuthorizationException **
The AWS user account does not have permission to perform the action. Check the IAM policy associated with this account.
HTTP Status Code: 400

 ** FailedDependencyException **
A dependency required to run the API is missing.
HTTP Status Code: 400

 ** FilterLimitExceededException **
The request uses too many filters or too many filter values.
HTTP Status Code: 400

 ** InvalidParameterValueException **
One or more parameter values are not valid.
HTTP Status Code: 400

 ** RateLimitExceededException **
Too many requests have been submitted. Try again after a brief wait.
HTTP Status Code: 400

 ** ServerInternalException **
The server experienced an internal error. Try again.
HTTP Status Code: 500

## See Also
<a name="API_ListResourceInventory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/license-manager-2018-08-01/ListResourceInventory)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/license-manager-2018-08-01/ListResourceInventory)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-2018-08-01/ListResourceInventory)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/license-manager-2018-08-01/ListResourceInventory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-2018-08-01/ListResourceInventory)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/license-manager-2018-08-01/ListResourceInventory)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/license-manager-2018-08-01/ListResourceInventory)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/license-manager-2018-08-01/ListResourceInventory)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/license-manager-2018-08-01/ListResourceInventory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-2018-08-01/ListResourceInventory)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS License Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query license-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
