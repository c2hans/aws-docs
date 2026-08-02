---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_NamespaceInfoV2.html
---

# NamespaceInfoV2
<a name="API_NamespaceInfoV2"></a>

The error type.

## Contents
<a name="API_NamespaceInfoV2_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Arn **   <a name="QS-Type-NamespaceInfoV2-Arn"></a>
The namespace ARN.
Type: String
Required: No

 ** CapacityRegion **   <a name="QS-Type-NamespaceInfoV2-CapacityRegion"></a>
The namespace AWS Region.
Type: String
Required: No

 ** CreationStatus **   <a name="QS-Type-NamespaceInfoV2-CreationStatus"></a>
The creation status of a namespace that is not yet completely created.
Type: String
Valid Values: `CREATED | CREATING | DELETING | RETRYABLE_FAILURE | NON_RETRYABLE_FAILURE`
Required: No

 ** IamIdentityCenterApplicationArn **   <a name="QS-Type-NamespaceInfoV2-IamIdentityCenterApplicationArn"></a>
The Amazon Resource Name (ARN) for the IAM Identity Center application.
Type: String
Required: No

 ** IamIdentityCenterInstanceArn **   <a name="QS-Type-NamespaceInfoV2-IamIdentityCenterInstanceArn"></a>
The Amazon Resource Name (ARN) for the IAM Identity Center instance.
Type: String
Required: No

 ** IdentityStore **   <a name="QS-Type-NamespaceInfoV2-IdentityStore"></a>
The identity store used for the namespace.
Type: String
Valid Values: `QUICKSIGHT`
Required: No

 ** Name **   <a name="QS-Type-NamespaceInfoV2-Name"></a>
The name of the error.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `^[a-zA-Z0-9._-]*$`
Required: No

 ** NamespaceError **   <a name="QS-Type-NamespaceInfoV2-NamespaceError"></a>
An error that occurred when the namespace was created.
Type: [NamespaceError](API_NamespaceError.md) object
Required: No

## See Also
<a name="API_NamespaceInfoV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/NamespaceInfoV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/NamespaceInfoV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/NamespaceInfoV2)
