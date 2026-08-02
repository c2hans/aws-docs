---
source_url: https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_UriPathRouteInput.html
---

# UriPathRouteInput
<a name="API_UriPathRouteInput"></a>

The configuration for the URI path route type.

## Contents
<a name="API_UriPathRouteInput_Contents"></a>

 ** ActivationState **   <a name="migrationhubrefactorspaces-Type-UriPathRouteInput-ActivationState"></a>
If set to `ACTIVE`, traffic is forwarded to this route’s service after the route is created.
Type: String
Valid Values: `ACTIVE | INACTIVE`
Required: Yes

 ** SourcePath **   <a name="migrationhubrefactorspaces-Type-UriPathRouteInput-SourcePath"></a>
This is the path that Refactor Spaces uses to match traffic. Paths must start with `/` and are relative to the base of the application. To use path parameters in the source path, add a variable in curly braces. For example, the resource path {user} represents a path parameter called 'user'.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `(/([a-zA-Z0-9._:-]+|\{[a-zA-Z0-9._:-]+\}))+`
Required: Yes

 ** AppendSourcePath **   <a name="migrationhubrefactorspaces-Type-UriPathRouteInput-AppendSourcePath"></a>
If set to `true`, this option appends the source path to the service URL endpoint.
Type: Boolean
Required: No

 ** IncludeChildPaths **   <a name="migrationhubrefactorspaces-Type-UriPathRouteInput-IncludeChildPaths"></a>
Indicates whether to match all subpaths of the given source path. If this value is `false`, requests must match the source path exactly before they are forwarded to this route's service.
Type: Boolean
Required: No

 ** Methods **   <a name="migrationhubrefactorspaces-Type-UriPathRouteInput-Methods"></a>
A list of HTTP methods to match. An empty list matches all values. If a method is present, only HTTP requests using that method are forwarded to this route’s service.
Type: Array of strings
Valid Values: `DELETE | GET | HEAD | OPTIONS | PATCH | POST | PUT`
Required: No

## See Also
<a name="API_UriPathRouteInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migration-hub-refactor-spaces-2021-10-26/UriPathRouteInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migration-hub-refactor-spaces-2021-10-26/UriPathRouteInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migration-hub-refactor-spaces-2021-10-26/UriPathRouteInput)
