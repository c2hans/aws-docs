---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ApiDestination.html
---

# ApiDestination
<a name="API_ApiDestination"></a>

Contains details about an API destination.

## Contents
<a name="API_ApiDestination_Contents"></a>

 ** ApiDestinationArn **   <a name="eventbridge-Type-ApiDestination-ApiDestinationArn"></a>
The ARN of the API destination.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws([a-z]|\-)*:events:([a-z]|\d|\-)*:([0-9]{12})?:api-destination\/[\.\-_A-Za-z0-9]+\/[\-A-Za-z0-9]+$`
Required: No

 ** ApiDestinationState **   <a name="eventbridge-Type-ApiDestination-ApiDestinationState"></a>
The state of the API destination.
Type: String
Valid Values: `ACTIVE | INACTIVE`
Required: No

 ** ConnectionArn **   <a name="eventbridge-Type-ApiDestination-ConnectionArn"></a>
The ARN of the connection specified for the API destination.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws([a-z]|\-)*:events:([a-z]|\d|\-)*:([0-9]{12})?:connection\/[\.\-_A-Za-z0-9]+\/[\-A-Za-z0-9]+$`
Required: No

 ** CreationTime **   <a name="eventbridge-Type-ApiDestination-CreationTime"></a>
A time stamp for the time that the API destination was created.
Type: Timestamp
Required: No

 ** HttpMethod **   <a name="eventbridge-Type-ApiDestination-HttpMethod"></a>
The method to use to connect to the HTTP endpoint.
Type: String
Valid Values: `POST | GET | HEAD | OPTIONS | PUT | PATCH | DELETE`
Required: No

 ** InvocationEndpoint **   <a name="eventbridge-Type-ApiDestination-InvocationEndpoint"></a>
The URL to the endpoint for the API destination.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^((%[0-9A-Fa-f]{2}|[-()_.!~*';/?:@\x26=+$,A-Za-z0-9])+)([).!';/?:,])?$`
Required: No

 ** InvocationRateLimitPerSecond **   <a name="eventbridge-Type-ApiDestination-InvocationRateLimitPerSecond"></a>
The maximum number of invocations per second to send to the HTTP endpoint.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** LastModifiedTime **   <a name="eventbridge-Type-ApiDestination-LastModifiedTime"></a>
A time stamp for the time that the API destination was last modified.
Type: Timestamp
Required: No

 ** Name **   <a name="eventbridge-Type-ApiDestination-Name"></a>
The name of the API destination.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_A-Za-z0-9]+`
Required: No

## See Also
<a name="API_ApiDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/ApiDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/ApiDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/ApiDestination)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
