---
source_url: https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_GetPortfolioPreferences.html
---

# GetPortfolioPreferences
<a name="API_GetPortfolioPreferences"></a>

**Note**
 AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Migration Hub](https://aws.amazon.com/transform).

 Retrieves your migration and modernization preferences.

## Request Syntax
<a name="API_GetPortfolioPreferences_RequestSyntax"></a>

```
GET /get-portfolio-preferences HTTP/1.1
```

## URI Request Parameters
<a name="API_GetPortfolioPreferences_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetPortfolioPreferences_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetPortfolioPreferences_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "applicationMode": "string",
   "applicationPreferences": {
      "managementPreference": { ... }
   },
   "databasePreferences": {
      "databaseManagementPreference": "string",
      "databaseMigrationPreference": { ... }
   },
   "prioritizeBusinessGoals": {
      "businessGoals": {
         "licenseCostReduction": number,
         "modernizeInfrastructureWithCloudNativeTechnologies": number,
         "reduceOperationalOverheadWithManagedServices": number,
         "speedOfMigration": number
      }
   }
}
```

## Response Elements
<a name="API_GetPortfolioPreferences_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [applicationMode](#API_GetPortfolioPreferences_ResponseSyntax) **   <a name="migrationhubstrategy-GetPortfolioPreferences-response-applicationMode"></a>
The classification for application component types.
Type: String
Valid Values: `ALL | KNOWN | UNKNOWN`

 ** [applicationPreferences](#API_GetPortfolioPreferences_ResponseSyntax) **   <a name="migrationhubstrategy-GetPortfolioPreferences-response-applicationPreferences"></a>
 The transformation preferences for non-database applications.
Type: [ApplicationPreferences](API_ApplicationPreferences.md) object

 ** [databasePreferences](#API_GetPortfolioPreferences_ResponseSyntax) **   <a name="migrationhubstrategy-GetPortfolioPreferences-response-databasePreferences"></a>
 The transformation preferences for database applications.
Type: [DatabasePreferences](API_DatabasePreferences.md) object

 ** [prioritizeBusinessGoals](#API_GetPortfolioPreferences_ResponseSyntax) **   <a name="migrationhubstrategy-GetPortfolioPreferences-response-prioritizeBusinessGoals"></a>
 The rank of business goals based on priority.
Type: [PrioritizeBusinessGoals](API_PrioritizeBusinessGoals.md) object

## Errors
<a name="API_GetPortfolioPreferences_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 The user does not have permission to perform the action. Check the AWS Identity and Access Management (IAM) policy associated with this user.
HTTP Status Code: 403

 ** InternalServerException **
 The server experienced an internal error. Try again.
HTTP Status Code: 500

 ** ResourceNotFoundException **
 The specified ID in the request is not found.
HTTP Status Code: 404

 ** ThrottlingException **
 The request was denied due to request throttling.
HTTP Status Code: 429

## See Also
<a name="API_GetPortfolioPreferences_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/migrationhubstrategy-2020-02-19/GetPortfolioPreferences)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/migrationhubstrategy-2020-02-19/GetPortfolioPreferences)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhubstrategy-2020-02-19/GetPortfolioPreferences)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/migrationhubstrategy-2020-02-19/GetPortfolioPreferences)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhubstrategy-2020-02-19/GetPortfolioPreferences)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/migrationhubstrategy-2020-02-19/GetPortfolioPreferences)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/migrationhubstrategy-2020-02-19/GetPortfolioPreferences)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/migrationhubstrategy-2020-02-19/GetPortfolioPreferences)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/migrationhubstrategy-2020-02-19/GetPortfolioPreferences)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhubstrategy-2020-02-19/GetPortfolioPreferences)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Hub Strategy Recommendations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-strategy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
