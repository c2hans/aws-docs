---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_CodeLocation.html
---

# CodeLocation
<a name="API_CodeLocation"></a>

Identifies a code location to instrument, including the programming language, code unit, class, method, file path, and optional line number.

## Contents
<a name="API_CodeLocation_Contents"></a>

 ** FilePath **   <a name="applicationsignals-Type-CodeLocation-FilePath"></a>
The source file path relative to the project or source root, such as `src/payment/PaymentProcessor.java` or `src/payment/PaymentProcessor.py`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** Language **   <a name="applicationsignals-Type-CodeLocation-Language"></a>
The programming language for this instrumentation point, such as Java, Python, or JavaScript.
Type: String
Valid Values: `Java | Python | Javascript`
Required: Yes

 ** ClassName **   <a name="applicationsignals-Type-CodeLocation-ClassName"></a>
The class or type name that contains the method. This is required for Java and optional for Python module-level functions.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** CodeUnit **   <a name="applicationsignals-Type-CodeLocation-CodeUnit"></a>
The package, module, or namespace that contains the target code, for example `com.amazon.payment` or `payment_service`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** LineNumber **   <a name="applicationsignals-Type-CodeLocation-LineNumber"></a>
The line number to instrument. Provide this to disambiguate overloaded methods and to target a specific line when needed.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** MethodName **   <a name="applicationsignals-Type-CodeLocation-MethodName"></a>
The method or function name to instrument, such as `validateCreditCard` or `__init__`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Required: No

## See Also
<a name="API_CodeLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/CodeLocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/CodeLocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/CodeLocation)
