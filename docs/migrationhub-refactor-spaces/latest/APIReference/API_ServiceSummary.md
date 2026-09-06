---
source_url: https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_ServiceSummary.html
---

# ServiceSummary
<a name="API_ServiceSummary"></a>

A summary for the service as a response to `ListServices`.

## Contents
<a name="API_ServiceSummary_Contents"></a>

 ** ApplicationId **   <a name="migrationhubrefactorspaces-Type-ServiceSummary-ApplicationId"></a>
The unique identifier of the application.
Type: String
Length Constraints: Fixed length of 14.
Pattern: `app-[0-9A-Za-z]{10}`
Required: No

 ** Arn **   <a name="migrationhubrefactorspaces-Type-ServiceSummary-Arn"></a>
The Amazon Resource Name (ARN) of the service.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws:refactor-spaces:[a-zA-Z0-9\-]+:\w{12}:[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

 ** CreatedByAccountId **   <a name="migrationhubrefactorspaces-Type-ServiceSummary-CreatedByAccountId"></a>
The AWS account ID of the service creator.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** CreatedTime **   <a name="migrationhubrefactorspaces-Type-ServiceSummary-CreatedTime"></a>
A timestamp that indicates when the service is created.
Type: Timestamp
Required: No

 ** Description **   <a name="migrationhubrefactorspaces-Type-ServiceSummary-Description"></a>
A description of the service.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9-_\s\.\!\*\#\@\']+`
Required: No

 ** EndpointType **   <a name="migrationhubrefactorspaces-Type-ServiceSummary-EndpointType"></a>
The endpoint type of the service.
Type: String
Valid Values: `LAMBDA | URL`
Required: No

 ** EnvironmentId **   <a name="migrationhubrefactorspaces-Type-ServiceSummary-EnvironmentId"></a>
The unique identifier of the environment.
Type: String
Length Constraints: Fixed length of 14.
Pattern: `env-[0-9A-Za-z]{10}`
Required: No

 ** Error **   <a name="migrationhubrefactorspaces-Type-ServiceSummary-Error"></a>
Any error associated with the service resource.
Type: [ErrorResponse](API_ErrorResponse.md) object
Required: No

 ** LambdaEndpoint **   <a name="migrationhubrefactorspaces-Type-ServiceSummary-LambdaEndpoint"></a>
A summary of the configuration for the AWS Lambda endpoint type.
Type: [LambdaEndpointSummary](API_LambdaEndpointSummary.md) object
Required: No

 ** LastUpdatedTime **   <a name="migrationhubrefactorspaces-Type-ServiceSummary-LastUpdatedTime"></a>
A timestamp that indicates when the service was last updated.
Type: Timestamp
Required: No

 ** Name **   <a name="migrationhubrefactorspaces-Type-ServiceSummary-Name"></a>
The name of the service.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `(?!svc-)[a-zA-Z0-9]+[a-zA-Z0-9-_ ]+`
Required: No

 ** OwnerAccountId **   <a name="migrationhubrefactorspaces-Type-ServiceSummary-OwnerAccountId"></a>
The AWS account ID of the service owner.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** ServiceId **   <a name="migrationhubrefactorspaces-Type-ServiceSummary-ServiceId"></a>
The unique identifier of the service.
Type: String
Length Constraints: Fixed length of 14.
Pattern: `svc-[0-9A-Za-z]{10}`
Required: No

 ** State **   <a name="migrationhubrefactorspaces-Type-ServiceSummary-State"></a>
The current state of the service.
Type: String
Valid Values: `CREATING | ACTIVE | DELETING | FAILED`
Required: No

 ** Tags **   <a name="migrationhubrefactorspaces-Type-ServiceSummary-Tags"></a>
The tags assigned to the service.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:).+.*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** UrlEndpoint **   <a name="migrationhubrefactorspaces-Type-ServiceSummary-UrlEndpoint"></a>
The summary of the configuration for the URL endpoint type.
Type: [UrlEndpointSummary](API_UrlEndpointSummary.md) object
Required: No

 ** VpcId **   <a name="migrationhubrefactorspaces-Type-ServiceSummary-VpcId"></a>
The ID of the virtual private cloud (VPC).
Type: String
Length Constraints: Minimum length of 12. Maximum length of 21.
Pattern: `vpc-[-a-f0-9]{8}([-a-f0-9]{9})?`
Required: No

## See Also
<a name="API_ServiceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migration-hub-refactor-spaces-2021-10-26/ServiceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migration-hub-refactor-spaces-2021-10-26/ServiceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migration-hub-refactor-spaces-2021-10-26/ServiceSummary)
