---
source_url: https://docs.aws.amazon.com/lambda/latest/microvm-api/API_MicrovmItem.html
---

# MicrovmItem
<a name="API_MicrovmItem"></a>

Contains summary information about a MicroVM instance.

## Contents
<a name="API_MicrovmItem_Contents"></a>

 ** imageArn **   <a name="lambdamicrovm-Type-MicrovmItem-imageArn"></a>
The ARN of the MicroVM image used to run this MicroVM.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: Yes

 ** imageVersion **   <a name="lambdamicrovm-Type-MicrovmItem-imageVersion"></a>
The version of the MicroVM image used to run this MicroVM.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\s]+`
Required: Yes

 ** microvmId **   <a name="lambdamicrovm-Type-MicrovmItem-microvmId"></a>
The unique identifier of the MicroVM.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** startedAt **   <a name="lambdamicrovm-Type-MicrovmItem-startedAt"></a>
The timestamp when the MicroVM started.
Type: Timestamp
Required: Yes

 ** state **   <a name="lambdamicrovm-Type-MicrovmItem-state"></a>
The current lifecycle state of the MicroVM.
Type: String
Valid Values: `PENDING | RUNNING | SUSPENDING | SUSPENDED | TERMINATING | TERMINATED`
Required: Yes

## See Also
<a name="API_MicrovmItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-microvms-2025-09-09/MicrovmItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-microvms-2025-09-09/MicrovmItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-microvms-2025-09-09/MicrovmItem)
