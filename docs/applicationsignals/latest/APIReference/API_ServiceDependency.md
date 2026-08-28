---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ServiceDependency.html
---

# ServiceDependency
<a name="API_ServiceDependency"></a>

This structure contains information about one dependency of this service.

## Contents
<a name="API_ServiceDependency_Contents"></a>

 ** DependencyKeyAttributes **   <a name="applicationsignals-Type-ServiceDependency-DependencyKeyAttributes"></a>
This is a string-to-string map. It can include the following fields.
+  `Type` designates the type of object this is.
+  `ResourceType` specifies the type of the resource. This field is used only when the value of the `Type` field is `Resource` or `AWS::Resource`.
+  `Name` specifies the name of the object. This is used only if the value of the `Type` field is `Service`, `RemoteService`, or `AWS::Service`.
+  `Identifier` identifies the resource objects of this resource. This is used only if the value of the `Type` field is `Resource` or `AWS::Resource`.
+  `Environment` specifies the location where this object is hosted, or what it belongs to.
Type: String to string map
Map Entries: Maximum number of 4 items.
Key Pattern: `[a-zA-Z]{1,50}`
Value Length Constraints: Minimum length of 1. Maximum length of 1024.
Value Pattern: `[ -~]*[!-~]+[ -~]*`
Required: Yes

 ** DependencyOperationName **   <a name="applicationsignals-Type-ServiceDependency-DependencyOperationName"></a>
The name of the called operation in the dependency.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** MetricReferences **   <a name="applicationsignals-Type-ServiceDependency-MetricReferences"></a>
An array of structures that each contain information about one metric associated with this service dependency that was discovered by Application Signals.
Type: Array of [MetricReference](API_MetricReference.md) objects
Required: Yes

 ** OperationName **   <a name="applicationsignals-Type-ServiceDependency-OperationName"></a>
The name of the operation in this service that calls the dependency.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## See Also
<a name="API_ServiceDependency_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/ServiceDependency)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/ServiceDependency)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/ServiceDependency)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Application Signals. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query applicationsignals` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
