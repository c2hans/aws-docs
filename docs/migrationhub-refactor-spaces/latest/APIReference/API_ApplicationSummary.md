---
source_url: https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_ApplicationSummary.html
---

# ApplicationSummary
<a name="API_ApplicationSummary"></a>

The list of `ApplicationSummary` objects.

## Contents
<a name="API_ApplicationSummary_Contents"></a>

 ** ApiGatewayProxy **   <a name="migrationhubrefactorspaces-Type-ApplicationSummary-ApiGatewayProxy"></a>
The endpoint URL of the Amazon API Gateway proxy.
Type: [ApiGatewayProxySummary](API_ApiGatewayProxySummary.md) object
Required: No

 ** ApplicationId **   <a name="migrationhubrefactorspaces-Type-ApplicationSummary-ApplicationId"></a>
The unique identifier of the application.
Type: String
Length Constraints: Fixed length of 14.
Pattern: `app-[0-9A-Za-z]{10}`
Required: No

 ** Arn **   <a name="migrationhubrefactorspaces-Type-ApplicationSummary-Arn"></a>
The Amazon Resource Name (ARN) of the application.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws:refactor-spaces:[a-zA-Z0-9\-]+:\w{12}:[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

 ** CreatedByAccountId **   <a name="migrationhubrefactorspaces-Type-ApplicationSummary-CreatedByAccountId"></a>
The AWS account ID of the application creator.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** CreatedTime **   <a name="migrationhubrefactorspaces-Type-ApplicationSummary-CreatedTime"></a>
A timestamp that indicates when the application is created.
Type: Timestamp
Required: No

 ** EnvironmentId **   <a name="migrationhubrefactorspaces-Type-ApplicationSummary-EnvironmentId"></a>
The unique identifier of the environment.
Type: String
Length Constraints: Fixed length of 14.
Pattern: `env-[0-9A-Za-z]{10}`
Required: No

 ** Error **   <a name="migrationhubrefactorspaces-Type-ApplicationSummary-Error"></a>
Any error associated with the application resource.
Type: [ErrorResponse](API_ErrorResponse.md) object
Required: No

 ** LastUpdatedTime **   <a name="migrationhubrefactorspaces-Type-ApplicationSummary-LastUpdatedTime"></a>
A timestamp that indicates when the application was last updated.
Type: Timestamp
Required: No

 ** Name **   <a name="migrationhubrefactorspaces-Type-ApplicationSummary-Name"></a>
The name of the application.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `(?!app-)[a-zA-Z0-9]+[a-zA-Z0-9-_ ]+`
Required: No

 ** OwnerAccountId **   <a name="migrationhubrefactorspaces-Type-ApplicationSummary-OwnerAccountId"></a>
The AWS account ID of the application owner (which is always the same as the environment owner account ID).
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** ProxyType **   <a name="migrationhubrefactorspaces-Type-ApplicationSummary-ProxyType"></a>
The proxy type of the proxy created within the application.
Type: String
Valid Values: `API_GATEWAY`
Required: No

 ** State **   <a name="migrationhubrefactorspaces-Type-ApplicationSummary-State"></a>
The current state of the application.
Type: String
Valid Values: `CREATING | ACTIVE | DELETING | FAILED | UPDATING`
Required: No

 ** Tags **   <a name="migrationhubrefactorspaces-Type-ApplicationSummary-Tags"></a>
The tags assigned to the application.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:).+.*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** VpcId **   <a name="migrationhubrefactorspaces-Type-ApplicationSummary-VpcId"></a>
The ID of the virtual private cloud (VPC).
Type: String
Length Constraints: Minimum length of 12. Maximum length of 21.
Pattern: `vpc-[-a-f0-9]{8}([-a-f0-9]{9})?`
Required: No

## See Also
<a name="API_ApplicationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migration-hub-refactor-spaces-2021-10-26/ApplicationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migration-hub-refactor-spaces-2021-10-26/ApplicationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migration-hub-refactor-spaces-2021-10-26/ApplicationSummary)
