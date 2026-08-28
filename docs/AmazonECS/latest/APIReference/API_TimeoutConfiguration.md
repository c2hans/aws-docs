---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TimeoutConfiguration.html
---

# TimeoutConfiguration
<a name="API_TimeoutConfiguration"></a>

An object that represents the timeout configurations for Service Connect.

**Note**
If `idleTimeout` is set to a time that is less than `perRequestTimeout`, the connection will close when the `idleTimeout` is reached and not the `perRequestTimeout`.

## Contents
<a name="API_TimeoutConfiguration_Contents"></a>

 ** idleTimeoutSeconds **   <a name="ECS-Type-TimeoutConfiguration-idleTimeoutSeconds"></a>
The amount of time in seconds a connection will stay active while idle. A value of `0` can be set to disable `idleTimeout`.
The `idleTimeout` default for `HTTP`/`HTTP2`/`GRPC` is 5 minutes.
The `idleTimeout` default for `TCP` is 1 hour.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: No

 ** perRequestTimeoutSeconds **   <a name="ECS-Type-TimeoutConfiguration-perRequestTimeoutSeconds"></a>
The amount of time waiting for the upstream to respond with a complete response per request. A value of `0` can be set to disable `perRequestTimeout`. `perRequestTimeout` can only be set if Service Connect `appProtocol` isn't `TCP`. Only `idleTimeout` is allowed for `TCP` `appProtocol`.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: No

## See Also
<a name="API_TimeoutConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/TimeoutConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/TimeoutConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/TimeoutConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
