---
source_url: https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_RouteSummary.html
---

# RouteSummary
<a name="API_RouteSummary"></a>

The summary information for the routes as a response to `ListRoutes`.

## Contents
<a name="API_RouteSummary_Contents"></a>

 ** AppendSourcePath **   <a name="migrationhubrefactorspaces-Type-RouteSummary-AppendSourcePath"></a>
If set to `true`, this option appends the source path to the service URL endpoint.
Type: Boolean
Required: No

 ** ApplicationId **   <a name="migrationhubrefactorspaces-Type-RouteSummary-ApplicationId"></a>
The unique identifier of the application.
Type: String
Length Constraints: Fixed length of 14.
Pattern: `app-[0-9A-Za-z]{10}`
Required: No

 ** Arn **   <a name="migrationhubrefactorspaces-Type-RouteSummary-Arn"></a>
The Amazon Resource Name (ARN) of the route.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws:refactor-spaces:[a-zA-Z0-9\-]+:\w{12}:[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

 ** CreatedByAccountId **   <a name="migrationhubrefactorspaces-Type-RouteSummary-CreatedByAccountId"></a>
The AWS account ID of the route creator.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** CreatedTime **   <a name="migrationhubrefactorspaces-Type-RouteSummary-CreatedTime"></a>
A timestamp that indicates when the route is created.
Type: Timestamp
Required: No

 ** EnvironmentId **   <a name="migrationhubrefactorspaces-Type-RouteSummary-EnvironmentId"></a>
The unique identifier of the environment.
Type: String
Length Constraints: Fixed length of 14.
Pattern: `env-[0-9A-Za-z]{10}`
Required: No

 ** Error **   <a name="migrationhubrefactorspaces-Type-RouteSummary-Error"></a>
Any error associated with the route resource.
Type: [ErrorResponse](API_ErrorResponse.md) object
Required: No

 ** IncludeChildPaths **   <a name="migrationhubrefactorspaces-Type-RouteSummary-IncludeChildPaths"></a>
Indicates whether to match all subpaths of the given source path. If this value is `false`, requests must match the source path exactly before they are forwarded to this route's service.
Type: Boolean
Required: No

 ** LastUpdatedTime **   <a name="migrationhubrefactorspaces-Type-RouteSummary-LastUpdatedTime"></a>
A timestamp that indicates when the route was last updated.
Type: Timestamp
Required: No

 ** Methods **   <a name="migrationhubrefactorspaces-Type-RouteSummary-Methods"></a>
A list of HTTP methods to match. An empty list matches all values. If a method is present, only HTTP requests using that method are forwarded to this route’s service.
Type: Array of strings
Valid Values: `DELETE | GET | HEAD | OPTIONS | PATCH | POST | PUT`
Required: No

 ** OwnerAccountId **   <a name="migrationhubrefactorspaces-Type-RouteSummary-OwnerAccountId"></a>
The AWS account ID of the route owner.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** PathResourceToId **   <a name="migrationhubrefactorspaces-Type-RouteSummary-PathResourceToId"></a>
A mapping of Amazon API Gateway path resources to resource IDs.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 2048.
Value Length Constraints: Fixed length of 10.
Value Pattern: `[a-z0-9]{10}`
Required: No

 ** RouteId **   <a name="migrationhubrefactorspaces-Type-RouteSummary-RouteId"></a>
The unique identifier of the route.
Type: String
Length Constraints: Fixed length of 14.
Pattern: `rte-[0-9A-Za-z]{10}`
Required: No

 ** RouteType **   <a name="migrationhubrefactorspaces-Type-RouteSummary-RouteType"></a>
The route type of the route.
Type: String
Valid Values: `DEFAULT | URI_PATH`
Required: No

 ** ServiceId **   <a name="migrationhubrefactorspaces-Type-RouteSummary-ServiceId"></a>
The unique identifier of the service.
Type: String
Length Constraints: Fixed length of 14.
Pattern: `svc-[0-9A-Za-z]{10}`
Required: No

 ** SourcePath **   <a name="migrationhubrefactorspaces-Type-RouteSummary-SourcePath"></a>
This is the path that Refactor Spaces uses to match traffic. Paths must start with `/` and are relative to the base of the application. To use path parameters in the source path, add a variable in curly braces. For example, the resource path {user} represents a path parameter called 'user'.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `(/([a-zA-Z0-9._:-]+|\{[a-zA-Z0-9._:-]+\}))+`
Required: No

 ** State **   <a name="migrationhubrefactorspaces-Type-RouteSummary-State"></a>
The current state of the route.
Type: String
Valid Values: `CREATING | ACTIVE | DELETING | FAILED | UPDATING | INACTIVE`
Required: No

 ** Tags **   <a name="migrationhubrefactorspaces-Type-RouteSummary-Tags"></a>
The tags assigned to the route.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:).+.*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_RouteSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migration-hub-refactor-spaces-2021-10-26/RouteSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migration-hub-refactor-spaces-2021-10-26/RouteSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migration-hub-refactor-spaces-2021-10-26/RouteSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Migration Hub Refactor Spaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-refactor-spaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
