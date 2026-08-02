---
source_url: https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_CreateRoute.html
---

# CreateRoute
<a name="API_CreateRoute"></a>

**Note**
 AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Migration Hub](https://aws.amazon.com/transform).

Creates an AWS Migration Hub Refactor Spaces route. The account owner of the service resource is always the environment owner, regardless of which account creates the route. Routes target a service in the application. If an application does not have any routes, then the first route must be created as a `DEFAULT` `RouteType`.

When created, the default route defaults to an active state. Therefore, state is not a required input. However, like all other state values, the state of the default route can be updated after creation, but only when all other routes are also inactive. Conversely, no route can be active without the default route also being active.

Refactor Spaces supports routes with [path parameters](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-routes.html). Path parameters are contained in curly braces. For example: `/users/{id}`, where `{id}` represents the parameter that is forwarded to the service. When using path parameters with Lambda services, the path parameters are parsed by API Gateway and are added to the Lambda [event object](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format).

When you create a route, Refactor Spaces configures the Amazon API Gateway to send traffic to the target service as follows:
+  **URL Endpoints**

  If the service has a URL endpoint, and the endpoint resolves to a private IP address, Refactor Spaces routes traffic using the API Gateway VPC link. If a service endpoint resolves to a public IP address, Refactor Spaces routes traffic over the public internet. Services can have HTTP or HTTPS URL endpoints. For HTTPS URLs, publicly-signed certificates are supported. Private Certificate Authorities (CAs) are permitted only if the CA's domain is also publicly resolvable.

  Refactor Spaces automatically resolves the public Domain Name System (DNS) names that are set in `CreateService:UrlEndpoint `when you create a service. The DNS names resolve when the DNS time-to-live (TTL) expires, or every 60 seconds for TTLs less than 60 seconds. This periodic DNS resolution ensures that the route configuration remains up-to-date.

  When using path parameters for URL endpoints, you must set AppendSourcePath to TRUE for Refactor Spaces to append the source path to the destination service URL endpoint. For example, given a service endpoint URL of `http://pets-svc/petclinic/api` and a route source path of `/pets/{id}`, Refactor Spaces appends the source path to the service endpoint URL. The path routed to the service will be `http://pets-svc/petclinic/api/pets/{id}`.For URL endpoints, your service must parse the parameters.

+  **One-time health check**

  A one-time health check is performed on the service when either the route is updated from inactive to active, or when it is created with an active state. If the health check fails, the route transitions the route state to `FAILED`, an error code of `SERVICE_ENDPOINT_HEALTH_CHECK_FAILURE` is provided, and no traffic is sent to the service.

  For private URLs, a target group is created on the Network Load Balancer and the load balancer target group runs default target health checks. By default, the health check is run against the service endpoint URL. Optionally, the health check can be performed against a different protocol, port, and/or path using the [CreateService:UrlEndpoint](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_CreateService.html#migrationhubrefactorspaces-CreateService-request-UrlEndpoint) parameter. All other health check settings for the load balancer use the default values described in the [Health checks for your target groups](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/target-group-health-checks.html) in the *Elastic Load Balancing guide*. The health check is considered successful if at least one target within the target group transitions to a healthy state.

+  ** AWS Lambda function endpoints**

  If the service has an AWS Lambda function endpoint, then Refactor Spaces configures the Lambda function's resource policy to allow the application's API Gateway to invoke the function.

  The Lambda function state is checked. If the function is not active, the function configuration is updated so that Lambda resources are provisioned. If the Lambda state is `Failed`, then the route creation fails. For more information, see the [GetFunctionConfiguration's State response parameter](https://docs.aws.amazon.com/lambda/latest/dg/API_GetFunctionConfiguration.html#SSS-GetFunctionConfiguration-response-State) in the * AWS Lambda Developer Guide*.

  A check is performed to determine that a AWS Lambda function with the specified ARN exists. If it does not exist, the health check fails. For public URLs, a connection is opened to the public endpoint. If the URL is not reachable, the health check fails.

  When using path parameters with AWS Lambda function endpoints, the path parameters are parsed by API Gateway and are added to the Lambda event object.

 **Environments without a network bridge**

When you create environments without a network bridge ([CreateEnvironment:NetworkFabricType](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_CreateEnvironment.html#migrationhubrefactorspaces-CreateEnvironment-request-NetworkFabricType) is `NONE)` and you use your own networking infrastructure, you need to configure [VPC to VPC connectivity](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/amazon-vpc-to-amazon-vpc-connectivity-options.html) between your network and the application proxy VPC. Route creation from the application proxy to service endpoints will fail if your network is not configured to connect to the application proxy VPC. For more information, see [ Create a route](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/userguide/getting-started-create-role.html) in the *Refactor Spaces User Guide*.

## Request Syntax
<a name="API_CreateRoute_RequestSyntax"></a>

```
POST /environments/{{EnvironmentIdentifier}}/applications/{{ApplicationIdentifier}}/routes HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "DefaultRoute": {
      "ActivationState": "{{string}}"
   },
   "RouteType": "{{string}}",
   "ServiceIdentifier": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   },
   "UriPathRoute": {
      "ActivationState": "{{string}}",
      "AppendSourcePath": {{boolean}},
      "IncludeChildPaths": {{boolean}},
      "Methods": [ "{{string}}" ],
      "SourcePath": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateRoute_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ApplicationIdentifier](#API_CreateRoute_RequestSyntax) **   <a name="migrationhubrefactorspaces-CreateRoute-request-uri-ApplicationIdentifier"></a>
The ID of the application within which the route is being created.
Length Constraints: Fixed length of 14.
Pattern: `app-[0-9A-Za-z]{10}`
Required: Yes

 ** [EnvironmentIdentifier](#API_CreateRoute_RequestSyntax) **   <a name="migrationhubrefactorspaces-CreateRoute-request-uri-EnvironmentIdentifier"></a>
The ID of the environment in which the route is created.
Length Constraints: Fixed length of 14.
Pattern: `env-[0-9A-Za-z]{10}`
Required: Yes

## Request Body
<a name="API_CreateRoute_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateRoute_RequestSyntax) **   <a name="migrationhubrefactorspaces-CreateRoute-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\x20-\x7E]{1,64}`
Required: No

 ** [DefaultRoute](#API_CreateRoute_RequestSyntax) **   <a name="migrationhubrefactorspaces-CreateRoute-request-DefaultRoute"></a>
 Configuration for the default route type.
Type: [DefaultRouteInput](API_DefaultRouteInput.md) object
Required: No

 ** [RouteType](#API_CreateRoute_RequestSyntax) **   <a name="migrationhubrefactorspaces-CreateRoute-request-RouteType"></a>
The route type of the route. `DEFAULT` indicates that all traffic that does not match another route is forwarded to the default route. Applications must have a default route before any other routes can be created. `URI_PATH` indicates a route that is based on a URI path.
Type: String
Valid Values: `DEFAULT | URI_PATH`
Required: Yes

 ** [ServiceIdentifier](#API_CreateRoute_RequestSyntax) **   <a name="migrationhubrefactorspaces-CreateRoute-request-ServiceIdentifier"></a>
The ID of the service in which the route is created. Traffic that matches this route is forwarded to this service.
Type: String
Length Constraints: Fixed length of 14.
Pattern: `svc-[0-9A-Za-z]{10}`
Required: Yes

 ** [Tags](#API_CreateRoute_RequestSyntax) **   <a name="migrationhubrefactorspaces-CreateRoute-request-Tags"></a>
The tags to assign to the route. A tag is a label that you assign to an AWS resource. Each tag consists of a key-value pair..
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:).+.*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [UriPathRoute](#API_CreateRoute_RequestSyntax) **   <a name="migrationhubrefactorspaces-CreateRoute-request-UriPathRoute"></a>
The configuration for the URI path route type.
Type: [UriPathRouteInput](API_UriPathRouteInput.md) object
Required: No

## Response Syntax
<a name="API_CreateRoute_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ApplicationId": "string",
   "Arn": "string",
   "CreatedByAccountId": "string",
   "CreatedTime": number,
   "LastUpdatedTime": number,
   "OwnerAccountId": "string",
   "RouteId": "string",
   "RouteType": "string",
   "ServiceId": "string",
   "State": "string",
   "Tags": {
      "string" : "string"
   },
   "UriPathRoute": {
      "ActivationState": "string",
      "AppendSourcePath": boolean,
      "IncludeChildPaths": boolean,
      "Methods": [ "string" ],
      "SourcePath": "string"
   }
}
```

## Response Elements
<a name="API_CreateRoute_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApplicationId](#API_CreateRoute_ResponseSyntax) **   <a name="migrationhubrefactorspaces-CreateRoute-response-ApplicationId"></a>
The ID of the application in which the route is created.
Type: String
Length Constraints: Fixed length of 14.
Pattern: `app-[0-9A-Za-z]{10}`

 ** [Arn](#API_CreateRoute_ResponseSyntax) **   <a name="migrationhubrefactorspaces-CreateRoute-response-Arn"></a>
The Amazon Resource Name (ARN) of the route. The format for this ARN is `arn:aws:refactor-spaces:region:account-id:resource-type/resource-id `. For more information about ARNs, see [ Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws:refactor-spaces:[a-zA-Z0-9\-]+:\w{12}:[a-zA-Z_0-9+=,.@\-_/]+`

 ** [CreatedByAccountId](#API_CreateRoute_ResponseSyntax) **   <a name="migrationhubrefactorspaces-CreateRoute-response-CreatedByAccountId"></a>
The AWS account ID of the route creator.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`

 ** [CreatedTime](#API_CreateRoute_ResponseSyntax) **   <a name="migrationhubrefactorspaces-CreateRoute-response-CreatedTime"></a>
A timestamp that indicates when the route is created.
Type: Timestamp

 ** [LastUpdatedTime](#API_CreateRoute_ResponseSyntax) **   <a name="migrationhubrefactorspaces-CreateRoute-response-LastUpdatedTime"></a>
A timestamp that indicates when the route was last updated.
Type: Timestamp

 ** [OwnerAccountId](#API_CreateRoute_ResponseSyntax) **   <a name="migrationhubrefactorspaces-CreateRoute-response-OwnerAccountId"></a>
The AWS account ID of the route owner.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`

 ** [RouteId](#API_CreateRoute_ResponseSyntax) **   <a name="migrationhubrefactorspaces-CreateRoute-response-RouteId"></a>
The unique identifier of the route.
Type: String
Length Constraints: Fixed length of 14.
Pattern: `rte-[0-9A-Za-z]{10}`

 ** [RouteType](#API_CreateRoute_ResponseSyntax) **   <a name="migrationhubrefactorspaces-CreateRoute-response-RouteType"></a>
The route type of the route.
Type: String
Valid Values: `DEFAULT | URI_PATH`

 ** [ServiceId](#API_CreateRoute_ResponseSyntax) **   <a name="migrationhubrefactorspaces-CreateRoute-response-ServiceId"></a>
The ID of service in which the route is created. Traffic that matches this route is forwarded to this service.
Type: String
Length Constraints: Fixed length of 14.
Pattern: `svc-[0-9A-Za-z]{10}`

 ** [State](#API_CreateRoute_ResponseSyntax) **   <a name="migrationhubrefactorspaces-CreateRoute-response-State"></a>
The current state of the route. Activation state only allows `ACTIVE` or `INACTIVE` as user inputs. `FAILED` is a route state that is system generated.
Type: String
Valid Values: `CREATING | ACTIVE | DELETING | FAILED | UPDATING | INACTIVE`

 ** [Tags](#API_CreateRoute_ResponseSyntax) **   <a name="migrationhubrefactorspaces-CreateRoute-response-Tags"></a>
The tags assigned to the created route. A tag is a label that you assign to an AWS resource. Each tag consists of a key-value pair.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:).+.*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [UriPathRoute](#API_CreateRoute_ResponseSyntax) **   <a name="migrationhubrefactorspaces-CreateRoute-response-UriPathRoute"></a>
Configuration for the URI path route type.
Type: [UriPathRouteInput](API_UriPathRouteInput.md) object

## Errors
<a name="API_CreateRoute_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
 ** ResourceId **
The ID of the resource.
 ** ResourceType **
The type of resource.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error occurred while processing the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request references a resource that does not exist.
 ** ResourceId **
The ID of the resource.
 ** ResourceType **
The type of resource.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request would cause a service quota to be exceeded.
 ** QuotaCode **
Service quota requirement to identify originating quota. Reached throttling quota exception.
 ** ResourceId **
The ID of the resource.
 ** ResourceType **
The type of resource.
 ** ServiceCode **
Service quota requirement to identify originating service. Reached throttling quota exception service code.
HTTP Status Code: 402

 ** ThrottlingException **
Request was denied because the request was throttled.
 ** QuotaCode **
Service quota requirement to identify originating quota. Reached throttling quota exception.
 ** RetryAfterSeconds **
The number of seconds to wait before retrying.
 ** ServiceCode **
Service quota requirement to identify originating service. Reached throttling quota exception service code.
HTTP Status Code: 429

 ** ValidationException **
The input does not satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_CreateRoute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/migration-hub-refactor-spaces-2021-10-26/CreateRoute)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/migration-hub-refactor-spaces-2021-10-26/CreateRoute)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migration-hub-refactor-spaces-2021-10-26/CreateRoute)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/migration-hub-refactor-spaces-2021-10-26/CreateRoute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migration-hub-refactor-spaces-2021-10-26/CreateRoute)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/migration-hub-refactor-spaces-2021-10-26/CreateRoute)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/migration-hub-refactor-spaces-2021-10-26/CreateRoute)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/migration-hub-refactor-spaces-2021-10-26/CreateRoute)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/migration-hub-refactor-spaces-2021-10-26/CreateRoute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migration-hub-refactor-spaces-2021-10-26/CreateRoute)
