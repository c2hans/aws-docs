---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_Stage.html
---

# Stage
<a name="API_Stage"></a>

Represents a unique identifier for a version of a deployed RestApi that is callable by users.

## Contents
<a name="API_Stage_Contents"></a>

 ** accessLogSettings **   <a name="apigw-Type-Stage-accessLogSettings"></a>
Settings for logging access in this stage.
Type: [AccessLogSettings](API_AccessLogSettings.md) object
Required: No

 ** cacheClusterEnabled **   <a name="apigw-Type-Stage-cacheClusterEnabled"></a>
Specifies whether a cache cluster is enabled for the stage. To activate a method-level cache, set `CachingEnabled` to `true` for a method.
Type: Boolean
Required: No

 ** cacheClusterSize **   <a name="apigw-Type-Stage-cacheClusterSize"></a>
The stage's cache capacity in GB. For more information about choosing a cache size, see [Enabling API caching to enhance responsiveness](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-caching.html).
Type: String
Valid Values: `0.5 | 1.6 | 6.1 | 13.5 | 28.4 | 58.2 | 118 | 237`
Required: No

 ** cacheClusterStatus **   <a name="apigw-Type-Stage-cacheClusterStatus"></a>
The status of the cache cluster for the stage, if enabled.
Type: String
Valid Values: `CREATE_IN_PROGRESS | AVAILABLE | DELETE_IN_PROGRESS | NOT_AVAILABLE | FLUSH_IN_PROGRESS`
Required: No

 ** canarySettings **   <a name="apigw-Type-Stage-canarySettings"></a>
Settings for the canary deployment in this stage.
Type: [CanarySettings](API_CanarySettings.md) object
Required: No

 ** clientCertificateId **   <a name="apigw-Type-Stage-clientCertificateId"></a>
The identifier of a client certificate for an API stage.
Type: String
Required: No

 ** createdDate **   <a name="apigw-Type-Stage-createdDate"></a>
The timestamp when the stage was created.
Type: Timestamp
Required: No

 ** deploymentId **   <a name="apigw-Type-Stage-deploymentId"></a>
The identifier of the Deployment that the stage points to.
Type: String
Required: No

 ** description **   <a name="apigw-Type-Stage-description"></a>
The stage's description.
Type: String
Required: No

 ** documentationVersion **   <a name="apigw-Type-Stage-documentationVersion"></a>
The version of the associated API documentation.
Type: String
Required: No

 ** lastUpdatedDate **   <a name="apigw-Type-Stage-lastUpdatedDate"></a>
The timestamp when the stage last updated.
Type: Timestamp
Required: No

 ** methodSettings **   <a name="apigw-Type-Stage-methodSettings"></a>
A map that defines the method settings for a Stage resource. Keys (designated as `/{method_setting_key` below) are method paths defined as `{resource_path}/{http_method}` for an individual method override, or `/\*/\*` for overriding all methods in the stage.
Type: String to [MethodSetting](API_MethodSetting.md) object map
Required: No

 ** stageName **   <a name="apigw-Type-Stage-stageName"></a>
The name of the stage is the first path segment in the Uniform Resource Identifier (URI) of a call to API Gateway. Stage names can only contain alphanumeric characters, hyphens, and underscores. Maximum length is 128 characters.
Type: String
Required: No

 ** tags **   <a name="apigw-Type-Stage-tags"></a>
The collection of tags. Each tag element is associated with a given resource.
Type: String to string map
Required: No

 ** tracingEnabled **   <a name="apigw-Type-Stage-tracingEnabled"></a>
Specifies whether active tracing with X-ray is enabled for the Stage.
Type: Boolean
Required: No

 ** variables **   <a name="apigw-Type-Stage-variables"></a>
A map that defines the stage variables for a Stage resource. Variable names can have alphanumeric and underscore characters, and the values must match `[A-Za-z0-9-._~:/?#&=,]+`.
Type: String to string map
Required: No

 ** webAclArn **   <a name="apigw-Type-Stage-webAclArn"></a>
The ARN of the WebAcl associated with the Stage.
Type: String
Required: No

## See Also
<a name="API_Stage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/Stage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/Stage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/Stage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
