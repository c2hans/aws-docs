---
source_url: https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_PutPortfolioPreferences.html
---

# PutPortfolioPreferences
<a name="API_PutPortfolioPreferences"></a>

**Note**
 AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Migration Hub](https://aws.amazon.com/transform).

 Saves the specified migration and modernization preferences.

## Request Syntax
<a name="API_PutPortfolioPreferences_RequestSyntax"></a>

```
POST /put-portfolio-preferences HTTP/1.1
Content-type: application/json

{
   "applicationMode": "{{string}}",
   "applicationPreferences": {
      "managementPreference": { ... }
   },
   "databasePreferences": {
      "databaseManagementPreference": "{{string}}",
      "databaseMigrationPreference": { ... }
   },
   "prioritizeBusinessGoals": {
      "businessGoals": {
         "licenseCostReduction": {{number}},
         "modernizeInfrastructureWithCloudNativeTechnologies": {{number}},
         "reduceOperationalOverheadWithManagedServices": {{number}},
         "speedOfMigration": {{number}}
      }
   }
}
```

## URI Request Parameters
<a name="API_PutPortfolioPreferences_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_PutPortfolioPreferences_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [applicationMode](#API_PutPortfolioPreferences_RequestSyntax) **   <a name="migrationhubstrategy-PutPortfolioPreferences-request-applicationMode"></a>
The classification for application component types.
Type: String
Valid Values: `ALL | KNOWN | UNKNOWN`
Required: No

 ** [applicationPreferences](#API_PutPortfolioPreferences_RequestSyntax) **   <a name="migrationhubstrategy-PutPortfolioPreferences-request-applicationPreferences"></a>
 The transformation preferences for non-database applications.
Type: [ApplicationPreferences](API_ApplicationPreferences.md) object
Required: No

 ** [databasePreferences](#API_PutPortfolioPreferences_RequestSyntax) **   <a name="migrationhubstrategy-PutPortfolioPreferences-request-databasePreferences"></a>
 The transformation preferences for database applications.
Type: [DatabasePreferences](API_DatabasePreferences.md) object
Required: No

 ** [prioritizeBusinessGoals](#API_PutPortfolioPreferences_RequestSyntax) **   <a name="migrationhubstrategy-PutPortfolioPreferences-request-prioritizeBusinessGoals"></a>
 The rank of the business goals based on priority.
Type: [PrioritizeBusinessGoals](API_PrioritizeBusinessGoals.md) object
Required: No

## Response Syntax
<a name="API_PutPortfolioPreferences_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_PutPortfolioPreferences_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutPortfolioPreferences_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 The user does not have permission to perform the action. Check the AWS Identity and Access Management (IAM) policy associated with this user.
HTTP Status Code: 403

 ** ConflictException **
 Exception to indicate that there is an ongoing task when a new task is created. Return when once the existing tasks are complete.
HTTP Status Code: 409

 ** InternalServerException **
 The server experienced an internal error. Try again.
HTTP Status Code: 500

 ** ThrottlingException **
 The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
 The request body isn't valid.
HTTP Status Code: 400

## See Also
<a name="API_PutPortfolioPreferences_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/migrationhubstrategy-2020-02-19/PutPortfolioPreferences)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/migrationhubstrategy-2020-02-19/PutPortfolioPreferences)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhubstrategy-2020-02-19/PutPortfolioPreferences)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/migrationhubstrategy-2020-02-19/PutPortfolioPreferences)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhubstrategy-2020-02-19/PutPortfolioPreferences)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/migrationhubstrategy-2020-02-19/PutPortfolioPreferences)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/migrationhubstrategy-2020-02-19/PutPortfolioPreferences)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/migrationhubstrategy-2020-02-19/PutPortfolioPreferences)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/migrationhubstrategy-2020-02-19/PutPortfolioPreferences)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhubstrategy-2020-02-19/PutPortfolioPreferences)
