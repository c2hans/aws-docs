---
source_url: https://docs.aws.amazon.com/cloud-map/latest/api/API_HttpInstanceSummary.html
---

# HttpInstanceSummary
<a name="API_HttpInstanceSummary"></a>

In a response to a [DiscoverInstances](https://docs.aws.amazon.com/cloud-map/latest/api/API_DiscoverInstances.html) request, `HttpInstanceSummary` contains information about one instance that matches the values that you specified in the request.

## Contents
<a name="API_HttpInstanceSummary_Contents"></a>

 ** Attributes **   <a name="cloudmap-Type-HttpInstanceSummary-Attributes"></a>
If you included any attributes when you registered the instance, the values of those attributes.
Type: String to string map
Key Length Constraints: Maximum length of 255.
Key Pattern: `^[a-zA-Z0-9!-~]+$`
Value Length Constraints: Maximum length of 1024.
Value Pattern: `^([a-zA-Z0-9!-~][ \ta-zA-Z0-9!-~]*){0,1}[a-zA-Z0-9!-~]{0,1}$`
Required: No

 ** HealthStatus **   <a name="cloudmap-Type-HttpInstanceSummary-HealthStatus"></a>
If you configured health checking in the service, the current health status of the service instance.
Type: String
Valid Values: `HEALTHY | UNHEALTHY | UNKNOWN`
Required: No

 ** InstanceId **   <a name="cloudmap-Type-HttpInstanceSummary-InstanceId"></a>
The ID of an instance that matches the values that you specified in the request.
Type: String
Length Constraints: Maximum length of 64.
Required: No

 ** NamespaceName **   <a name="cloudmap-Type-HttpInstanceSummary-NamespaceName"></a>
The `HttpName` name of the namespace. It's found in the `HttpProperties` member of the `Properties` member of the namespace.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^(?!arn:)[!-~]{1,1024}$`
Required: No

 ** ServiceName **   <a name="cloudmap-Type-HttpInstanceSummary-ServiceName"></a>
The name of the service that you specified when you registered the instance.
Type: String
Pattern: `((?=^.{1,127}$)^([a-zA-Z0-9_][a-zA-Z0-9-_]{0,61}[a-zA-Z0-9_]|[a-zA-Z0-9])(\.([a-zA-Z0-9_][a-zA-Z0-9-_]{0,61}[a-zA-Z0-9_]|[a-zA-Z0-9]))*$)|(^\.$)`
Required: No

## See Also
<a name="API_HttpInstanceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicediscovery-2017-03-14/HttpInstanceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicediscovery-2017-03-14/HttpInstanceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicediscovery-2017-03-14/HttpInstanceSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Cloud Map. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloud-map` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
