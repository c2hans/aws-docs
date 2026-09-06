---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_DependencyConfig.html
---

# DependencyConfig
<a name="API_DependencyConfig"></a>

Identifies the dependency using the `DependencyKeyAttributes` and `DependencyOperationName`.

When creating a service dependency SLO, you must specify the `KeyAttributes` of the service, and the `DependencyConfig` for the dependency. You can specify the `OperationName` of the service, from which it calls the dependency. Alternatively, you can exclude `OperationName` and the SLO will monitor all of the service's operations that call the dependency.

## Contents
<a name="API_DependencyConfig_Contents"></a>

 ** DependencyKeyAttributes **   <a name="applicationsignals-Type-DependencyConfig-DependencyKeyAttributes"></a>
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

 ** DependencyOperationName **   <a name="applicationsignals-Type-DependencyConfig-DependencyOperationName"></a>
The name of the called operation in the dependency.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## See Also
<a name="API_DependencyConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/DependencyConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/DependencyConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/DependencyConfig)
