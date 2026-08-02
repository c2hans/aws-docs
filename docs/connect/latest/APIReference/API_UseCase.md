---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_UseCase.html
---

# UseCase
<a name="API_UseCase"></a>

Contains the use case.

## Contents
<a name="API_UseCase_Contents"></a>

 ** UseCaseArn **   <a name="connect-Type-UseCase-UseCaseArn"></a>
The Amazon Resource Name (ARN) for the use case.
Type: String
Required: No

 ** UseCaseId **   <a name="connect-Type-UseCase-UseCaseId"></a>
The identifier for the use case.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: No

 ** UseCaseType **   <a name="connect-Type-UseCase-UseCaseType"></a>
The type of use case to associate to the integration association. Each integration association can have only one of each use case type.
Type: String
Valid Values: `RULES_EVALUATION | CONNECT_CAMPAIGNS`
Required: No

## See Also
<a name="API_UseCase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/UseCase)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/UseCase)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/UseCase)
