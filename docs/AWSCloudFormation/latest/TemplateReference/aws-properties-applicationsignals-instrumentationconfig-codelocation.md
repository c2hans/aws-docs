---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-applicationsignals-instrumentationconfig-codelocation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApplicationSignals::InstrumentationConfig CodeLocation
<a name="aws-properties-applicationsignals-instrumentationconfig-codelocation"></a>

Identifies a code location to instrument, including the programming language, code unit, class, method, file path, and optional line number.

## Syntax
<a name="aws-properties-applicationsignals-instrumentationconfig-codelocation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-applicationsignals-instrumentationconfig-codelocation-syntax.json"></a>

```
{
  "[ClassName](#cfn-applicationsignals-instrumentationconfig-codelocation-classname)" : {{String}},
  "[CodeUnit](#cfn-applicationsignals-instrumentationconfig-codelocation-codeunit)" : {{String}},
  "[FilePath](#cfn-applicationsignals-instrumentationconfig-codelocation-filepath)" : {{String}},
  "[Language](#cfn-applicationsignals-instrumentationconfig-codelocation-language)" : {{String}},
  "[LineNumber](#cfn-applicationsignals-instrumentationconfig-codelocation-linenumber)" : {{Integer}},
  "[MethodName](#cfn-applicationsignals-instrumentationconfig-codelocation-methodname)" : {{String}}
}
```

### YAML
<a name="aws-properties-applicationsignals-instrumentationconfig-codelocation-syntax.yaml"></a>

```
  [ClassName](#cfn-applicationsignals-instrumentationconfig-codelocation-classname): {{String}}
  [CodeUnit](#cfn-applicationsignals-instrumentationconfig-codelocation-codeunit): {{String}}
  [FilePath](#cfn-applicationsignals-instrumentationconfig-codelocation-filepath): {{String}}
  [Language](#cfn-applicationsignals-instrumentationconfig-codelocation-language): {{String}}
  [LineNumber](#cfn-applicationsignals-instrumentationconfig-codelocation-linenumber): {{Integer}}
  [MethodName](#cfn-applicationsignals-instrumentationconfig-codelocation-methodname): {{String}}
```

## Properties
<a name="aws-properties-applicationsignals-instrumentationconfig-codelocation-properties"></a>

`ClassName`  <a name="cfn-applicationsignals-instrumentationconfig-codelocation-classname"></a>
The class or type name that contains the method. This is required for Java and optional for Python module-level functions.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CodeUnit`  <a name="cfn-applicationsignals-instrumentationconfig-codelocation-codeunit"></a>
The package, module, or namespace that contains the target code, for example `com.amazon.payment` or `payment_service`.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FilePath`  <a name="cfn-applicationsignals-instrumentationconfig-codelocation-filepath"></a>
The source file path relative to the project or source root, such as `src/payment/PaymentProcessor.java` or `src/payment/PaymentProcessor.py`.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Language`  <a name="cfn-applicationsignals-instrumentationconfig-codelocation-language"></a>
The programming language for this instrumentation point, such as Java, Python, or JavaScript.
*Required*: Yes
*Type*: String
*Allowed values*: `Java | Python | Javascript`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LineNumber`  <a name="cfn-applicationsignals-instrumentationconfig-codelocation-linenumber"></a>
The line number to instrument. Provide this to disambiguate overloaded methods and to target a specific line when needed.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MethodName`  <a name="cfn-applicationsignals-instrumentationconfig-codelocation-methodname"></a>
The method or function name to instrument, such as `validateCreditCard` or `__init__`.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `80`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
